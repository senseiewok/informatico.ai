#!/usr/bin/env python3
"""Deterministic Bilingual Crossword Puzzle Compiler & Dataset for Informatico.ai (32 Folios + Hub).

Generates and verifies 66 independent newspaper-grade Mini-Crossword puzzles:
  - 33 English Edition (`en`) crosswords (Hub + E.01-E.08, A.01-A.08, P.01-P.08, M.01-M.08)
  - 33 Independent Mexican Spanish Edition (`es-MX` / `es`) crosswords constructed natively from
    authentic Spanish scientific, engineering, architectural, physical, and mathematical vocabulary.

Every puzzle is deterministically compiled and verified against four strict invariants:
  1. Single Connected Component: Every word intersects at least one orthogonal word at a matching letter.
  2. Strict Newspaper Adjacency: Zero accidental 2+ letter runs; every contiguous horizontal or vertical
     run of >= 2 letters in the grid is an explicitly clued Across or Down word.
  3. Canonical Reading-Order Numbering: Cell clue numbers (1..N) are assigned top-to-bottom, left-to-right.
  4. Independent EN vs ES-MX Grids: The Spanish puzzle is its own distinct crossword grid and word set,
     never a mere clue translation of the English grid.
"""

from __future__ import annotations

from typing import Any


def _can_place(
    grid: dict[tuple[int, int], str],
    word: str,
    r: int,
    c: int,
    direction: str,
) -> int:
    """Return intersection count (>= 1) if `word` can be placed validly with strict crossword adjacency, else -1."""
    length = len(word)
    dr, dc = (0, 1) if direction == "across" else (1, 0)
    pr, pc = (1, 0) if direction == "across" else (0, 1)

    # Cell immediately before start and immediately after end must be empty
    if (r - dr, c - dc) in grid:
        return -1
    if (r + length * dr, c + length * dc) in grid:
        return -1

    intersections = 0
    for i, ch in enumerate(word):
        cr, cc = r + i * dr, c + i * dc
        existing = grid.get((cr, cc))
        if existing is not None:
            if existing != ch:
                return -1
            intersections += 1
        else:
            # Perpendicular neighbors must be empty so we don't create accidental 2-letter side-by-side runs
            if (cr - pr, cc - pc) in grid or (cr + pr, cc + pc) in grid:
                return -1

    return intersections


def compile_crossword(entries_spec: list[tuple[str, str, str]], max_span: int = 10) -> dict[str, Any]:
    """Deterministically pack `(word, clue, act)` entries into a compact, strict-adjacency crossword grid."""
    cleaned = [(w.strip().upper(), clue.strip(), act.strip()) for w, clue, act in entries_spec]
    indexed = list(enumerate(cleaned))
    indexed.sort(key=lambda item: (-len(item[1][0]), item[0]))

    best_solution: list[tuple[int, str, int, int, str, str, str]] | None = None
    best_score: tuple[int, int, int] = (-1, -9999, -9999)

    def backtrack(
        placed: list[tuple[int, str, int, int, str, str, str]],
        remaining: list[tuple[int, tuple[str, str, str]]],
        grid: dict[tuple[int, int], str],
    ) -> None:
        nonlocal best_solution, best_score
        if not remaining:
            rows = [pos[0] for pos in grid]
            cols = [pos[1] for pos in grid]
            h = max(rows) - min(rows) + 1
            w = max(cols) - min(cols) + 1
            area = h * w
            aspect_penalty = abs(h - w)
            total_letters = sum(len(item[1]) for item in placed)
            crossings = total_letters - len(grid)
            score = (crossings, -area, -aspect_penalty)
            if score > best_score:
                best_score = score
                best_solution = list(placed)
            return

        # Try any remaining word that can intersect the already-placed words
        for rem_i, (orig_idx, (word, clue, act)) in enumerate(remaining):
            rest = remaining[:rem_i] + remaining[rem_i + 1 :]
            candidates: list[tuple[int, int, int, str]] = []
            for p_orig, p_word, pr, pc, p_dir, _, _ in placed:
                c_dir = "down" if p_dir == "across" else "across"
                p_dr, p_dc = (0, 1) if p_dir == "across" else (1, 0)
                c_dr, c_dc = (0, 1) if c_dir == "across" else (1, 0)
                for pi, pch in enumerate(p_word):
                    cell_r = pr + pi * p_dr
                    cell_c = pc + pi * p_dc
                    for wi, wch in enumerate(word):
                        if wch != pch:
                            continue
                        start_r = cell_r - wi * c_dr
                        start_c = cell_c - wi * c_dc
                        cross_cnt = _can_place(grid, word, start_r, start_c, c_dir)
                        if cross_cnt >= 1:
                            new_rows = [pos[0] for pos in grid] + [start_r, start_r + (len(word) - 1) * c_dr]
                            new_cols = [pos[1] for pos in grid] + [start_c, start_c + (len(word) - 1) * c_dc]
                            if (max(new_rows) - min(new_rows) + 1) <= max_span and (
                                max(new_cols) - min(new_cols) + 1
                            ) <= max_span:
                                candidates.append((cross_cnt, start_r, start_c, c_dir))

            if not candidates:
                continue

            seen = set()
            unique_cands = []
            for cross_cnt, sr, sc, c_dir in candidates:
                key = (sr, sc, c_dir)
                if key not in seen:
                    seen.add(key)
                    unique_cands.append((cross_cnt, sr, sc, c_dir))
            unique_cands.sort(key=lambda x: (-x[0], abs(x[1]) + abs(x[2]), x[1], x[2], x[3]))

            for _, sr, sc, c_dir in unique_cands[:8]:
                c_dr, c_dc = (0, 1) if c_dir == "across" else (1, 0)
                added: list[tuple[int, int]] = []
                for wi, wch in enumerate(word):
                    pos = (sr + wi * c_dr, sc + wi * c_dc)
                    if pos not in grid:
                        grid[pos] = wch
                        added.append(pos)
                placed.append((orig_idx, word, sr, sc, c_dir, clue, act))
                backtrack(placed, rest, grid)
                placed.pop()
                for pos in added:
                    del grid[pos]
                if best_solution is not None:
                    return

    first_idx, (first_word, first_clue, first_act) = indexed[0]
    init_grid = {(0, i): ch for i, ch in enumerate(first_word)}
    backtrack(
        [(first_idx, first_word, 0, 0, "across", first_clue, first_act)],
        indexed[1:],
        init_grid,
    )

    if best_solution is None:
        raise ValueError(f"Could not compile valid connected crossword for words: {[w for w, _, _ in cleaned]}")

    # Normalize coordinates to 0-based bounding box
    all_positions: dict[tuple[int, int], str] = {}
    for _, word, sr, sc, c_dir, _, _ in best_solution:
        dr, dc = (0, 1) if c_dir == "across" else (1, 0)
        for i, ch in enumerate(word):
            all_positions[(sr + i * dr, sc + i * dc)] = ch

    min_r = min(r for r, _ in all_positions)
    max_r = max(r for r, _ in all_positions)
    min_c = min(c for _, c in all_positions)
    max_c = max(c for _, c in all_positions)
    rows = max_r - min_r + 1
    cols = max_c - min_c + 1

    norm_placed = []
    start_map: dict[tuple[int, int, str], dict[str, Any]] = {}
    for orig_idx, word, sr, sc, c_dir, clue, act in best_solution:
        nr, nc = sr - min_r, sc - min_c
        entry = {
            "word": word,
            "row": nr,
            "col": nc,
            "dir": c_dir,
            "clue": clue,
            "act": act,
        }
        norm_placed.append(entry)
        start_map[(nr, nc, c_dir)] = entry

    # Assign canonical reading-order clue numbers (1..N)
    cell_numbers: dict[tuple[int, int], int] = {}
    next_num = 1
    for r in range(rows):
        for c in range(cols):
            if (r, c, "across") in start_map or (r, c, "down") in start_map:
                cell_numbers[(r, c)] = next_num
                if (r, c, "across") in start_map:
                    start_map[(r, c, "across")]["num"] = next_num
                if (r, c, "down") in start_map:
                    start_map[(r, c, "down")]["num"] = next_num
                next_num += 1

    grid_rows: list[str] = []
    for r in range(rows):
        row_chars = []
        for c in range(cols):
            ch = all_positions.get((r + min_r, c + min_c), "#")
            row_chars.append(ch)
        grid_rows.append("".join(row_chars))

    across_clues = sorted(
        [e for e in norm_placed if e["dir"] == "across"],
        key=lambda e: e["num"],
    )
    down_clues = sorted(
        [e for e in norm_placed if e["dir"] == "down"],
        key=lambda e: e["num"],
    )

    puzzle = {
        "rows": rows,
        "cols": cols,
        "grid": grid_rows,
        "across": across_clues,
        "down": down_clues,
    }
    verify_crossword_grid(puzzle)
    return puzzle


def verify_crossword_grid(puzzle: dict[str, Any]) -> None:
    """Verify strict crossword invariants: bounds, exact intersections, zero un-clued runs, reading-order numbers."""
    rows = puzzle["rows"]
    cols = puzzle["cols"]
    grid = puzzle["grid"]
    assert len(grid) == rows, f"Expected {rows} rows, got {len(grid)}"
    for r_str in grid:
        assert len(r_str) == cols, f"Row {r_str!r} length != {cols}"

    all_entries = list(puzzle["across"]) + list(puzzle["down"])
    assert len(all_entries) >= 5, f"Crossword must have at least 5 words, got {len(all_entries)}"
    assert len(puzzle["across"]) >= 2 and len(puzzle["down"]) >= 2, "Must have both Across and Down words"

    # 1. Verify each entry matches the grid letters and boundaries
    declared_runs: set[tuple[int, int, str, str]] = set()
    covered_cells: set[tuple[int, int]] = set()
    for e in all_entries:
        w = e["word"]
        r, c = e["row"], e["col"]
        d = e["dir"]
        dr, dc = (0, 1) if d == "across" else (1, 0)
        assert 3 <= len(w) <= 10, f"Invalid word length: {w}"
        assert w.isalpha() and w.isupper() and w.isascii(), f"Word must be uppercase ASCII A-Z: {w}"
        for i, ch in enumerate(w):
            cr, cc = r + i * dr, c + i * dc
            assert 0 <= cr < rows and 0 <= cc < cols, f"Out of bounds: {w} at ({cr},{cc})"
            assert grid[cr][cc] == ch, f"Mismatch at ({cr},{cc}): grid has {grid[cr][cc]}, word {w} expects {ch}"
            covered_cells.add((cr, cc))
        declared_runs.add((r, c, d, w))

    # 2. Verify every non-'#' cell in grid belongs to at least one word
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "#":
                assert (r, c) in covered_cells, f"Orphan letter cell at ({r},{c})"

    # 3. Verify every maximal horizontal/vertical contiguous run of >= 2 letters is a declared word
    for r in range(rows):
        c = 0
        while c < cols:
            if grid[r][c] == "#":
                c += 1
                continue
            start_c = c
            chars = []
            while c < cols and grid[r][c] != "#":
                chars.append(grid[r][c])
                c += 1
            if len(chars) >= 2:
                run_w = "".join(chars)
                assert (r, start_c, "across", run_w) in declared_runs, (
                    f"Un-clued horizontal run {run_w!r} at ({r},{start_c})"
                )

    for c in range(cols):
        r = 0
        while r < rows:
            if grid[r][c] == "#":
                r += 1
                continue
            start_r = r
            chars = []
            while r < rows and grid[r][c] != "#":
                chars.append(grid[r][c])
                r += 1
            if len(chars) >= 2:
                run_w = "".join(chars)
                assert (start_r, c, "down", run_w) in declared_runs, (
                    f"Un-clued vertical run {run_w!r} at ({start_r},{c})"
                )

    # 4. Verify single connected component of letter cells via BFS
    start_cell = next(iter(covered_cells))
    visited = {start_cell}
    queue = [start_cell]
    while queue:
        cr, cc = queue.pop(0)
        for nr, nc in ((cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)):
            if (nr, nc) in covered_cells and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))
    assert len(visited) == len(covered_cells), (
        f"Disconnected crossword graph: visited {len(visited)} of {len(covered_cells)} letter cells"
    )


def pad_puzzle_to_square(puzzle: dict[str, Any], target_size: int = 9) -> dict[str, Any]:
    """Center a verified crossword inside a uniform `target_size x target_size` square grid for zero-CLS theme/lang switching."""
    rows, cols = puzzle["rows"], puzzle["cols"]
    assert rows <= target_size and cols <= target_size, (
        f"Puzzle ({rows}x{cols}) exceeds target square size {target_size}x{target_size}"
    )
    pad_top = (target_size - rows) // 2
    pad_left = (target_size - cols) // 2
    pad_bottom = target_size - rows - pad_top
    pad_right = target_size - cols - pad_left

    empty_row = "#" * target_size
    new_grid = (
        [empty_row for _ in range(pad_top)]
        + [("#" * pad_left) + r_str + ("#" * pad_right) for r_str in puzzle["grid"]]
        + [empty_row for _ in range(pad_bottom)]
    )

    def shift_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
        out = []
        for e in entries:
            shifted = dict(e)
            shifted["row"] = e["row"] + pad_top
            shifted["col"] = e["col"] + pad_left
            shifted["number"] = e["num"]
            shifted["length"] = len(e["word"])
            out.append(shifted)
        return out

    shifted_across = shift_entries(puzzle["across"])
    shifted_down = shift_entries(puzzle["down"])
    numbers_matrix = [[0 for _ in range(target_size)] for _ in range(target_size)]
    for entry in shifted_across + shifted_down:
        numbers_matrix[entry["row"]][entry["col"]] = entry["number"]

    padded = {
        "rows": target_size,
        "cols": target_size,
        "grid": new_grid,
        "numbers": numbers_matrix,
        "across": shifted_across,
        "down": shifted_down,
    }
    verify_crossword_grid(padded)
    return padded


RAW_PUZZLE_SPECS: dict[str, dict[str, Any]] = {
    "hub": {
        "title_en": "Informatico.ai · Grand 4-Pillar Synthesis Crossword",
        "title_es": "Informatico.ai · Gran Crucigrama de Síntesis en 4 Pilares",
        "en": [
            ("VIGNELLI", "Italian modernist master whose canon inspires our 3-typeface editorial hierarchy", "Act I"),
            ("TUFTE", "Pioneer of margin sidenotes and high-density visual evidence alongside prose", "Act II"),
            ("LEAN", "Formal proof assistant that verified 29,500+ lemmas of Fermat's Last Theorem", "Act IV"),
            ("VAULT", "Masonry funicular compression shell analyzed by Hooke, Gaudí, and Heyman", "Act III"),
            ("FLUID", "Continuum phase governed by Navier-Stokes, Darcy-Brinkman, and Venturi laws", "Act III"),
            ("GRID", "Swiss 12-column typographic and structural modular coordinate system", "Act I"),
        ],
        "es": [
            ("CIENCIA", "Conocimiento verificable que une física, matemáticas, arquitectura e ingeniería", "Acto I"),
            ("TEOREMA", "Proposición matemática demostrada formalmente sin axiomas pendientes en Lean 4", "Acto IV"),
            ("BOVEDA", "Cubierta arqueada de piedra o ladrillo que trabaja en compresión funicular", "Acto III"),
            ("FLUJO", "Movimiento continuo de un fluido poroso, sanguíneo o aerodinámico", "Acto III"),
            ("MURO", "Elemento arquitectónico vertical que en la obra de Luis Barragán se viste de luz y color", "Acto II"),
            ("ARCO", "Estructura curva cuya línea de empuje invierte la cadena colgante de Hooke", "Acto I"),
        ],
    },
    # ---------------- PILLAR I: CIVIL ENGINEERING & CONSTRUCTION (E.01 - E.08) ----------------
    "e01": {
        "title_en": "Folio E.01 · Darcy–Brinkman Porous Mortar Crossword",
        "title_es": "Folio E.01 · Crucigrama de Percolación Darcy–Brinkman en Morteros",
        "en": [
            ("BRINKMAN", "1949 viscous-shear extension to Darcy's law across coarse-to-fine porous interfaces", "Act II"),
            ("MORTAR", "Sacrificial lime-pozzolan mineral matrix laid between historic masonry units", "Act I"),
            ("DARCY", "1856 Dijon fountain engineer who formulated linear porous filtration velocity", "Act I"),
            ("PORE", "Microscopic capillary void space whose tortuosity governs fluid permeability", "Act III"),
            ("LIME", "Calcined calcium carbonate binder that breathes moisture in heritage walls", "Act I"),
            ("PARETO", "Multi-objective frontier balancing hydraulic conductivity against energy delay", "Act IV"),
        ],
        "es": [
            ("MORTERO", "Mezcla mineral porosa de cal y puzolana que protege la piedra histórica", "Acto I"),
            ("DARCY", "Ingeniero francés de Dijon que formuló en 1856 la ley de filtración lineal", "Acto I"),
            ("PORO", "Cavidad capilar microscópica cuya fracción volumétrica define la permeabilidad", "Acto III"),
            ("FLUJO", "Caudal de agua o vapor que atraviesa la matriz mineral bajo gradiente de presión", "Acto II"),
            ("ROCA", "Sustrato pétreo de mampostería protegido por la junta de sacrificio", "Acto I"),
            ("CAL", "Ligante tradicional transpirable empleado desde Vitruvio en muros históricos", "Acto I"),
        ],
    },
    "e02": {
        "title_en": "Folio E.02 · Herschel–Bulkley Concrete Rheology Crossword",
        "title_es": "Folio E.02 · Crucigrama de Reología y Bombeo de Concreto",
        "en": [
            ("BINGHAM", "1922 rheologist who modeled viscoplastic fluids with a finite yield stress threshold", "Act I"),
            ("TREMIE", "Gravity-fed submerged pipe used to pour concrete from the bottom up in deep piles", "Act III"),
            ("SLUMP", "Abrams cone subsidence test measuring fresh concrete workability on site", "Act II"),
            ("PLUG", "Unsheared central core traveling as a solid cylinder inside a slickline pipe", "Act II"),
            ("PUMP", "High-pressure hydraulic piston unit driving fresh concrete up supertall cores", "Act III"),
            ("GROUT", "Lubricating cement-water slurry layer lining the steel pipe wall", "Act II"),
        ],
        "es": [
            ("CONCRETO", "Mezcla estructural bombeada a alta presión con comportamiento viscoplástico", "Acto I"),
            ("TREMIE", "Tubería sumergida que vierte el colado desde el fondo sin segregar el agregado", "Acto III"),
            ("TAPON", "Núcleo central no cizallado que avanza como cilindro sólido dentro de la tubería", "Acto II"),
            ("BOMBA", "Equipo hidráulico de pistones que impulsa la mezcla hacia grandes alturas", "Acto III"),
            ("REOLOGIA", "Ciencia del flujo y deformación gobernada por la ley de Herschel-Bulkley", "Acto II"),
            ("CONO", "Molde troncocónico de Abrams usado para medir el revenimiento en obra", "Acto I"),
        ],
    },
    "e03": {
        "title_en": "Folio E.03 · Sub-Wavelength Acoustic Metamaterials Crossword",
        "title_es": "Folio E.03 · Crucigrama de Metamateriales Acústicos de Helmholtz",
        "en": [
            ("ACOUSTIC", "Pertaining to sound-wave propagation and sub-wavelength noise attenuation", "Act I"),
            ("CAVITY", "Internal compliant air volume acting as the spring of a Helmholtz resonator", "Act II"),
            ("NECK", "Narrow viscothermal aperture where oscillating air mass dissipates acoustic energy", "Act II"),
            ("PHASE", "Wavefront angle reversed across a locally resonant dipole bandgap", "Act III"),
            ("ROOFLINE", "Williams-Waterman-Patterson operational intensity performance model", "Act IV"),
            ("SOUND", "Mechanical pressure wave blocked by sub-wavelength labyrinthine panels", "Act I"),
        ],
        "es": [
            ("ACUSTICO", "Relativo al aislamiento y control de ondas sonoras de baja frecuencia", "Acto I"),
            ("CAVIDAD", "Volumen interno de aire que actúa como resorte compresible en el resonador", "Acto II"),
            ("CUELLO", "Conducto estrecho donde la capa límite viscosa disipa la energía del sonido", "Acto II"),
            ("SONIDO", "Onda de presión mecánica atenuada por paneles laberínticos sub-longitud de onda", "Acto I"),
            ("ONDA", "Perturbación armónica reflejada cuando la masa efectiva se vuelve negativa", "Acto III"),
            ("FASE", "Ángulo de oscilación que se invierte al cruzar la frecuencia de resonancia", "Acto III"),
        ],
    },
    "e04": {
        "title_en": "Folio E.04 · Counter-Current Enthalpy Recovery Crossword",
        "title_es": "Folio E.04 · Crucigrama de Recuperación de Entalpía a Contracorriente",
        "en": [
            ("ENTHALPY", "Combined sensible heat and latent moisture energy recovered in cleanroom cores", "Act I"),
            ("LATENT", "Hidden phase-change energy carried by water vapor across a selective membrane", "Act II"),
            ("CLEAN", "ISO-classified sterile air regime maintained by high-recovery ventilation", "Act IV"),
            ("CORE", "Cross-fluted counter-current heat and moisture exchanger heart", "Act III"),
            ("NTU", "Number of Transfer Units governing heat-exchanger effectiveness (Kays & London)", "Act II"),
            ("AIR", "Counter-flowing supply and exhaust gas streams separated by polymer plates", "Act I"),
        ],
        "es": [
            ("ENTALPIA", "Energía termodinámica total que suma el calor sensible y el calor latente", "Acto I"),
            ("LATENTE", "Calor asociado al vapor de agua transferido a través de la membrana selectiva", "Acto II"),
            ("NUCLEO", "Corazón intercambiador de placas a contracorriente descrito por Kays y London", "Acto III"),
            ("CALOR", "Energía térmica sensible recuperada entre el flujo de extracción y el de inyección", "Acto II"),
            ("VAPOR", "Fase gaseosa del agua cuya humedad se regula en salas limpias hospitalarias", "Acto IV"),
            ("AIRE", "Fluido de ventilación renovado sin perder la energía térmica del edificio", "Acto I"),
        ],
    },
    "e05": {
        "title_en": "Folio E.05 · Terzaghi Consolidation & CFA Piling Crossword",
        "title_es": "Folio E.05 · Crucigrama de Consolidación de Terzaghi y Pilotes CFA",
        "en": [
            ("TERZAGHI", "1925 father of soil mechanics who formulated the effective stress principle", "Act I"),
            ("AUGER", "Continuous hollow-stem helical drill used to bore CFA deep foundations", "Act III"),
            ("CLAY", "Low-permeability cohesive soil whose pore water drains slowly under load", "Act II"),
            ("PILE", "Deep cylindrical concrete foundation element transferring load to bearing strata", "Act III"),
            ("STRESS", "Total overburden pressure minus pore-water pressure gives its effective value", "Act II"),
            ("SOIL", "Multiphase porous skeleton of mineral grains and interstitial water", "Act I"),
        ],
        "es": [
            ("TERZAGHI", "Padre de la mecánica de suelos moderna que formuló el esfuerzo efectivo en 1925", "Acto I"),
            ("PILOTE", "Elemento de cimentación profunda perforado con barrena continua (CFA)", "Acto III"),
            ("ARCILLA", "Suelo cohesivo de baja permeabilidad que se consolida al drenar el agua intersticial", "Acto II"),
            ("SUELO", "Esqueleto mineral multifásico que soporta las cargas de la superestructura", "Acto I"),
            ("CARGA", "Fuerza gravitatoria transmitida por la cimentación hacia estratos resistentes", "Acto III"),
            ("AGUA", "Fluido en los poros cuya sobrepresión se disipa durante la consolidación primaria", "Acto II"),
        ],
    },
    "e06": {
        "title_en": "Folio E.06 · ASCE 7-22 Seismic Base Isolation Crossword",
        "title_es": "Folio E.06 · Crucigrama de Aislamiento Sísmico de Base ASCE 7-22",
        "en": [
            ("SEISMIC", "Pertaining to earthquake ground motions decoupled by base-isolation bearings", "Act I"),
            ("RUBBER", "Elastomeric vulcanized layers vulcanized to steel shims in a Robinson bearing", "Act II"),
            ("LEAD", "Central plastic core inside an LRB that yields to dissipate earthquake energy", "Act II"),
            ("PERIOD", "Fundamental oscillation time shifted past 3.0 seconds to slash floor accelerations", "Act III"),
            ("HYSTERESIS", "Bilinear force-displacement loop area measuring energy absorbed per cycle", "Act III"),
            ("BASE", "Foundation interface plane where isolators decouple the hospital from the ground", "Act I"),
        ],
        "es": [
            ("SISMICO", "Relativo a los movimientos telúricos desacoplados para proteger hospitales", "Acto I"),
            ("PLOMO", "Núcleo central metálico del apoyo LRB que fluye plásticamente y disipa energía", "Acto II"),
            ("CAUCHO", "Elastómero laminado con placas de acero que aporta flexibilidad horizontal", "Acto II"),
            ("PERIODO", "Tiempo natural de oscilación alargado más allá de 3 segundos (ASCE 7-22)", "Acto III"),
            ("APOYO", "Dispositivo estructural instalado en la base para aislar el edificio del suelo", "Acto III"),
            ("BASE", "Nivel inferior de la estructura donde se montan los aisladores elastoméricos", "Acto I"),
        ],
    },
    "e07": {
        "title_en": "Folio E.07 · Suspension Bridge Aeroelastic Flutter Crossword",
        "title_es": "Folio E.07 · Crucigrama de Aeroelasticidad en Puentes Colgantes",
        "en": [
            ("SCANLAN", "Pioneer whose 18 flutter derivatives quantify wind-deck self-excited forces", "Act I"),
            ("FLUTTER", "Catastrophic coupled torsional-vertical aeroelastic instability in long spans", "Act II"),
            ("BRIDGE", "Long-span cable-supported crossing such as Tacoma Narrows or Storebælt", "Act I"),
            ("VORTEX", "Alternating Kármán wake eddy shed from a bluff girder at critical Strouhal number", "Act II"),
            ("CABLE", "Parabolic high-strength steel main suspension tendon carrying deck tension", "Act III"),
            ("SPAN", "Clear distance between main towers governing torsional frequency ratios", "Act III"),
        ],
        "es": [
            ("SCANLAN", "Ingeniero que formuló las derivadas de flameo aeroelástico en tableros de puentes", "Acto I"),
            ("PUENTE", "Estructura colgante de gran claro sujeta a fuerzas de viento y vórtices", "Acto I"),
            ("VIENTO", "Corriente atmosférica que induce acoplamiento entre flexión y torsión", "Acto II"),
            ("CABLE", "Tendón principal parabólico de acero de alta resistencia que sostiene el tablero", "Acto III"),
            ("TORRE", "Pilono vertical que transmite las cargas de los cables hacia la cimentación", "Acto III"),
            ("ALETEO", "Inestabilidad aeroelástica autoexcitada conocida en inglés como flutter", "Acto II"),
        ],
    },
    "e08": {
        "title_en": "Folio E.08 · EPB-TBM Tunneling & Peck Settlement Crossword",
        "title_es": "Folio E.08 · Crucigrama de Tuneladoras EPB-TBM y Asentamiento de Peck",
        "en": [
            ("TUNNEL", "Subsurface bored transit corridor excavated beneath historic urban fabric", "Act I"),
            ("SHIELD", "Pressurized cylindrical steel skin protecting the TBM cutterhead and crew", "Act II"),
            ("TROUGH", "Peck-Mair inverted Gaussian surface settlement profile above a bored cavity", "Act II"),
            ("LINER", "Watertight ring of bolted precast concrete segments erected inside the TBM tail", "Act III"),
            ("GROUT", "Two-component tail-void mortar injected behind precast concrete segments", "Act III"),
            ("FOAM", "Surfactant conditioner injected into excavated muck to balance earth pressure", "Act III"),
        ],
        "es": [
            ("TUNEL", "Galería subterránea excavada bajo ciudades mediante escudo presurizado", "Acto I"),
            ("ESCUDO", "Coraza cilíndrica de acero de la tuneladora EPB que sostiene el frente", "Acto II"),
            ("DOVELA", "Segmento prefabricado de concreto armado que conforma el anillo del revestimiento", "Acto III"),
            ("ESPUMA", "Agente tensoactivo inyectado para acondicionar el terreno en la cámara de presión", "Acto III"),
            ("PECK", "Autor de la campana gaussiana de asentamiento superficial sobre excavaciones", "Acto I"),
            ("FRENTE", "Cara de excavación cuya presión de tierra equilibra el empuje hidrostático", "Acto II"),
        ],
    },
    # ---------------- PILLAR II: ARCHITECTURE (A.01 - A.08) ----------------
    "a01": {
        "title_en": "Folio A.01 · Funicular Masonry Vaults & Glaser Crossword",
        "title_es": "Folio A.01 · Crucigrama de Bóvedas Funiculares y Condensación de Glaser",
        "en": [
            ("CATENARY", "Hanging chain curve of Hooke and Gaudí that inverts into a pure compression arch", "Act I"),
            ("HEYMAN", "Cambridge structural theorist of the safe theorem for unreinforced stone vaults", "Act I"),
            ("THRUST", "Internal compressive force trajectory that must stay inside the middle-third kern", "Act II"),
            ("VAULT", "Curved masonry ceiling shell standing for centuries without tensile steel", "Act III"),
            ("GLASER", "Dew-point vapor diffusion profile preventing interstitial wall condensation", "Act IV"),
            ("ARCH", "Compression ring of wedge-shaped voussoirs locked by a central keystone", "Act II"),
        ],
        "es": [
            ("BOVEDA", "Cubierta curva de mampostería que trabaja en compresión pura sin acero", "Acto I"),
            ("HEYMAN", "Autor del teorema plástico de seguridad para estructuras históricas de piedra", "Acto I"),
            ("EMPUJE", "Línea de fuerza compresiva que debe permanecer dentro del núcleo central", "Acto II"),
            ("GLASER", "Método gráfico de presión de vapor para evitar condensación intersticial", "Acto IV"),
            ("PIEDRA", "Material estereotómico tallado en dovelas para resistir esfuerzos de compresión", "Acto III"),
            ("ARCO", "Forma antifunicular que invierte la cadena colgante de Robert Hooke y Gaudí", "Acto II"),
        ],
    },
    "a02": {
        "title_en": "Folio A.02 · Reciprocal Timber Gridshells Crossword",
        "title_es": "Folio A.02 · Crucigrama de Retículas Recíprocas de Madera (Nexorades)",
        "en": [
            ("NEXORADE", "Reciprocal timber frame where each beam rests upon and supports its neighbor", "Act I"),
            ("TIMBER", "Anisotropic renewable structural wood engineered under Eurocode 5 rules", "Act II"),
            ("VILLARD", "13th-century sketchbook master (de Honnecourt) who drew reciprocal floor grillages", "Act I"),
            ("JOINT", "Notched lap connection whose eccentricity governs gridshell curvature", "Act III"),
            ("SPAN", "Column-free hall width bridged by short interlocking wooden laths", "Act III"),
            ("BEAM", "Individual short structural member in a Leonardo or Serlio reciprocal fan", "Act II"),
        ],
        "es": [
            ("MADERA", "Material estructural renovable y anisotrópico dimensionado según el Eurocódigo 5", "Acto I"),
            ("NEXOR", "Elemento corto entrelazado en una retícula recíproca que salva grandes claros", "Acto II"),
            ("NUDO", "Unión ensamblada cuya excentricidad define la curvatura de la cúpula", "Acto III"),
            ("VIGA", "Pieza lineal que se apoya sobre su vecina y a la vez sostiene la siguiente", "Acto II"),
            ("DOMO", "Cubierta espacial curva formada sin cimbra mediante barras recíprocas", "Acto III"),
            ("RED", "Malla estructural tejida inspirada en los cuadernos de Villard de Honnecourt", "Acto I"),
        ],
    },
    "a03": {
        "title_en": "Folio A.03 · Double-Skin Buoyancy & Circadian Daylight Crossword",
        "title_es": "Folio A.03 · Crucigrama de Fachadas de Doble Piel y Luz Circadiana",
        "en": [
            ("BUOYANCY", "Thermal stack-effect lift driving natural airflow up a sun-warmed facade cavity", "Act II"),
            ("FACADE", "Double-skin glazed building envelope with operable solar shading louvers", "Act I"),
            ("DAYLIGHT", "Natural sky illumination metered to entrain human melanopic circadian rhythms", "Act III"),
            ("STACK", "Vertical solar chimney effect governed by indoor-outdoor density differences", "Act II"),
            ("GLARE", "Excessive visual contrast suppressed by exterior louvers while keeping views", "Act III"),
            ("SOLAR", "Radiant energy from the sun harnessed for passive winter heating and ventilation", "Act I"),
        ],
        "es": [
            ("FACHADA", "Envolvente arquitectónica de doble piel acristalada con ventilación natural", "Acto I"),
            ("SOLAR", "Energía radiante que calienta la cavidad e impulsa el tiro térmico ascendente", "Acto II"),
            ("TIRO", "Efecto chimenea por flotabilidad térmica que extrae el aire caliente sin ventiladores", "Acto II"),
            ("CELOSIA", "Sistema de lamas exteriores que controla el deslumbramiento y la ganancia térmica", "Acto III"),
            ("RITMO", "Ciclo biológico circadiano sincronizado por los luxes melanópicos de luz natural", "Acto IV"),
            ("LUZ", "Iluminación diurna natural conducida hacia el interior profundo del edificio", "Acto III"),
        ],
    },
    "a04": {
        "title_en": "Folio A.04 · Archigram to British High-Tech Exoskeleton Crossword",
        "title_es": "Folio A.04 · Crucigrama de Archigram a Exoesqueletos High-Tech",
        "en": [
            ("POMPIDOU", "1977 Paris cultural center by Piano, Rogers, and Rice with external steel trusses", "Act I"),
            ("ARCHIGRAM", "1960s avant-garde group behind Plug-In City and Ron Herron's Walking City", "Act I"),
            ("TRUSS", "Maxwell-determinate pin-jointed span hanging from cast-steel gerberettes", "Act II"),
            ("FOSTER", "High-Tech architect of the mast-suspended Hongkong and Shanghai Bank headquarters", "Act I"),
            ("RICE", "Ove Arup structural engineer who designed the cast-steel gerberette rocker beam", "Act II"),
            ("POD", "Crane-replaceable modular service or cleanroom capsule clipped to a 100-year frame", "Act IV"),
        ],
        "es": [
            ("POMPIDOU", "Centro parisino de 1977 de Piano, Rogers y Rice con estructura y ductos exteriores", "Acto I"),
            ("CERCHA", "Viga celosía de gran claro articulada sobre gerberettes de acero fundido", "Acto II"),
            ("CAPSULA", "Módulo clínico o habitacional enchufable (Plug-In) reemplazable mediante grúa", "Acto IV"),
            ("ACERO", "Aleación fundida empleada por Peter Rice para fabricar las ménsulas gerberette", "Acto II"),
            ("ROGER", "Apellido (sin s) de Richard, coautor del edificio Lloyd's de Londres y el Pompidou", "Acto I"),
            ("RED", "Megaestructura reticular permanente de 100 años que aloja módulos renovables", "Acto III"),
        ],
    },
    "a05": {
        "title_en": "Folio A.05 · Sabine Reverberation & Schroeder Diffusers Crossword",
        "title_es": "Folio A.05 · Crucigrama de Acústica de Sabine y Difusores de Schroeder",
        "en": [
            ("SABINE", "Harvard physicist who discovered in 1898 that reverberation time scales as V / A", "Act I"),
            ("ECHO", "Focused specular sound reflection scattered by quadratic-residue coffered vaults", "Act II"),
            ("VAULT", "Curved ceiling whose prime-number well depths diffuse sound uniformly", "Act III"),
            ("DECIBEL", "Logarithmic sound pressure level unit dropping by 60 dB across reverberation time RT60", "Act II"),
            ("PRIME", "Number-theoretic modulus p used by Manfred Schroeder to size diffuser wells", "Act III"),
            ("HALL", "Concert or lecture room tuned for crystalline speech intelligibility", "Act I"),
        ],
        "es": [
            ("SABINE", "Físico de Harvard que formuló en 1898 la ley del tiempo de reverberación RT60", "Acto I"),
            ("DIFUSOR", "Panel de pozos de residuo cuadrático de Schroeder que dispersa el sonido", "Acto III"),
            ("PRIMO", "Número entero p que determina la secuencia de profundidades en el techo acústico", "Acto III"),
            ("SALA", "Recinto arquitectónico diseñado para lograr claridad verbal y riqueza musical", "Acto I"),
            ("ECO", "Reflexión acústica focalizada que se elimina mediante casetones difusores", "Acto II"),
            ("VOZ", "Señal hablada cuya inteligibilidad depende de un tiempo de reverberación controlado", "Acto II"),
        ],
    },
    "a06": {
        "title_en": "Folio A.06 · Constructed Wetlands & Sterile Plumbing Crossword",
        "title_es": "Folio A.06 · Crucigrama de Humedales Construidos y Plomería Estéril",
        "en": [
            ("WETLAND", "Subsurface gravel root-zone biofilter governed by Kadlec-Knight P-k-C* kinetics", "Act I"),
            ("BIOFILM", "Pipe-wall microbial slime layer prevented by 60°C thermal loop circulation", "Act II"),
            ("STERILE", "Pathogen-free clinical water regime achieved via 254 nm UV-C irradiation", "Act IV"),
            ("REED", "Phragmites aquatic plant pumping oxygen into the rhizosphere gravel bed", "Act II"),
            ("GRAVEL", "Porous mineral substrate supporting nitrifying bacteria in greywater beds", "Act III"),
            ("UVC", "Short-wave germicidal ultraviolet light band that dimerizesopportunistic DNA", "Act III"),
        ],
        "es": [
            ("HUMEDAL", "Filtro biológico fitodepurador gobernado por la cinética de Kadlec y Knight", "Acto I"),
            ("ESTERIL", "Condición libre de patógenos lograda con luz UV-C y recirculación térmica", "Acto IV"),
            ("GRAVA", "Lecho granular subsuperficial donde las raíces oxigenan el agua gris", "Acto III"),
            ("RAIZ", "Zona de la rizosfera vegetal que aloja consorcios bacterianos depuradores", "Acto II"),
            ("TUBO", "Conducto hidráulico clínico mantenido sobre 60 °C según la norma ASHRAE 188", "Acto II"),
            ("AGUA", "Recurso vital reciclado a escala de edificio con cero descarga contaminante", "Acto I"),
        ],
    },
    "a07": {
        "title_en": "Folio A.07 · Luis Barragán Chromatic Tectonics Crossword",
        "title_es": "Folio A.07 · Crucigrama de la Tectónica Cromática de Luis Barragán",
        "en": [
            ("BARRAGAN", "1980 Pritzker laureate who transformed Mexican walls into vessels of colored light", "Act I"),
            ("GILARDI", "1976 Mexico City house where a Jacaranda courtyard leads to a sunlit indoor pool", "Act I"),
            ("ALBERS", "Bauhaus color theorist of 'Interaction of Color' who inspired chromatic relativity", "Act II"),
            ("PINK", "Signature 'Rosa Mexicano' pigment whose Kubelka-Munk K/S ratio warms courtyard air", "Act III"),
            ("STUCCO", "Matte lime-sand plaster finish that scatters sunlight into a soft Lambertian glow", "Act II"),
            ("POOL", "Indoor water mirror at Casa Gilardi bisected by a vibrant red structural column", "Act III"),
        ],
        "es": [
            ("BARRAGAN", "Arquitecto tapatío ganador del Pritzker 1980, maestro de la luz, el muro y el silencio", "Acto I"),
            ("GILARDI", "Casa estudio de 1976 en Tacubaya célebre por su alberca interior y su jacaranda", "Acto I"),
            ("ALBERS", "Autor de 'La interacción del color' cuya relatividad cromática dialoga con Barragán", "Acto II"),
            ("ESTUCO", "Acabado mineral mate de cal y arena cuya dispersión sigue la teoría de Kubelka-Munk", "Acto II"),
            ("ROSA", "Tono mexicano emblemático inspirado en bugambilias y textiles tradicionales", "Acto III"),
            ("LUZ", "Materia prima que rebota entre muros amarillos y rosas tiñendo el espacio", "Acto III"),
        ],
    },
    "a08": {
        "title_en": "Folio A.08 · Daytime Radiative Sky-Cooling Envelopes Crossword",
        "title_es": "Folio A.08 · Crucigrama de Enfriamiento Radiativo Diurno al Cielo",
        "en": [
            ("PHOTONIC", "Multi-layer dielectric roof film that reflects 97% of sunlight while emitting IR", "Act I"),
            ("STEFAN", "Phase-change moving boundary problem (and T^4 radiation law) in thermal roofs", "Act II"),
            ("WINDOW", "The 8–13 micrometer atmospheric transparency band straight into 3 K deep space", "Act II"),
            ("ALBEDO", "Solar reflectance fraction that must exceed 0.94 for sub-ambient daytime cooling", "Act III"),
            ("SPACE", "The 3 Kelvin cosmic heat sink receiving infrared photons through the atmosphere", "Act I"),
            ("ROOF", "Sky-facing building surface cooled below ambient air temperature without electricity", "Act III"),
        ],
        "es": [
            ("FOTONICO", "Recubrimiento multicapa que refleja el sol y emite calor hacia el espacio profundo", "Acto I"),
            ("VENTANA", "Banda de transparencia atmosférica de 8 a 13 micrómetros en el infrarrojo térmico", "Acto II"),
            ("ALBEDO", "Fracción de reflectancia solar superior a 0.94 necesaria para enfriar bajo el sol", "Acto III"),
            ("STEFAN", "Apellido asociado tanto a la radiación T^4 como al cambio de fase sólido-líquido", "Acto II"),
            ("CIELO", "Bóveda atmosférica atravesada por la emisión térmica rumbo al universo a 3 K", "Acto I"),
            ("TECHO", "Cubierta arquitectónica que disipa calor pasivamente sin consumir electricidad", "Acto III"),
        ],
    },
    # ---------------- PILLAR III: PHYSICS (P.01 - P.08) ----------------
    "p01": {
        "title_en": "Folio P.01 · Non-Equilibrium Fluctuation-Dissipation Crossword",
        "title_es": "Folio P.01 · Crucigrama de Fluctuación-Disipación Fuera del Equilibrio",
        "en": [
            ("SEIFERT", "Pioneer of stochastic thermodynamics and trajectory entropy production", "Act I"),
            ("KEIZER", "Statistical physicist who generalized fluctuation-dissipation to driven steady states", "Act I"),
            ("ENTROPY", "Measure of irreversibility bounded by the Thermodynamic Uncertainty Relation (TUR)", "Act II"),
            ("MARKOV", "Memoryless stochastic jump network governing ion-channel conformational states", "Act III"),
            ("ATP", "Cellular chemical fuel whose hydrolysis breaks detailed balance in ion-channel gating", "Act IV"),
            ("FLUX", "Net probability current circulating around a non-equilibrium biochemical cycle", "Act II"),
        ],
        "es": [
            ("ENTROPIA", "Magnitud termodinámica cuya producción mide la irreversibilidad de un ciclo activo", "Acto II"),
            ("SEIFERT", "Físico que formuló la termodinámica estocástica a nivel de trayectorias individuales", "Acto I"),
            ("KEIZER", "Autor de la teoría de fluctuación y disipación en estados estacionarios fuera del equilibrio", "Acto I"),
            ("MARKOV", "Red de transiciones estocásticas entre estados abiertos y cerrados de un canal", "Acto III"),
            ("CICLO", "Bucle bioquímico impulsado por hidrólisis de ATP que rompe el balance detallado", "Acto IV"),
            ("FLUJO", "Corriente neta de probabilidad que circula en un motor molecular activo", "Acto II"),
        ],
    },
    "p02": {
        "title_en": "Folio P.02 · Kuramoto Ciliary Metachronal Waves Crossword",
        "title_es": "Folio P.02 · Crucigrama de Ondas Metacronales de Cilios y Kuramoto",
        "en": [
            ("KURAMOTO", "Japanese physicist whose coupled-oscillator model explains phase synchronization", "Act I"),
            ("HUYGENS", "17th-century scientist who first observed pendulum clock synchronization on a beam", "Act I"),
            ("CILIA", "Microscopic hair-like airway organelles beating at 12–15 Hz to clear mucus", "Act II"),
            ("STOKES", "Low-Reynolds-number viscous flow regime where Oseen hydrodynamic tensors couple cilia", "Act II"),
            ("WAVE", "Traveling metachronal phase pattern that propels the airway mucus blanket", "Act III"),
            ("SYNC", "Coherent phase-locked state emerging above critical hydrodynamic coupling K_c", "Act III"),
        ],
        "es": [
            ("KURAMOTO", "Físico japonés autor del modelo paradigmático de osciladores acoplados en fase", "Acto I"),
            ("HUYGENS", "Científico que descubrió en 1665 la simpatía de dos relojes de péndulo", "Acto I"),
            ("CILIOS", "Orgánulos epiteliales microscópicos que baten en sincronía para limpiar el pulmón", "Acto II"),
            ("STOKES", "Régimen viscoso a bajo número de Reynolds gobernado por el tensor de Oseen", "Acto II"),
            ("FASE", "Ángulo de batido cuyo acoplamiento hidrodinámico genera coordinación colectiva", "Acto III"),
            ("ONDA", "Patrón metacronal viajero que impulsa el moco respiratorio hacia la faringe", "Acto III"),
        ],
    },
    "p03": {
        "title_en": "Folio P.03 · de Gennes Polymer Scaling & Subdiffusion Crossword",
        "title_es": "Folio P.03 · Crucigrama de Escalamiento Polimérico de de Gennes",
        "en": [
            ("DEGENNES", "1991 Nobel laureate who established blob scaling laws in entangled polymer meshes", "Act I"),
            ("CARREAU", "Shear-thinning constitutive law describing mucus viscosity drop under cough shear", "Act II"),
            ("MUCIN", "High-molecular-weight glycosylated biopolymer (MUC5AC / MUC5B) forming airway gels", "Act IV"),
            ("MESH", "Entangled macromolecular network with correlation pore size xi", "Act II"),
            ("BLOB", "Fundamental de Gennes thermal correlation volume inside a semi-dilute polymer", "Act I"),
            ("GEL", "Viscoelastic disulfide-crosslinked hydrogel barrier lining the bronchial tree", "Act III"),
        ],
        "es": [
            ("POLIMERO", "Macromolécula encadenada cuyo enredo físico fue modelado por Pierre-Gilles de Gennes", "Acto I"),
            ("CARREAU", "Modelo reológico que describe el adelgazamiento por corte de fluidos complejos", "Acto II"),
            ("MUCINA", "Glicoproteína formadora de gel (MUC5B y MUC5AC) en la superficie respiratoria", "Acto IV"),
            ("MALLA", "Red tridimensional cuyo tamaño de poro filtra nanopartículas por impedimento estérico", "Acto III"),
            ("PORO", "Abertura nanométrica de correlación entre cadenas poliméricas entrelazadas", "Acto II"),
            ("GEL", "Red viscoelástica reticulada por puentes disulfuro en el moco bronquial", "Acto III"),
        ],
    },
    "p04": {
        "title_en": "Folio P.04 · Button–Boucher Two-Gel Osmotic Brush Crossword",
        "title_es": "Folio P.04 · Crucigrama del Modelo de Cepillo Osmótico de Dos Geles",
        "en": [
            ("OSMOTIC", "Colloid pressure balance between the mucus layer and the periciliary brush", "Act I"),
            ("BOUCHER", "UNC pulmonary physician-scientist behind the two-gel airway hydration paradigm", "Act I"),
            ("BRUSH", "Dense tethered glycocalyx polymer carpet keeping the 7-micrometer PCL upright", "Act II"),
            ("FLORY", "Nobel polymer chemist whose Huggins mixing theory governs hydrogel swelling", "Act II"),
            ("SALT", "Chloride and sodium ions whose ion-channel transport draws water onto the airway surface", "Act IV"),
            ("PCL", "Periciliary layer whose osmotic collapse crushes beating cilia in CF", "Act III"),
        ],
        "es": [
            ("OSMOTICO", "Equilibrio de presión entre la capa de moco y el cepillo periciliar", "Acto I"),
            ("CEPILLO", "Alfombra densa de mucinas ancladas que protege el batido de los cilios", "Acto II"),
            ("BOUCHER", "Investigador coautor en Science (2012) del modelo de dos geles en la vía aérea", "Acto I"),
            ("FLORY", "Premio Nobel cuya termodinámica de redes explica el hinchamiento de hidrogeles", "Acto II"),
            ("AGUA", "Solvente vital atraído por los iones cloruro y bicarbonato hacia el epitelio", "Acto IV"),
            ("SAL", "Electrolito cuyo transporte defectuoso en FQ deshidrata la superficie bronquial", "Acto III"),
        ],
    },
    "p05": {
        "title_en": "Folio P.05 · Gamow WKB Quantum Proton Tunneling Crossword",
        "title_es": "Folio P.05 · Crucigrama de Efecto Túnel Cuántico de Protones (WKB)",
        "en": [
            ("TUNNEL", "Quantum mechanical barrier penetration where a particle crosses a classically forbidden hill", "Act I"),
            ("GAMOW", "Physicist who explained alpha decay in 1928 via quantum wave-function penetration", "Act I"),
            ("PROTON", "Hydrogen nucleus whose light mass enables measurable quantum tunneling in enzymes", "Act II"),
            ("ISOTOPE", "Kinetic H/D mass substitution (KIE) that proves proton tunneling across a barrier", "Act III"),
            ("ACTION", "WKB integral of momentum across the classically forbidden barrier width", "Act II"),
            ("WKB", "Wentzel-Kramers-Brillouin semiclassical approximation for exponential transmission", "Act I"),
        ],
        "es": [
            ("CUANTICO", "Régimen físico donde una partícula atraviesa barreras prohibidas por la mecánica clásica", "Acto I"),
            ("PROTON", "Núcleo de hidrógeno cuya baja masa favorece el efecto túnel en enlaces de hidrógeno", "Acto II"),
            ("ISOTOPO", "Sustitución de hidrógeno por deuterio (efecto cinético KIE) que revela el túnel", "Acto III"),
            ("BARRERA", "Cresta de energía potencial flanqueada por un doble pozo simétrico o asimétrico", "Acto II"),
            ("GAMOW", "Físico que aplicó en 1928 la mecánica ondulatoria al escape por efecto túnel", "Acto I"),
            ("POZO", "Mínimo local de energía potencial donde reside el estado fundamental del enlace", "Acto III"),
        ],
    },
    "p06": {
        "title_en": "Folio P.06 · Doi–Edwards Tube Reptation of 4.5 kb Chains Crossword",
        "title_es": "Folio P.06 · Crucigrama de Reptación Tubular de Doi–Edwards",
        "en": [
            ("EDWARDS", "British physicist who with Masao Doi formulated the tube model of polymer dynamics", "Act I"),
            ("TUBE", "Topological confining channel formed by surrounding entangled polymer chains", "Act II"),
            ("SNAKE", "Slithering creature that inspired de Gennes's term 'reptation' (from Latin reptare)", "Act I"),
            ("MRNA", "4.5-kilobase genetic transcript whose entanglement scales as N^3 inside dense gels", "Act IV"),
            ("CHAIN", "Long flexible macromolecule escaping its topological tube via curvilinear diffusion", "Act II"),
            ("DOI", "Japanese physicist who co-authored 'The Theory of Polymer Dynamics' with Edwards", "Act I"),
        ],
        "es": [
            ("EDWARDS", "Físico británico coautor junto con Masao Doi de la teoría del tubo polimérico", "Acto I"),
            ("CADENA", "Macromolécula larga de ARN mensajero (4.5 kb) que se desliza entre obstáculos", "Acto II"),
            ("TUBO", "Conducto virtual topológico formado por las restricciones de las cadenas vecinas", "Acto II"),
            ("ARNM", "Sigla en español del ácido ribonucleico mensajero terapéutico para el canal CFTR", "Acto IV"),
            ("NUDO", "Restricción topológica que impide el movimiento transversal de la macromolécula", "Acto III"),
            ("DOI", "Físico japonés que demostró el escalamiento cúbico del tiempo de desenredo", "Acto I"),
        ],
    },
    "p07": {
        "title_en": "Folio P.07 · 2026 Formula 1 Ground-Effect Active Aero Crossword",
        "title_es": "Folio P.07 · Crucigrama de Aerodinámica Activa y Efecto Suelo en Fórmula 1",
        "en": [
            ("VENTURI", "Converging-diverging underfloor channels accelerating air to suck an F1 car down", "Act I"),
            ("VORTEX", "Spinning floor-edge air seal that blocks high-pressure ambient air from leaking under", "Act II"),
            ("WING", "Active 2026 front and rear aero element switching between Z-mode and low-drag X-mode", "Act III"),
            ("STALL", "Abrupt aerodynamic suction loss when the floor bottom-outs, triggering porpoising", "Act II"),
            ("DRAG", "Parasitic aerodynamic resistance slashed by 55% on straights in 2026 X-mode", "Act III"),
            ("DOWN", "Direction of aerodynamic grip load enabling 5g cornering without adding car mass", "Act I"),
        ],
        "es": [
            ("VENTURI", "Túnel convergente-divergente bajo el piso de un Fórmula 1 que genera succión", "Acto I"),
            ("ALERON", "Elemento aerodinámico activo delantero y trasero que conmuta entre modo Z y modo X", "Acto III"),
            ("VORTICE", "Torbellino giratorio que sella los bordes del piso contra entradas de aire lateral", "Acto II"),
            ("SUELO", "Superficie del asfalto cuya proximidad amplifica la carga aerodinámica por efecto...", "Acto I"),
            ("CARGA", "Fuerza vertical descendente (downforce) que pega los neumáticos en curvas de 5g", "Acto II"),
            ("AIRE", "Fluido acelerado a más de 300 km/h bajo el difusor trasero del monoplaza", "Acto III"),
        ],
    },
    "p08": {
        "title_en": "Folio P.08 · Bragg Pearlescent Paint vs. Matte Stucco Optics Crossword",
        "title_es": "Folio P.08 · Crucigrama de Óptica Ondulatoria del Color y Pintura Automotriz",
        "en": [
            ("PEARL", "Mica-titania nano-flake pigment that shifts hue with viewing angle via interference", "Act I"),
            ("BRAGG", "Constructive optical path-length interference law governing thin-film color travel", "Act II"),
            ("MATTE", "Diffuse Lambertian reflection character of Luis Barragán's mineral lime stucco", "Act II"),
            ("MICA", "Transparent mineral platelet coated with TiO2 inside gonioapparent automotive lacquer", "Act III"),
            ("GLOSS", "Specular clearcoat surface reflection contrasting with Barragán's chalky walls", "Act III"),
            ("ANGLE", "Gonioapparent viewing inclination across which pearlescent automotive paint shifts color", "Act I"),
        ],
        "es": [
            ("BRAGG", "Ley de interferencia constructiva en películas delgadas que explica la iridiscencia", "Acto II"),
            ("NACAR", "Efecto perlado de escamas de mica recubiertas con dióxido de titanio en carrocerías", "Acto I"),
            ("ESTUCO", "Revestimiento mineral mate de Barragán que dispersa la luz en todas direcciones", "Acto II"),
            ("COLOR", "Sensación luminosa emergente de la interferencia de ondas o la absorción selectiva", "Acto I"),
            ("MICA", "Laminilla mineral microscópica suspendida en la laca automotriz gonioaparente", "Acto III"),
            ("ONDA", "Oscilación electromagnética cuya fase se suma o cancela según el ángulo de visión", "Acto III"),
        ],
    },
    # ---------------- PILLAR IV: MATHEMATICS (M.01 - M.08) ----------------
    "m01": {
        "title_en": "Folio M.01 · Lean 4 Fermat's Last Theorem & Modularity Crossword",
        "title_es": "Folio M.01 · Crucigrama del Último Teorema de Fermat en Lean 4",
        "en": [
            ("FERMAT", "17th-century jurist who wrote in his Arithmetica margin that a^p + b^p = c^p has no solutions", "Act I"),
            ("WILES", "Mathematician who proved semistable elliptic curve modularity with Richard Taylor", "Act I"),
            ("RIBET", "Proved that Frey's hypothetical curve would force a level-2 modular form", "Act II"),
            ("FREY", "Constructed the semistable elliptic curve linking a Fermat counterexample to modularity", "Act II"),
            ("LEAN", "Formal theorem prover hosting the 29,500-lemma machine-checked FLT blueprint", "Act IV"),
            ("CUSP", "Weight-2 modular form space S_2(Gamma_0(2)) whose zero dimension closes the proof", "Act III"),
        ],
        "es": [
            ("FERMAT", "Autor de la conjetura marginal sobre a^p + b^p = c^p que desafió 358 años a la humanidad", "Acto I"),
            ("WILES", "Matemático que demostró el levantamiento de modularidad junto con Richard Taylor", "Acto I"),
            ("RIBET", "Demostró el teorema de descenso de nivel hasta el espacio vacío de nivel N = 2", "Acto II"),
            ("CURVA", "Objeto algebraico elíptico semistable de Frey asociado a un supuesto contraejemplo", "Acto II"),
            ("LEAN", "Asistente de demostración formal donde se verificaron más de 29,500 lemas sin huecos", "Acto IV"),
            ("PRIMO", "Exponente p mayor o igual a 3 donde colapsa toda solución entera no trivial", "Acto III"),
        ],
    },
    "m02": {
        "title_en": "Folio M.02 · Riemann Zeta Zero-Density & XiPrime Crossword",
        "title_es": "Folio M.02 · Crucigrama de la Función Zeta de Riemann y XiPrime",
        "en": [
            ("RIEMANN", "1859 mathematician who connected prime distribution to complex zeros of zeta(s)", "Act I"),
            ("SIEVE", "Montgomery-Halász large orthogonality inequality bounding Dirichlet polynomials", "Act II"),
            ("ZETA", "Analytic function sum n^(-s) whose non-trivial zeros lie in the critical strip", "Act I"),
            ("CONREY", "Proved in 1989 via mollifiers that more than 2/5 of zeros lie on Re(s) = 1/2", "Act II"),
            ("STRIP", "Vertical complex region 0 < Re(s) < 1 governed by Ingham-Huxley zero-density bounds", "Act III"),
            ("ZERO", "Complex root rho = beta + i*gamma whose spectral gap governs prime fluctuations", "Act III"),
        ],
        "es": [
            ("RIEMANN", "Matemático que vinculó en 1859 los números primos con los ceros complejos de zeta(s)", "Acto I"),
            ("CRIBA", "Gran desigualdad de Montgomery y Halász que acota polinomios de Dirichlet", "Acto II"),
            ("FRANJA", "Región crítica vertical del plano complejo entre parte real 0 y parte real 1", "Acto III"),
            ("ZETA", "Función analítica cuyos ceros no triviales concentran su densidad en Re(s) = 1/2", "Acto I"),
            ("PRIMO", "Número divisible sólo por 1 y por sí mismo cuya distribución sigue el espectro de ceros", "Acto II"),
            ("CERO", "Raíz compleja verificada formalmente en el módulo Challenge/XiPrime.lean", "Acto IV"),
        ],
    },
    "m03": {
        "title_en": "Folio M.03 · FunSearch Cap Sets & AlphaEvolve Tensors Crossword",
        "title_es": "Folio M.03 · Crucigrama de Conjuntos Cap (FunSearch) y Tensores",
        "en": [
            ("TENSOR", "Bilinear 3D algebraic array whose rank-48 decomposition multiplies 4x4 matrices", "Act II"),
            ("CAPSET", "Subset of F_3^n containing no three-term arithmetic progression (line-free)", "Act I"),
            ("SLICE", "Polynomial rank method used by Ellenberg and Gijswijt to bound |S| <= 2.755^n", "Act II"),
            ("RANK", "Minimum number of scalar multiplications required to compute a matrix product", "Act III"),
            ("CODON", "Nucleotide triplet packed via finite-field coding to avoid mRNA hairpins", "Act IV"),
            ("SET", "Collection of 512 line-free vectors in F_3^8 discovered by DeepMind's FunSearch", "Act I"),
        ],
        "es": [
            ("TENSOR", "Arreglo algebraico tridimensional cuyo rango mide la complejidad de multiplicar matrices", "Acto II"),
            ("RANGO", "Número mínimo de productos escalares reducido a 48 por AlphaEvolve en matrices 4x4", "Acto III"),
            ("RECTA", "Línea afín de tres puntos en F_3^n prohibida dentro de un conjunto Cap (Cap Set)", "Acto I"),
            ("CODON", "Triplete genético optimizado combinatoriamente para estabilizar el ARNm terapéutico", "Acto IV"),
            ("MATRIZ", "Tabla cuadrada de números complejos multiplicada mediante descomposición bilineal", "Acto II"),
            ("RED", "Espacio vectorial finito F_3^8 donde FunSearch halló 512 vectores sin ternas colineales", "Acto I"),
        ],
    },
    "m04": {
        "title_en": "Folio M.04 · Polynomial Freiman–Ruzsa & Magma Graph Crossword",
        "title_es": "Folio M.04 · Crucigrama de Entropía de Freiman–Ruzsa (PFR) y Magmas",
        "en": [
            ("ENTROPY", "Shannon information measure used by Gowers, Green, Manners, and Tao to prove PFR", "Act II"),
            ("MAGMA", "Universal algebraic set with a single binary operation charted across 22M implications", "Act I"),
            ("RUZSA", "Hungarian combinatorialist behind the entropic triangle inequality and doubling distance", "Act I"),
            ("COSET", "Translated subgroup covering a set of small doubling with polynomial efficiency", "Act III"),
            ("TAO", "Fields Medalist who led the collaborative Lean 4 formalization of the PFR conjecture", "Act IV"),
            ("DAG", "Directed acyclic graph of 4,694 equational laws resolved by automated tactics", "Act III"),
        ],
        "es": [
            ("ENTROPIA", "Medida de incertidumbre de Shannon usada para demostrar la conjetura PFR en Lean 4", "Acto II"),
            ("MAGMA", "Estructura algebraica con una sola operación binaria analizada en 22 millones de leyes", "Acto I"),
            ("RUZSA", "Matemático autor de la distancia entrópica y la desigualdad triangular aditiva", "Acto I"),
            ("GRAFO", "Red dirigida de 4,694 ecuaciones algebraicas clasificada colaborativamente", "Acto III"),
            ("GRUPO", "Subestructura algebraica cuyos traslados cubren conjuntos con baja duplicación", "Acto III"),
            ("TAO", "Medallista Fields que dirigió la formalización en Lean 4 del teorema PFR", "Acto IV"),
        ],
    },
    "m05": {
        "title_en": "Folio M.05 · AlphaGeometry 2 Neuro-Symbolic Olympiad Crossword",
        "title_es": "Folio M.05 · Crucigrama de Geometría Olímpica Neuro-Simbólica (AlphaGeometry 2)",
        "en": [
            ("GEOMETRY", "Euclidean axiomatic science where neural intuition proposes auxiliary points", "Act I"),
            ("CIRCLE", "Cyclic four-point locus connecting inscribed angles in Olympiad proofs", "Act II"),
            ("CHORD", "Line segment joining two points on a circumcircle in cyclic quadrangle chasing", "Act III"),
            ("ANGLE", "Directed geometric rotation tracked symbolically by the DD+AR deduction engine", "Act II"),
            ("PROOF", "Deductive chain certified at gold-medal IMO level by neuro-symbolic search", "Act IV"),
            ("ARC", "Portion of a circle subtending equal inscribed angles across a cyclic polygon", "Act III"),
        ],
        "es": [
            ("CIRCULO", "Lugar geométrico auxiliar trazado para inscribir cuadriláteros cíclicos olímpicos", "Acto II"),
            ("ANGULO", "Rotación dirigida cuyas igualdades encadena el motor deductivo simbólico DD+AR", "Acto II"),
            ("CUERDA", "Segmento que une dos puntos de una circunferencia en un problema de la IMO", "Acto III"),
            ("PRUEBA", "Demostración sintética verificada paso a paso sin aproximación numérica", "Acto IV"),
            ("PUNTO", "Construcción auxiliar propuesta por la red neuronal para desbloquear el teorema", "Acto I"),
            ("ARCO", "Tramo de circunferencia que subtiende ángulos inscritos iguales", "Acto III"),
        ],
    },
    "m06": {
        "title_en": "Folio M.06 · Sub-Cubic APSP, 3SUM & Step Verification Crossword",
        "title_es": "Folio M.06 · Crucigrama de Complejidad Subcúbica (APSP / 3SUM) y PRM800K",
        "en": [
            ("MATRIX", "Tropical min-plus distance array multiplied in sub-cubic time by Williams's algorithm", "Act I"),
            ("GRAPH", "Weighted vertex-edge network whose all-pairs shortest paths (APSP) are computed", "Act II"),
            ("PATH", "Minimum-weight route between vertex pairs accelerated by Razborov-Smolensky circuits", "Act II"),
            ("ROUND", "Semidefinite programming relaxation step proven optimal for CSPs by Raghavendra", "Act III"),
            ("STEP", "Individual reasoning line audited by process reward models (PRM800K)", "Act IV"),
            ("NODE", "Vertex in a weighted shortest-path network or reasoning search tree", "Act III"),
        ],
        "es": [
            ("CAMINO", "Ruta más corta entre todos los pares de vértices (APSP) en un grafo ponderado", "Acto I"),
            ("GRAFO", "Red de nodos y aristas analizada mediante el producto matricial tropical min-plus", "Acto II"),
            ("CIRCUito".upper(), "Polinomio booleano de Razborov-Smolensky que acelera la búsqueda subcúbica", "Acto II"),
            ("PASO", "Eslabón individual de razonamiento verificado por modelos de recompensa de proceso", "Acto IV"),
            ("NODO", "Vértice de una red combinatoria o árbol de búsqueda en complejidad fina", "Acto III"),
            ("RED", "Estructura de restricciones donde la naturaleza evita paisajes NP-duros", "Acto IV"),
        ],
    },
    "m07": {
        "title_en": "Folio M.07 · Formula 1 Pontryagin Control & FNO Crossword",
        "title_es": "Folio M.07 · Crucigrama de Control Óptimo de Pontryagin y FNO en Fórmula 1",
        "en": [
            ("COSTATE", "Shadow price multiplier lambda(s) governing electric battery deployment per lap", "Act II"),
            ("FOURIER", "Spectral transform inside Neural Operators (FNO) solving 3D wake PDEs in milliseconds", "Act III"),
            ("BATTERY", "4 MJ lithium-ion energy store harvested and deployed by the 350 kW MGU-K motor", "Act I"),
            ("CLIP", "Power derating at the end of a straight when the battery state-of-charge hits zero", "Act II"),
            ("APEX", "Minimum-radius cornering point where traction ellipse grip limits MGU-K harvesting", "Act III"),
            ("LAP", "Complete circuit trajectory minimized via Hamilton-Jacobi-Bellman optimal control", "Act I"),
        ],
        "es": [
            ("BATERIA", "Almacén de energía de 4 MJ gestionado por el motor eléctrico MGU-K de 350 kW", "Acto I"),
            ("FOURIER", "Transformada espectral empleada por los Operadores Neurales (FNO) aerodinámicos", "Acto III"),
            ("VUELTA", "Recorrido completo al circuito cuyo tiempo minimiza el principio de Pontryagin", "Acto I"),
            ("CURVA", "Sector del trazado donde el agarre del neumático limita la regeneración eléctrica", "Acto II"),
            ("MOTOR", "Unidad de potencia híbrida 2026 con reparto 50/50 entre combustión y electricidad", "Acto II"),
            ("META", "Línea final de la recta donde un mal coestado provoca pérdida de potencia (clipping)", "Acto III"),
        ],
    },
    "m08": {
        "title_en": "Folio M.08 · Schrödinger Riemannian Color Manifolds Crossword",
        "title_es": "Folio M.08 · Crucigrama de Geometría Riemanniana del Color de Schrödinger",
        "en": [
            ("MACADAM", "1942 physicist who measured just-noticeable color discrimination ellipses in human vision", "Act I"),
            ("METRIC", "Riemannian tensor g_ij measuring true perceptual distance across 3D color space", "Act II"),
            ("GEODESIC", "Shortest curved path in Schrödinger's color manifold explaining the Abney hue shift", "Act II"),
            ("CONE", "Retinal L, M, or S photoreceptor projecting infinite spectra into 3D tristimulus space", "Act I"),
            ("ELLIPSE", "Covariance contour of indistinguishable chromaticity points on the CIE diagram", "Act III"),
            ("EYE", "Human optical organ whose non-Euclidean Fisher-Rao metric curves color space", "Act III"),
        ],
        "es": [
            ("MACADAM", "Físico que midió en 1942 las elipses de discriminación cromática del ojo humano", "Acto I"),
            ("METRICA", "Tensor riemanniano que define la distancia perceptual real entre dos colores", "Acto II"),
            ("ELIPSE", "Contorno de incertidumbre visual dentro del cual dos tonos resultan indistinguibles", "Acto III"),
            ("CONO", "Fotorreceptor retiniano (L, M o S) que proyecta el espectro en tres dimensiones", "Acto I"),
            ("COLOR", "Variedad curva tridimensional estudiada por Helmholtz y Erwin Schrödinger en 1920", "Acto II"),
            ("OJO", "Órgano visual cuya respuesta logarítmica genera la curvatura del espacio cromático", "Acto III"),
        ],
    },
    "e09": {
        "title_en": "Folio E.09 · Autogenous Bacterial Self-Healing Concrete Crossword",
        "title_es": "Folio E.09 · Crucigrama de Concreto Autocurativo Bacteriano y Calcita",
        "en": [
            ("CALCITE", "Rhombohedral CaCO3 mineral precipitated by alkaliphilic Bacillus spores to seal cracks", "Act II"),
            ("SPORE", "Dormant bacterial capsule embedded in expanded clay aggregate that awakens upon water ingress", "Act I"),
            ("CRACK", "Tensile micro-fissure whose cubic Poiseuille leakage drops 99% as mineral bridges grow", "Act II"),
            ("CODA", "Multiply scattered ultrasonic wave interferometry (CWI) tracking internal stiffness recovery", "Act III"),
            ("LACTATE", "Bio-available calcium precursor metabolized by bacteria into carbonate ions", "Act I"),
            ("PORE", "Capillary throat governed by Lucas-Washburn root-time imbibition z(t)", "Act II"),
        ],
        "es": [
            ("CALCITA", "Cristal romboédrico de carbonato de calcio precipitado por bacterias para sellar fisuras", "Acto II"),
            ("ESPORA", "Cápsula bacteriana latente de Bacillus que despierta al ingresar agua por capilaridad", "Acto I"),
            ("FISURA", "Grieta milimétrica cuyo flujo de fuga cae con la ley cúbica al mineralizarse", "Acto II"),
            ("LACTATO", "Precursor orgánico de calcio transformado en iones carbonato dentro de la grieta", "Acto I"),
            ("SONIDO", "Onda ultrasónica coda dispersada que verifica el cierre interno sin dañar el puente", "Acto III"),
            ("AGUA", "Fluido que asciende por imbibición capilar de Lucas-Washburn activando la autocuración", "Acto II"),
        ],
    },
    "e10": {
        "title_en": "Folio E.10 · 3D Concrete Printing (3DCP) & Roussel Thixotropy Crossword",
        "title_es": "Folio E.10 · Crucigrama de Impresión 3D de Concreto y Tixotropía de Roussel",
        "en": [
            ("ROUSSEL", "Rheologist who formulated the linear structuration rate A_thix for printable concretes", "Act I"),
            ("NOZZLE", "Robotic extrusion printhead depositing wet mortar filaments without formwork", "Act I"),
            ("LAYER", "Freshly printed horizontal mortar filament carrying the hydrostatic weight of upper courses", "Act II"),
            ("BUCKLE", "Suiker elastic stability failure mode when a slender printed wall bends laterally", "Act II"),
            ("YIELD", "Tresca plastic collapse threshold tau_0(t) that must outpace vertical build rate", "Act II"),
            ("PUMP", "High-shear delivery stage before flocculation rebuilds static structure on the print bed", "Act III"),
        ],
        "es": [
            ("ROUSSEL", "Autor de las leyes de estructuración tixotrópica A_thix para concreto imprimible", "Acto I"),
            ("CAPA", "Filamento horizontal de mortero depositado por el robot sin necesidad de cimbra", "Acto I"),
            ("PANDEO", "Falla de inestabilidad elástica lateral de Suiker en muros impresos esbeltos", "Acto II"),
            ("ROBOT", "Brazo extrusor cuya velocidad de avance se acopla al endurecimiento del cemento", "Acto III"),
            ("FLUJO", "Movimiento del mortero fresco a través de la boquilla antes de su refloculación", "Acto II"),
            ("PESO", "Carga gravitacional acumulada que exige superar el esfuerzo de cedencia plástico", "Acto II"),
        ],
    },
    "a09": {
        "title_en": "Folio A.09 · Hygroscopic Timber Skins & Timoshenko Curvature Crossword",
        "title_es": "Folio A.09 · Crucigrama de Pieles de Madera Higroscópica y Timoshenko",
        "en": [
            ("BILAYER", "Two-ply cross-grained veneer laminate that bends autonomously under humidity shifts", "Act II"),
            ("BEECH", "European hardwood (Fagus sylvatica) used in the HygroSkin zero-energy climate pavilions", "Act I"),
            ("SWELL", "Orthotropic moisture expansion of cellulose microfibrils below the fiber saturation point", "Act II"),
            ("CONE", "Spruce seed scale whose passive wet/dry opening inspired biomimetic timber facades", "Act I"),
            ("GRAIN", "Anisotropic wood fiber orientation controlling radial versus longitudinal stiffness", "Act III"),
            ("ARCH", "Self-forming elastic shell curvature kappa predicted by Timoshenko's 1925 theorem", "Act II"),
        ],
        "es": [
            ("MADERA", "Material celular ortotrópico cuyas microfibrillas de celulosa responden a la humedad", "Acto I"),
            ("BICAPA", "Laminado de dos chapas con veta cruzada cuya curvatura gobierna la ley de Timoshenko", "Acto II"),
            ("CLIMA", "Ambiente exterior cuya humedad relativa abre y cierra la fachada con cero energía", "Acto III"),
            ("HAYA", "Especie forestal empleada por Achim Menges en los pabellones autónomos HygroSkin", "Acto I"),
            ("FIBRA", "Elemento estructural cuya orientación define el hinchamiento diferencial sin motores", "Acto II"),
            ("ARCO", "Geometría curva adoptada espontáneamente por el panel al variar el contenido de agua", "Acto II"),
        ],
    },
    "a10": {
        "title_en": "Folio A.10 · Kinetic Origami & Miura-Ori Auxetic Facades Crossword",
        "title_es": "Folio A.10 · Crucigrama de Origami Cinético y Fachadas Auxéticas Miura-Ori",
        "en": [
            ("MIURA", "Japanese astrophysicist who invented the rigid-foldable parallelogram origami tessellation", "Act I"),
            ("CREASE", "Mountain or valley fold line acting as a zero-backlash elastic hinge between facets", "Act II"),
            ("AUXETIC", "Metamaterial property of negative in-plane Poisson ratio expanding in both axes at once", "Act II"),
            ("SOLAR", "Radiative heat gain modulated dynamically by kinetic Mashrabiya origami shading modules", "Act III"),
            ("VERTEX", "Degree-4 spherical linkage intersection where Kawasaki's alternating angle sum holds", "Act II"),
            ("FOLD", "Single-degree-of-freedom isometric actuation mode of a rigid origami sheet", "Act I"),
        ],
        "es": [
            ("ORIGAMI", "Arte y geometría de plegado isométrico aplicado a envolventes solares desplegables", "Acto I"),
            ("MIURA", "Creador de la teselación de paralelogramos con razón de Poisson negativa en el plano", "Acto I"),
            ("PLIEGUE", "Línea de bisagra en montaña o valle que articula facetas rígidas sin fricción", "Acto II"),
            ("SOLAR", "Radiación térmica regulada por módulos cinéticos inspirados en la celosía Mashrabiya", "Acto III"),
            ("VERTICE", "Nodo de grado cuatro donde la suma de ángulos alternos cumple el teorema de Kawasaki", "Acto II"),
            ("MAPA", "Hoja plegada que se despliega de forma sincronizada con un solo grado de libertad", "Acto I"),
        ],
    },
    "p09": {
        "title_en": "Folio P.09 · Taylor-Cone Electrohydrodynamic Aerosols Crossword",
        "title_es": "Folio P.09 · Crucigrama de Conos de Taylor y Aerosoles Monodispersos",
        "en": [
            ("TAYLOR", "Fluid physicist who derived the exact 49.3-degree electrohydrodynamic equilibrium half-angle", "Act I"),
            ("DROPLET", "Monodisperse 2.4-micron inhalable mist sphere carrying intact mRNA lipid nanoparticles", "Act III"),
            ("CHARGE", "Surface electrostatic repulsion balanced against capillary surface tension gamma", "Act II"),
            ("PLUME", "Fine aerosol cloud emitted from the apex micro-jet without ultrasonic shear damage", "Act III"),
            ("CONE", "Legendre P_1/2 equipotential meniscus geometry formed under critical voltage", "Act II"),
            ("JET", "Sub-micron liquid filament emerging from the meniscus apex before varicose breakup", "Act II"),
        ],
        "es": [
            ("TAYLOR", "Físico que demostró en 1964 el semiángulo exacto de 49.3 grados del menisco eléctrico", "Acto I"),
            ("AEROSOL", "Niebla monodispersa de gotas micrométricas inhalables para entrega pulmonar profunda", "Acto III"),
            ("CARGA", "Repulsión electrostática superficial que vence la tensión capilar en el límite de Rayleigh", "Acto II"),
            ("GOTA", "Esfera líquida de 2.4 micrómetros que preserva intactas las nanopartículas de ARNm", "Acto III"),
            ("CONO", "Geometría equipotencial de Legendre formada en la punta del capilar bajo alto voltaje", "Acto II"),
            ("RED", "Malla vibrante o boquilla microfluídica que nebuliza terapias génicas sin cizalla", "Acto III"),
        ],
    },
    "p10": {
        "title_en": "Folio P.10 · Topological Photonics & Haldane-Raghu Chern Insulators Crossword",
        "title_es": "Folio P.10 · Crucigrama de Fotónica Topológica y Aislantes de Chern",
        "en": [
            ("CHERN", "Quantized integer topological invariant C governing unidirectional edge waveguiding", "Act II"),
            ("BERRY", "Momentum-space gauge curvature Omega_n(k) integrated across the photonic Brillouin zone", "Act II"),
            ("PHOTON", "Light quantum routed around sharp 90-degree crystal defects with zero backscatter", "Act I"),
            ("HALDANE", "Nobel physicist who with Raghu extended quantum Hall chiral edge states to photonics", "Act I"),
            ("EDGE", "Topologically protected boundary channel immune to cavity disorder and roughness", "Act III"),
            ("MODE", "One-way electromagnetic eigenstate confined between crystals of distinct topology", "Act II"),
        ],
        "es": [
            ("FOTON", "Cuanto de luz guiado sin reflexión alrededor de esquinas de 90 grados e impurezas", "Acto I"),
            ("CHERN", "Invariante topológico entero que determina el número de canales quirales de borde", "Acto II"),
            ("BERRY", "Curvatura geométrica en el espacio de momentos integrada sobre la zona de Brillouin", "Acto II"),
            ("BORDE", "Frontera protegida topológicamente donde la onda viaja en un solo sentido sin pérdidas", "Acto III"),
            ("CRISTAL", "Red fotónica periódica cuya ruptura de simetría abre una brecha de banda no trivial", "Acto I"),
            ("ONDA", "Perturbación electromagnética o acústica inmune a la retrodispersión por desorden", "Acto III"),
        ],
    },
    "m09": {
        "title_en": "Folio M.09 · Wasserstein-2 Optimal Transport & Sinkhorn Flow Crossword",
        "title_es": "Folio M.09 · Crucigrama de Transporte Óptimo Wasserstein-2 y Sinkhorn",
        "en": [
            ("OPTIMAL", "Minimum-cost coupling plan between source and target probability measures", "Act I"),
            ("MONGE", "1781 engineer-geometer who posed the foundational earth-moving transport problem", "Act I"),
            ("ENTROPY", "Kullback-Leibler regularization enabling fast GPU Sinkhorn matrix scaling", "Act III"),
            ("FLOW", "Continuous velocity field v_t transporting probability mass along a geodesic bridge", "Act II"),
            ("COST", "Quadratic ground distance |x - y|^2 minimized across couplings in Kantorovich duality", "Act I"),
            ("MASS", "Conserved probability density rho(t,x) satisfying the Benamou-Brenier continuity PDE", "Act II"),
        ],
        "es": [
            ("MONGE", "Matemático francés que formuló en 1781 el problema geométrico de mover tierra con costo mínimo", "Acto I"),
            ("BRENIER", "Coautor de la formulación dinámica de fluidos para la distancia geodésica Wasserstein-2", "Acto II"),
            ("FLUJO", "Campo de velocidad continuo que transporta distribuciones celulares o generativas", "Acto II"),
            ("COSTO", "Integral cuadrática de transporte minimizada entre la distribución inicial y la final", "Acto I"),
            ("MASA", "Densidad de probabilidad conservada a lo largo de la ecuación de continuidad", "Acto II"),
            ("RED", "Acoplamiento óptimo calculado en paralelo mediante el algoritmo entrópico de Sinkhorn", "Acto III"),
        ],
    },
    "m10": {
        "title_en": "Folio M.10 · Persistent Homology, Betti Barcodes & Percolation Crossword",
        "title_es": "Folio M.10 · Crucigrama de Homología Persistente y Códigos de Betti",
        "en": [
            ("BARCODE", "Multiset of birth-to-death filtration intervals [b_i, d_i) distinguishing signal from noise", "Act II"),
            ("BETTI", "Topological invariant beta_k counting connected components (k=0), loops (k=1), and voids (k=2)", "Act I"),
            ("SIMPLEX", "Vertex, edge, triangle, or tetrahedron building block in a Vietoris-Rips filtration", "Act II"),
            ("CYCLE", "Closed 1D chain of edges surrounding a percolating pore throat in disordered media", "Act III"),
            ("HOLE", "Topological tunnel or cavity whose persistence lifetime measures structural bottlenecks", "Act I"),
            ("SPAN", "Filtration persistence lifetime d_i - b_i stable under Gromov-Hausdorff perturbations", "Act II"),
        ],
        "es": [
            ("BETTI", "Número topológico que cuenta componentes conexas, túneles y cavidades en un complejo", "Acto I"),
            ("CICLO", "Lazo cerrado de aristas que rodea una garganta de poro percolante en moco o concreto", "Acto II"),
            ("FILTRO", "Familia anidada de complejos simpliciales de Vietoris-Rips al crecer la escala epsilon", "Acto II"),
            ("BARRA", "Intervalo de nacimiento a muerte que separa la topología real del ruido experimental", "Acto III"),
            ("PORO", "Canal tridimensional cuyo radio crítico de percolación queda certificado por homología", "Acto III"),
            ("DATO", "Nube de puntos ruidosa cuya forma global es inmune a perturbaciones según Cohen-Steiner", "Acto I"),
        ],
    },
    "e11": {
        "title_en": "Folio E.11 · SIMP Topology Optimization, Michell Trusses & Inerter Damping Crossword",
        "title_es": "Folio E.11 · Crucigrama de Optimización Topológica SIMP y Amortiguadores Inerter",
        "en": [
            ("INERTER", "Two-terminal mechanical flywheel device generating force proportional to relative acceleration", "Act II"),
            ("MICHELL", "1904 engineer who derived minimum-weight orthogonal funicular truss layouts", "Act I"),
            ("BONE", "Trabecular skeletal tissue that remodels along principal stress trajectories under Wolff's Law", "Act I"),
            ("SIMP", "Power-law density penalization driving continuum finite elements toward 0/1 structural ribs", "Act II"),
            ("SLAB", "Floor plate whose dead concrete mass is cut by 65 percent via funicular rib carving", "Act III"),
            ("MASS", "Apparent inertial resistance amplified 200-fold by a spinning rack-and-pinion flywheel", "Act II"),
        ],
        "es": [
            ("MICHELL", "Ingeniero de 1904 que formuló las redes ortogonales de peso mínimo en tensión y compresión", "Acto I"),
            ("HUESO", "Tejido trabecular del fémur que inspira nervaduras estructurales con 65% menos cemento", "Acto I"),
            ("LOSA", "Placa de entrepiso esculpida sin cimbra mediante elementos finitos en FEniCS/dolfinx", "Acto III"),
            ("GIRO", "Rotación de alta velocidad del volante de inercia que frena la oscilación por viento", "Acto II"),
            ("PESO", "Masa muerta de concreto eliminada donde el esfuerzo principal es cercano a cero", "Acto II"),
            ("RED", "Malla de elementos finitos regularizada con el filtro PDE de Helmholtz", "Acto III"),
        ],
    },
    "e12": {
        "title_en": "Folio E.12 · RISC-V Silicon, Control Barrier Functions & Firefly Grid Sync Crossword",
        "title_es": "Folio E.12 · Crucigrama de Silicio RISC-V y Barreras de Control en Redes",
        "en": [
            ("BARRIER", "Lyapunov-like safety function h(x) >= 0 that keeps model trajectories out of blackout states", "Act II"),
            ("RISCV", "Open instruction-set architecture whose small processors have been verified in Coq with Kami", "Act I"),
            ("INVERTER", "Grid-forming power electronics converter programmed with synthetic rotational inertia", "Act II"),
            ("GRID", "Continental 60 Hz electrical network synchronized via Kuramoto phase-locking laws", "Act I"),
            ("SAFE", "Forward-invariant operating region certified by Nagumo's subtangentiality theorem", "Act II"),
            ("ROCQ", "Current name of the Coq proof assistant, used with Kami to verify hardware designs", "Act IV"),
        ],
        "es": [
            ("BARRERA", "Función matemática de control h(x) >= 0 que impide cruzar la frontera de apagón eléctrico", "Acto II"),
            ("INERCIA", "Resistencia rotacional sintética programada en inversores para frenar caídas de frecuencia", "Acto II"),
            ("SILICIO", "Material del chip RISC-V cuya prueba formal es una hipótesis de diseño en este folio", "Acto I"),
            ("FASE", "Ángulo de sincronización acoplado entre inversores solares como luciérnagas de Kuramoto", "Acto II"),
            ("RED", "Sistema eléctrico 100% renovable modelado en software abierto PyPSA sin turbinas de carbón", "Acto I"),
            ("GIRO", "Rotación virtual sincronizada a 60 Hz en cada barra de la red continental", "Acto III"),
        ],
    },
    "a11": {
        "title_en": "Folio A.11 · 3D Polyhedral Graphic Statics, Airy Stress & Guastavino Vaults Crossword",
        "title_es": "Folio A.11 · Crucigrama de Estática Gráfica Poliédrica 3D y Bóvedas sin Acero",
        "en": [
            ("MAXWELL", "Physicist who proved in 1864 that reciprocal force diagrams are projections of 3D stress polyhedra", "Act I"),
            ("VAULT", "Thin compression-only masonry or tile shell spanning 16 meters with zero steel rebar", "Act I"),
            ("DUAL", "Reciprocal force polyhedron whose closed face areas equal the axial forces in the form ribs", "Act II"),
            ("AIRY", "Stress potential surface Phi(x,y) whose strict concavity certifies pure compression", "Act II"),
            ("TILE", "Thin terracotta timbrel unit used by Rafael Guastavino in Grand Central Terminal", "Act I"),
            ("RIB", "Funicular stiffening arch sculpted in open-source COMPAS to cut floor concrete by 72%", "Act III"),
        ],
        "es": [
            ("BOVEDA", "Cubierta delgada de piedra o ladrillo que trabaja a pura compresión sin varillas de acero", "Acto I"),
            ("MAXWELL", "Científico que descubrió la dualidad entre poliedros de fuerza 3D y superficies de Airy", "Acto I"),
            ("CARA", "Polígono del poliedro recíproco cuya área mide exactamente la fuerza axial en la nervadura", "Acto II"),
            ("ARCO", "Trayectoria funicular de empuje contenida dentro del núcleo central de Heyman", "Acto II"),
            ("LOSA", "Piso abovedado diseñado con software abierto COMPAS que ahorra 72% de carbono", "Acto IV"),
            ("CAL", "Mortero tradicional cohesivo empleado en bóvedas tabicadas de Guastavino", "Acto I"),
        ],
    },
    "a12": {
        "title_en": "Folio A.12 · Tensegrity Cable-Strut Domes & 8-13 um Radiative Sky-Cooling Crossword",
        "title_es": "Folio A.12 · Crucigrama de Domos de Tensegridad y Enfriamiento Radiativo al Cielo",
        "en": [
            ("SNELSON", "Sculptor whose floating-compression needle towers inspired Buckminster Fuller's tensegrity", "Act I"),
            ("CABLE", "Continuous prestressed tension element that stabilizes isolated compression struts via K_G", "Act II"),
            ("STRUT", "Isolated compression bar floating inside a tension net without touching neighboring bars", "Act I"),
            ("WINDOW", "8 to 13 micrometer atmospheric infrared transparency band beaming heat to 3 Kelvin space", "Act II"),
            ("DOME", "Ultralight 12 kg/m2 Geiger cable-strut canopy spanning 120 meters over urban plazas", "Act III"),
            ("COOL", "Sub-ambient daytime temperature drop of 5.2 C achieved with zero compressor electricity", "Act IV"),
        ],
        "es": [
            ("CABLE", "Elemento continuo en tracción cuyo preesfuerzo t_0 rigidiza los mecanismos del domo", "Acto II"),
            ("DOMO", "Cubierta ultraligera de tensegridad de 12 kg/m2 que cubre grandes plazas urbanas", "Acto I"),
            ("CIELO", "Sumidero térmico a 3 Kelvin que recibe calor infrarrojo por la ventana de 8 a 13 micras", "Acto II"),
            ("BARRA", "Puntal aislado de acero en compresión que flota sin tocar ninguna otra barra", "Acto I"),
            ("SOL", "Radiación visible reflejada al 97% por la membrana fotónica microporosa", "Acto III"),
            ("RED", "Malla en equilibrio analizada mediante descomposición en valores singulares de Pellegrino", "Acto II"),
        ],
    },
    "p11": {
        "title_en": "Folio P.11 · Surface-Code Quantum Error Correction & FeMoCo Nitrogen Catalysis Crossword",
        "title_es": "Folio P.11 · Crucigrama de Corrección Cuántica de Superficie y Catálisis de Nitrógeno",
        "en": [
            ("SURFACE", "Topological 2D stabilizer code by Kitaev with a 1 percent fault-tolerance threshold", "Act II"),
            ("QUBIT", "Quantum superposition state protected by commuting star X and plaquette Z parity checks", "Act II"),
            ("FEMOCO", "Iron-molybdenum [Fe7MoS9C] nitrogenase cofactor that fixes N2 at ambient temperature", "Act I"),
            ("ANYON", "Non-Abelian quasiparticle excitation braided in 2+1D spacetime to execute faultless gates", "Act II"),
            ("STIM", "Craig Gidney's fast open-source stabilizer circuit simulator for quantum error correction", "Act IV"),
            ("CODE", "Distance-27 logical encoding crushing error rates to 3e-16 per syndrome round", "Act III"),
        ],
        "es": [
            ("CUANTICO", "Procesador tolerante a fallos capaz de simular los electrones entrelazados de la nitrogenasa", "Acto I"),
            ("CODIGO", "Red topológica de superficie de Kitaev que corrige errores bajo el umbral del 1 por ciento", "Acto II"),
            ("PARIDAD", "Chequeo conmutativo de estrella y plaqueta que detecta fallos sin destruir la superposición", "Acto II"),
            ("AMONIACO", "Fertilizante esencial producido a temperatura ambiente por el cofactor FeMoCo", "Acto I"),
            ("RED", "Cuadrícula bidimensional de qubits simulada a gran velocidad en software abierto Stim", "Acto IV"),
            ("FASE", "Estimación cuántica de autovalores en PySCF con precisión química menor a 1 kcal/mol", "Acto III"),
        ],
    },
    "p12": {
        "title_en": "Folio P.12 · Hilbert's Sixth Problem: Boltzmann Kinetics to Navier-Stokes Crossword",
        "title_es": "Folio P.12 · Crucigrama del Sexto Problema de Hilbert: De Boltzmann a Navier-Stokes",
        "en": [
            ("HILBERT", "Mathematician who posed in 1900 the 6th Problem of axiomatizing physics from atoms to fluids", "Act I"),
            ("SPHERE", "Elastic Newtonian billiard particle of diameter epsilon in the Boltzmann-Grad limit", "Act II"),
            ("FLUID", "Macroscopic incompressible Navier-Stokes continuum emerging as Knudsen number Kn -> 0", "Act II"),
            ("TREE", "Layered Feynman-like interaction graph pruned by Deng, Hani, and Ma to bound recollisions", "Act II"),
            ("SCALE", "Hydrodynamic continuum regime bridged from microscopic collisions across 15 orders of magnitude", "Act I"),
            ("LIMIT", "Boltzmann-Grad and Knudsen scaling threshold where kinetic gases converge to continuum PDEs", "Act IV"),
        ],
        "es": [
            ("HILBERT", "Matemático que planteó en 1900 el sexto problema sobre el paso de átomos al continuo fluido", "Acto I"),
            ("ESFERA", "Partícula dura newtoniana cuyas colisiones reversibles generan la ecuación de Boltzmann", "Acto I"),
            ("FLUIDO", "Medio continuo gobernado por Navier-Stokes cuando el número de Knudsen tiende a cero", "Acto II"),
            ("ARBOL", "Grafo de interacción por capas de Deng, Hani y Ma que acota las recolisiones a largo plazo", "Acto II"),
            ("CAOS", "Hipótesis de descorrelación molecular de Boltzmann demostrada rigurosamente en 2025", "Acto I"),
            ("OLA", "Corriente macroscópica y vórtice climático predicho 10,000 veces más rápido con operadores", "Acto IV"),
        ],
    },
    "m11": {
        "title_en": "Folio M.11 · 3D Kakeya Conjecture (Wang-Zahl) & Guth-Maynard 30/13 Riemann Bound Crossword",
        "title_es": "Folio M.11 · Crucigrama de la Conjetura de Kakeya 3D y la Cota 30/13 de Guth-Maynard",
        "en": [
            ("KAKEYA", "Conjecture resolved in 3D by Wang and Zahl proving direction-complete needle sets have dimension 3", "Act I"),
            ("NEEDLE", "Unit line segment rotated through all 3D directions inside a Besicovitch set", "Act I"),
            ("PRIME", "Integer building block whose consecutive gap is bounded by p_n^(17/30) via Guth-Maynard", "Act II"),
            ("ZETA", "Riemann analytic function whose off-critical-line zeros are bounded by exponent 30/13", "Act II"),
            ("TUBE", "Thin cylindrical wave-packet support of width delta analyzed across sticky and grainy scales", "Act II"),
            ("GAP", "Interval between consecutive primes narrowed by breaking Ingham's 1940 zero-density barrier", "Act III"),
        ],
        "es": [
            ("KAKEYA", "Conjetura tridimensional resuelta en 2025 por Hong Wang y Joshua Zahl con dimensión 3", "Acto I"),
            ("RECTA", "Segmento unitario de Besicovitch capaz de girar en todas las direcciones del espacio", "Acto I"),
            ("PRIMO", "Número entero cuya brecha consecutiva queda acotada por el exponente 17/30", "Acto II"),
            ("TUBO", "Cilindro delgado de ancho delta donde se concentran paquetes de ondas de Fourier", "Acto II"),
            ("CERO", "Raíz de la función zeta de Riemann acotada con el exponente 30/13 de Guth y Maynard", "Acto II"),
            ("LEAN", "Asistente de pruebas formales donde anthropics/formal-math verifica cotas espectrales Zeta23", "Acto IV"),
        ],
    },
    "m12": {
        "title_en": "Folio M.12 · Anthropic Lean 4 Complexity (ETHIsFalse) & Post-Quantum Lattices Crossword",
        "title_es": "Folio M.12 · Crucigrama de Complejidad en Lean 4 y Retículos Post-Cuánticos ML-KEM",
        "en": [
            ("LATTICE", "768-dimensional periodic crystal grid underlying NIST FIPS 203 ML-KEM post-quantum security", "Act II"),
            ("QUANTUM", "Shor's Fourier period-finding threat neutralized by Module Learning With Errors (ML-KEM)", "Act I"),
            ("NOISE", "Centered binomial error vector e hiding the secret lattice point b = A*s + e (mod 3329)", "Act II"),
            ("LEAN", "Formal theorem prover hosting zero-sorry proofs in anthropics/formal-math (EightSquare & ETHIsFalse)", "Act I"),
            ("RANK", "Bilinear multiplication count compressed from 64 to <= 28 in EightSquare.lean", "Act III"),
            ("KEY", "Cryptographic public encapsulation verified in open-quantum-safe/liboqs", "Act IV"),
        ],
        "es": [
            ("RETICULO", "Red cristalina en 768 dimensiones que protege el estándar post-cuántico NIST FIPS 203", "Acto II"),
            ("PRUEBA", "Demostración verificada por máquina sin axiomas sorry en anthropics/formal-math", "Acto I"),
            ("RUIDO", "Vector de error binomial e que oculta el secreto en la niebla de Learning With Errors", "Acto II"),
            ("CLAVE", "Llave criptográfica resistente al algoritmo cuántico de Shor mediante liboqs", "Acto IV"),
            ("RANGO", "Complejidad bilineal de ocho cuadrados reducida de 64 a 28 productos en Lean 4", "Acto III"),
            ("RED", "Grafo de dependencias formales verificado por el núcleo de tipos de Lean 4", "Acto I"),
        ],
    },
}


def build_all_folio_puzzles(target_size: int = 10) -> dict[str, dict[str, Any]]:
    """Compile and verify all 33 EN and 33 ES-MX crosswords into uniform `target_size x target_size` grids."""
    compiled: dict[str, dict[str, Any]] = {}
    for slug, spec in RAW_PUZZLE_SPECS.items():
        en_puzzle = pad_puzzle_to_square(compile_crossword(spec["en"], max_span=target_size), target_size=target_size)
        es_puzzle = pad_puzzle_to_square(compile_crossword(spec["es"], max_span=target_size), target_size=target_size)
        en_puzzle["title"] = spec["title_en"]
        es_puzzle["title"] = spec["title_es"]
        # Verify EN and ES grids are distinct puzzles
        assert en_puzzle["grid"] != es_puzzle["grid"], f"{slug}: EN and ES-MX grids must be distinct!"
        en_words = {e["word"] for e in en_puzzle["across"] + en_puzzle["down"]}
        es_words = {e["word"] for e in es_puzzle["across"] + es_puzzle["down"]}
        assert en_words != es_words, f"{slug}: EN and ES-MX word sets must be distinct!"

        compiled[slug] = {
            "slug": slug,
            "title_en": spec["title_en"],
            "title_es": spec["title_es"],
            "en": en_puzzle,
            "es": es_puzzle,
        }
    return compiled


FOLIO_PUZZLES: dict[str, dict[str, Any]] = build_all_folio_puzzles(target_size=10)


if __name__ == "__main__":
    print(f"PASS: Compiled and verified {len(FOLIO_PUZZLES)} bilingual Folio puzzle pairs ({len(FOLIO_PUZZLES) * 2} total 10x10 crosswords: EN + ES-MX).")
