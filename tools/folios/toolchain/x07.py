# -*- coding: utf-8 -*-
"""Tech & Tools · The Toolbox — Folio X.07: Discrete Gauss–Bonnet Curvature & Cotangent-Laplacian Mesh Quality Audit."""

FOLIO = {
    'slug': 'x07',
    'folio_id': 'X.07',
    'tool_id': 'TOOL-CORE-2',
    'cat': 'core',
    'plate_slug': 'x07',
    'pillar_label_en': 'Core Geometry Instrument · Discrete Curvature & Delaunay Audit',
    'pillar_label_es': 'Instrumento Geométrico Central · Curvatura Discreta y Auditoría Delaunay',
    'badge_en': 'TOOLBOX X.07 · GAUSS–BONNET CURVATURE + COTANGENT LAPLACIAN AUDIT (GLB · 3MF · STEP)',
    'badge_es': 'HERRAMIENTA X.07 · CURVATURA GAUSS–BONNET + LAPLACIANO COTANGENTE (GLB · 3MF · STEP)',
    'title': 'Discrete Gauss–Bonnet Curvature & Cotangent-Laplacian Mesh Quality Audit',
    'title_es': 'Auditoría de Curvatura Discreta de Gauss–Bonnet y Laplaciano Cotangente en Mallas',
    'subtitle': 'How a pure-Python standard-library audit tests whether a triangulated shell satisfies '
                'topological angle-deficit closure, Meyer mixed Voronoi area conservation, and '
                'non-negative cotangent edge weights across GLB, 3MF, and STEP.',
    'subtitle_es': 'Cómo una auditoría en Python estándar comprueba si una cáscara triangulada cumple '
                   'el cierre de déficit angular, la conservación de área mixta de Voronoi de Meyer '
                   'y pesos cotangentes no negativos en GLB, 3MF y STEP.',
    'why_en': 'A curved architectural canopy or finite-element shell can pass a basic triangle-count '
              'check and still distort stress smoothing or surface heat flow when thin sliver facets '
              'appear. Measuring the angle deficit around every corner, checking Voronoi cell areas, '
              'and flagging negative cotangent weights reveals where the mesh geometry quietly '
              'breaks down—before a designer trusts a solver output.',
    'why_es': 'Una cubierta arquitectónica curva o malla de elementos finitos puede superar un conteo '
              'básico de triángulos y aun así distorsionar el suavizado de esfuerzos cuando aparecen '
              'facetas alargadas. Medir el déficit angular en cada vértice, revisar las áreas de '
              'Voronoi y detectar pesos cotangentes negativos revela dónde falla la geometría antes '
              'de confiar en un modelo numérico.',
    'governing_law': '∑_{v ∈ V} (2π − ∑_{j} θ_{v,j}) = 2πχ = 4π · w_{ij} = ½(cot α_{ij} + cot β_{ij}) ≥ 0',
    'pass_pill_en': 'PASS · ∑ δ_v = 4π (err < 1e-12) · 0/120 NON-DELAUNAY · GLB+3MF+STEP',
    'pass_pill_es': 'APROBADO · ∑ δ_v = 4π (err < 1e-12) · 0/120 NO-DELAUNAY · GLB+3MF+STEP',
    'generator_script': 'skills/toolchain/x07/make_x07.py',
    'verifier_script': 'skills/toolchain/x07/verify_x07_toolchain_x07_gauss_bonnet_audit.py',
    'skill_dir': 'skills/toolchain/x07',
    'skill_name': 'toolchain-x07-gauss-bonnet-audit',
    'formats': ('glb', '3mf', 'step'),
    'primary_doi': '10.1145/1508044.1508063',
    'scite_summary': 'Wardetzky et al. (2007) discrete Laplace no-free-lunch bounds, Meyer et al. (2003) '
                     'mixed Voronoi areas, and discrete Gauss-Bonnet closure checked offline.',
    'date_published': '2026-11-20',
    'date_redated': '2026-11-20',
    'current_edition': 'REV 1.0',
    'reading_time': '22 MIN READ',
    'small_studio_kit_en': 'Zero-Cost Studio Curvature Stack (Blender 4.2 + FreeCAD 1.0 + Python 3 stdlib): '
                           'Run make_x07.py to emit x07_artifact.glb with per-vertex curvature colors, '
                           'x07_artifact.3mf, and x07_artifact.step; run verify_x07 to check angle-deficit '
                           'closure, mixed Voronoi area conservation, and negative cotangent weights in < 0.05s.',
    'small_studio_kit_es': 'Stack de Curvatura sin Costo (Blender 4.2 + FreeCAD 1.0 + Python 3 stdlib): '
                           'Ejecuta make_x07.py para generar x07_artifact.glb con colores de curvatura por '
                           'vértice, x07_artifact.3mf y x07_artifact.step; corre verify_x07 para revisar '
                           'cierre angular, áreas mixtas de Voronoi y pesos cotangentes negativos en < 0.05s.',
    'companion_folios': [
        ('architecture', 'a01', 'Folio A.01', 'Funicular Thrust Surfaces in Stone and Timber Shells'),
        ('architecture', 'a09', 'Folio A.09', 'Bending-Active & Hygroscopic Programmable Timber Skins'),
        ('architecture', 'a11', 'Folio A.11', '3D Polyhedral Graphic Statics & Stone Vaults'),
        ('engineering', 'e11', 'Folio E.11', 'SIMP Topology Optimization & Inerter Damping'),
    ],
    'external_links': [
        ('geometry-central (MIT Discrete Differential Geometry)', 'https://geometry-central.net/'),
        ('elalish/manifold (Apache-2.0 CSG Kernel)', 'https://github.com/elalish/manifold'),
        ('mikedh/trimesh (MIT Mesh Inspector)', 'https://github.com/mikedh/trimesh'),
    ],
    'act1_dropcap': 'In the summer of 1827, Carl Friedrich Gauss worked through field notebooks at his observatory '
                    'desk in Göttingen after years of surveying triangulation chains across the Kingdom of Hanover. '
                    'Using brass theodolites, his field crews had measured tiny excesses in the corner angles of large '
                    'triangles spanning hilltops from the Brocken to the Inselsberg. Gauss noticed a striking geometric '
                    'fact. Even if a curved sheet bends like a saddle or a dome, the total curvature inside a closed '
                    'patch depends solely on distances measured along the surface itself. Nearly two centuries later, '
                    'engineers who slice smooth shells into flat digital triangles face the discrete cousin of that '
                    'discovery. A curved canopy exported from a modeling tool can look clean on screen while narrow '
                    'sliver triangles quietly invert stiffness weights. Auditing corner angles restores that physical '
                    'compass.',
    'act1_plain_bridge': 'In plain words: imagine wrapping a basketball with flat paper triangles taped neatly edge '
                         'to edge. At each corner where triangles meet, you can lay the flat paper corners around a '
                         'tabletop circle. Because a ball curves away, the paper corners leave a tiny pie-shaped gap '
                         'before closing the circle. Adding those gaps together across the whole ball gives the same '
                         'total turn, whether you use forty big triangles or four thousand tiny ones. That constant '
                         'total gives engineers a fast safety check for three-dimensional files. When a file hides an '
                         'open seam, an inverted triangle, or pinched sliver faces, standard smoothing algorithms can '
                         'overshoot wildly. This page ships a lightweight browser inspector and open Python scripts that '
                         'measure every corner gap, check vertex area patches, and export clean neutral models in binary '
                         'glTF, Three-Dimensional Manufacturing Format, and Standard for the Exchange of Product Model '
                         'Data without paid software.',
    'act1_body': 'Converting smooth curved surfaces into polyhedral meshes exposes a classic tension between '
                 'topological invariants and metric discretization. Ulrich Pinkall and Konrad Polthier (Experimental '
                 'Mathematics, DOI 10.1080/10586458.1993.10504266) derived the cotangent formula for discrete minimal '
                 'surfaces, expressing mean-curvature normals at each vertex via the cotangents of opposite interior '
                 'angles. Soon after, Mathieu Desbrun, Mark Meyer, Peter Schröder, and Alan Barr (SIGGRAPH 1999, DOI '
                 '10.1145/311535.311576) applied implicit curvature flow to fair noisy meshes without shrinking '
                 'feature volume, and Meyer, Desbrun, Schröder, and Barr (Visualization and Mathematics III, DOI '
                 '10.1007/978-3-662-05105-4_2) introduced mixed Voronoi cell areas to clamp obtuse triangles that '
                 'push circumcenters outside their host face. Yet Max Wardetzky, Saurabh Mathur, Felix Kälberer, and '
                 'Eitan Grinspun (Symposium on Geometry Processing 2007, DOI 10.1145/1508044.1508063) showed a '
                 'fundamental limit: no discrete Laplace operator on arbitrary triangulations satisfies symmetry, '
                 'locality, linear precision, and non-negative edge weights all at once. In Folio X.07, our pure-Python '
                 'standard-library verifier pairs topological Gauss–Bonnet checking with an explicit Delaunay edge '
                 'audit so practitioners can see when a stretched mesh crosses into negative cotangent weights.',
    'act1_stakes': 'Why does a subtle sign flip inside a stiffness matrix matter to a small architectural practice or '
                   'solo structural analyst? Think about how form-finding and thermal diffusion solvers behave on thin '
                   'shells. Commercial geometry kernels often hide negative edge weights behind black-box mesh repair '
                   'dialogs, charging steep annual fees while masking numerical oscillations. When a stretched mesh '
                   'violates the local Delaunay condition along even a handful of seams, discrete harmonic heat flow '
                   'or membrane smoothing can produce spurious ripples that overshoot boundary temperatures or '
                   'elevations. Conversely, checking interior angles with standard trigonometric identities takes less '
                   'than fifty milliseconds on a desktop or laptop. Putting both the Gauss–Bonnet closure test and the '
                   'cotangent sign check into a readable script lets independent studios screen every binary glTF, '
                   'STEP AP242, and 3MF export before sending geometry to a structural solver or CNC toolpath.',
    'pullquote': 'Topological angle deficits stay locked to 2πχ as long as every half-edge pairs cleanly; yet '
                 'stretching a single axis too far flips opposite angle sums past π and turns cotangent weights '
                 'negative.',
    'chronology': [
        ('1639', 'René Descartes notes the total angular defect of a convex polyhedron equals 4π radians in '
                 'his unpublished manuscript De solidorum elementis.'),
        ('1827', 'Carl Friedrich Gauss publishes Disquisitiones generales circa superficies curvas, linking '
                 'Gaussian curvature to geodesic triangle angle excess.'),
        ('1993', 'Ulrich Pinkall and Konrad Polthier formulate the cotangent Laplacian for discrete minimal '
                 'surfaces (DOI 10.1080/10586458.1993.10504266).'),
        ('1996', 'Brian Mirtich formalizes fast polyhedral mass-property integration via the divergence theorem '
                 '(DOI 10.1080/10867651.1996.10487458).'),
        ('1999–2003', 'Desbrun, Meyer, Schröder, and Barr introduce implicit curvature flow (DOI '
                      '10.1145/311535.311576) and mixed Voronoi area clamping (DOI 10.1007/978-3-662-05105-4_2).'),
        ('2007', 'Wardetzky, Mathur, Kälberer, and Grinspun formulate the discrete Laplace no-free-lunch '
                 'bounds (DOI 10.1145/1508044.1508063).'),
        ('2026', 'Informatico.ai ships X.07: a frequency-2 triaxial geodesic polyhedron (V=42, E=120, F=80) '
                 'with per-vertex curvature shading, mixed Voronoi audit, and negative-weight knockout.'),
    ],
    'act2_analogy': 'Picture tailoring a fitted canvas canopy out of flat triangular cloth panels sewn tightly over a '
                    'curved wooden dome. Around a gentle dome peak, five or six neat equilateral triangles meet cleanly, '
                    'and the seam tension pulls evenly along every stitch. Now squash that dome sharply downward into '
                    'a flat pancake without re-cutting the seams: narrow sliver triangles form along the rim, and '
                    'pulling one thread makes the neighboring fabric buckle instead of lying smooth. Here is where the '
                    'picture stops: cloth fibers stretch and wrinkle under real friction, whereas discrete differential '
                    'geometry stays purely mathematical, assigning each edge an algebraic stiffness weight fixed solely '
                    'by its two opposite triangle angles.',
    'act2_plain_primer': 'In the Act III workbench below, two sliders let you reshape our forty-two-vertex geodesic '
                         'dome in real time. The first slider varies the Semi-Axis X Radius between eighteen and '
                         'forty-eight millimeters. Stretching the shell along its horizontal span shifts Gaussian '
                         'curvature toward the tight ends while testing whether every triangle pair stays well shaped. '
                         'The second slider adjusts the Semi-Axis Z Height between eight and twenty-eight millimeters. '
                         'Lower the height below eleven millimeters and watch what happens: the pinched triaxial shell '
                         'crosses a geometric boundary where opposing corner angles exceed one hundred eighty degrees, '
                         'triggering negative cotangent weights across sixteen edges even though Euler closure still '
                         'holds. Finally, clicking the Planted-Defect / Boundary Knockout button simulates an inverted '
                         'face winding so you can verify that both the half-edge check and the Gauss–Bonnet sum catch '
                         'broken topology at once.',
    'act2_intuition': 'Two distinct mathematical layers govern discrete curvature on a triangulated 2-manifold M = (V, '
                      'E, F). First comes pure topology: at each vertex v, summing the interior angles θ_{v,j} of '
                      'incident triangles and subtracting from 2π yields the angle deficit δ_v = 2π − ∑_j θ_{v,j}. '
                      'Summing δ_v over all vertices telescopes via the handshaking identity 3F = 2E into 2π(V − E + F) '
                      '= 2πχ, independent of vertex positions as long as faces stay non-degenerate and consistently '
                      'oriented. Second comes metric geometry: to convert angle deficit into pointwise Gaussian '
                      'curvature K_v = δ_v / A_v^{mixed}, Meyer et al. (2003, DOI 10.1007/978-3-662-05105-4_2) compute '
                      'the Voronoi circumcenter area inside non-obtuse triangles and clamp obtuse triangles to A_T / 2 '
                      'at the obtuse vertex and A_T / 4 at the two acute corners, keeping ∑_v A_v^{mixed} equal to the '
                      'total triangle surface area within floating-point roundoff. Across each interior edge (i, j) '
                      'shared by two triangles with opposite angles α_{ij} and β_{ij}, the cotangent weight w_{ij} = '
                      '½(cot α_{ij} + cot β_{ij}) remains non-negative when α_{ij} + β_{ij} ≤ π, matching the local '
                      'Delaunay criterion.',
    'act2_deepening': 'Open Question, Hypothesis (Tier T0/T1), and Falsification Boundary: Wardetzky et al. (2007, '
                      'DOI 10.1145/1508044.1508063) showed that symmetry, locality, linear precision, and non-negative '
                      'edge weights cannot coexist on every triangle mesh. We test this boundary directly on a '
                      'deterministic frequency-2 icosahedral shell (V = 42, E = 120, F = 80, χ = 2). Under baseline '
                      'triaxial radii (30, 24, 18) mm (Tier T0 deterministic computation), all 80 faces remain acute '
                      '(angles between 40.72° and 89.96°), 0 of 120 edges violate the Delaunay bound (minimum weight '
                      'w_min = +0.043248), total angle deficit ∑ δ_v matches 4π within 0.00e+00 rad, mixed Voronoi '
                      'areas sum to 6,665.5656 mm² within 1.82e-12 mm², and the cotangent Laplacian normal sum vanishes '
                      'within 5.86e-15 mm. Hypothesis (Tier T1): under anisotropic z-compression to (30, 24, 9) mm, '
                      'topological Gauss–Bonnet closure and mixed Voronoi area conservation will still hold, whereas '
                      'cotangent positivity will fail on flattened rim edges. Testing measures 24 of 80 obtuse faces, '
                      '16 of 120 non-Delaunay edges, and w_min = −0.429055. What would falsify our baseline audit? Any '
                      'mesh whose ∑ δ_v departs from 2πχ by > 10^-10 rad falsifies closed 2-manifold orientation, and '
                      'any edge with w_{ij} < −10^-12 falsifies the discrete maximum principle.',
    'sliders': [
        {'id': 'tp-tool-s0', 'label': 'Semi-Axis X Radius a_x', 'min': 18, 'max': 48, 'step': 2, 'value': 30, 'unit': ' mm'},
        {'id': 'tp-tool-s1', 'label': 'Semi-Axis Z Height c_z', 'min': 8, 'max': 28, 'step': 1, 'value': 18, 'unit': ' mm'},
    ],
    'readouts': [
        {'label': '2-Manifold Topology (V, E, F)', 'value': 'V=42, E=120, F=80 · χ=2'},
        {'label': 'Gauss–Bonnet Closure ∑ δ_v', 'value': '12.5664 rad (4π · err < 1e-12)'},
        {'label': 'Delaunay Edge Weights & Volume', 'value': '47,416.9 mm³ · 0/120 Non-Delaunay'},
        {'label': 'Audit & Knockout Gate', 'value': 'PASS · DEFECT REJECTED'},
    ],
    'steps': [
        'Stage 1: Frequency-2 Geodesic Dome Synthesis — Subdivide a regular icosahedron once using canonical '
        '(min(u, v), max(u, v)) edge midpoints projected onto the unit sphere and scaled by (30, 24, 18) mm to '
        'build a closed 42-vertex, 120-edge, 80-face shell (χ = 2) with curvature-mapped COLOR_0 shading.',
        'Stage 2: Stable Interior Angles & Gauss–Bonnet Closure — Evaluate corner angles via atan2(||u × v||, u · v) '
        'and check ∑_{v ∈ V} (2π − ∑_j θ_{v,j}) = 4π within 1e-10 rad alongside 3F = 2E half-edge closure.',
        'Stage 3: Meyer Mixed Voronoi Area & Cotangent Divergence Audit — Partition each triangle into Voronoi '
        'regions (clamped to A_T/2 and A_T/4 on obtuse triangles) so ∑ A_v^{mixed} = A_surface (6,665.5656 mm²) '
        'and check ∑_v (L x)_v = 0 and w_{ij} ≥ 0 across all 120 edges.',
        'Stage 4: Anisotropic Pinched Counterexample & Planted-Defect Knockout — Verify that compressing radii to '
        '(30, 24, 9) mm exposes 16/120 negative cotangent weights (w_min = −0.429055), and test that flipping '
        'triangle 0 winding triggers non-zero failure under --planted-defect.',
    ],
    'rules': [
        'Discrete Gauss–Bonnet Topological Invariant: On any closed orientable 2-manifold of Euler characteristic χ, '
        'the sum of vertex angle deficits ∑_v (2π − ∑_j θ_{v,j}) must stay within 1e-10 rad of 2πχ (4π for χ = 2).',
        'Meyer Mixed Voronoi & Divergence Conservation Invariant: Clamped mixed Voronoi vertex areas must sum to '
        'total triangle area within 1e-8 mm², and summed cotangent Laplacian vectors must vanish within 1e-10 mm.',
        'Delaunay & Planted-Defect Sensitivity Invariant: Baseline dome edges must hold w_{ij} > 0 while the '
        'pinched (30, 24, 9) mm mesh triggers w_{ij} < 0, and flipping triangle 0 must fail verify_x07.',
    ],
    'sidenote_1': {
        'kicker': 'SIDENOTE X.07-A · WHY ATAN2 BEATS ACOS AT CORNERS',
        'body': 'Evaluating triangle angles with acos(u·v / |u||v|) loses precision near 0 and π radians where cosine '
                'flattens out. Using atan2(||u × v||, u · v) preserves machine-precision closure to 0.00e+00 rad on '
                'our 42-vertex dome.',
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE X.07-B · WARDETZKY ET AL. (2007) BOUNDARY',
        'body': 'Compressing z from 18 mm to 9 mm keeps Gauss–Bonnet error at 3.55e-15 rad and mixed area error at '
                '9.09e-13 mm², yet flips 16 of 120 edges to negative cotangent weights (w_min = −0.4291).',
    },
    'walkthrough': [
        'Orbit and zoom the 42-vertex curvature-shaded geodesic dome in the WebGL2 viewer below; warmer amber '
        'patches mark higher Gaussian curvature K_v around the narrow ends while cooler blue marks flatter zones.',
        'Drag Semi-Axis Z Height c_z down from 18 mm to 9 mm to cross the Wardetzky Delaunay threshold and watch '
        'the live readout switch from 0/120 non-Delaunay edges to negative cotangent edge weights.',
        'Download x07_artifact.glb, x07_artifact.3mf, and x07_artifact.step and run verify_x07 locally to check '
        'both the baseline pass and the --planted-defect failure path.',
    ],
    't0_t1_certified': [
        'Deterministic Python stdlib generator (skills/toolchain/x07/make_x07.py) emitting curvature-colored '
        'x07_artifact.glb, watertight x07_artifact.3mf, and B-rep x07_artifact.step.',
        'Stdlib differential-geometry verifier (verify_x07_toolchain_x07_gauss_bonnet_audit.py) checking '
        'Gauss–Bonnet ∑ δ_v = 4π (err < 1e-12 rad), Meyer mixed Voronoi area conservation, 0/120 non-Delaunay '
        'edges at (30, 24, 18) mm, and 16/120 negative-weight edges at (30, 24, 9) mm.',
        'Planted-defect knockout rejecting triangle-winding flips and malformed 3MF XML.',
    ],
    't2_t3_open_horizon': [
        'Educational Geometry Boundary: Every file on this page is an educational artifact, not a '
        'stamped, load-bearing, printable, safe, or fit-for-purpose design.',
        'Future Edition 2 Extensions: Intrinsic Delaunay edge-flipping (iDT) retriangulation and geodesic heat '
        'kernel distance solvers remain outside the v1 static verification subset.',
    ],
    'sources': [
        'Wardetzky, M., Mathur, S., Kälberer, F., & Grinspun, E. (2007). Discrete Laplace operators: no free '
        'lunch. Proceedings of the Fifth Eurographics Symposium on Geometry Processing (SGP ’07), 33–37. DOI '
        '10.1145/1508044.1508063',
        'Meyer, M., Desbrun, M., Schröder, P., & Barr, A. H. (2003). Discrete differential-geometry operators for '
        'triangulated 2-manifolds. Visualization and Mathematics III, 35–57. DOI 10.1007/978-3-662-05105-4_2',
        'Pinkall, U., & Polthier, K. (1993). Computing discrete minimal surfaces and their conjugates. '
        'Experimental Mathematics, 2(1), 15–36. DOI 10.1080/10586458.1993.10504266',
        'Desbrun, M., Meyer, M., Schröder, P., & Barr, A. H. (1999). Implicit fairing of irregular meshes using '
        'diffusion and curvature flow. Proceedings of SIGGRAPH ’99, 317–324. DOI 10.1145/311535.311576',
        'Mirtich, B. (1996). Fast and accurate computation of polyhedral mass properties. Journal of Graphics '
        'Tools, 1(2), 31–50. DOI 10.1080/10867651.1996.10487458',
    ],
    'act4_human_ai': 'When an engineer asks a language model to subdivide or decimate a curved structural shell, '
                     'visual inspection by itself can miss pinched triangles that undermine finite-element stiffness '
                     'matrices. Folio X.07 pairs human spatial design with a deterministic mathematical gate. The '
                     'practitioner sets target span proportions and curvature tolerances, while the AI assistant '
                     'updates make_x07.py following the workflow in SKILL.md. Before any mesh enters a structural '
                     'or fabrication pipeline, verify_x07 checks half-edge closure, polyhedral volume, total angular '
                     'defect, Meyer mixed Voronoi area balance, and Delaunay cotangent signs using only Python '
                     'standard libraries. If a script edit introduces pinched sliver triangles or reversed facet '
                     'winding, the verifier halts with explicit numeric diagnostics so the human retains clear control.',
    'act4_deepening': 'Discrete differential geometry links four analytical pillars across Informatico.ai. In '
                      'Architecture (Folio A.01 and Folio A.11), compression-only vaults and polyhedral thrust '
                      'networks balance internal shell forces through mean-curvature geometry and well-conditioned '
                      'facet angles. In bending-active timber skins (Folio A.09), Gaussian curvature dictates whether '
                      'a flat sheet can bend into a doubly curved canopy without stretching or buckling. In structural '
                      'topology optimization (Folio E.11), smooth density-field filtering relies on discrete Laplace '
                      'operators whose positive weights prevent checkerboard instabilities and spurious extrema. '
                      'Checking Gauss–Bonnet closure alongside cotangent sign bounds in Toolbox X.07 equips small '
                      'studios and solo researchers with the same geometric safeguards that anchor larger '
                      'computational mechanics pipelines, without proprietary runtime dependencies.',
    'plain_es': 'Imaginen envolver un balón con pequeños triángulos planos de papel pegados cuidadosamente borde con '
                'borde. Si colocan las esquinas de papel alrededor de un punto sobre una mesa plana, notarán que falta '
                'una pequeña rebanada para cerrar el círculo completo porque el balón es curvo. Al sumar todas esas '
                'rebanadas faltantes en cada esquina del balón cerrado, el total da exactamente la misma cantidad sin '
                'importar cuántos triángulos usen. Esa suma constante sirve como una brújula rápida para revisar '
                'archivos tridimensionales antes de usarlos en un cálculo de ingeniería. Cuando una malla tiene '
                'triángulos demasiado delgados y estirados, los algoritmos de suavizado pueden oscilar y distorsionar '
                'resultados térmicos o mecánicos. Esta página entrega un visor en el navegador y scripts abiertos en '
                'Python para medir cada déficit angular, revisar áreas de Voronoi y exportar modelos limpios en GLB, '
                '3MF y STEP.',
    'deep_es': 'La auditoría geométrica de la herramienta X.07 separa la invariancia topológica del condicionamiento '
               'métrico sobre una 2-variedad cerrada M = (V, E, F) con V = 42, E = 120 y F = 80. En el nivel topológico, '
               'sumar los déficits angulares δ_v = 2π − ∑_j θ_{v,j} evaluados con atan2(||u × v||, u · v) reproduce '
               '2πχ = 4π rad con error inferior a 1e-12 rad. En el nivel métrico, las áreas mixtas de Voronoi de Meyer '
               '(2003) acotan triángulos obtusos a A_T / 2 y A_T / 4 para conservar el área total de 6,665.5656 mm². '
               'Al comprimir el semieje Z de 18 mm a 9 mm, la suma de Gauss–Bonnet permanece intacta, pero dieciséis de '
               'ciento veinte aristas violan la condición de Delaunay con pesos cotangentes negativos (w_min = '
               '−0.429055), ilustrando en código verificable la cota de Wardetzky et al. (2007).',
    'distill_diagram': {
        'analogy_title': 'The Tailored Canopy & Pinch',
        'analogy_sub': 'Sliver facets buckle smoothness even when seams close.',
        'force_a_title': 'Gauss–Bonnet Deficit ∑ δ_v = 4π',
        'force_a_sub': 'Corner angle gaps track closed 2-manifold topology χ = 2.',
        'force_b_title': 'Cotangent Weights w_{ij} ≥ 0',
        'force_b_sub': 'Opposite angles α + β ≤ π keep discrete diffusion monotone.',
        'threshold_title': 'Wardetzky–Meyer Delaunay Boundary',
        'threshold_pass': 'Dome (30,24,18) mm: ∑ δ_v = 4π, 0/120 non-Delaunay edges.',
        'threshold_fail': 'Pinched (30,24,9) mm: 16/120 negative cotangent weights; defect fails.',
    },
}
