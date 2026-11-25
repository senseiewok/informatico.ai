# -*- coding: utf-8 -*-
"""Tech & Tools · The Toolbox — Folio X.08: Polyhedral Mass Properties, Principal Inertia & Static Tip-Over Audit."""

FOLIO = {
    'slug': 'x08',
    'folio_id': 'X.08',
    'tool_id': 'TOOL-PHYS-MATH-2',
    'cat': 'physics_math',
    'plate_slug': 'x08',
    'pillar_label_en': 'Physics & Math Mechanics Toolbox · Rigid-Body Inertia & Static Equilibrium',
    'pillar_label_es': 'Herramientas de Física y Matemáticas · Inercia de Cuerpo Rígido y Equilibrio Estático',
    'badge_en': 'TOOLBOX X.08 · POLYHEDRAL INERTIA TENSOR + SUPPORT-HULL TIP-OVER AUDIT (GLB · 3MF · STEP)',
    'badge_es': 'HERRAMIENTA X.08 · TENSOR DE INERCIA POLIÉDRICO + AUDITORÍA DE VOLCAMIENTO (GLB · 3MF · STEP)',
    'title': 'Polyhedral Mass Properties, Principal Inertia & Static Tip-Over Audit',
    'title_es': 'Propiedades de Masa Poliédrica, Inercia Principal y Auditoría de Volcamiento',
    'subtitle': (
        'How a pure-Python standard-library audit computes signed simplex volume, center of mass, '
        'geometric principal moments of inertia, and base convex-hull tip-over margin across GLB, 3MF, and STEP.'
    ),
    'subtitle_es': (
        'Cómo una auditoría en Python estándar calcula el volumen por símplices con signo, el centro de masa, '
        'los momentos principales de inercia geométrica y el margen de volcamiento en GLB, 3MF y STEP.'
    ),
    'why_en': (
        'A cantilevered stone model, architectural study block, or printed part can pass every watertight '
        'half-edge check and still topple on the workbench as soon as gravity acts on its overhang. '
        'Integrating first and second moments across boundary triangles—and cross-checking them against '
        'rational three-cuboid sums—turns neutral 3D files into inspectable rigid-body balance models.'
    ),
    'why_es': (
        'Una maqueta en voladizo de piedra, madera o impresión tridimensional puede superar cada prueba '
        'de malla cerrada y aun así volcarse sobre la mesa en cuanto actúa su propio peso. Integrar los '
        'primeros y segundos momentos sobre los triángulos de frontera convierte archivos 3D neutros en '
        'modelos auditables de equilibrio estático.'
    ),
    'governing_law': 'r_cm = (1/V) ∑ V_f c_f · I_geom = tr(S_cm) I_3 − S_cm · I_1 + I_2 ≥ I_3 · m_tip > 0',
    'pass_pill_en': 'PASS · m_tip = +7.80 mm (θ = 14.30°) · I_1 + I_2 − I_3 > 0 · GLB+3MF+STEP',
    'pass_pill_es': 'APROBADO · m_tip = +7.80 mm (θ = 14.30°) · I_1 + I_2 − I_3 > 0 · GLB+3MF+STEP',
    'generator_script': 'skills/toolchain/x08/make_x08.py',
    'verifier_script': 'skills/toolchain/x08/verify_x08_toolchain_x08_polyhedral_inertia_tipover.py',
    'skill_dir': 'skills/toolchain/x08',
    'skill_name': 'toolchain-x08-polyhedral-inertia-tipover',
    'formats': ('glb', '3mf', 'step'),
    'primary_doi': '10.1080/10867651.1996.10487458',
    'scite_summary': (
        'Mirtich (1996) polyhedral mass integrals, Lien & Kajiya (1984) simplex decomposition, '
        'Kallay (2006) triangle-mesh inertia, Prévost et al. (2013) static balance, and Bächer et al. (2014) '
        'principal-axis inertia alignment checked offline.'
    ),
    'date_published': '2026-11-24',
    'date_redated': '2026-11-24',
    'current_edition': 'REV 1.0',
    'reading_time': '22 MIN READ',
    'small_studio_kit_en': (
        'Open Studio Rigid-Body Stack (Blender 4.2 + FreeCAD 1.0 + Python 3 stdlib): '
        'Run make_x08.py to emit x08_artifact.glb, x08_artifact.3mf, and x08_artifact.step for our '
        '16-vertex cantilevered pier-and-arm block; run verify_x08 to check simplex vs. Fraction cuboid '
        'inertia, Jacobi principal eigenvalues, triangle-inequality slack, and base tip-over margin.'
    ),
    'small_studio_kit_es': (
        'Stack Abierto de Equilibrio Rígido (Blender 4.2 + FreeCAD 1.0 + Python 3 stdlib): '
        'Ejecuta make_x08.py para generar x08_artifact.glb, x08_artifact.3mf y x08_artifact.step del '
        'bloque monolítico en voladizo de 16 vértices; corre verify_x08 para auditar centro de masa, '
        'autovalores principales de Jacobi, desigualdad triangular y margen de volcamiento.'
    ),
    'companion_folios': [
        ('architecture', 'a01', 'Folio A.01', 'Funicular Thrust Surfaces in Stone and Timber Shells'),
        ('engineering', 'e06', 'Folio E.06', 'ASCE 7-22 Seismic Base Isolation & Hysteretic Bearings'),
        ('engineering', 'e11', 'Folio E.11', 'SIMP Topology Optimization & Inerter Damping'),
        ('architecture', 'a11', 'Folio A.11', '3D Polyhedral Graphic Statics & Stone Vaults'),
    ],
    'external_links': [
        ('mikedh/trimesh (MIT Mesh Mass Properties)', 'https://github.com/mikedh/trimesh'),
        ('FreeCAD 1.0 (LGPL-2.0-or-later Parametric Solid Modeler)', 'https://www.freecad.org/'),
        ('Blender 4.2 LTS (Open 3D Modeling & glTF 2.0)', 'https://www.blender.org/'),
    ],
    'act1_dropcap': (
        'Inside a quiet stone-carving workshop in Florence, a master mason hangs a pointed brass plumb bob from a '
        'linen cord before lifting a cantilevered corbel block onto its square stone pier. On a computer screen, an '
        'overhanging timber arm joined to a slender stone post stands completely still because viewport '
        'cameras ignore gravity. Once that model leaves the screen for a milling table or desktop printer, '
        'mass distribution takes command. Every cubic millimeter of material pulls downward around the outer '
        'edge of the base footprint. If the combined balance point drifts even one millimeter past that '
        'supporting rim, the finished piece tips forward on the bench. Checking whether a closed mesh will '
        'stand upright—and how its mass resists rotation around three perpendicular axes—links pure '
        'polyhedral geometry to everyday physical craft.'
    ),
    'act1_plain_bridge': (
        'In plain words: a three-dimensional computer file can be completely watertight, free of holes, and '
        'still fall flat on its face the moment you set the physical object on a table. Whether a shape stands '
        'or tips depends on two geometric regions. First, you find the single balance point—the center of '
        'mass—where all the solid weight acts together. Second, you trace a rubber band around every flat '
        'bottom corner touching the tabletop to mark the base footprint. As long as a straight vertical line '
        'dropped from the balance point lands inside that footprint, the block rests upright. Push an '
        'upper arm too far outward and the line crosses the edge, tipping the piece over. This page provides '
        'a browser inspector and open Python scripts that compute volume, balance point, rotational inertia, '
        'and tipping distance across binary Graphics Language Transmission Format, Three-Dimensional '
        'Manufacturing Format, and Standard for the Exchange of Product Model Data files.'
    ),
    'act1_body': (
        'Evaluating rigid-body integrals directly from boundary facets has a clean mathematical lineage. '
        'Sheue-ling Lien and James Kajiya (IEEE Computer Graphics and Applications 1984, DOI '
        '10.1109/MCG.1984.6429334) presented a symbolic central-projection method that decomposes an '
        'arbitrary nonconvex polyhedron into signed three-dimensional simplices to integrate polynomials in '
        'time linear in the size of the boundary. Brian Mirtich (Journal of Graphics Tools 1996, DOI '
        '10.1080/10867651.1996.10487458) formulated a single-walk boundary reduction for uniform-density '
        'polyhedral center of mass and moments and products of inertia that limits alignment conditioning '
        'errors, and Michael Kallay (Journal of Graphics Tools 2006, DOI 10.1080/2151237X.2006.10129220) '
        'gave a compact triangle-mesh inertia expression. In digital fabrication, Romain Prévost, Emily '
        'Whiting, Sylvain Lefebvre, and Olga Sorkine-Hornung (ACM Transactions on Graphics 2013, DOI '
        '10.1145/2461912.2461957) noted that fabricated 3D models topple when imbalanced poses meet gravity '
        'and formulated volume-modifying energy minimization so printed shapes stand without glue or heavy '
        'pedestals, while Moritz Bächer, Whiting, Bernd Bickel, and Sorkine-Hornung (ACM Transactions on '
        'Graphics 2014, DOI 10.1145/2601097.2601157) optimized internal adaptive voxel voids to align '
        'principal inertia directions with a target spin axis and maximize the dominant principal moment.'
    ),
    'act1_stakes': (
        'Important Educational Non-Design Boundary: this monograph and its companion scripts provide an '
        'explanation of polyhedral integral geometry and rigid-body statics, not a structural, seismic, '
        'foundation, rigging, or fabrication design method. None of the numbers computed on this page may '
        'be used on a real building element, cantilevered bracket, sculpture mount, or load-bearing support, '
        'because overturning in the physical world also depends on wind, ground slope, material inhomogeneity, '
        'base crushing, dynamic impact, and local safety codes. Within educational modeling and open-source '
        'geometry pipelines, pairing Mirtich and Kallay simplex integration with a rational cuboid cross-check '
        'catches two silent failure modes in exported meshes: a watertight overhang whose center of mass exits '
        'its downward-oriented base polygon, and an inverted cavity or corrupted tensor that violates the '
        'rigid-body triangle inequality.'
    ),
    'pullquote': (
        'Watertight half-edge pairing keeps a polyhedron closed, yet static balance requires the projected '
        'center of mass to stay inside the downward-oriented base convex hull while principal moments obey '
        'I_1 + I_2 ≥ I_3.'
    ),
    'chronology': [
        (
            '1984',
            'Sheue-ling Lien and James T. Kajiya publish symbolic simplex decomposition for polynomial '
            'integrals over arbitrary nonconvex polyhedra (DOI 10.1109/MCG.1984.6429334).',
        ),
        (
            '1996',
            'Brian Mirtich publishes single-walk volume-integral reductions for uniform-density polyhedral '
            'center of mass and inertia tensors (DOI 10.1080/10867651.1996.10487458).',
        ),
        (
            '2006',
            'Michael Kallay publishes a simplified closed-form moment-of-inertia expression for solids '
            'bounded by triangle meshes (DOI 10.1080/2151237X.2006.10129220).',
        ),
        (
            '2013',
            'Prévost, Whiting, Lefebvre, and Sorkine-Hornung formulate Make It Stand volume optimization '
            'so fabricated 3D-printed models stand without toppling (DOI 10.1145/2461912.2461957).',
        ),
        (
            '2014',
            'Bächer, Whiting, Bickel, and Sorkine-Hornung introduce Spin-It internal void optimization to '
            'align principal inertia directions with a rotation axis (DOI 10.1145/2601097.2601157).',
        ),
        (
            '2026',
            'Informatico.ai ships X.08: a 16-vertex conforming cantilevered block audited simultaneously by '
            'surface-simplex integration, rational three-cuboid decomposition, Jacobi eigensolvers, and '
            'base-hull tip-over distance.',
        ),
    ],
    'act2_analogy': (
        'Picture setting a thick stoneware mug on a narrow cork coaster and attaching a heavy wooden spoon '
        'horizontally out from the rim. While the spoon is short, the combined balance point sits comfortably '
        'over the flat circular foot of the mug, and a gentle nudge rocks the mug back to rest. Slide a '
        'longer, heavier spoon outward along the rim and the balance point creeps toward the right edge of '
        'the foot; the instant it crosses that rim, gravity tips the mug sideways off the coaster. Here is '
        'where the picture stops: a mug on soft cork compresses its rim and slides under table friction, '
        'whereas our polyhedral model treats the solid and horizontal plane as idealized, uniform-density '
        'rigid geometry with zero elastic deformation.'
    ),
    'act2_plain_primer': (
        'In the Act III workbench below, two sliders reshape our sixteen-vertex cantilevered block while '
        'keeping the supporting vertical pier fixed at twenty-four millimeters wide, thirty millimeters deep, '
        'and thirty-six millimeters tall up to the underside of the arm. The first slider varies Cantilever '
        'Reach between six and fifty-two millimeters, extending the overhanging horizontal arm to the right '
        'of the pier. The second slider varies Cap Thickness between eight and thirty millimeters, thickening '
        'the top cap across both pier and overhang. In the four readout boxes, Readout 0 displays fixed '
        'manifold vertex, edge, and face counts on the normal mesh (switching to unpaired-edge counts when '
        'the Planted-Defect mode button is active), while Readouts 1, 2, and 3 recompute live center-of-mass '
        'margin, all three principal geometric inertia moments, and the tip-over boundary gate.'
    ),
    'act2_intuition': (
        'Our own stdlib solver combines surface-simplex integration with two geometric coordinate checks '
        'under assumed model dimensions b = 24 mm, W = 30 mm, and h_stem = 36 mm, factoring out uniform mass '
        'density ρ so geometric inertia I_geom = I / ρ carries pure units of mm⁵. Each oriented boundary '
        'triangle f = (a, b, c) spans a signed tetrahedron T_f with the origin of signed volume V_f = '
        '(1/6) a · (b × c). Summing V_f gives total volume V, and weighting each tetrahedron centroid '
        '(a + b + c) / 4 gives the center of mass r_cm = (1/V) ∑_f V_f (a + b + c) / 4. Using the canonical '
        'simplex quadratic form over T_f, the second-moment matrix about the origin is S^(O)_{pq} = '
        '∑_f (V_f / 20) ((a_p + b_p + c_p)(a_q + b_q + c_q) + a_p a_q + b_p b_q + c_p c_q). Shifting to r_cm '
        'by the Huygens–Steiner parallel-axis identity S^(cm)_{pq} = S^(O)_{pq} − V r_{cm,p} r_{cm,q} yields '
        'the central geometric inertia tensor I^(cm)_{pq} = tr(S^(cm)) δ_{pq} − S^(cm)_{pq}, which a cyclic '
        '3×3 Jacobi rotation diagonalizes into principal moments I_1 ≤ I_2 ≤ I_3.'
    ),
    'act2_deepening': (
        'Open Question, Hypothesis (Tier T0/T1), and Falsification Boundary: can an offline standard-library '
        'audit separate topological mesh closure from rigid-body physical realizability and static tipping '
        'across GLB, STEP, and 3MF? On our baseline cantilevered solid (L_c = 18 mm, t_cap = 18 mm; Tier T0 '
        'model computation), surface-simplex integration and an independent fractions.Fraction three-cuboid '
        'parallel-axis calculation agree to 0.00e+00 mm⁵ across all nine inertia components: V = 48,600.0 mm³, '
        'r_cm = (16.2000, 0.0000, 30.6000) mm, I_1 = 8,092,688.82 mm⁵, I_2 = 16,984,911.18 mm⁵, I_3 = '
        '17,787,600.00 mm⁵, triangle-inequality slack I_1 + I_2 − I_3 = 2 S^(cm)_{yy} = 7,290,000.00 mm⁵ > 0, '
        'and signed inward distance from (x_cm, y_cm) to the downward-normal base hull [0, 24] × [−15, 15] mm '
        'is m_tip = +7.8000 mm (static tilt angle θ_tip = atan2(7.8, 30.6) = 14.3003°). Balancing pier and '
        'arm moments about x = b gives the closed-form tipping reach L_{c,crit}(t_cap) = b √(1 + h_stem / '
        't_cap) = 24 √(1 + 36 / t_cap), or 41.5692 mm at t_cap = 18 mm and 37.9473 mm at t_cap = 24 mm. '
        'Hypothesis (Tier T0 model test): extending (L_c, t_cap) to (48, 24) mm preserves watertight '
        'Euler closure (V = 16, E = 42, F = 28, χ = 2, V = 77,760.0 mm³) while shifting r_cm to (28.0, 0.0, '
        '38.0) mm and flipping m_tip to −4.0000 mm (θ_tip = −6.0090°). Any mesh with m_tip ≤ 0 mm falsifies '
        'flat-plane static equilibrium, and any tensor with I_1 ≤ 0 or I_1 + I_2 < I_3 falsifies positive-mass '
        'rigid-body realizability.'
    ),
    'sliders': [
        {'id': 'tp-tool-s0', 'label': 'Cantilever Reach L_c', 'min': 6, 'max': 52, 'step': 2, 'value': 18, 'unit': ' mm'},
        {'id': 'tp-tool-s1', 'label': 'Cap Thickness t_cap', 'min': 8, 'max': 30, 'step': 2, 'value': 18, 'unit': ' mm'},
    ],
    'readouts': [
        {'label': '2-Manifold Topology (Fixed Mesh Text)', 'value': 'V=16, E=42, F=28 · χ=2'},
        {'label': 'CoM x_cm & Base Tip Margin m_tip', 'value': 'x_cm=16.20 mm · m_tip=+7.80 mm (14.30°)'},
        {'label': 'Principal Inertia I_1..I_3 (I/ρ)', 'value': '8.09 / 16.98 / 17.79 ×10⁶ mm⁵'},
        {'label': 'Equilibrium & Knockout Gate', 'value': 'PASS · STANDS IN BASE HULL'},
    ],
    'steps': [
        'Stage 1: Conforming 16-Vertex Cantilever Synthesis — Assemble occupied grid cells (0,0,0), (0,0,1), '
        'and (1,0,1) on x ∈ {0, 24, 24 + L_c} mm, y ∈ {−15, +15} mm, and z ∈ {0, 36, 36 + t_cap} mm to emit '
        '28 outward-oriented triangles with zero T-junctions across GLB, 3MF, and STEP AP242.',
        'Stage 2: Dual Simplex vs. Rational Cuboid Integration — Integrate V = 48,600.0 mm³, r_cm = '
        '(16.2, 0.0, 30.6) mm, and central geometric inertia I_geom (mm⁵) over boundary tetrahedra and '
        'cross-check every component against an independent fractions.Fraction three-cuboid parallel-axis sum.',
        'Stage 3: Cyclic 3×3 Jacobi Diagonalization & Triangle Inequality — Diagonalize I_geom into '
        'I_1 = 8,092,688.82, I_2 = 16,984,911.18, and I_3 = 17,787,600.00 mm⁵, checking eigenvector '
        'orthogonality (< 1e-11), I_1 > 0, and slack I_1 + I_2 − I_3 = 7,290,000.00 mm⁵ ≥ 0.',
        'Stage 4: Downward-Normal Support Hull & Tip-Over Knockout — Extract z = 0 contact vertices strictly '
        'from downward −Z triangles, compute the 2D monotone-chain hull, check m_tip = +7.80 mm > 0 at '
        '(18, 18) mm, and check rejection at (48, 24) mm (m_tip = −4.00 mm) and under --planted-defect.',
    ],
    'rules': [
        'Non-Design Educational Safety Boundary: This skill and verifier explain idealized uniform-density '
        'polyhedral geometry and statics; do not use their outputs as a structural, seismic, foundation, '
        'rigging, or fabrication design check on real parts or structures.',
        'Dual-Method Inertia & Realizability Invariant: Surface-simplex volume, centroid, and central '
        'geometric inertia must match the rational cuboid parallel-axis sum within 1e-2 mm⁵ on the reference '
        'solid, and principal moments must satisfy I_1 > 0 and I_1 + I_2 − I_3 ≥ 0.',
        'Downward-Normal Support Hull & Knockout Invariant: Base support vertices on z = z_min must belong '
        'to downward-oriented faces (n_z ≤ −1 + 1e-7), baseline m_tip must equal +7.80 mm within 1e-4 mm, '
        'and both the (48, 24) mm overhang (m_tip = −4.00 mm) and flipped triangle 0 must fail closed.',
    ],
    'sidenote_1': {
        'kicker': 'SIDENOTE X.08-A · WHY CONFORMING GRIDS AVOID T-JUNCTIONS',
        'body': (
            'Placing an 18 mm tall cantilever arm directly against an undivided 54 mm pier wall creates '
            'unpaired T-junction edges at z = 36 mm. Splitting the pier at z = 36 mm keeps 3F = 2E (42 edges, '
            '28 faces, 0 unpaired half-edges) across every slider setting.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE X.08-B · CLOSED-FORM TRIANGLE-INEQUALITY SLACK',
        'body': (
            'Because the block is symmetric across y ∈ [−15, +15] mm, I_yy = 17,787,600.0 mm⁵ is the largest '
            'principal moment I_3, and I_1 + I_2 − I_3 equals 2 S^(cm)_{yy} = (1/6) V W² = 7,290,000.0 mm⁵.'
        ),
    },
    'walkthrough': [
        'Orbit the 16-vertex limestone-and-walnut cantilevered solid in the WebGL2 stage below; notice how '
        'the pier footprint spans x ∈ [0, 24] mm while the upper arm overhangs to x = 42 mm at baseline.',
        'Drag Cantilever Reach L_c past 42 mm at Cap Thickness t_cap = 18 mm (crossing L_{c,crit} = 41.57 mm) '
        'and watch live x_cm cross 24.00 mm while m_tip flips negative in Readouts 1 and 3.',
        'Click Planted-Defect / Boundary Knockout to jump to (L_c = 48 mm, t_cap = 24 mm, m_tip = −4.00 mm), '
        'or export custom .glb and .step solids whose piecewise pier dimensions stay unstretched.',
    ],
    't0_t1_certified': [
        'Deterministic Python stdlib generator (skills/toolchain/x08/make_x08.py) emitting x08_artifact.glb, '
        'watertight x08_artifact.3mf, and B-rep x08_artifact.step for the 16-vertex cantilevered monolith.',
        'Dual-method stdlib verifier (verify_x08_toolchain_x08_polyhedral_inertia_tipover.py) cross-checking '
        'surface-simplex moments against fractions.Fraction three-cuboid sums, 3×3 Jacobi eigenvalues, '
        'I_1 + I_2 ≥ I_3, and downward-normal base convex-hull margin m_tip = +7.80 mm.',
        'Negative controls rejecting the (48, 24) mm tip-over geometry (m_tip = −4.00 mm), non-physical '
        'inertia tensors (I_1 + I_2 < I_3), flipped base winding, and malformed 3MF XML.',
    ],
    't2_t3_open_horizon': [
        'Educational Non-Design Boundary: Every file and readout on this page is an explanatory geometric '
        'model, not a structural, seismic, rigging, or fabrication design calculation.',
        'Future Edition 2 Extensions: Multi-material density fields, frictional inclined-plane sliding '
        'envelopes, and internal void optimization remain outside this uniform-density static check.',
    ],
    'sources': [
        'Mirtich, B. (1996). Fast and accurate computation of polyhedral mass properties. Journal of Graphics '
        'Tools, 1(2), 31–50. DOI 10.1080/10867651.1996.10487458',
        'Lien, S., & Kajiya, J. T. (1984). A symbolic method for calculating the integral properties of '
        'arbitrary nonconvex polyhedra. IEEE Computer Graphics and Applications, 4(10), 35–42. DOI '
        '10.1109/MCG.1984.6429334',
        'Kallay, M. (2006). Computing the moment of inertia of a solid defined by a triangle mesh. Journal '
        'of Graphics Tools, 11(2), 51–57. DOI 10.1080/2151237X.2006.10129220',
        'Prévost, R., Whiting, E., Lefebvre, S., & Sorkine-Hornung, O. (2013). Make it stand: balancing '
        'shapes for 3D fabrication. ACM Transactions on Graphics, 32(4), 1–10. DOI 10.1145/2461912.2461957',
        'Bächer, M., Whiting, E., Bickel, B., & Sorkine-Hornung, O. (2014). Spin-it: optimizing moment of '
        'inertia for spinnable objects. ACM Transactions on Graphics, 33(4), 1–10. DOI '
        '10.1145/2601097.2601157',
    ],
    'act4_human_ai': (
        'When a practitioner or student asks an AI assistant to adjust a cantilevered form in Python CAD, '
        'checking only whether the exported mesh is watertight leaves mechanical balance unexamined. Folio '
        'X.08 pairs parametric authoring with an inspectable geometric gate. Following SKILL.md, an agent can '
        'modify cantilever reach or cap thickness in make_x08.py and run verify_x08 locally without external '
        'packages or network access. The verifier parses the resulting GLB, STEP AP242, and 3MF files byte by '
        'byte, checks that surface-simplex integrals match rational cuboid parallel-axis formulas on the '
        'reference shape, diagonalizes the 3×3 central geometric inertia tensor, and checks whether the '
        'projected center of mass remains inside the downward-oriented base polygon. Any edit that pushes '
        'm_tip to zero or below—or flips a base triangle normal—stops with a numeric diagnostic.'
    ),
    'act4_deepening': (
        'Polyhedral mass and support-hull geometry connect four analytical threads across Informatico.ai. In '
        'Architecture (Folio A.01 and Folio A.11), stone voussoirs and compression shells remain standing '
        'when resultant thrust lines stay inside geometric kern boundaries, the structural counterpart of a '
        'projected center of mass staying inside its base hull. In seismic engineering (Folio E.06) and '
        'structural optimization (Folio E.11), translational mass and rotational inertia matrices govern '
        'natural rocking and vibration periods under base excitation. Within the Toolbox itself, X.08 '
        'completes the five-step geometric audit sequence from half-edge topology (X.01), B-rep chordal '
        'sagitta (X.02), and build-plate overhang slope (X.05) to discrete curvature (X.07) and rigid-body '
        'balance—giving independent makers and educators a transparent, zero-cost way to inspect 3D solids.'
    ),
    'plain_es': (
        'Aviso educativo importante: esta página ofrece una explicación geométrica y de estática de cuerpos '
        'rígidos, no un método de diseño estructural, sísmico, de cimentación ni de fabricación; ninguno de '
        'sus valores de modelo debe aplicarse a una estructura o soporte real. En palabras sencillas, un '
        'archivo tridimensional puede estar completamente cerrado, sin huecos en su malla, y aun así caerse '
        'de frente al colocar la pieza física sobre una mesa. Que un bloque permanezca de pie depende de dos '
        'elementos: el centro de masa donde se concentra su peso y el polígono de apoyo formado por las caras '
        'inferiores que tocan la mesa. Mientras la plomada vertical que baja desde el centro de masa caiga '
        'dentro de esa huella, la pieza descansa estable; si el brazo superior se alarga demasiado y cruza el '
        'borde, se vuelca.'
    ),
    'deep_es': (
        'Este modelo explicativo (no apto para diseño real) integra propiedades de masa sobre nuestro bloque '
        'monolítico en voladizo de dieciséis vértices, cuarenta y dos aristas y veintiocho caras (χ = 2) con '
        'dimensiones base asumidas b = 24 mm, W = 30 mm y h_stem = 36 mm, factorizando la densidad uniforme '
        'ρ para expresar la inercia geométrica I_geom = I / ρ en mm⁵. En el punto de referencia (L_c = 18 mm, '
        't_cap = 18 mm), la integración por símplices superficiales y la suma paralela en fractions.Fraction '
        'sobre tres cuboides coinciden en V = 48,600.0 mm³, r_cm = (16.2, 0.0, 30.6) mm, momentos principales '
        'I_1 = 8,092,688.82, I_2 = 16,984,911.18 e I_3 = 17,787,600.00 mm⁵ (holgura triangular '
        '7,290,000.00 mm⁵ > 0) y margen de apoyo m_tip = +7.80 mm (inclinación estática 14.30°). Al extender '
        'a (48, 24) mm, la malla sigue siendo hermética pero r_cm pasa a (28.0, 0.0, 38.0) mm y m_tip cae a '
        '−4.00 mm.'
    ),
    'distill_diagram': {
        'analogy_title': 'The Coaster, Mug & Heavy Spoon',
        'analogy_sub': 'Extending an overhanging handle shifts the plumb line toward the rim.',
        'force_a_title': 'Pier Stabilizing Moment (x ∈ [0, 24] mm)',
        'force_a_sub': 'Vertical post mass anchors x_cm inside the downward −Z base hull.',
        'force_b_title': 'Cantilever Arm Moment & Principal I/ρ',
        'force_b_sub': 'Overhanging mass pulls x_cm outward and rotates principal inertia axes.',
        'threshold_title': 'Base Support Edge x = 24 mm & I_1 + I_2 ≥ I_3',
        'threshold_pass': 'Baseline (18, 18) mm: x_cm = 16.20 mm, m_tip = +7.80 mm (14.30°), I_1 + I_2 > I_3.',
        'threshold_fail': 'Extended (48, 24) mm: x_cm = 28.00 mm, m_tip = −4.00 mm; tips across x = 24 mm.',
    },
}
