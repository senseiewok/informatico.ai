# -*- coding: utf-8 -*-
"""Tech & Tools · The Toolbox — Folio X.05: Topology-Optimized Structural Struts to Watertight 3MF & Build-Plate Overhang Audit."""

FOLIO = {
    'slug': 'x05',
    'folio_id': 'X.05',
    'tool_id': 'TOOL-FAB-1',
    'cat': 'engineering',
    'plate_slug': 'x05',
    'pillar_label_en': 'Additive & Structural Toolbox · Tapered Struts to Watertight 3MF',
    'pillar_label_es': 'Herramientas Aditivas y Estructurales · Puntales Ahusados a 3MF Hermético',
    'badge_en': 'TOOLBOX X.05 · TAPERED STRUT FRUSTUM → MANIFOLD 3MF · GLB · STEP + OVERHANG AUDIT',
    'badge_es': 'HERRAMIENTA X.05 · TRONCO AHUSADO → 3MF · GLB · STEP HERMÉTICO + AUDITORÍA DE VOLADIZO',
    'title': 'Topology-Optimized Structural Struts to Watertight 3MF & Build-Plate Overhang Audit',
    'title_es': 'Puntales Estructurales Optimizados por Topología a 3MF Hermético y Auditoría de Voladizo',
    'subtitle': (
        'How an illustrative four-station tapered strut is triangulated into closed 2-manifold 3MF, '
        'GLB, and Part-21 STEP files while pure Python checks frustum volume and build-plate overhang slope.'
    ),
    'subtitle_es': (
        'Cómo un puntal ahusado ilustrativo de cuatro estaciones se triangula en archivos cerrados '
        '2-variedad 3MF, GLB y STEP Parte 21 mientras Python puro audita el volumen y el ángulo de voladizo.'
    ),
    'why_en': (
        'Thresholding a voxel topology-optimization grid into triangles can leave open seams, '
        'inverted normals, or steep overhangs that stall desktop slicers. Stitching an illustrative '
        'tapered strut from closed rings—and checking half-edge pairing, volume, and wall tilt '
        'offline—turns an opaque export into an inspectable geometric record.'
    ),
    'why_es': (
        'Convertir una malla de vóxeles de optimización topológica en triángulos puede dejar bordes '
        'abiertos, normales invertidas o voladizos pronunciados que detienen los laminadores. Tejer '
        'un puntal ahusado ilustrativo desde anillos cerrados permite auditar semi-aristas, volumen '
        'y pendiente de pared fuera de línea.'
    ),
    'governing_law': (
        'V = ∑_{k=1}^3 (h_k / 3)(A_{k-1} + A_k + √(A_{k-1} A_k)) = 46,080 mm³ · '
        'θ_wall = arcsin(max(0, −n_f · ẑ)) = arctan(max(0, Δhw) / Δz) = 14.04° ≤ 45°'
    ),
    'pass_pill_en': 'PASS · V = 46,080 mm³ · θ_max = 14.04° ≤ 45° · 3MF+GLB+STEP',
    'pass_pill_es': 'APROBADO · V = 46,080 mm³ · θ_max = 14.04° ≤ 45° · 3MF+GLB+STEP',
    'generator_script': 'skills/toolchain/x05/make_x05.py',
    'verifier_script': 'skills/toolchain/x05/verify_x05_toolchain_x05_simp_manifold_3mf.py',
    'skill_dir': 'skills/toolchain/x05',
    'skill_name': 'toolchain-x05-simp-manifold-3mf',
    'formats': ('glb', '3mf', 'step'),
    'primary_doi': '10.1007/s001580050176',
    'scite_summary': (
        'Grounded in Michell (1904), Bendsøe (1989), Bendsøe & Sigmund (1999), Sigmund (2001), '
        'Mirtich (1996), Crane et al. (2013), and Feeney et al. (2015), checked offline.'
    ),
    'date_published': '2026-11-08',
    'date_redated': '2026-11-08',
    'current_edition': 'REV 1.0',
    'reading_time': '22 MIN READ',
    'small_studio_kit_en': (
        'Independent Structural & Maker Stack (Manifold Apache-2.0 + OrcaSlicer / PrusaSlicer + '
        'FreeCAD): Run make_x05.py to emit x05_artifact.3mf (1,769 B), x05_artifact.glb (2,936 B), '
        'and Part-21 x05_artifact.step (11,824 B), then run verify_x05 to check half-edge closure, '
        'frustum volume, and lateral overhang slope.'
    ),
    'small_studio_kit_es': (
        'Stack Abierto para Ingenieros y Makers (Manifold Apache-2.0 + OrcaSlicer / PrusaSlicer + '
        'FreeCAD): Ejecuten make_x05.py para generar x05_artifact.3mf (1,769 B), x05_artifact.glb '
        '(2,936 B) y x05_artifact.step Parte 21 (11,824 B), y corran verify_x05 para auditar '
        'semi-aristas, volumen de tronco piramidal y pendiente de voladizo.'
    ),
    'companion_folios': [
        ('engineering', 'e11', 'Folio E.11', 'SIMP Topology Optimization & Inerter Dampers'),
        ('physics', 'p07', 'Folio P.07', 'Formula 1 Ground-Effect Venturi Aerodynamics'),
        ('engineering', 'e10', 'Folio E.10', '3D Concrete Printing Thixotropy & Suiker Buckling'),
        ('math', 'm09', 'Folio M.09', 'Benamou–Brenier Wasserstein-2 Optimal Transport'),
    ],
    'external_links': [
        ('elalish/manifold (Apache-2.0 Exact Manifold CSG)', 'https://github.com/elalish/manifold'),
        ('3MF Consortium Core & Beam Lattice Specifications', 'https://github.com/3MFConsortium/spec_core'),
        ('TopOpt Group (DTU Mechanical Engineering)', 'https://www.topopt.mek.dtu.dk/'),
    ],
    'act1_dropcap': (
        'In 1904, the Australian engineer Anthony George Maldon Michell derived minimum-volume frame '
        'layouts whose tension and compression members follow orthogonal curves. Workshop mills could '
        'rarely carve such branching ribs from solid metal stock. Eight decades later in Denmark, '
        'Martin Bendsøe and Ole Sigmund recast layout optimization as continuous material '
        'distribution across finite-element grids. Yet turning a pixelated density grid into a clean '
        'solid boundary remains tricky. Thresholded voxel surfaces can leave stepped facets, open '
        'seams, or inverted triangles that stall additive slicers. Rather than extracting noisy '
        'isosurfaces, this page constructs an illustrative four-station tapered strut directly from '
        'closed square rings. A standard-library verification script then audits every shared edge, '
        'enclosed cubic millimeter, and outward wall tilt across three open file formats. The result '
        'is an educational geometry walkthrough, never a structural design method for a real '
        'load-bearing part.'
    ),
    'act1_plain_bridge': (
        'Think of a digital part for a three-dimensional printer like a cardboard shell taped along '
        'every corner, where one open seam or flipped triangle leaves slicing software unable to '
        'separate solid interior from empty air. Steep overhangs pose a second hurdle. Walls leaning '
        'far past vertical sag without temporary supports beneath them. Here, an illustrative '
        'tapered strut is stitched from four horizontal square rings so every edge pairs cleanly by '
        'construction. Move the two browser sliders to adjust its middle waist and top flare while '
        'volume and wall tilt update live on screen. Download the neutral files and run the Python '
        'checker offline on your own geometry. This page is an explanation of mesh and overhang '
        'geometry, not a structural design method. '
        'None of its numbers or files may be used on a real structure.'
    ),
    'act1_body': (
        'Bendsøe (1989, DOI 10.1007/bf01650949) posed shape optimization as material distribution, '
        'Bendsøe and Sigmund (1999, DOI 10.1007/s004190050248) compared power-law interpolation '
        'against microstructural bounds, and Sigmund (2001, DOI 10.1007/s001580050176) published a '
        '99-line compliance-minimization code. Exporting solid files requires boundaries that '
        'separate interior from exterior (Requicha, 1980, DOI 10.1145/356827.356833), as enforced in '
        'Emmett Lalish’s Apache-2.0 Manifold library and unit-indexed 3MF Core v1.2.3 archives. '
        'Here, make_x05.py builds a prescribed four-ring strut—an illustrative fixture, not a '
        'finite-element SIMP output—into x05_artifact.3mf (1,769 B), x05_artifact.glb (2,936 B), and '
        'an illustrative Part-21 POLY_LOOP sketch x05_artifact.step (11,824 B; compare full analytic '
        'EDGE_LOOP STEP AP242 exchange in Feeney, Frechette, & Srinivasan, 2015, DOI '
        '10.1115/1.4029050). This folio is an explanation, not a design method, and none of its '
        'numbers or files may be used on a real structure.'
    ),
    'act1_stakes': (
        'When an exported mesh carries an unpaired half-edge, a flipped normal, or an unnoticed '
        'downward ledge, smooth shading can hide the flaw until a slicer or mesher aborts. Checking '
        'closure and wall tilt in standard Python lets solo engineers, students, and small workshops '
        'inspect open mesh archives in continuous integration without paid repair suites. The '
        'companion verifier parses all three committed files, checks single-shell edge pairing, '
        'recomputes the three-segment frustum volume sum, and audits every non-base facet normal '
        'against an illustrative forty-five-degree overhang rule of thumb.'
    ),
    'pullquote': (
        'Checking half-edge closure (3F = 2E) and facet overhang tilt θ_wall = arcsin(max(0, −n_f · '
        'ẑ)) verifies only a geometric mesh; qualifying any real structural part requires physical '
        'engineering analysis and testing that this educational script never performs.'
    ),
    'chronology': [
        (
            '1904',
            'A. G. M. Michell derives analytical minimum-volume frame layouts along orthogonal '
            'strain trajectories (DOI 10.1080/14786440409463229).',
        ),
        (
            '1989–2001',
            'Martin Bendsøe (1989, DOI 10.1007/bf01650949), Bendsøe and Ole Sigmund (1999, DOI '
            '10.1007/s004190050248), and Sigmund (2001, DOI 10.1007/s001580050176) establish '
            'material-distribution interpolation and the 99-line educational SIMP code.',
        ),
        (
            '1996–2015',
            'Brian Mirtich (1996, DOI 10.1080/10867651.1996.10487458) formulates polyhedral '
            'divergence-volume integration; Feeney et al. (2015, DOI 10.1115/1.4029050) review the '
            'ISO 10303-242 STEP AP242 exchange and PMI tolerancing standard.',
        ),
        (
            '2026',
            'Informatico.ai ships X.05: an illustrative four-station tapered strut exported to 3MF, '
            'GLB, and Part-21 STEP with frustum-volume and facet-overhang verification.',
        ),
    ],
    'act2_analogy': (
        'Picture a mason corbeling flat courses of brick outward from a pillar, stepping each layer '
        'slightly past the one below without wooden falsework. So long as each outward step stays '
        'modest relative to course height, the wall rests stably while its outer faces form one '
        'continuous skin. Where the analogy stops: real masonry resists collapse through mortar '
        'bedding, friction, and dead-weight compression, whereas our digital audit measures only '
        'combinatorial triangle pairing and geometric facet slope without modeling gravity, polymer '
        'rheology, thermal warping, or buckling.'
    ),
    'act2_plain_primer': (
        'Two sliders and one mode toggle drive the workbench below. Mid-Span Waist Width sets the '
        'full square width at the thirty-two-millimeter waist between 12 and 36 millimeters '
        '(widening past 32 millimeters also tilts the middle segment outward). Upper Head Flare adds '
        '0 to 24 millimeters of outward half-width per side at the forty-eight-millimeter crown '
        'relative to the waist, raising lateral overhang from 0 degrees to 14.04 degrees at 4 '
        'millimeters and crossing 45 degrees above 16 millimeters. The second readout card stays '
        'fixed text because all slider settings keep the same 28-triangle connectivity. Clicking the '
        'Planted-Defect / Boundary Knockout button resets Mid-Span Waist Width to 24 millimeters and '
        'sets Upper Head Flare to 20 millimeters (51.34 degrees, 66,560.0 cubic millimeters) to fire '
        'the browser overhang alert, while running the Python verifier with its planted-defect flag '
        'flips Triangle 0 in memory to test half-edge rejection.'
    ),
    'act2_intuition': (
        'Two elementary relations govern the illustrative strut across z ∈ {0, 16, 32, 48} mm with '
        'square half-widths hw ∈ {20, 16, 12, 16} mm (areas A ∈ {1,600, 1,024, 576, 1,024} mm²). '
        'Summing the square-frustum formula across the three h_k = 16 mm segments gives V = '
        '∑_{k=1}^3 (h_k / 3)(A_{k-1} + A_k + √(A_{k-1} A_k)) = 20,821.33 + 12,629.33 + 12,629.33 = '
        '46,080.0 mm³, matching the boundary divergence sum V = (1/6) ∑ v_0 · (v_1 × v_2) (Mirtich, '
        '1996, DOI 10.1080/10867651.1996.10487458). A lateral wall rising by Δz with outward '
        'half-width change Δhw = Δw / 2 has unit normal n_f = (Δz, 0, −Δhw) / √(Δz² + Δhw²) on the '
        '+X face, so −n_f · ẑ = sin θ_wall (whereas arccos(−n_f · ẑ) = 75.96° is the polar '
        'complement). Thus θ_wall = arcsin(max(0, −n_f · ẑ)) = arctan(max(0, Δhw) / Δz) equals 0° '
        'below z = 32 mm and arctan(4 / 16) = 14.04° on the flared head, within an assumed 45.0° '
        'rule-of-thumb ceiling (not a material constant). Paired half-edges (3F = 2E; Crane et al., '
        '2013, DOI 10.1145/2504435.2504442) close V = 16, E = 42, F = 28 into χ = 2.'
    ),
    'act2_deepening': (
        'In Requicha’s (1980, DOI 10.1145/356827.356833) framework, rigid solids are regular closed '
        'point sets; the stricter single-shell 2-manifold and overhang checks here belong to '
        'run_x05_strut_checks in tools/toolchain_x05_checks.py. Build-plate contact is identified '
        'strictly by vertex elevation (all three vertices at z = 0 mm), never by n_z ≈ −1 alone: the '
        '2 base facets sit on the bed, whereas any suspended horizontal soffit at z > 0 evaluates '
        'arcsin(1) = 90.0° and fails closed. Across the other 26 facets, 2 crown facets face +Z, 16 '
        'lower wall facets taper inward at −14.0362° (0° overhang), and 8 head facets flare outward '
        'at +14.0362°. In src/modules/glb-viewer.mjs, slider moves update the z = 32 and z = 48 '
        'rings, recompute WebGL2 vertex normals and signed volume, and evaluate max(0, hw_2 − 16, '
        'Δhw_top) for live GLB and Part-21 STEP export.'
    ),
    'sliders': [
        {
            'id': 'tp-tool-s0',
            'label': 'Mid-Span Waist Width',
            'min': 12,
            'max': 36,
            'step': 2,
            'value': 24,
            'unit': ' mm',
        },
        {
            'id': 'tp-tool-s1',
            'label': 'Upper Head Flare',
            'min': 0,
            'max': 24,
            'step': 2,
            'value': 4,
            'unit': ' mm',
        },
    ],
    'readouts': [
        {'label': '3-Stage Frustum Volume', 'value': '46,080.0 mm³ (ΔV = 0.00%)'},
        {'label': '2-Manifold Closure (V, E, F)', 'value': 'V=16, E=42, F=28 · χ=2'},
        {'label': 'Max Wall Overhang Angle θ', 'value': '14.04° ≤ 45.0° (GEOMETRY)'},
        {'label': '3MF / GLB / STEP Gate', 'value': 'PASS · DEFECT REJECTED'},
    ],
    'steps': [
        'Stage 1: Four-Station Strut Rings — Place square stations along z ∈ {0, 16, 32, 48} mm with '
        'half-widths hw ∈ {20, 16, 12, 16} mm (widths 40, 32, 24, 32 mm).',
        'Stage 2: Single-Shell 2-Manifold Triangulation — Stitch consecutive rings with outward '
        'counter-clockwise quads and seal z = 0 and z = 48 into V = 16, E = 42, F = 28, β_0 = 1, χ = 2.',
        'Stage 3: Frustum & Cross-Format Volume Parity — Sum V = ∑_{k=1}^3 (16/3)(A_{k-1} + A_k + '
        '√(A_{k-1}A_k)) = 46,080.0 mm³ against divergence volume (Mirtich, 1996, DOI '
        '10.1080/10867651.1996.10487458) across GLB, 3MF, and Part-21 STEP.',
        'Stage 4: Elevation-Gated Overhang Audit — Check non-base facets (outside z = 0 mm) for '
        'θ_f = arcsin(max(0, −n_f · ẑ)) = 14.0362° ≤ 45.0° and reject flipped normals, Δhw_top = '
        '20 mm (51.34°), and z > 0 horizontal soffits (90.0°).',
    ],
    'rules': [
        'Explanation-Only Non-Design Rule: This folio and skill are an explanation of mesh closure '
        'and overhang geometry, not a structural design method, and none of their numbers or files '
        'may be used on a real structure.',
        'Cross-Format Frustum & Manifold Parity: GLB, millimeter 3MF ([Content_Types].xml, '
        '_rels/.rels, 3D/3dmodel.model, identity transform), and Part-21 STEP POLY_LOOP entities '
        'must match V = 16, E = 42, F = 28, β_0 = 1, χ = 2, and V = 46,080.0 mm³.',
        'Elevation-Gated Overhang & Knockout Rule: Excluding only z = 0 mm base facets, every '
        'normal n_f must satisfy θ_f = arcsin(max(0, −n_f · ẑ)) ≤ 45.0° (assumed geometric bound, '
        'not a printability claim), rejecting flipped normals, flare > 16 mm, and z > 0 soffits.',
    ],
    'sidenote_1': {
        'kicker': 'SIDENOTE X.05-A · ARCSIN OVERHANG VS. POLAR ARCCOS COMPLEMENT',
        'body': (
            'For outward wall normal n_f = (Δz, 0, −Δhw)/√(Δz² + Δhw²), −n_f · ẑ equals sin θ_wall, '
            'so tilt from vertical is arcsin(−n_f · ẑ) = arctan(Δhw/Δz) = 14.04°, whereas '
            'arccos(−n_f · ẑ) = 75.96° measures angle from −ẑ.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE X.05-B · FIXED 3MF TIMESTAMPS & PART-21 STEP SKETCH',
        'body': (
            'write_3mf pins ZipInfo.date_time for Git reproducibility, and write_step_ap242 emits an '
            'illustrative Part-21 POLY_LOOP sketch (use build123d or CadQuery on OpenCascade for '
            'EDGE_LOOP STEP AP242 solids).'
        ),
    },
    'walkthrough': [
        'Inspect the four-station strut in the WebGL2 viewer below; the flared upper head '
        '(z ∈ [32, 48] mm) in amber inclines outward at 14.04° from vertical.',
        'Slide Mid-Span Waist Width to reshape the waist volume, or drag Upper Head Flare past '
        '16 mm (or click [⚡ Planted-Defect / Boundary Knockout (Verifier FAIL)], setting waist '
        '24 mm and flare 20 mm → 51.34° and 66,560.0 mm³) to trigger the overhang alert.',
        'Download x05_artifact.3mf, x05_artifact.glb, and x05_artifact.step, or run '
        'verify_x05_toolchain_x05_simp_manifold_3mf.py (and with --planted-defect) locally.',
    ],
    't0_t1_certified': [
        'Deterministic stdlib generator (skills/toolchain/x05/make_x05.py) emitting '
        'x05_artifact.3mf (1,769 B), x05_artifact.glb (2,936 B), and an illustrative Part-21 '
        'POLY_LOOP x05_artifact.step (11,824 B).',
        'Byte-level verifier (verify_x05_toolchain_x05_simp_manifold_3mf.py + '
        'tools/toolchain_x05_checks.py) checking β_0 = 1, χ = 2, 46,080.0 mm³ frustum/divergence '
        'parity, θ_max = 14.0362° ≤ 45.0° across GLB, STEP, and 3MF, and overhang/normal knockouts.',
        'Synchronized WebGL2 4-ring deformation, normal recomputation, and custom GLB/STEP/DXF '
        'export in src/modules/glb-viewer.mjs.',
    ],
    't2_t3_open_horizon': [
        'Educational Geometry Boundary: Every file on this page is an educational artifact and an '
        'explanation, not a structural design method; nothing is certified as load-bearing, '
        'printable, safe, or fit for any purpose.',
        'Open-Toolchain Horizon: Coupled finite-element SIMP extraction to 3MF Beam Lattice '
        '(<beamlattice>) and OpenCascade EDGE_LOOP STEP AP242 export via build123d.',
    ],
    'sources': [
        'Michell, A. G. M. (1904). LVIII. The limits of economy of material in frame-structures. '
        'Philosophical Magazine, 8(47), 589–597. DOI 10.1080/14786440409463229',
        'Requicha, A. A. G. (1980). Representations for rigid solids: Theory, methods, and systems. '
        'ACM Computing Surveys, 12(4), 437–464. DOI 10.1145/356827.356833',
        'Bendsøe, M. P. (1989). Optimal shape design as a material distribution problem. Structural '
        'Optimization, 1(4), 193–202. DOI 10.1007/bf01650949',
        'Mirtich, B. (1996). Fast and accurate computation of polyhedral mass properties. Journal of '
        'Graphics Tools, 1(2), 31–50. DOI 10.1080/10867651.1996.10487458',
        'Bendsøe, M. P., & Sigmund, O. (1999). Material interpolation schemes in topology '
        'optimization. Archive of Applied Mechanics, 69(9–10), 635–654. DOI 10.1007/s004190050248',
        'Benamou, J.-D., & Brenier, Y. (2000). A computational fluid mechanics solution to the '
        'Monge-Kantorovich mass transfer problem. Numerische Mathematik, 84(3), 375–393. DOI '
        '10.1007/s002110050002',
        'Sigmund, O. (2001). A 99 line topology optimization code written in Matlab. Structural and '
        'Multidisciplinary Optimization, 21(2), 120–127. DOI 10.1007/s001580050176',
        'Smith, M. C. (2002). Synthesis of mechanical networks: The inerter. IEEE Transactions on '
        'Automatic Control, 47(10), 1648–1662. DOI 10.1109/tac.2002.803532',
        'Katz, J. (2006). Aerodynamics of race cars. Annual Review of Fluid Mechanics, 38, 27–63. '
        'DOI 10.1146/annurev.fluid.38.050304.092016',
        'Crane, K., de Goes, F., Desbrun, M., & Schröder, P. (2013). Digital geometry processing '
        'with discrete exterior calculus. ACM SIGGRAPH 2013 Courses, Art. 7. DOI '
        '10.1145/2504435.2504442',
        'Feeney, A. B., Frechette, S. P., & Srinivasan, V. (2015). A portrait of an ISO STEP '
        'tolerancing standard as an enabler of smart manufacturing systems. Journal of Computing and '
        'Information Science in Engineering, 15(2), 021001. DOI 10.1115/1.4029050',
        'Suiker, A. S. J. (2018). Mechanical performance of wall structures in 3D printing '
        'processes: Theory, design tools and experiments. International Journal of Mechanical '
        'Sciences, 137, 145–170. DOI 10.1016/j.ijmecsci.2018.01.010',
        'Lalish, E. (2023–2026). Manifold: Exact manifold triangular meshes (Apache-2.0), '
        'https://github.com/elalish/manifold; and 3MF Consortium (2023), 3MF Core Specification '
        'v1.2.3, https://github.com/3MFConsortium/spec_core',
    ],
    'act4_human_ai': (
        'Coding agents asked to script 3D brackets can misstate overhang trigonometry, omit 3MF '
        'archive relationships, or leave seams open. Guided by SKILL.md, make_x05.py emits '
        'x05_artifact.3mf, x05_artifact.glb, x05_artifact.step, and manifest.json, while verify_x05 '
        'checks SHA-256 hashes, 3MF OPC entries and millimeter units, single-shell closure (3F = 2E, '
        'χ = 2), 46,080.0 mm³ frustum and divergence volume parity across all three files, and '
        'non-base (outside z = 0 mm) overhang tilt θ_f = arcsin(max(0, −n_f · ẑ)) ≤ 45.0°, rejecting '
        'flipped normals, 20 mm flare knockouts (51.34°), and z > 0 horizontal soffits (90.0°).'
    ),
    'act4_deepening': (
        'Closed frustum meshes connect to four companion Folios on Informatico.ai. In Folio E.11, '
        'SIMP density fields (Sigmund, 2001, DOI 10.1007/s001580050176) and mechanical inerter '
        'networks (Smith, 2002, DOI 10.1109/tac.2002.803532) require watertight boundary conversion '
        'before fabrication. In Folio P.07, underbody Venturi tunnels (Katz, 2006, DOI '
        '10.1146/annurev.fluid.38.050304.092016) load slender aero stays where mesh checks never '
        'replace structural testing. In Folio E.10, Suiker (2018, DOI 10.1016/j.ijmecsci.2018.01.010) '
        'models buckling and plastic collapse of 3D-printed walls omitted by purely geometric '
        'overhang rules. And in Folio M.09, Benamou and Brenier (2000, DOI 10.1007/s002110050002) '
        'formulate Monge–Kantorovich mass transfer as continuum density flow between cross-sections.'
    ),
    'plain_es': (
        'Piensen en una pieza digital para impresión tridimensional como una maqueta de cartón '
        'sellada en cada arista, donde una unión abierta o un triángulo invertido impide distinguir '
        'el interior sólido del aire vacío. Los voladizos crean otro reto. Las paredes muy '
        'inclinadas ceden sin soportes temporales debajo. Aquí se teje un puntal ahusado ilustrativo '
        'con cuatro anillos cuadrados horizontales para cerrar cada arista desde el origen. Ustedes '
        'pueden mover los dos controles para ajustar la cintura central y el ensanchamiento superior '
        'mientras cambian el volumen y la inclinación. Descarguen los archivos abiertos y corran el '
        'verificador en Python fuera de línea. Este folio es una explicación, no un método de diseño '
        'estructural. Ninguna de sus cifras o archivos puede usarse en una estructura real.'
    ),
    'deep_es': (
        'Este puntal ilustrativo en z ∈ {0, 16, 32, 48} mm con semianchos hw ∈ {20, 16, 12, 16} mm '
        '(no una corrida SIMP; Bendsøe, 1989; Sigmund, 2001) suma V = ∑_{k=1}^3 (h_k / 3)(A_{k-1} + '
        'A_k + √(A_{k-1} A_k)) = 46,080.0 mm³, igual al volumen por divergencia (Mirtich, 1996) en '
        'GLB, 3MF y el boceto Parte 21 POLY_LOOP STEP (compárese con STEP AP242 analítico en Feeney '
        'et al., 2015). En cada pared lateral con Δhw = Δw / 2, θ_wall = arcsin(max(0, −n_f · ẑ)) = '
        'arctan(max(0, Δhw) / Δz) = 14.04° ≤ 45.0° (arccos(−n_f · ẑ) = 75.96° es el complemento '
        'polar), y run_x05_strut_checks audita χ = 2 y 3F = 2E (Crane et al., 2013) excluyendo solo '
        'la base en z = 0 mm. Este folio es una explicación, no un método de diseño estructural, y '
        'ninguna de sus cifras o archivos puede usarse en una estructura real.'
    ),
    'distill_diagram': {
        'analogy_title': 'The Stepped Brick Corbel',
        'analogy_sub': 'Modest outward steps and sealed seams hold shape without falsework.',
        'force_a_title': 'Mid-Span Waist Width (w_2)',
        'force_a_sub': 'Sets the z = 32 mm square waist section and enclosed frustum volume.',
        'force_b_title': 'Upper Head Flare (Δhw_top)',
        'force_b_sub': 'Widens the z = 48 mm crown per side and steepens wall overhang.',
        'threshold_title': 'Geometric Overhang Rule of Thumb (θ ≤ 45°)',
        'threshold_pass': 'Wall tilt θ = 14.04° ≤ 45°: Within geometric overhang bound.',
        'threshold_fail': 'Flare past 16 mm forces θ > 45°: Exceeds geometric overhang bound.',
    },
}
