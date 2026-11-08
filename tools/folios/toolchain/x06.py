# -*- coding: utf-8 -*-
"""Tech & Tools · The Toolbox — Folio X.06: Sub-Wavelength Acoustic & Topological Metamaterial Unit Cells: Genus g = 1 & Betti-Number Verification."""

FOLIO = {'slug': 'x06',
 'folio_id': 'X.06',
 'tool_id': 'TOOL-PHYS-MATH-1',
 'cat': 'physics_math',
 'plate_slug': 'm10',
 'pillar_label_en': 'Physics & Math Explorer Toolbox · Topological Genus & Acoustic Metamaterials',
 'pillar_label_es': 'Herramientas de Física y Matemáticas · Género Topológico y Metamateriales '
                    'Acústicos',
 'badge_en': 'TOOLBOX X.06 · GENUS-1 METAMATERIAL UNIT CELL (χ = 0 · β₁ = 2 · GLB · 3MF · STEP)',
 'badge_es': 'HERRAMIENTA X.06 · CELDA UNITARIA DE METAMATERIAL GÉNERO-1 (χ = 0 · β₁ = 2 · GLB · '
             '3MF · STEP)',
 'title': 'Sub-Wavelength Acoustic & Topological Metamaterial Unit Cells: Genus g = 1 & '
          'Betti-Number Verification',
 'title_es': 'Celdas Unitarias de Metamateriales Acústicos y Topológicos: Verificación de Género g '
             '= 1 y Números de Betti',
 'subtitle': 'Empowering independent physicists, acoustic designers, and math educators to '
             'generate pierced toroidal metamaterial unit cells (.glb, .3mf, .step) and verify '
             'Euler–Poincaré χ = V − E + F = 2 − 2g = 0 and Betti numbers (β₀=1, β₁=2, β₂=1) in '
             'stdlib Python.',
 'subtitle_es': 'Empoderando a físicos independientes, diseñadores acústicos y educadores '
                'matemáticos para generar celdas unitarias toroidales de metamateriales (.glb, '
                '.3mf, .step) y verificar Euler–Poincaré χ = V − E + F = 2 − 2g = 0 y los números '
                'de Betti (β₀=1, β₁=2, β₂=1) en Python puro.',
 'why_en': 'Why do topological physicists, acoustic engineers, and pure mathematicians care about '
           'the holes inside a 3D unit cell? Because a pierced channel changes the topology of the '
           'boundary surface from a sphere (genus g = 0, χ = 2) to a torus (genus g = 1, χ = 0, '
           'first Betti number β₁ = 2), creating the exact sub-wavelength neck-and-cavity geometry '
           'needed for Helmholtz acoustic metamaterials (Folio E.03), photonic/phononic crystals '
           '(Folio P.10), and persistent homology barcodes (Folio M.10).',
 'why_es': '¿Por qué a los físicos topológicos, ingenieros acústicos y matemáticos les importan '
           'los túneles dentro de una celda unitaria 3D? Porque un canal pasante transforma la '
           'topología de la superficie frontera de una esfera (género g = 0, χ = 2) a un toro '
           '(género g = 1, χ = 0, primer número de Betti β₁ = 2), creando la geometría exacta de '
           'cuello y cavidad necesaria para los metamateriales acústicos de Helmholtz (Folio '
           'E.03), cristales fotónicos/fonónicos (Folio P.10) y códigos de barras de homología '
           'persistente (Folio M.10).',
 'governing_law': 'χ = V − E + F = 16 − 48 + 32 = 0 = 2 − 2g (g = 1, β₁ = 2) · V = (L_o² − L_i²) H '
                  '= 349,440 mm³ · φ = 0.090',
 'pass_pill_en': 'PASS · GENUS g = 1 (χ = 0) · V = 349,440 mm³ · GLB+3MF+STEP',
 'pass_pill_es': 'APROBADO · GÉNERO g = 1 (χ = 0) · V = 349,440 mm³ · GLB+3MF+STEP',
 'generator_script': 'skills/toolchain/x06/make_x06.py',
 'verifier_script': 'skills/toolchain/x06/verify_x06_toolchain_x06_topological_metamaterial_cell.py',
 'skill_dir': 'skills/toolchain/x06',
 'skill_name': 'toolchain-x06-topological-metamaterial-cell',
 'formats': ('glb', '3mf', 'step'),
 'primary_doi': '10.1007/s00454-002-2885-2',
 'scite_summary': 'Edelsbrunner, Letscher & Zomorodian (2002) topological persistence and '
                  'Euler–Poincaré / Betti-number surface invariants verified offline.',
 'date_published': '2026-11-08',
 'date_redated': '2026-11-08',
 'current_edition': 'REV 1.0',
 'reading_time': '22 MIN READ',
 'small_studio_kit_en': 'Independent Physicist, Acoustic Designer & Math Educator Kit (Python 3 '
                        'stdlib + Blender + FreeCAD + Ripser/GUDHI): Generate a genus-1 pierced '
                        'metamaterial unit cell (x06_artifact.glb, x06_artifact.3mf, '
                        'x06_artifact.step), inspect the inward-facing acoustic neck normals vs. '
                        'outward cell walls in WebGL2, and verify χ = V − E + F = 0 with '
                        'verify_x06.',
 'small_studio_kit_es': 'Kit para Físicos Independientes, Diseñadores Acústicos y Educadores '
                        'Matemáticos (Python 3 stdlib + Blender + FreeCAD + Ripser/GUDHI): Genera '
                        'una celda unitaria de metamaterial de género 1 (x06_artifact.glb, '
                        'x06_artifact.3mf, x06_artifact.step), inspecciona las normales del canal '
                        'acústico interior frente a las paredes exteriores en WebGL2 y verifica χ '
                        '= V − E + F = 0 con verify_x06.',
 'companion_folios': [('math',
                       'm10',
                       'Folio M.10',
                       'Persistent Homology Barcodes & Topological Data Analysis'),
                      ('engineering',
                       'e03',
                       'Folio E.03',
                       'Helmholtz Viscothermal Acoustic Metamaterials'),
                      ('physics',
                       'p10',
                       'Folio P.10',
                       'Topological Photonics & Integer Chern Numbers'),
                      ('engineering', 'e01', 'Folio E.01', 'Darcy–Brinkman Porous Percolation')],
 'external_links': [('GUDHI Library (MIT/GPL Topological Data Analysis)',
                     'https://gudhi.inria.fr/'),
                    ('scikit-tda / Ripser.py (MIT Persistent Homology)',
                     'https://github.com/scikit-tda/ripser.py'),
                    ('mikedh/trimesh (MIT Mesh Topology Inspector)',
                     'https://github.com/mikedh/trimesh')],
 'act1_dropcap': 'In the chill autumn of 1860, inside his laboratory at Heidelberg, Hermann von '
                 'Helmholtz peered into blown glass spheres to decipher the hidden architecture of '
                 'musical timbre. By holding the narrow neck of a hollow bulb to his ear while '
                 'striking tuning forks, Helmholtz discovered that a trapped volume of air acts as '
                 'an acoustic spring, resonating with astonishing purity at a single '
                 'characteristic pitch. Thirty-five years later in Paris, Henri Poincaré published '
                 'his landmark treatise Analysis Situs, fundamentally rewriting modern geometry. '
                 'Poincaré asked how one could classify higher-dimensional spaces regardless of '
                 'how they are stretched or deformed. He invented topological invariants known as '
                 'Betti numbers, counting the independent loops and hollow cavities that define '
                 'the essence of shape. For generations, acoustic resonance and abstract algebraic '
                 'topology lived in separate intellectual universes, waiting for modern materials '
                 'science to weave their profound principles together.',
 'act1_body': 'That historic convergence arrived at the turn of the twenty-first century as '
              'computational topology met sub-wavelength wave physics. In 2002, Herbert '
              'Edelsbrunner, David Letscher, and Afra Zomorodian published their foundational '
              'framework for persistent homology (Discrete & Computational Geometry, DOI '
              '10.1007/s00454-002-2885-2), proving that multi-scale topological features could be '
              'computed algebraically using boundary matrices over binary fields. Four years '
              'later, Nicholas Fang and his collaborators demonstrated in Nature Materials that '
              'sub-wavelength acoustic metamaterials could manipulate ultrasonic sound waves by '
              'chaining pierced resonant cavities into periodic lattice arrays. By tuning the '
              'acoustic impedance of narrow neck channels, they achieved effective negative bulk '
              'moduli, redirecting sound waves around obstacles with zero reflection. Today, '
              'metamaterial engineering demands strict mathematical verification before '
              'fabrication. If an automated meshing tool flips a triangle winding on an inner '
              'channel or closes an interior void, the underlying Euler–Poincaré characteristic '
              'changes, destroying the designed sub-wavelength acoustic bandgap before physical '
              'testing even begins.',
 'pullquote': 'When an inward-oriented channel pierces a 3D solid, two miracles happen at once in '
              'the triangle mesh: V − E + F drops from 2 to 0 to record the topological handle, '
              'and the divergence theorem automatically subtracts the void volume.',
 'chronology': [('1895',
                 "Henri Poincaré publishes 'Analysis Situs', generalizing Euler's formula to "
                 'n-dimensional manifolds via alternating sums of Betti numbers χ = ∑ (−1)^k β_k.'),
                ('1860–1863',
                 'Hermann von Helmholtz analyzes acoustic resonators whose neck mass and cavity '
                 'compliance absorb sound far below the free-space wavelength.'),
                ('2002',
                 'Herbert Edelsbrunner, David Letscher, and Afra Zomorodian formalize persistent '
                 'homology (DOI 10.1007/s00454-002-2885-2) to track topological features across '
                 'filtration scales.'),
                ('2026',
                 'Informatico.ai ships X.06: a genus-1 metamaterial unit cell exported to GLB, '
                 '3MF, and STEP AP242 with stdlib Euler–Betti and pore-volume verification.')],
 'act2_intuition': 'The topological identity of a pierced unit cell is defined by its boundary '
                   'surface invariants. A closed topological sphere possesses Euler characteristic '
                   'χ = 2 with genus g = 0. Piercing a through-hole converts the exterior into a '
                   'closed orientable two-manifold of genus g = 1, identically matching a '
                   'geometric torus. In our discretized mesh of sixteen vertices, forty-eight '
                   'edges, and thirty-two triangular facets, the Euler–Poincaré formula confirms χ '
                   '= V − E + F = 16 − 48 + 32 = 0 = 2 − 2g. The corresponding surface Betti '
                   'numbers evaluate to β₀ = 1 (a single connected component), β₁ = 2 (two '
                   'independent non-contractible one-cycles winding around the central channel and '
                   'through the toroidal body), and β₂ = 1 (a single closed two-dimensional '
                   'enclosing boundary). Analytically, the solid volume obeys exact divergence '
                   'void subtraction: V = (L_o² − L_i²) H = (80² − 24²) × 60 = 349,440 mm³, '
                   'establishing a baseline acoustic porosity φ = 0.090 with zero volumetric '
                   'leakage.',
 'sliders': [{'id': 'tp-tool-s0',
              'label': 'Acoustic Channel Width L_i',
              'min': 8,
              'max': 56,
              'step': 4,
              'value': 24,
              'unit': ' mm'},
             {'id': 'tp-tool-s1',
              'label': 'Unit Cell Height H_cell',
              'min': 30,
              'max': 90,
              'step': 6,
              'value': 60,
              'unit': ' mm'}],
 'readouts': [{'label': 'Euler–Poincaré & Genus', 'value': 'V=16, E=48, F=32 · χ=0 (g=1)'},
              {'label': 'Surface Betti Numbers', 'value': 'β₀ = 1 · β₁ = 2 · β₂ = 1'},
              {'label': 'Solid Volume & Porosity φ', 'value': '349,440 mm³ · φ = 9.00%'},
              {'label': 'GLB / 3MF / STEP Verdict', 'value': 'PASS · DEFECT REJECTED'}],
 'steps': ['Stage 1: Outer Block & Pierced Channel Ring Construction — Place 8 outer vertices '
           '(±40, ±40, ±30 mm) and 8 inner channel vertices (±12, ±12, ±30 mm).',
           'Stage 2: Annular Terrace Stitching & Opposite-Winding Channel Walls — Orient outer '
           'walls away from the origin, inner channel walls toward the channel axis, and stitch '
           'top/bottom annular terraces into a 32-triangle closed 2-torus.',
           'Stage 3: Euler–Poincaré & Betti-Number Certification — Verify 3F = 2E (96 = 96), χ = V '
           '− E + F = 16 − 48 + 32 = 0, genus g = (2 − χ)/2 = 1, and first Betti number β₁ = 2g = '
           '2.',
           'Stage 4: Signed Void Subtraction & Multi-Format Export — Confirm V_mesh = (80² − 24²) '
           '× 60 = 349,440.0 mm³ and φ = 0.0900 across x06_artifact.glb, x06_artifact.3mf, and '
           'x06_artifact.step, and run the planted-defect knockout.'],
 'rules': ['Toroidal Euler–Poincaré Invariant: For a single connected closed orientable 2-manifold '
           'of genus g = 1, the vertex, edge, and face counts must satisfy χ = V − E + F = 2 − 2g '
           '= 0 and 3F = 2E.',
           'Divergence Void-Subtraction Identity: Reversing the winding of the inner channel walls '
           'so normals point into the void must yield exact signed volume V = (L_o² − L_i²) H = '
           '349,440.0 mm³.',
           'Planted-Defect Topological Sensitivity: Flipping any single triangle on the annular '
           'terrace or inner channel wall must immediately break half-edge closure and fail '
           'verify_x06.'],
 'sidenote_1': {'kicker': 'SIDENOTE X.06-A · WHY GENUS g = 1 TESTS WHAT CONVEX BOXES CANNOT',
                'body': "A verifier that only ever checks χ = 2 could hard-code Euler's sphere "
                        "formula. By testing χ = 2 (X.01, X.02, X.04, X.05), χ = 14 (X.03's 7 "
                        "voussoirs), and χ = 0 (X.06's genus-1 resonator), our topological "
                        'verifier is exercised across three distinct homology classes.'},
 'sidenote_2': {'kicker': 'SIDENOTE X.06-B · BRIDGING E.03, P.10 & M.10',
                'body': 'This single downloadable unit cell connects three pillars of '
                        'Informatico.ai: acoustic viscothermal metamaterials (E.03), periodic '
                        'photonic/phononic lattices (P.10), and persistent homology Betti barcodes '
                        '(M.10).'},
 'walkthrough': ['Orbit and tilt the pierced metamaterial unit cell in the WebGL2 viewer below; '
                 'notice the inner acoustic neck channel highlighted in warm minium orange against '
                 'the Prussian-blue outer shell.',
                 'Toggle Cross-Section or Wireframe to inspect how the top and bottom annular '
                 'terraces stitch the outer ring (0..7) to the inner channel ring (8..15) without '
                 'a single T-junction.',
                 'Download x06_artifact.glb, x06_artifact.3mf, and x06_artifact.step and run '
                 'verify_x06 locally to see χ = 0 and V = 349,440.0 mm³ verified.'],
 't0_t1_certified': ['Deterministic generator (skills/toolchain/x06/make_x06.py) emitting genus-1 '
                     'toroidal unit-cell artifacts in .glb, .3mf, and .step formats.',
                     'Stdlib topological verifier '
                     '(verify_x06_toolchain_x06_topological_metamaterial_cell.py) certifying χ = V '
                     '− E + F = 0, genus g = 1, β₁ = 2, signed volume 349,440.0 mm³, and '
                     'planted-defect rejection.',
                     'Cross-pillar bridge connecting Engineering (E.03), Physics (P.10), and '
                     'Mathematics (M.10).'],
 't2_t3_open_horizon': ['Educational Geometry Boundary: Every file on this page is an educational '
                        'artifact; nothing is certified as load-bearing, printable, safe, or fit '
                        'for any purpose.',
                        'Future Edition 2 Extensions: Triply periodic minimal surface (Schoen '
                        'Gyroid genus g = 3 unit cell) marching-tetrahedra extraction and '
                        'Vietoris–Rips filtration barcodes.'],
 'sources': ['Edelsbrunner, H., Letscher, D., & Zomorodian, A. (2002). Topological persistence and '
             'simplification. Discrete & Computational Geometry, 28(4), 511–533. DOI '
             '10.1007/s00454-002-2885-2',
             'Fang, N., et al. (2006). Ultrasonic metamaterials with negative modulus. Nature '
             'Materials, 5(6), 452–456. DOI 10.1038/nmat1644',
             'Zomorodian, A., & Carlsson, G. (2005). Computing persistent homology. Discrete & '
             'Computational Geometry, 33(2), 249–274. DOI 10.1007/s00454-004-1146-y',
             'Crane, K. (2018). Discrete Differential Geometry: An Applied Introduction. Carnegie '
             'Mellon University.'],
 'act1_plain_bridge': 'Controlling sound waves and vibrations inside compact devices requires '
                      'engineering materials that trap or steer acoustic energy through geometry '
                      'rather than sheer mass. When you pierce a solid block with a hollow central '
                      'tunnel, you transform a simple solid block into a toroidal acoustic '
                      'resonator capable of silencing harsh engine hums or guiding ultrasound '
                      'waves. This interactive studio allows independent physicists, acoustic '
                      'engineers, and educators to design sub-wavelength metamaterial unit cells '
                      'with mathematically certified topological invariants. You can adjust the '
                      'internal sound tunnel width and overall cell height in real time, '
                      'inspecting the inward-facing acoustic channel and verifying that the '
                      'structure contains exactly one continuous through-hole. When your geometry '
                      'passes every topological check, you can download production-ready files in '
                      'standard GL Transmission Format, 3D Manufacturing Format, or neutral STEP '
                      'boundary representations. You can immediately import these models into '
                      'OrcaSlicer, PrusaSlicer, FreeCAD, or Blender to fabricate acoustic filters.',
 'act1_stakes': 'For independent acoustic designers, medical ultrasound researchers, and '
                'specialized audio studios, validating metamaterial unit cells before physical '
                'fabrication represents the boundary between breakthrough innovation and wasted '
                'capital. Machining acoustic metamaterials from solid brass or 3D-printing '
                'delicate sub-wavelength lattices on stereolithography rigs costs hundreds of '
                'dollars per specimen and requires days of meticulous post-curing. If an '
                'unverified unit cell contains self-intersecting boundary faces or topological '
                'defects, its acoustic transmission spectrum shifts unpredictably, shifting sharp '
                'resonant attenuation notches into unusable frequency bands. Furthermore, running '
                'multi-physics finite-element acoustic simulations on non-manifold meshes leads to '
                'non-converging matrix solvers or false boundary resonances that mislead '
                'researchers. By auditing topological invariants—such as Euler–Poincaré '
                'characteristic and Betti numbers—in pure client-side Python prior to meshing, '
                'independent practitioners ensure their periodic unit cells preserve exact '
                'genus-one connectivity. They can confidently build acoustic cloaks, '
                'noise-canceling ventilation panels, and medical transducers without relying on '
                'costly proprietary CAE licenses.',
 'act2_analogy': "Imagine holding a solid cube of potter's clay in your hands. If you press a "
                 'wooden dowel straight through the center and pull it out, you pierce a '
                 'continuous tunnel through the block, transforming it into a rectangular doughnut '
                 "or coffee mug handle. At that exact moment, the object's topology shifts: it "
                 'gains a permanent hole that cannot be erased without slicing or gluing the clay. '
                 'Now imagine blowing gently across the opening of a glass bottle. The trapped '
                 'column of air inside the tunnel bounces against the walls, creating a crisp '
                 "acoustic note tuned strictly by the opening's geometric dimensions.",
 'act2_plain_primer': 'You can explore and test this acoustic metamaterial unit cell using two '
                      'continuous sliders and an intentional diagnostic stress-test button. The '
                      'first slider adjusts the Acoustic Channel Width, scaling the square central '
                      'through-hole between eight and fifty-six millimeters. Widening this throat '
                      "increases the unit cell's void fraction and shifts its viscothermal "
                      'acoustic impedance, allowing sound waves of varying frequencies to pass or '
                      'reflect. The second slider governs the Unit Cell Height, expanding the '
                      'prism between thirty and ninety millimeters to tune the resonant acoustic '
                      'path length and adjust the effective mass density of the metamaterial '
                      'lattice. Finally, pressing the Counterfactual Axiom-Knockout button '
                      'deliberately corrupts the underlying geometry. It flips the vertex winding '
                      'order of a single triangular facet along the top annular terrace, breaking '
                      'the closed half-edge boundary condition. The Euler–Poincaré characteristic '
                      'and genus invariants instantly fail their audit, visually demonstrating how '
                      'the software detects and rejects defective mesh topology before production.',
 'act2_deepening': 'At the algorithmic level, verifying the metamaterial unit cell requires '
                   'evaluating both algebraic topology and physical acoustic boundary conditions. '
                   'The Python generator stitches the outer perimeter and interior acoustic tunnel '
                   'using an annular terrace triangulation that enforces strict half-edge pairing: '
                   'every directed edge must be traversed exactly once in each direction across '
                   'neighboring facets (3F = 2E). Facet normals along the outer walls point '
                   'outward away from the cell centroid, whereas normals lining the interior '
                   'acoustic conduit face inward toward the central axis, accurately defining the '
                   'solid-fluid boundary. In acoustic finite-element simulations, this '
                   'inward-facing surface governs the viscothermal dissipation layer modeled by '
                   'the Johnson–Champoux–Allard equations. Computing the discrete divergence '
                   'theorem by summing signed tetrahedra yields identical results to analytical '
                   'void subtraction (L_o² − L_i²) H, proving that the mesh encloses a perfectly '
                   'watertight domain. This dual algebraic and geometric verification ensures that '
                   'sub-wavelength acoustic simulations evaluate real physical resonances rather '
                   'than artificial numerical boundary reflections.',
 'act4_human_ai': 'Pairing independent researchers with AI coding agents accelerates the synthesis '
                  'of advanced topological metamaterials while maintaining absolute formal rigor. '
                  'A physicist or acoustic engineer formulates a target sub-wavelength dispersion '
                  "relation, then prompts an AI agent to adjust the unit cell's parametric "
                  'dimensions. Guided by the protocol embedded within the accompanying SKILL.md '
                  'file, the assistant modifies make_x06.py to regenerate the GLB, 3MF, and STEP '
                  'artifact suite. Before any geometry is accepted into an experimental catalog or '
                  'uploaded to a fabrication service, the autonomous workflow runs '
                  'verify_x06_toolchain_x06_topological_metamaterial_cell.py. This deterministic '
                  'test script computes the Euler–Poincaré invariant χ = V − E + F, validates '
                  'half-edge closure (3F = 2E), audits surface Betti numbers, and verifies exact '
                  'solid volume conservation. By subjecting AI-generated geometric code to '
                  'deterministic topological verification, human researchers eliminate silent mesh '
                  'corruption, ensuring every fabricated metamaterial unit cell performs reliably '
                  'in physical acoustic wave experiments.',
 'act4_deepening': 'The topological invariants verified in this unit cell establish an '
                   'intellectual conduit connecting abstract data science, continuum acoustics, '
                   'quantum electrodynamics, and porous materials engineering. In topological data '
                   'analysis (Folio M.10), computing persistent homology barcodes via simplicial '
                   'filtration tracks the birth and death of the exact one-cycles (β₁ = 2) that '
                   "define this unit cell's toroidal geometry across varying spatial resolutions. "
                   'In acoustic engineering (Folio E.03), periodic arrangements of these pierced '
                   'cells act as Helmholtz viscothermal resonators, creating broad sub-wavelength '
                   'attenuation bands that trap low-frequency mechanical rumblings without '
                   'blocking steady airflow. When applied to optical waveguides in Folio P.10, '
                   'analogous geometric topologies yield non-zero integer Chern numbers, '
                   'establishing topologically protected chiral edge states that guide laser '
                   'photons around sharp structural corners without backscattering. Even in civil '
                   'hydrology and filtration physics (Folio E.01), Darcy–Brinkman percolation '
                   'across disordered porous media depends directly on whether connected toroidal '
                   'pore networks span across the solid matrix or remain trapped beneath '
                   'percolation thresholds.',
 'plain_es': 'Controlar las ondas acústicas y las vibraciones mecánicas dentro de equipos modernos '
             'requiere diseñar materiales capaces de absorber o desviar el sonido mediante su '
             'forma geométrica. Al perforar un bloque sólido con un túnel central continuo, '
             'transformamos una caja simple en un resonador toroidal capaz de disipar zumbidos '
             'molestos o enfocar señales de ultrasonido. Este laboratorio digital permite a '
             'físicos independientes, ingenieros acústicos y docentes diseñar celdas unitarias de '
             'metamateriales con invariantes topológicos certificados por computadora. Desde su '
             'navegador, ustedes pueden ajustar el ancho del canal acústico interior y la altura '
             'de la celda en tiempo real, verificando que la estructura conserve exactamente un '
             'túnel pasante sin fisuras. Una vez aprobada la geometría, pueden descargar '
             'inmediatamente los archivos listos para fabricación en formatos GLB, 3MF y STEP. '
             'Estos modelos se abren directamente en OrcaSlicer, PrusaSlicer, FreeCAD o Blender '
             'para imprimir filtros acústicos de alto rendimiento sin requerir reparaciones '
             'manuales.',
 'deep_es': 'La caracterización topológica de esta celda de metamaterial acústico se fundamenta en '
            'la invariancia algebraica de su superficie frontera. Al perforar el prisma con un '
            'canal central pasante, la topología transiciona de una esfera a una 2-variedad '
            'orientable de género g = 1, equivalente a un toro. La discretización en dieciséis '
            'vértices, cuarenta y ocho aristas y treinta y dos caras triangulares satisface '
            'estrictamente la relación de Euler–Poincaré: χ = V − E + F = 16 − 48 + 32 = 0 = 2 − '
            '2g, con números de Betti β₀ = 1, β₁ = 2 y β₂ = 1. El volumen auditado obedece la '
            'sustracción V = (L_o² − L_i²) H = (80² − 24²) × 60 = 349,440 mm³, fijando una '
            'porosidad acústica base de φ = 0.090 sin fugas. Esta rigurosa formulación garantiza '
            'que las simulaciones por elementos finitos evalúen modos resonantes viscotermales '
            'auténticos y no artefactos causados por mallas abiertas.',
 'distill_diagram': {'analogy_title': 'The Pierced Clay & Bottle Neck',
                     'analogy_sub': 'Pierced channels trap and steer sound like blown glass '
                                    'bottles.',
                     'force_a_title': 'Acoustic Channel Width L_i',
                     'force_a_sub': 'Tunes viscothermal impedance and internal void fraction φ.',
                     'force_b_title': 'Unit Cell Height H_cell',
                     'force_b_sub': 'Adjusts resonant wave travel distance and effective mass '
                                    'density.',
                     'threshold_title': 'Euler–Poincaré Genus Invariant (χ = 0)',
                     'threshold_pass': 'Closed torus χ = 0 (g = 1, β₁ = 2): Valid acoustic unit '
                                       'cell.',
                     'threshold_fail': 'Flipped triangle breaks 3F = 2E: Broken genus g=1 '
                                       'topology.'}}
