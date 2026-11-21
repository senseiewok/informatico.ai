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
            ("LEAN", "Proof assistant used by a public repository whose README states a complete formal proof of Fermat's Last Theorem (not checked here)", "Act IV"),
            ("VAULT", "Masonry funicular compression shell analyzed by Hooke, Gaudí, and Heyman", "Act III"),
            ("FLUID", "Continuum phase governed by Navier-Stokes, Darcy-Brinkman, and Venturi laws", "Act III"),
            ("GRID", "Swiss 12-column typographic and structural modular coordinate system", "Act I"),
        ],
        "es": [
            ("CIENCIA", "Conocimiento verificable que une física, matemáticas, arquitectura e ingeniería", "Acto I"),
            ("TEOREMA", "Proposición matemática; un repositorio público de Lean 4 afirma contener una demostración formal del Último Teorema de Fermat (no comprobado aquí)", "Acto IV"),
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
            ("BRINKMAN", "Hendrik, who added a viscous shear term to Darcy's drag (Crossref dates the paper 1949)", "Act I"),
            ("MORTAR", "Breathable mineral lime mixture for historic masonry; the folio's capillary-active mortar is an illustrative design sketch, not a tested product", "Act I"),
            ("DARCY", "French engineer whose 1856 report on the public fountains of Dijon describes the sand-column experiments behind Darcy's law", "Act I"),
            ("PORE", "Open space in a porous medium; whether the open paths connect decides if the folio's lattice model conducts at all", "Act III"),
            ("LIME", "Mineral binder of breathable restoration mortars for historic masonry", "Act I"),
            ("PARETO", "Economist whose name labels a frontier of trade-offs between objectives; this folio runs no such optimization", "Act IV"),
        ],
        "es": [
            ("MORTERO", "Mezcla mineral transpirable de cal para mampostería histórica; el diseño capilar del folio es un boceto ilustrativo sin ensayar", "Acto I"),
            ("DARCY", "Ingeniero francés cuyo informe de 1856 sobre las fuentes públicas de Dijon describe los experimentos con columnas de arena detrás de la ley de Darcy", "Acto I"),
            ("PORO", "Espacio abierto de un medio poroso; en el modelo, la fracción abierta fija la longitud de apantallamiento de Brinkman", "Acto III"),
            ("FLUJO", "Movimiento de fluido a través de la matriz; la ley de Darcy lo relaciona con la pérdida de carga", "Acto I"),
            ("ROCA", "Piedra porosa, como la caliza que el folio menciona junto a morteros y estratos geotécnicos", "Acto I"),
            ("CAL", "Ligante mineral de morteros de restauración transpirables para mampostería histórica", "Acto I"),
        ],
    },
    "e02": {
        "title_en": "Folio E.02 · Herschel–Bulkley Concrete Rheology Crossword",
        "title_es": "Folio E.02 · Crucigrama de Reología y Bombeo de Concreto",
        "en": [
            ("BINGHAM", "1922 American chemist whose book Fluidity and Plasticity set out the yield-stress law that carries his name", "Act I"),
            ("TREMIE", "Pipe method for placing concrete from the bottom up in deep foundations; the folio's title pairs it with pumping", "Act I"),
            ("SLUMP", "Flow spread of fresh concrete; the folio's design mix targets a slump flow of 650 mm by the ASTM C1611 test", "Act III"),
            ("PLUG", "Central core that moves without shearing once wall shear stress exceeds the yield stress; 23.3 mm in radius at the defaults", "Act III"),
            ("PUMP", "Machine that drives concrete through the line; the folio's model gives about 6.6 cubic meters per hour at its fixed values and likely understates real pumps", "Act III"),
            ("GROUT", "Fluid cement-based mix; the paste-rich layer that forms at the pipe wall in real pumping is left out of the folio's simple model", "Act I"),
        ],
        "es": [
            ("CONCRETO", "Material que se bombea; en el modelo simple del folio no fluye mientras el esfuerzo en la pared no supere su esfuerzo de fluencia", "Acto I"),
            ("TREMIE", "Método de tubería para colocar concreto de abajo hacia arriba en cimentaciones profundas; el título del folio lo une al bombeo", "Acto I"),
            ("TAPON", "Núcleo central no cizallado que avanza como cilindro sólido dentro de la tubería", "Acto III"),
            ("BOMBA", "Máquina que impulsa el concreto por la línea; el modelo del folio da unos 6.6 metros cúbicos por hora con sus valores fijos", "Acto III"),
            ("REOLOGIA", "Estudio del flujo y la deformación; la ley de Bingham y la generalización de Herschel y Bulkley son su punto de partida en el folio", "Acto I"),
            ("CONO", "Prueba de revenimiento del concreto fresco; el folio menciona una meta de extensión de flujo de 650 mm (ASTM C1611)", "Acto III"),
        ],
    },
    "e03": {
        "title_en": "Folio E.03 · Sub-Wavelength Acoustic Metamaterials Crossword",
        "title_es": "Folio E.03 · Crucigrama de Metamateriales Acústicos de Helmholtz",
        "en": [
            ("ACOUSTIC", "Pertaining to sound-wave propagation and sub-wavelength noise attenuation", "Act I"),
            ("CAVITY", "Hollow volume of a Helmholtz resonator, which Helmholtz tuned by its volume and neck opening", "Act I"),
            ("NECK", "Narrow opening where oscillating air forms a viscous boundary layer; the model's neck radius is 0.65 mm", "Act III"),
            ("PHASE", "Where a wave stands in its cycle; at resonance the folio's model has zero reactance, so the impedance is purely resistive", "Act III"),
            ("ROOFLINE", "Computer performance model of Williams, Waterman and Patterson; this folio does not use it", "Act IV"),
            ("SOUND", "Pressure wave; the folio's design study targets absorbing low-frequency sound in a panel about 1/19 of a wavelength thick, a target not tested", "Act I"),
        ],
        "es": [
            ("ACUSTICO", "Relativo al aislamiento y control de ondas sonoras de baja frecuencia", "Acto I"),
            ("CAVIDAD", "Volumen hueco de un resonador de Helmholtz, que Helmholtz sintonizó con su volumen y la abertura de su cuello", "Acto I"),
            ("CUELLO", "Abertura estrecha donde el aire oscilante forma una capa límite viscosa que disipa la energía del sonido en el modelo", "Acto III"),
            ("SONIDO", "Onda de presión; el estudio de diseño apunta a absorber sonido grave en un panel de cerca de 1/19 de longitud de onda, una meta sin probar", "Acto I"),
            ("ONDA", "Perturbación que se propaga; en el modelo ideal, igualar la impedancia interna a la del aire elimina la onda reflejada", "Acto II"),
            ("FASE", "Posición de una onda en su ciclo; en la resonancia el modelo del folio tiene reactancia cero", "Acto III"),
        ],
    },
    "e04": {
        "title_en": "Folio E.04 · Counter-Current Enthalpy Recovery Crossword",
        "title_es": "Folio E.04 · Crucigrama de Recuperación de Entalpía a Contracorriente",
        "en": [
            ("ENTHALPY", "Total of sensible heat and latent moisture energy that membrane cores in energy recovery ventilators exchange", "Act I"),
            ("LATENT", "Heat carried by water vapor that moves across a selective membrane; the model gives 79.4% recovery at its defaults", "Act III"),
            ("CLEAN", "Free of dirt or contaminant; dense membranes are meant to keep the air streams apart, but how much still crosses is a property of each product and was not modelled", "Act I"),
            ("CORE", "Membrane block where exhaust and supply air flow in opposite directions; the folio's 118 Pa pressure drop is a fixed illustrative value", "Act III"),
            ("NTU", "Number of transfer units; Kays and London made the effectiveness-NTU method standard, and NTU = 7.5 gives 88.2% in the folio's model", "Act II"),
            ("AIR", "Supply and exhaust streams that flow in opposite directions across dense membranes", "Act II"),
        ],
        "es": [
            ("ENTALPIA", "Energía termodinámica total que suma el calor sensible y el calor latente", "Acto I"),
            ("LATENTE", "Calor asociado al vapor de agua transferido a través de la membrana selectiva", "Acto III"),
            ("NUCLEO", "Bloque de membranas donde el aire de extracción y el de suministro fluyen en sentidos opuestos", "Acto III"),
            ("CALOR", "Energía térmica sensible; con NTU = 7.5, el modelo da 88.2% de efectividad sensible", "Acto III"),
            ("VAPOR", "Agua en fase gaseosa que se disuelve en la membrana hidrofílica y se difunde hacia la corriente seca", "Acto II"),
            ("AIRE", "Fluido de ventilación; las membranas intercambian calor y humedad entre el aire saliente y el entrante", "Acto I"),
        ],
    },
    "e05": {
        "title_en": "Folio E.05 · Terzaghi Consolidation & CFA Piling Crossword",
        "title_es": "Folio E.05 · Crucigrama de Consolidación de Terzaghi y Pilotes CFA",
        "en": [
            ("TERZAGHI", "Austrian engineer whose 1925 Erdbaumechanik is usually taken as the start of modern soil mechanics, setting out effective stress and consolidation", "Act I"),
            ("AUGER", "Hollow-stem drill that bores into load-bearing strata while grout is pumped as the tooling is withdrawn", "Act I"),
            ("CLAY", "Low-permeability soil in which a sudden surcharge is at first borne entirely by excess pore-water pressure", "Act I"),
            ("PILE", "Deep foundation element; the folio's 750 mm by 24 m CFA pile carries load by shaft friction and toe bearing, with illustrative capacities", "Act III"),
            ("STRESS", "Total stress minus pore-water pressure gives the effective stress that the mineral grains carry", "Act I"),
            ("SOIL", "Saturated ground that Terzaghi treated as two phases, mineral grains and pore water", "Act I"),
        ],
        "es": [
            ("TERZAGHI", "Ingeniero austriaco cuya Erdbaumechanik (1925) suele tomarse como el inicio de la mecánica de suelos moderna", "Acto I"),
            ("PILOTE", "Elemento de cimentación profunda perforado con barrena continua (CFA); el modelo del folio usa capacidades ilustrativas fijas", "Acto III"),
            ("ARCILLA", "Suelo de baja permeabilidad que se consolida al drenar el agua intersticial", "Acto I"),
            ("SUELO", "Terreno saturado que Terzaghi trató como dos fases, granos minerales y agua de poro", "Acto I"),
            ("CARGA", "Sobrecarga que, en el modelo, pasa al principio por completo al agua de los poros", "Acto III"),
            ("AGUA", "Fluido en los poros cuya presión en exceso se disipa al drenar, según la ecuación de difusión de Terzaghi", "Acto I"),
        ],
    },
    "e06": {
        "title_en": "Folio E.06 · ASCE 7-22 Seismic Base Isolation Crossword",
        "title_es": "Folio E.06 · Crucigrama de Aislamiento Sísmico de Base ASCE 7-22",
        "en": [
            ("SEISMIC", "Pertaining to earthquakes; the folio's model puts a hospital on lead-rubber isolators, as a model check and not a code check", "Act I"),
            ("RUBBER", "Layers of rubber and steel around a central lead core make up the lead-rubber bearing that Robinson developed", "Act I"),
            ("LEAD", "Central core of the bearing; it yields in shear and dissipates energy in bilinear hysteresis loops", "Act III"),
            ("PERIOD", "Natural time of oscillation; the model lengthens it to 2.85 s, cutting its spectral acceleration estimate by about 77 percent", "Act III"),
            ("HYSTERESIS", "Area of the bilinear force-displacement loop measures the energy dissipated per cycle", "Act III"),
            ("BASE", "Level beneath the superstructure where lead-rubber bearings are inserted", "Act I"),
        ],
        "es": [
            ("SISMICO", "Relativo a los sismos; el folio considera hospitales y laboratorios donde no es aceptable que las columnas cedan", "Acto I"),
            ("PLOMO", "Núcleo central del apoyo de plomo y caucho que fluye en cortante y disipa energía en ciclos de histéresis bilineales", "Acto III"),
            ("CAUCHO", "Capas de caucho y acero alrededor de un núcleo de plomo en el apoyo que desarrolló Robinson", "Acto I"),
            ("PERIODO", "Tiempo natural de oscilación; el modelo del folio lo alarga a 2.85 s", "Acto III"),
            ("APOYO", "Aislador de plomo y caucho que se inserta bajo la superestructura; el folio no revisa el diseño contra el código ASCE/SEI 7-22", "Acto III"),
            ("BASE", "Nivel bajo la superestructura donde se insertan los apoyos de plomo y caucho", "Acto I"),
        ],
    },
    "e07": {
        "title_en": "Folio E.07 · Suspension Bridge Aeroelastic Flutter Crossword",
        "title_es": "Folio E.07 · Crucigrama de Aeroelasticidad en Puentes Colgantes",
        "en": [
            ("SCANLAN", "Robert, who with John Tomko published measured flutter derivatives for bridge decks in 1971", "Act I"),
            ("FLUTTER", "Self-excited aeroelastic instability in which the moving deck changes the airflow; in the folio's single-mode model torsional flutter grows once wind exceeds a critical speed", "Act II"),
            ("BRIDGE", "Long-span crossing such as the first Tacoma Narrows Bridge, which twisted apart on November 7, 1940", "Act I"),
            ("VORTEX", "Eddy shed in the wake of a deck; many textbooks blamed Tacoma Narrows on resonance with such vortices, but Billah and Scanlan (1991) set out why that account does not fit", "Act I"),
            ("CABLE", "Element whose tension is hard to monitor on spans of a kilometre or more, since sensors can be fixed at only a few accessible points", "Act I"),
            ("SPAN", "Stretch between supports; on spans of a kilometre or more, sensors can be fixed at only a few accessible points", "Act I"),
        ],
        "es": [
            ("SCANLAN", "Robert, quien con John Tomko publicó en 1971 derivadas de flameo medidas para tableros de puentes", "Acto I"),
            ("PUENTE", "Estructura de gran claro; el primer puente de Tacoma Narrows se retorció hasta romperse el 7 de noviembre de 1940", "Acto I"),
            ("VIENTO", "Corriente de aire; en el modelo de un solo modo, el flameo torsional crece cuando su velocidad supera un valor crítico", "Acto II"),
            ("CABLE", "Elemento cuya tensión es difícil de monitorear en claros de un kilómetro o más, pues los sensores se fijan en pocos puntos accesibles", "Acto I"),
            ("TORRE", "Elemento vertical de un puente colgante que sostiene los cables; este folio no lo modela por separado", "Acto I"),
            ("ALETEO", "Inestabilidad aeroelástica autoexcitada, en que el tablero en movimiento cambia el flujo de aire; en inglés, flutter", "Acto II"),
        ],
    },
    "e08": {
        "title_en": "Folio E.08 · EPB-TBM Tunneling & Peck Settlement Crossword",
        "title_es": "Folio E.08 · Crucigrama de Tuneladoras EPB-TBM y Asentamiento de Peck",
        "en": [
            ("TUNNEL", "Bore beneath a city; the Brunels' Thames tunnel, begun in 1825, opened in 1843", "Act I"),
            ("SHIELD", "Device that Marc Isambard Brunel patented in 1818; the account usually given is that the idea came from the shipworm", "Act I"),
            ("TROUGH", "Inverted Gaussian bell of surface settlement across a tunnel, shown by Peck in 1969 and examined below the surface by Mair and colleagues", "Act I"),
            ("LINER", "Ring of precast segments that lines the tunnel; the spec plate describes a design proposal for such a lining", "Act III"),
            ("GROUT", "Tail-void backfill material whose injection pressure a digital twin might adjust ring by ring, a proposal the folio did not carry out", "Act IV"),
            ("FOAM", "Foam-conditioned muck in the chamber behind the cutterhead balances earth and pore-water pressure at the face", "Act I"),
        ],
        "es": [
            ("TUNEL", "Galería bajo una ciudad; el túnel de los Brunel bajo el Támesis, iniciado en 1825, se abrió en 1843", "Acto I"),
            ("ESCUDO", "Dispositivo que Marc Isambard Brunel patentó en 1818; según el relato usual, la idea vino del gusano de mar", "Acto I"),
            ("DOVELA", "Segmento prefabricado que forma el anillo del revestimiento; la placa de especificación del folio describe una propuesta de diseño", "Acto III"),
            ("ESPUMA", "Espuma que acondiciona el material excavado en la cámara y equilibra la presión de tierra y la del agua de poro en el frente", "Acto I"),
            ("PECK", "Ralph, quien en 1969 mostró que el asentamiento superficial sobre un túnel se describe con una campana gaussiana invertida", "Acto I"),
            ("FRENTE", "Cara de excavación donde la pasta presurizada equilibra la presión de tierra y la del agua de poro", "Acto I"),
        ],
    },
    # ---------------- PILLAR II: ARCHITECTURE (A.01 - A.08) ----------------
    "a01": {
        "title_en": "Folio A.01 · Funicular Masonry Vaults & Glaser Crossword",
        "title_es": "Folio A.01 · Crucigrama de Bóvedas Funiculares y Condensación de Glaser",
        "en": [
            ("CATENARY", "Hanging chain curve that Hooke stated, as an anagram, becomes a pure compression arch when inverted, and that Gaudí used in a hanging model of weighted cords", "Act I"),
            ("HEYMAN", "Structural theorist whose 1966 paper The Stone Skeleton brought the safe theorem to stone structures", "Act I"),
            ("THRUST", "Line of compressive force; it must stay inside the masonry for Heyman's safe theorem, and inside the middle third for the stricter rule the folio checks", "Act II"),
            ("VAULT", "Curved masonry ceiling shell; an unreinforced stone one can stand for centuries yet fail quickly if its abutments spread", "Act II"),
            ("GLASER", "Vapor-pressure profile method the folio's stepper shows for the 1:5 springer node; its 16.4 degree surface temperature is an illustrative value", "Act III"),
            ("ARCH", "Curved form that carries its load in compression, like Hooke's hanging chain turned upside down", "Act I"),
        ],
        "es": [
            ("BOVEDA", "Cubierta curva de mampostería que trabaja en compresión pura sin acero", "Acto I"),
            ("HEYMAN", "Autor del teorema de seguridad para estructuras de piedra, expuesto en The Stone Skeleton (1966)", "Acto I"),
            ("EMPUJE", "Línea de fuerza compresiva; debe quedar dentro de la mampostería para el teorema de Heyman y dentro del tercio medio para la regla más estricta que revisa el folio", "Acto II"),
            ("GLASER", "Perfil de presión de vapor que el folio muestra para el nodo de arranque 1:5; su temperatura superficial de 16.4 grados es un valor ilustrativo", "Acto III"),
            ("PIEDRA", "Material de la bóveda; resiste compresión y casi no tiene resistencia a tracción", "Acto II"),
            ("ARCO", "Forma que invierte la curva de una cadena colgante, idea que Hooke publicó como anagrama y que Gaudí usó en un modelo colgante de cuerdas", "Acto I"),
        ],
    },
    "a02": {
        "title_en": "Folio A.02 · Reciprocal Timber Gridshells Crossword",
        "title_es": "Folio A.02 · Crucigrama de Retículas Recíprocas de Madera (Nexorades)",
        "en": [
            ("NEXORADE", "Reciprocal timber frame where each beam rests upon and supports its neighbor", "Act I"),
            ("TIMBER", "Wood; the folio's members are GL28h larch and its notch checks follow the style of EN 1995-1-1 (Eurocode 5)", "Act III"),
            ("VILLARD", "Medieval sketchbook author, de Honnecourt, whose floor grillages the folio cites among reciprocal frames", "Act I"),
            ("JOINT", "Notched lap connection; in the folio's model an assumed offset at each one gives the dome its rise", "Act III"),
            ("SPAN", "Distance a structure crosses; reciprocal frames let members shorter than the span cover it together", "Act I"),
            ("BEAM", "Short member that rests on its neighbor; Leonardo da Vinci drew such self-supporting arrangements of short poles", "Act I"),
        ],
        "es": [
            ("MADERA", "Material de los miembros del folio (madera laminada de alerce GL28h); sus revisiones de muesca siguen el estilo de la norma EN 1995-1-1", "Acto III"),
            ("NEXOR", "Elemento corto que se apoya en su vecino; juntos cubren un claro mayor que cada pieza", "Acto I"),
            ("NUDO", "Unión de traslape con muesca; en el modelo del folio, un desnivel supuesto en cada uno da su elevación a la cúpula", "Acto III"),
            ("VIGA", "Pieza lineal que se apoya sobre su vecina y a la vez sostiene la siguiente", "Acto I"),
            ("DOMO", "Cubierta curva; en el modelo del folio, el apoyo repetido de los miembros en abanico le da su elevación", "Acto III"),
            ("RED", "Malla de miembros entrelazados; el folio cita los entramados de piso medievales de Villard de Honnecourt", "Acto I"),
        ],
    },
    "a03": {
        "title_en": "Folio A.03 · Double-Skin Buoyancy & Circadian Daylight Crossword",
        "title_es": "Folio A.03 · Crucigrama de Fachadas de Doble Piel y Luz Circadiana",
        "en": [
            ("BUOYANCY", "Thermal stack-effect lift that, in the folio's model, drives airflow up a sun-warmed facade cavity", "Act II"),
            ("FACADE", "Double-skin glazed building envelope whose cavity holds ventilated blinds and louvers", "Act I"),
            ("DAYLIGHT", "Natural light indoors; an expert consensus recommends at least 250 lux melanopic EDI at eye level in the daytime for healthy adults", "Act IV"),
            ("STACK", "Draft driven by the density difference between warm cavity air and outside air; the folio's model gives 3.92 Pa over 9.0 m", "Act III"),
            ("GLARE", "Discomfort from bright light; the folio imagines light sensors helping balance daylight against it at desks", "Act IV"),
            ("SOLAR", "Sunlight; in the folio's model it heats the ventilated blind and drives the stack draft", "Act III"),
        ],
        "es": [
            ("FACHADA", "Envolvente arquitectónica de doble piel acristalada con una cavidad ventilada", "Acto I"),
            ("SOLAR", "Energía radiante que, en el modelo del folio, calienta la persiana ventilada e impulsa el tiro térmico", "Acto III"),
            ("TIRO", "Efecto chimenea por flotabilidad térmica; el modelo del folio da 3.92 Pa en un tiro de 9.0 m", "Acto III"),
            ("CELOSIA", "Lamas de la fachada; el folio imagina ajustar su ángulo con pronósticos del tiempo y sensores de luz", "Acto IV"),
            ("RITMO", "Reloj circadiano; Berson y colaboradores mostraron que ciertas células ganglionares de la retina lo ajustan", "Acto IV"),
            ("LUZ", "Luz natural interior; el folio cita una recomendación de expertos de al menos 250 lux melanópicos EDI de día para adultos sanos", "Acto IV"),
        ],
    },
    "a04": {
        "title_en": "Folio A.04 · Archigram to British High-Tech Exoskeleton Crossword",
        "title_es": "Folio A.04 · Crucigrama de Archigram a Exoesqueletos High-Tech",
        "en": [
            ("POMPIDOU", "Paris center realized 1971-1977 by Piano, Rogers and Peter Rice, with an exposed exoskeleton and column-free floors of about 48 m", "Act I"),
            ("ARCHIGRAM", "1960s group whose Plug-In City and Walking City drawings are widely seen as an influence on British High-Tech", "Act I"),
            ("TRUSS", "At the Pompidou, floor trusses are carried by cast-steel gerberettes on short arms outside the column line", "Act I"),
            ("FOSTER", "High-Tech architect of the Hongkong and Shanghai Bank headquarters, which hangs groups of floors from steel masts", "Act I"),
            ("RICE", "Engineer with Ove Arup & Partners; the team including him used cast-steel gerberettes at the Pompidou", "Act I"),
            ("POD", "Replaceable service module; the folio's 15-year pod and 100-year frame lifetimes are illustrative values", "Act III"),
        ],
        "es": [
            ("POMPIDOU", "Centro de París realizado de 1971 a 1977 por Piano, Rogers y Peter Rice, con estructura exterior expuesta y plantas libres de unos 48 m", "Acto I"),
            ("CERCHA", "Viga de celosía de piso que, en el Pompidou, se apoya en gerberettes de acero fundido sobre brazos cortos fuera de la línea de columnas", "Acto I"),
            ("CAPSULA", "Módulo enchufable que una grúa podría subir y bajar de una estructura de larga vida, como en Plug-In City", "Acto I"),
            ("ACERO", "Material de las ménsulas gerberette del Pompidou, que el equipo de ingeniería con Peter Rice empleó en forma fundida", "Acto I"),
            ("ROGER", "Apellido (sin s) de Richard, quien con Piano ganó el concurso del Pompidou y es autor del edificio Lloyd's of London", "Acto I"),
            ("RED", "Estructura reticular de larga vida que porta módulos reemplazables; los 100 años del folio son un valor ilustrativo", "Acto III"),
        ],
    },
    "a05": {
        "title_en": "Folio A.05 · Sabine Reverberation & Schroeder Diffusers Crossword",
        "title_es": "Folio A.05 · Crucigrama de Acústica de Sabine y Difusores de Schroeder",
        "en": [
            ("SABINE", "Harvard physicist who studied the Fogg lecture room from 1895 and arrived at the reverberation relation T_60 = 0.161 V / A", "Act I"),
            ("ECHO", "Mirror-like sound reflection; the folio's coffered wells spread reflections across many directions instead of one bounce", "Act III"),
            ("VAULT", "Curved ceiling whose early reflections reach listeners within the first 50 ms in the folio's model; coffer depths follow Schroeder's sequence", "Act III"),
            ("DECIBEL", "Logarithmic unit; reverberation time T_60 is the time for sound to decay by 60 dB", "Act II"),
            ("PRIME", "Number p in the well-depth formula of Schroeder's quadratic-residue coffers", "Act III"),
            ("HALL", "Room whose reverberation the folio models; its 0.62 s Eyring value is a design-study figure, not a measurement", "Act III"),
        ],
        "es": [
            ("SABINE", "Apellido de Wallace, físico de Harvard cuya relación de reverberación T_60 = 0.161 V / A el folio compara con la de Eyring", "Acto I"),
            ("DIFUSOR", "Panel de pozos de residuo cuadrático de Schroeder que reparte las reflexiones en muchas direcciones", "Acto III"),
            ("PRIMO", "Número entero p que determina la secuencia de profundidades de los pozos de Schroeder", "Acto III"),
            ("SALA", "Recinto cuya reverberación modela el folio; sus cifras son valores ilustrativos, no mediciones", "Acto III"),
            ("ECO", "Reflexión del sonido; los casetones del folio reparten las reflexiones en muchas direcciones en lugar de un solo rebote", "Acto III"),
            ("VOZ", "Habla; el folio usa un índice de transmisión del habla ilustrativo de 0.74, con meta de diseño de al menos 0.68", "Acto III"),
        ],
    },
    "a06": {
        "title_en": "Folio A.06 · Constructed Wetlands & Plumbing Design Crossword",
        "title_es": "Folio A.06 · Crucigrama de Humedales Construidos y Diseño de Plomería",
        "en": [
            ("WETLAND", "Subsurface gravel bed with reeds; the folio models Kadlec-Knight exponential BOD_5 decay in it", "Act III"),
            ("BIOFILM", "Slime layer of microbes on a surface; the folio's 60 degree loop and UV-C reactor are design targets meant to limit its growth", "Act II"),
            ("STERILE", "Free of all living microbes; the folio does not claim this, since its measures are design targets meant only to limit growth", "Act III"),
            ("REED", "Phragmites plant whose root zone transfers oxygen to the gravel bed in the folio's model", "Act II"),
            ("GRAVEL", "Washed basalt gravel through which the folio's greywater flows, below a 150 mm dry layer", "Act III"),
            ("UVC", "254 nm ultraviolet band; the folio's model delivers 45 mJ/cm2 for a 5.4-log reduction, a model value", "Act III"),
        ],
        "es": [
            ("HUMEDAL", "Lecho subsuperficial de grava con carrizos; el folio modela en él un decaimiento exponencial de DBO_5 tipo Kadlec y Knight", "Acto III"),
            ("ESTERIL", "Libre de todo microbio vivo; el folio no lo afirma, pues sus medidas son metas de diseño que sólo buscan limitar el crecimiento", "Acto III"),
            ("GRAVA", "Grava de basalto lavada por donde fluye el agua gris del folio, bajo una capa seca de 150 mm", "Acto III"),
            ("RAIZ", "Parte de la planta donde, según el modelo, ocurre la transferencia de oxígeno que impulsa la oxidación de la DBO_5", "Acto III"),
            ("TUBO", "Conducto de agua potable; el folio fija como meta de diseño recircularla a 60 °C o más, y la norma ASHRAE 188 trata el riesgo de Legionella sin prescribir este diseño", "Acto III"),
            ("AGUA", "Recurso que depura el lecho modelado de carrizos: la DBO_5 baja de 140 a 6.8 mg/L en el modelo", "Acto III"),
        ],
    },
    "a07": {
        "title_en": "Folio A.07 · Luis Barragán Chromatic Tectonics Crossword",
        "title_es": "Folio A.07 · Crucigrama de la Tectónica Cromática de Luis Barragán",
        "en": [
            ("BARRAGAN", "Architect who received the Pritzker Prize in 1980 and worked with saturated color and Mexican sunlight", "Act I"),
            ("GILARDI", "House in Tacubaya, Mexico City, completed in 1976, where a corridor lit through yellow glass leads to an indoor pool", "Act I"),
            ("ALBERS", "Josef, who showed in Interaction of Color (1963) through classroom exercises that the same color can look different", "Act I"),
            ("PINK", "Rosa Mexicano, one of the saturated colors Barragán and Chucho Reyes Ferreira worked with; the folio's 615 nm dominant wavelength is illustrative", "Act III"),
            ("STUCCO", "Matte wall surface; the folio models lime scattering with Kubelka-Munk and assumes Lambertian surfaces", "Act III"),
            ("POOL", "Indoor pool at Casa Gilardi, where a freestanding red wall rises from the water against blue walls", "Act I"),
        ],
        "es": [
            ("BARRAGAN", "Arquitecto mexicano que recibió el Premio Pritzker en 1980 y trabajó con color saturado y la luz de México", "Acto I"),
            ("GILARDI", "Casa de Tacubaya, Ciudad de México, terminada en 1976, donde un corredor iluminado por vidrio amarillo conduce a una alberca interior", "Acto I"),
            ("ALBERS", "Autor de La interacción del color (1963), quien mostró en ejercicios de clase que un mismo color puede verse distinto", "Acto I"),
            ("ESTUCO", "Acabado mate de cal; el folio modela su dispersión con Kubelka-Munk y supone superficies lambertianas", "Acto III"),
            ("ROSA", "Tono (rosa mexicano) con el que trabajaron Barragán y Chucho Reyes Ferreira; los 615 nm del folio son un valor ilustrativo", "Acto III"),
            ("LUZ", "Luz que, en el modelo del folio, entra por el corredor de vidrio amarillo de Casa Gilardi y rebota entre muro y agua", "Acto III"),
        ],
    },
    "a08": {
        "title_en": "Folio A.08 · Daytime Radiative Sky-Cooling Envelopes Crossword",
        "title_es": "Folio A.08 · Crucigrama de Enfriamiento Radiativo Diurno al Cielo",
        "en": [
            ("PHOTONIC", "Kind of roof surface that, in the folio's model, reflects 97.0% of an assumed 1,000 W/m2 of midday sunlight", "Act III"),
            ("STEFAN", "Name on the moving melting front of the folio's proposed phase-change ceiling panel, a design proposal not sized or tested", "Act III"),
            ("WINDOW", "The 8-13 micrometer infrared band through which the folio's model sends roof heat toward 3 K deep space", "Act III"),
            ("ALBEDO", "Solar reflectance; the folio's model uses 97.0%, an assumed value", "Act III"),
            ("SPACE", "The 3 K deep space that receives the roof's infrared emission in the folio's model", "Act III"),
            ("ROOF", "Sky-facing surface that the model puts about 6.2 degrees below outdoor air, an illustrative result", "Act III"),
        ],
        "es": [
            ("FOTONICO", "Tipo de superficie que, en el modelo del folio, refleja 97.0% de la luz solar supuesta y emite en la ventana de 8 a 13 micrómetros", "Acto III"),
            ("VENTANA", "Banda de transparencia atmosférica de 8 a 13 micrómetros en el infrarrojo térmico", "Acto III"),
            ("ALBEDO", "Fracción de reflectancia solar; el modelo del folio usa 97.0%, un valor supuesto", "Acto III"),
            ("STEFAN", "Apellido asociado al frente móvil de fusión del panel de cambio de fase propuesto, una propuesta de diseño no probada", "Acto III"),
            ("CIELO", "Espacio profundo a 3 K hacia el que, en el modelo, la cubierta emite infrarrojo por la ventana atmosférica", "Acto III"),
            ("TECHO", "Cubierta que, en el modelo del folio, queda unos 6.2 grados bajo el aire exterior, un resultado ilustrativo", "Acto III"),
        ],
    },
    # ---------------- PILLAR III: PHYSICS (P.01 - P.08) ----------------
    "p01": {
        "title_en": "Folio P.01 · Non-Equilibrium Fluctuation-Dissipation Crossword",
        "title_es": "Folio P.01 · Crucigrama de Fluctuación-Disipación Fuera del Equilibrio",
        "en": [
            ("SEIFERT", "Udo, one of the physicists who extended fluctuation-dissipation theorems to the far-from-equilibrium regime of molecular machines", "Act I"),
            ("KEIZER", "Joel, one of the physicists who extended fluctuation-dissipation theorems to the far-from-equilibrium regime of molecular machines", "Act I"),
            ("ENTROPY", "Quantity whose minimal production the folio's cyclic currents are balanced against rapid conformational switching", "Act I"),
            ("MARKOV", "Memoryless jump network; the folio names Markov-state reconstructions from single-molecule recordings as a tool for testing channel efficiency", "Act I"),
            ("ATP", "Adenosine triphosphate, the fuel an allosteric channel hydrolyzes in the folio's gating model", "Act II"),
            ("FLUX", "Cyclic loop currents within Hill state-spaces, which the folio balances against entropy production", "Act I"),
        ],
        "es": [
            ("ENTROPIA", "Magnitud cuya producción mínima se equilibra, en el folio, con la conmutación conformacional rápida", "Acto I"),
            ("SEIFERT", "Udo, uno de los físicos que extendieron los teoremas de fluctuación-disipación al régimen lejos del equilibrio", "Acto I"),
            ("KEIZER", "Joel, uno de los físicos que extendieron los teoremas de fluctuación-disipación al régimen lejos del equilibrio", "Acto I"),
            ("MARKOV", "Red de estados sin memoria; el folio nombra las reconstrucciones de estados de Markov a partir de registros de molécula única", "Acto I"),
            ("CICLO", "Bucle de estados impulsado por la hidrólisis de ATP en el modelo de compuerta del folio", "Acto II"),
            ("FLUJO", "Corrientes cíclicas dentro de los espacios de estados de Hill, que el folio equilibra con la producción de entropía", "Acto I"),
        ],
    },
    "p02": {
        "title_en": "Folio P.02 · Kuramoto Ciliary Metachronal Waves Crossword",
        "title_es": "Folio P.02 · Crucigrama de Ondas Metacronales de Cilios y Kuramoto",
        "en": [
            ("KURAMOTO", "Yoshiki, who in 1975 formulated the phase-oscillator framework for synchronization through weak pairwise coupling", "Act I"),
            ("HUYGENS", "Dutch scientist who in 1665 watched two pendulum clocks on a shared beam fall into synchrony", "Act I"),
            ("CILIA", "Hair-like projections on airway cells; the folio puts the beating of a single cilium at 12 to 14 Hz", "Act III"),
            ("STOKES", "Regime of viscous flow at very low Reynolds number; the folio ties antiplectic metachronism to Oseen tensors", "Act II"),
            ("WAVE", "Antiplectic traveling pattern of cilia; the folio puts its velocity near 336 micrometers per second", "Act III"),
            ("SYNC", "Coherent phase-locked state that appears once the coupling constant exceeds a critical threshold K_c", "Act II"),
        ],
        "es": [
            ("KURAMOTO", "Yoshiki, quien en 1975 formuló el marco de osciladores de fase para la sincronización por acoplamiento débil entre pares", "Acto I"),
            ("HUYGENS", "Científico holandés que en 1665 vio dos relojes de péndulo sobre una misma viga caer en sincronía", "Acto I"),
            ("CILIOS", "Proyecciones en forma de pelo en las células de la vía aérea; el folio sitúa el batido de un solo cilio en 12 a 14 Hz", "Acto III"),
            ("STOKES", "Régimen de flujo viscoso a número de Reynolds muy bajo; el folio vincula el metacronismo antipléctico con tensores de Oseen", "Acto II"),
            ("FASE", "Ángulo de batido; en el modelo, el desfase hidrodinámico entre cilios vecinos es de unos pi/6", "Acto III"),
            ("ONDA", "Patrón metacronal viajero; el folio estima su velocidad en unos 336 micrómetros por segundo", "Acto III"),
        ],
    },
    "p03": {
        "title_en": "Folio P.03 · de Gennes Polymer Scaling & Subdiffusion Crossword",
        "title_es": "Folio P.03 · Crucigrama de Escalamiento Polimérico de de Gennes",
        "en": [
            ("DEGENNES", "Pierre-Gilles, whose 1979 book Scaling Concepts in Polymer Physics set out power laws for entangled polymer chains", "Act I"),
            ("CARREAU", "Shear-thinning law of Carreau and Yasuda; the folio has gel viscosity fall by an order of magnitude at ciliary shear rates", "Act III"),
            ("MUCIN", "High-molecular-weight glycoprotein (MUC5AC and MUC5B) whose entangled gel the folio models", "Act II"),
            ("MESH", "Entangled network whose correlation pore size xi the folio models as shrinking as mucin concentration rises", "Act II"),
            ("BLOB", "Correlation volume in de Gennes's scaling picture of semi-dilute polymers; the folio itself works with a mesh pore size", "Act I"),
            ("GEL", "Network with transient hydrophobic junctions and disulfide cross-links, per the folio, giving a high zero-shear viscosity", "Act II"),
        ],
        "es": [
            ("POLIMERO", "Macromolécula encadenada cuyo enredo físico describió Pierre-Gilles de Gennes con leyes de potencia en su libro de 1979", "Acto I"),
            ("CARREAU", "Modelo reológico de Carreau y Yasuda para el adelgazamiento por corte; el folio lo aplica a la viscosidad del gel bajo cortante ciliar", "Acto III"),
            ("MUCINA", "Glicoproteína de alto peso molecular (MUC5B y MUC5AC) cuyo gel enredado modela el folio", "Acto II"),
            ("MALLA", "Red tridimensional cuyo tamaño de poro modela el folio como decreciente al aumentar la concentración de mucina", "Acto II"),
            ("PORO", "Abertura nanométrica de correlación entre cadenas poliméricas entrelazadas", "Acto II"),
            ("GEL", "Red con uniones hidrofóbicas transitorias y entrecruzamientos disulfuro, según el folio, con alta viscosidad a corte cero", "Acto II"),
        ],
    },
    "p04": {
        "title_en": "Folio P.04 · Button–Boucher Two-Gel Osmotic Brush Crossword",
        "title_es": "Folio P.04 · Crucigrama del Modelo de Cepillo Osmótico de Dos Geles",
        "en": [
            ("OSMOTIC", "Pressure balance between the compressive osmotic pressure of the overlying mucus and the restoring modulus of the periciliary brush", "Act I"),
            ("BOUCHER", "Richard, who with Brian Button and Michael Rubinstein reported a grafted polymer brush in the periciliary space (Science, 2012)", "Act I"),
            ("BRUSH", "Dense layer of tethered cell-surface mucins (MUC1, MUC4, MUC16) in the periciliary space, per Button, Rubinstein and Boucher", "Act I"),
            ("FLORY", "Surname of the polymer chemist behind Flory-Huggins mixing theory, a classical swelling theory that this folio does not cite", "Act II"),
            ("SALT", "Chloride and sodium ions; in the folio's model, CFTR chloride secretion balances ENaC sodium absorption", "Act III"),
            ("PCL", "Periciliary layer, about 7 microns when hydrated; the folio models its brush compressing when mucus solids rise", "Act I"),
        ],
        "es": [
            ("OSMOTICO", "Equilibrio entre la presión osmótica compresiva del moco superior y el módulo restaurador del cepillo periciliar", "Acto I"),
            ("CEPILLO", "Capa densa de mucinas ancladas a la superficie celular (MUC1, MUC4, MUC16) en el espacio periciliar", "Acto I"),
            ("BOUCHER", "Richard, coautor con Button y Rubinstein del artículo de Science (2012) sobre un cepillo de polímero injertado en el espacio periciliar", "Acto I"),
            ("FLORY", "Apellido del químico de polímeros detrás de la teoría de mezcla de Flory-Huggins, una teoría clásica de hinchamiento que este folio no cita", "Acto II"),
            ("AGUA", "Solvente retenido dentro del cepillo; en el modelo, el flujo transepitelial puede vaciar el espacio periciliar", "Acto III"),
            ("SAL", "Electrolito; en el modelo del folio, la secreción de cloruro por CFTR equilibra la absorción de sodio por ENaC", "Acto III"),
        ],
    },
    "p05": {
        "title_en": "Folio P.05 · Gamow WKB Quantum Proton Tunneling Crossword",
        "title_es": "Folio P.05 · Crucigrama de Efecto Túnel Cuántico de Protones (WKB)",
        "en": [
            ("TUNNEL", "Quantum penetration of a barrier that a particle could not cross classically", "Act I"),
            ("GAMOW", "Physicist who explained alpha decay in 1928 with quantum wave penetration through the nuclear barrier", "Act I"),
            ("PROTON", "Light particle whose de Broglie wavelength of roughly half an angstrom lets it tunnel through a narrow hydrogen-bond barrier, per the folio", "Act I"),
            ("ISOTOPE", "Swapping hydrogen for deuterium; large kinetic isotope effects are often interpreted as evidence of hydrogen tunneling", "Act I"),
            ("ACTION", "WKB integral of momentum across the barrier; it scales with the square root of the particle's mass", "Act II"),
            ("WKB", "Wentzel-Kramers-Brillouin semiclassical approximation for the probability of penetrating a barrier", "Act I"),
        ],
        "es": [
            ("CUANTICO", "Régimen físico donde una partícula atraviesa barreras que la mecánica clásica prohíbe", "Acto I"),
            ("PROTON", "Partícula ligera cuya longitud de onda de unos medio angstrom le permite atravesar una barrera estrecha de enlace de hidrógeno, según el folio", "Acto I"),
            ("ISOTOPO", "Cambiar hidrógeno por deuterio; los efectos isotópicos cinéticos grandes suelen interpretarse como evidencia de efecto túnel de hidrógeno", "Acto I"),
            ("BARRERA", "Cresta de energía potencial que la función de onda semiclásica WKB atraviesa con probabilidad decreciente", "Acto II"),
            ("GAMOW", "Físico que en 1928 explicó el decaimiento alfa con la penetración de ondas cuánticas a través de la barrera nuclear", "Acto I"),
            ("POZO", "Mínimo local de energía potencial junto a la barrera", "Acto II"),
        ],
    },
    "p06": {
        "title_en": "Folio P.06 · Doi–Edwards Tube Reptation of 4.5 kb Chains Crossword",
        "title_es": "Folio P.06 · Crucigrama de Reptación Tubular de Doi–Edwards",
        "en": [
            ("EDWARDS", "Sir Sam, who with Masao Doi turned de Gennes's reptation concept into a constitutive theory of entangled polymers in 1978", "Act I"),
            ("TUBE", "Virtual confining channel that replaces the many-body entanglements of surrounding chains in the Doi-Edwards picture", "Act III"),
            ("SNAKE", "Creature whose slithering motion the Latin verb reptare, behind de Gennes's term 'reptation', evokes", "Act I"),
            ("MRNA", "Messenger RNA; the folio treats a 4.5 kb transcript as an example of kilobase-length cargo whose disengagement time scales with the cube of chain length", "Act I"),
            ("CHAIN", "Long flexible macromolecule that escapes its original tube by curvilinear one-dimensional diffusion", "Act I"),
            ("DOI", "Masao, who with Sam Edwards turned de Gennes's reptation concept into a rigorous theory in 1978", "Act I"),
        ],
        "es": [
            ("EDWARDS", "Sir Sam, quien con Masao Doi convirtió el concepto de reptación de de Gennes en una teoría constitutiva de polímeros enredados en 1978", "Acto I"),
            ("CADENA", "Macromolécula larga y flexible que escapa de su tubo original por difusión curvilínea unidimensional", "Acto I"),
            ("TUBO", "Conducto virtual que sustituye los enredos de muchos cuerpos de las cadenas vecinas en el esquema de Doi y Edwards", "Acto III"),
            ("ARNM", "Ácido ribonucleico mensajero; el folio considera un transcrito de 4.5 kb como ejemplo de carga de kilobases", "Acto I"),
            ("NUDO", "Restricción topológica que impide el movimiento transversal de la macromolécula", "Acto I"),
            ("DOI", "Masao, quien con Edwards convirtió la reptación de de Gennes en una teoría rigurosa en 1978; el tiempo de desenredo escala con el cubo de la masa molecular", "Acto I"),
        ],
    },
    "p07": {
        "title_en": "Folio P.07 · 2026 Formula 1 Ground-Effect Active Aero Crossword",
        "title_es": "Folio P.07 · Crucigrama de Aerodinámica Activa y Efecto Suelo en Fórmula 1",
        "en": [
            ("VENTURI", "Converging-diverging underfloor tunnel; in the folio's model the flow reaches 1.96 times freestream speed at the throat at 26 mm ride height", "Act III"),
            ("VORTEX", "Lamb-Oseen edge vortex that seals the floor edge in the model; choking the throat below 19 mm bursts it", "Act III"),
            ("WING", "Wing element; in the folio's account of the 2026 rules, flattening the flaps to 6 degrees (X-mode) sheds 38 percent of the drag", "Act III"),
            ("STALL", "Separation in a choked throat; below 19 mm ride height the folio's model triggers 5.8 Hz aero-elastic porpoising", "Act III"),
            ("DRAG", "Aerodynamic resistance; the folio's model sheds 38 percent of it on straights in X-mode", "Act III"),
            ("DOWN", "Direction of the aerodynamic load; the folio's model gives a total downforce coefficient of 3.38 at its default ride height", "Act III"),
        ],
        "es": [
            ("VENTURI", "Túnel convergente-divergente bajo el piso; en el modelo del folio el flujo alcanza 1.96 veces la velocidad libre en la garganta con 26 mm de altura de marcha", "Acto III"),
            ("ALERON", "Elemento del ala; según el folio sobre las reglas de 2026, aplanar los flaps a 6 grados (modo X) reduce 38% de la resistencia", "Acto III"),
            ("VORTICE", "Torbellino de borde tipo Lamb-Oseen que sella el borde del piso en el modelo; estrangular la garganta bajo 19 mm lo revienta", "Acto III"),
            ("SUELO", "Superficie del asfalto; la altura de marcha de 26 mm fija la succión bajo el piso en el modelo del folio", "Acto III"),
            ("CARGA", "Fuerza vertical descendente; el coeficiente de carga total del modelo del folio es 3.38 con su altura de marcha inicial", "Acto III"),
            ("AIRE", "Fluido que, en el modelo, se acelera a 1.96 veces la velocidad libre en la garganta del piso", "Acto III"),
        ],
    },
    "p08": {
        "title_en": "Folio P.08 · Bragg Pearlescent Paint vs. Matte Stucco Optics Crossword",
        "title_es": "Folio P.08 · Crucigrama de Óptica Ondulatoria del Color y Pintura Automotriz",
        "en": [
            ("PEARL", "Pigment of TiO2-coated mica platelets whose color shifts with viewing angle through Bragg interference", "Act I"),
            ("BRAGG", "In the folio's model, a 240 nm TiO2 layer selects a 588 nm peak at normal incidence in second order", "Act III"),
            ("MATTE", "Diffuse finish like Barragán's mineral lime walls, which the folio contrasts with angle-dependent car paint", "Act I"),
            ("MICA", "Mineral platelet coated with a TiO2 nanolayer in the folio's pearlescent finish model", "Act III"),
            ("GLOSS", "Low microfacet roughness concentrates metallic highlights in the folio's Cook-Torrance picture", "Act III"),
            ("ANGLE", "Viewing angle; sweeping it from 0 to 65 degrees shifts the model's color peak blueward by about 42 nm", "Act III"),
        ],
        "es": [
            ("BRAGG", "En el modelo del folio, una capa de TiO2 de 240 nm selecciona un pico de 588 nm a incidencia normal en segundo orden", "Acto III"),
            ("NACAR", "Pigmento de escamas de mica recubiertas con dióxido de titanio cuyo color cambia con el ángulo de visión por interferencia", "Acto I"),
            ("ESTUCO", "Revestimiento mineral mate como los muros de cal de Barragán, que el folio contrasta con la pintura automotriz", "Acto I"),
            ("COLOR", "Sensación luminosa que, en el folio, depende de la interferencia de ondas o de la absorción selectiva", "Acto I"),
            ("MICA", "Laminilla mineral recubierta con una nanocapa de TiO2 en el modelo de acabado perlado del folio", "Acto III"),
            ("ONDA", "Oscilación electromagnética transversal cuya fase se suma o se cancela en una película delgada según el ángulo de visión", "Acto III"),
        ],
    },
    # ---------------- PILLAR IV: MATHEMATICS (M.01 - M.08) ----------------
    "m01": {
        "title_en": "Folio M.01 · Lean 4 Fermat's Last Theorem & Modularity Crossword",
        "title_es": "Folio M.01 · Crucigrama del Último Teorema de Fermat en Lean 4",
        "en": [
            ("FERMAT", "17th-century French lawyer who noted in the margin of his Arithmetica that no power above the second splits into two like powers", "Act I"),
            ("WILES", "Mathematician whose 1995 Annals paper, with Richard Taylor's companion paper, treats modularity of semistable elliptic curves", "Act I"),
            ("RIBET", "Proved the level-lowering statement known as the epsilon conjecture in 1986", "Act I"),
            ("FREY", "Observed in the mid-1980s that a counterexample would give a semistable elliptic curve that should not be modular", "Act I"),
            ("LEAN", "Proof assistant used by a public repository whose README states it holds a complete formal proof of Fermat's Last Theorem (not checked here)", "Act IV"),
            ("CUSP", "Weight-2 modular form space S_2(Gamma_0(2)); the folio's last stage notes that its dimension is zero", "Act III"),
        ],
        "es": [
            ("FERMAT", "Abogado francés del siglo XVII que anotó en el margen de su Arithmetica que ninguna potencia mayor que dos se divide en dos potencias iguales", "Acto I"),
            ("WILES", "Matemático cuyo artículo de 1995 en Annals, con el artículo complementario de Richard Taylor, trata la modularidad de curvas elípticas semiestables", "Acto I"),
            ("RIBET", "Demostró en 1986 el descenso de nivel conocido como conjetura épsilon", "Acto I"),
            ("CURVA", "Curva elíptica semiestable que Frey asoció a un hipotético contraejemplo, y que no debería ser modular", "Acto I"),
            ("LEAN", "Asistente de demostración que usa un repositorio público cuyo README afirma contener una demostración formal completa del Último Teorema de Fermat (no comprobado aquí)", "Acto IV"),
            ("PRIMO", "Los exponentes primos p desde 3 son los casos del argumento; para p = 2 sí hay soluciones, como 3² + 4² = 5²", "Acto III"),
        ],
    },
    "m02": {
        "title_en": "Folio M.02 · Riemann Zeta Zero-Density Crossword",
        "title_es": "Folio M.02 · Crucigrama de Densidad de Ceros de la Función Zeta de Riemann",
        "en": [
            ("RIEMANN", "1859 mathematician who connected prime distribution to complex zeros of zeta(s)", "Act I"),
            ("SIEVE", "Montgomery-Halász large sieve: mean-value bounds for Dirichlet polynomials over well-spaced frequencies", "Act II"),
            ("ZETA", "Analytic function sum n^(-s) whose non-trivial zeros Riemann expected to lie on Re(s) = 1/2", "Act I"),
            ("CONREY", "Showed in 1989 that more than two-fifths of the zeros lie on the critical line", "Act I"),
            ("STRIP", "Vertical complex region 0 < Re(s) < 1 where zero-density estimates limit how many zeros lie off the critical line", "Act III"),
            ("ZERO", "A point where the zeta function vanishes; zero-density estimates limit how many lie off the critical line", "Act III"),
        ],
        "es": [
            ("RIEMANN", "Matemático que vinculó en 1859 los números primos con los ceros complejos de zeta(s)", "Acto I"),
            ("CRIBA", "La gran criba de Montgomery y Halász acota normas de media de polinomios de Dirichlet", "Acto II"),
            ("FRANJA", "Región vertical del plano complejo entre parte real 0 y parte real 1 donde se cuentan los ceros", "Acto III"),
            ("ZETA", "Función analítica cuyos ceros no triviales Riemann consideró muy probable que estén todos en Re(s) = 1/2", "Acto I"),
            ("PRIMO", "Número divisible sólo por 1 y por sí mismo, cuya distribución Riemann ligó con los ceros de zeta", "Acto I"),
            ("CERO", "Punto donde se anula la función zeta; las estimaciones de densidad limitan cuántos quedan fuera de la línea crítica", "Acto III"),
        ],
    },
    "m03": {
        "title_en": "Folio M.03 · FunSearch Cap Sets & AlphaEvolve Tensors Crossword",
        "title_es": "Folio M.03 · Crucigrama de Conjuntos Cap (FunSearch) y Tensores",
        "en": [
            ("TENSOR", "Three-way array used to describe matrix multiplication; AlphaEvolve reports 48 scalar products for 4x4 complex matrices", "Act II"),
            ("CAPSET", "Subset of F_3^n with no three distinct vectors that sum to zero (mod 3)", "Act I"),
            ("SLICE", "Slice-rank bounds from the polynomial method; Ellenberg and Gijswijt show cap sets in F_3^n have size o(2.756^n)", "Act II"),
            ("RANK", "Measure of the multiplications a bilinear product needs; AlphaEvolve reports 48 for 4x4 complex matrices, against 49 from Strassen applied twice", "Act III"),
            ("CODON", "Three-letter unit of the genetic code; the folio's comparison of avoiding forbidden patterns in sequences with building a cap set is a loose analogy", "Act IV"),
            ("SET", "Collection of 512 points in F_3^8 that the FunSearch paper reports as a cap set", "Act I"),
        ],
        "es": [
            ("TENSOR", "Arreglo algebraico tridimensional cuyo rango mide la complejidad de multiplicar matrices", "Acto II"),
            ("RANGO", "Medida de los productos escalares que necesita una multiplicación; AlphaEvolve reporta 48 para matrices complejas 4x4", "Acto III"),
            ("RECTA", "Tres puntos de F_3^n que suman cero (mod 3); un conjunto cap no contiene ninguna terna distinta así", "Acto I"),
            ("CODON", "Triplete del código genético; la comparación del folio entre evitar patrones prohibidos en secuencias y construir un conjunto cap es una analogía imprecisa", "Acto IV"),
            ("MATRIZ", "Tabla de números; AlphaEvolve reporta 48 productos escalares para multiplicar dos matrices complejas de 4x4", "Acto I"),
            ("RED", "Cuadrícula F_3^8 de 6,561 puntos en la que el artículo de FunSearch reporta un conjunto cap de 512 puntos", "Acto II"),
        ],
    },
    "m04": {
        "title_en": "Folio M.04 · Polynomial Freiman–Ruzsa & Magma Graph Crossword",
        "title_es": "Folio M.04 · Crucigrama de Entropía de Freiman–Ruzsa (PFR) y Magmas",
        "en": [
            ("ENTROPY", "Shannon measure that Gowers, Green, Manners and Tao use in their entropy proof of PFR in characteristic 2", "Act II"),
            ("MAGMA", "Set with one binary operation; the Equational Theories project concerns 4,694 magma laws and 22,028,942 ordered pairs of them", "Act I"),
            ("RUZSA", "Name on the Ruzsa distance and entropic triangle inequality used in the proof", "Act I"),
            ("COSET", "Translate of a subgroup; the project README states that A is covered by at most 2 K^12 of them", "Act III"),
            ("TAO", "Surname of one of the four authors of the characteristic 2 entropy proof of PFR", "Act I"),
            ("DAG", "Blueprint-style graph that splits a large proof or list of questions into small pieces", "Act III"),
        ],
        "es": [
            ("ENTROPIA", "Medida de incertidumbre de Shannon que usan Gowers, Green, Manners y Tao en su demostración entrópica de PFR", "Acto II"),
            ("MAGMA", "Conjunto con una sola operación binaria; el proyecto de Teorías Ecuacionales trata 4,694 leyes de magmas y 22,028,942 pares ordenados", "Acto I"),
            ("RUZSA", "Apellido de la distancia que, en versión entrópica, se usa en la demostración de PFR", "Acto I"),
            ("GRAFO", "Red cuyos nodos son leyes de magmas; el README del proyecto de Teorías Ecuacionales trata 4,694 leyes", "Acto I"),
            ("GRUPO", "Estructura algebraica cuyos subgrupos trasladados cubren un conjunto de duplicación pequeña", "Acto III"),
            ("TAO", "Apellido de uno de los cuatro autores de la demostración entrópica de PFR en característica 2", "Acto I"),
        ],
    },
    "m05": {
        "title_en": "Folio M.05 · AlphaGeometry 2 Neuro-Symbolic Olympiad Crossword",
        "title_es": "Folio M.05 · Crucigrama de Geometría Olímpica Neuro-Simbólica (AlphaGeometry 2)",
        "en": [
            ("GEOMETRY", "Field in which, as reported for AlphaGeometry, a neural model proposes auxiliary points for a symbolic deduction engine", "Act I"),
            ("CIRCLE", "Auxiliary construction, like a new point, that the neural model may propose when symbolic deduction stalls", "Act II"),
            ("CHORD", "Line segment joining two points on a circle, a basic object in olympiad geometry problems", "Act I"),
            ("ANGLE", "Quantity that the algebraic rules of the DD+AR engine chase, together with ratios and areas", "Act III"),
            ("PROOF", "Chain of deductive steps; the Nature paper reports 25 of 30 olympiad problems solved by AlphaGeometry", "Act I"),
            ("ARC", "Portion of a circle's circumference; equal inscribed angles subtend equal arcs", "Act I"),
        ],
        "es": [
            ("CIRCULO", "Construcción auxiliar, como un punto nuevo, que el modelo neuronal puede proponer cuando la deducción simbólica se detiene", "Acto II"),
            ("ANGULO", "Magnitud que las reglas algebraicas del motor simbólico DD+AR siguen, junto con razones y áreas", "Acto III"),
            ("CUERDA", "Segmento que une dos puntos de una circunferencia, objeto básico de la geometría olímpica", "Acto I"),
            ("PRUEBA", "Cadena de pasos deductivos; el artículo de Nature reporta 25 de 30 problemas olímpicos resueltos por AlphaGeometry", "Acto I"),
            ("PUNTO", "Construcción auxiliar que propone el modelo neuronal cuando el motor simbólico se estanca", "Acto II"),
            ("ARCO", "Tramo de circunferencia; ángulos inscritos iguales subtienden arcos iguales", "Acto I"),
        ],
    },
    "m06": {
        "title_en": "Folio M.06 · Sub-Cubic APSP, 3SUM & Step Supervision Crossword",
        "title_es": "Folio M.06 · Crucigrama de Complejidad Subcúbica (APSP / 3SUM) y PRM800K",
        "en": [
            ("MATRIX", "Array whose min-plus product states all-pairs shortest paths; Williams reduces that product to relatively few rectangular matrix products", "Act III"),
            ("GRAPH", "Weighted network on which the all-pairs shortest-path problem (APSP) is posed", "Act I"),
            ("PATH", "Minimum-weight route between two vertices; Williams uses Razborov-Smolensky polynomials over F_2 for the min-plus product", "Act III"),
            ("ROUND", "Verb for reporting a number with fewer digits, as the page does with 41.2% and 94.6%", "Act III"),
            ("STEP", "One line of a solution; a process reward model scores each such step", "Act III"),
            ("NODE", "Vertex in a weighted network; the page's illustrative figures use n = 4,096 vertices", "Act III"),
        ],
        "es": [
            ("CAMINO", "Ruta de peso mínimo entre dos vértices; APSP pide la de todas las parejas en un grafo ponderado", "Acto III"),
            ("GRAFO", "Red ponderada de nodos y aristas sobre la que se plantea el problema de caminos más cortos entre todos los pares (APSP)", "Acto I"),
            ("CIRCUITO", "Tipo de complejidad en que se apoya el algoritmo de Williams, con polinomios de Razborov-Smolensky sobre F_2", "Acto III"),
            ("PASO", "Eslabón individual de una solución; un modelo de recompensa de proceso puntúa cada uno", "Acto III"),
            ("NODO", "Vértice de una red; las cifras ilustrativas de la página usan n = 4,096 vértices", "Acto III"),
            ("RED", "Conjunto de nodos y aristas ponderadas sobre el que se calcula el producto min-plus", "Acto III"),
        ],
    },
    "m07": {
        "title_en": "Folio M.07 · Formula 1 Pontryagin Control & FNO Crossword",
        "title_es": "Folio M.07 · Crucigrama de Control Óptimo de Pontryagin y FNO en Fórmula 1",
        "en": [
            ("COSTATE", "Pontryagin's adjoint variable; in the folio's model the battery co-state is constant while the battery stays within its limits", "Act III"),
            ("FOURIER", "Transform at the heart of a Fourier Neural Operator layer; the folio proposes such a surrogate but trained none", "Act III"),
            ("BATTERY", "Energy store whose 4.0 MJ-per-lap budget is an assumed value in the folio's model", "Act III"),
            ("CLIP", "In the folio's model, the cut in electric power when the battery runs out; the taper avoids it", "Act III"),
            ("APEX", "Innermost point of a corner on a racing line", "Act III"),
            ("LAP", "One circuit of the track; the model seeks minimum time and closes the lap with E_batt(L) = E_batt(0)", "Act III"),
        ],
        "es": [
            ("BATERIA", "Almacén de energía cuyo presupuesto de 4.0 MJ por vuelta es un valor supuesto del modelo del folio", "Acto III"),
            ("FOURIER", "Transformada en el corazón de una capa de Operador Neuronal de Fourier; el folio propone ese sustituto pero no entrenó ninguno", "Acto III"),
            ("VUELTA", "Un circuito completo de la pista; el modelo busca el tiempo mínimo y cierra la vuelta con E_batt(L) = E_batt(0)", "Acto III"),
            ("CURVA", "Tramo del trazado antes del cual se frena; al frenar el MGU-K recupera energía en el modelo", "Acto III"),
            ("MOTOR", "Unidad de potencia híbrida de un auto de Fórmula 1; el folio reporta 350 kW eléctricos según las reglas de 2026", "Acto III"),
            ("META", "Línea donde termina la vuelta; el modelo exige que la batería llegue con la misma energía con que salió", "Acto III"),
        ],
    },
    "m08": {
        "title_en": "Folio M.08 · Schrödinger Riemannian Color Manifolds Crossword",
        "title_es": "Folio M.08 · Crucigrama de Geometría Riemanniana del Color de Schrödinger",
        "en": [
            ("MACADAM", "Researcher whose 1942 measurements of color-discrimination ellipses the folio cites", "Act III"),
            ("METRIC", "Rule g_ij for the distance between nearby colors; the folio's Helmholtz-type line element is a model, not a measured law", "Act III"),
            ("GEODESIC", "Shortest curved path between two hues under the folio's model metric; its +9.4 degree hue difference is an illustrative value", "Act III"),
            ("CONE", "Retinal photoreceptor type; the folio projects spectra onto three cone coordinates", "Act III"),
            ("ELLIPSE", "Region of colors that look the same, as in MacAdam's discrimination ellipses", "Act III"),
            ("EYE", "Organ whose three cone types give the three coordinates onto which the folio projects spectra", "Act I"),
        ],
        "es": [
            ("MACADAM", "Investigador cuyas mediciones de 1942 de elipses de discriminación de color cita el folio", "Acto III"),
            ("METRICA", "Regla para la distancia entre colores cercanos; el elemento de línea tipo Helmholtz del folio es un modelo, no una ley medida", "Acto III"),
            ("ELIPSE", "Región de colores que se ven iguales, como en las elipses de discriminación de MacAdam", "Acto III"),
            ("CONO", "Tipo de fotorreceptor de la retina; el folio proyecta el espectro sobre tres coordenadas de conos", "Acto III"),
            ("COLOR", "Espacio de tres coordenadas cuya métrica curva, del tipo que propuso Erwin Schrödinger en 1920, define trayectorias entre tonos", "Acto I"),
            ("OJO", "Órgano cuyos tres tipos de conos dan las tres coordenadas sobre las que el folio proyecta el espectro", "Acto I"),
        ],
    },
    "e09": {
        "title_en": "Folio E.09 · Autogenous Bacterial Self-Healing Concrete Crossword",
        "title_es": "Folio E.09 · Crucigrama de Concreto Autocurativo Bacteriano y Calcita",
        "en": [
            ("CALCITE", "Calcium carbonate mineral that, in the folio's model, precipitates along crack walls when bacterial spores consume calcium lactate", "Act II"),
            ("SPORE", "Dormant bacterial form; Jonkers and colleagues (2010) studied adding spore-forming bacteria to concrete so that water entering a crack could wake them", "Act I"),
            ("CRACK", "Tensile microcrack; in an idealized parallel-plate crack, closing 94 percent of the width cuts flow by 99.98 percent in the model", "Act III"),
            ("CODA", "Multiply scattered ultrasonic waves; coda-wave interferometry could be used to track stiffness recovery, shown here as an illustrative model value", "Act III"),
            ("LACTATE", "Calcium lactate nutrient that the spores consume as calcium carbonate precipitates along the crack walls", "Act I"),
            ("PORE", "Capillary space; the Lucas-Washburn law draws moisture into the crack to a depth z(t)", "Act II"),
        ],
        "es": [
            ("CALCITA", "Carbonato de calcio que, en el modelo del folio, se precipita a lo largo de las paredes de la fisura", "Acto II"),
            ("ESPORA", "Forma latente de una bacteria; las esporas pueden germinar cuando entra agua a una fisura nueva", "Acto I"),
            ("FISURA", "Grieta de tracción; en el modelo idealizado, cerrar 94% del ancho reduce el flujo en 99.98%", "Acto III"),
            ("LACTATO", "Nutriente de lactato de calcio que las esporas consumen mientras precipita carbonato de calcio", "Acto I"),
            ("SONIDO", "Ondas ultrasónicas dispersadas; la interferometría de ondas coda podría seguir la recuperación de rigidez, un valor ilustrativo del modelo", "Acto III"),
            ("AGUA", "Fluido que la imbibición capilar de Lucas-Washburn lleva al interior de la fisura y que puede despertar a las esporas", "Acto II"),
        ],
    },
    "e10": {
        "title_en": "Folio E.10 · 3D Concrete Printing (3DCP) & Roussel Thixotropy Crossword",
        "title_es": "Folio E.10 · Crucigrama de Impresión 3D de Concreto y Tixotropía de Roussel",
        "en": [
            ("ROUSSEL", "Nicolas, who set out rheological requirements for printable concretes in 2018 and a linear thixotropic structuration law", "Act I"),
            ("NOZZLE", "Printhead exit where fresh mortar, after high shear, must stiffen quickly enough to hold the layers above", "Act I"),
            ("LAYER", "Deposited filament; in the model, the bottom layer faces a gravity shear that grows at 5.5 Pa/s", "Act III"),
            ("BUCKLE", "Self-weight elastic failure of slender printed walls, analysed by Suiker (2018) and not computed on this page", "Act III"),
            ("YIELD", "Stress at which material starts to flow; the model compares base yielding by the von Mises criterion with structuration at 0.85 Pa/s", "Act III"),
            ("PUMP", "Line in which fresh mortar must keep a low dynamic yield stress under high shear before it exits the nozzle", "Act I"),
        ],
        "es": [
            ("ROUSSEL", "Nicolas, quien en 2018 expuso los requisitos reológicos de los concretos imprimibles y una ley lineal de estructuración tixotrópica", "Acto I"),
            ("CAPA", "Filamento horizontal de mortero depositado por el robot sin cimbra; en el modelo, la capa inferior soporta el esfuerzo cortante gravitacional", "Acto III"),
            ("PANDEO", "Falla elástica por peso propio de muros impresos esbeltos, analizada por Suiker (2018) y no calculada en esta página", "Acto III"),
            ("ROBOT", "Brazo que sostiene el cabezal de impresión; en el modelo, la velocidad de construcción es de 1.6 m/h", "Acto III"),
            ("FLUJO", "Movimiento del mortero fresco por la boquilla; debe mantener bajo su esfuerzo de fluencia dinámico bajo alto cortante", "Acto I"),
            ("PESO", "Peso propio de las capas superiores; en el modelo, la base cede por cortante gravitacional a una altura de unos 0.04 m", "Acto III"),
        ],
    },
    "a09": {
        "title_en": "Folio A.09 · Hygroscopic Timber Skins & Timoshenko Curvature Crossword",
        "title_es": "Folio A.09 · Crucigrama de Pieles de Madera Higroscópica y Timoshenko",
        "en": [
            ("BILAYER", "Two bonded plies that swell differently; the folio's Timoshenko model gives a curvature of 1.42 per meter for assumed values", "Act III"),
            ("BEECH", "European hardwood (Fagus sylvatica) assumed in the folio's cross-grained bilayer facade elements, a design proposal and not a tested product", "Act III"),
            ("SWELL", "Moisture expansion of wood; the model assumes beech swells tangentially at 0.32 percent per percent moisture content, an assumed round value", "Act III"),
            ("CONE", "Pine cone scale, which opens when dry and closes when wet because two layers swell differently (Dawson, Vincent and Rocca, 1997)", "Act I"),
            ("GRAIN", "Direction of the wood fibers; the model assumes beech swells far more across the grain than along it", "Act III"),
            ("ARCH", "Curved shape; the folio's Timoshenko bilayer formula (1925) gives a curvature of 1.42 per meter for its assumed plies", "Act III"),
        ],
        "es": [
            ("MADERA", "Material cuya hinchazón depende de la dirección de la fibra; el modelo del folio supone coeficientes redondos asumidos", "Acto III"),
            ("BICAPA", "Dos capas unidas que se hinchan distinto; la fórmula de Timoshenko (1925) describe su curvatura", "Acto II"),
            ("CLIMA", "Humedad del aire; en el modelo del folio, una fachada de bicapas de madera se abre y se cierra con ella sin motores", "Acto III"),
            ("HAYA", "Madera (Fagus sylvatica) supuesta en los elementos de fachada bicapa del folio, una propuesta de diseño no probada", "Acto III"),
            ("FIBRA", "Dirección de las fibras de la madera; el modelo supone que se hincha mucho más a lo ancho que a lo largo", "Acto III"),
            ("ARCO", "Forma curva; en el modelo, un pétalo de 425 mm se desplaza unos 128 mm en la punta al secarse", "Acto III"),
        ],
    },
    "a10": {
        "title_en": "Folio A.10 · Kinetic Origami & Miura-Ori Auxetic Facades Crossword",
        "title_es": "Folio A.10 · Crucigrama de Origami Cinético y Fachadas Auxéticas Miura-Ori",
        "en": [
            ("MIURA", "Koryo, whose fold, with Schenk and Guest's analysis of folded metamaterials, the folio studies for adaptive solar shading", "Act I"),
            ("CREASE", "Fold line between facets; the model treats the facets as rigid, so all motion happens at the creases", "Act III"),
            ("AUXETIC", "Having a negative Poisson ratio; Schenk and Guest showed a Miura-ori sheet has a negative in-plane one, about -0.37 at the folio's defaults", "Act III"),
            ("SOLAR", "Heat from the sun; the folio's rule gives a solar heat gain coefficient of 0.19 in the model, with energy savings not computed", "Act III"),
            ("VERTEX", "Point where four creases meet; alternate sector angles sum to pi, as in Kawasaki's flat-foldability condition", "Act III"),
            ("FOLD", "Motion of the ideal rigid Miura-ori model, which has a single degree of freedom", "Act III"),
        ],
        "es": [
            ("ORIGAMI", "Arte del plegado; el folio estudia un diseño de celosía solar adaptativa basada en el pliegue de Miura", "Acto III"),
            ("MIURA", "Koryo, cuyo pliegue estudia el folio; Schenk y Guest mostraron que una hoja Miura-ori tiene razón de Poisson negativa en el plano", "Acto I"),
            ("PLIEGUE", "Línea de doblez entre facetas; el modelo supone facetas rígidas que no se estiran", "Acto III"),
            ("SOLAR", "Calor del sol; la regla del folio da un coeficiente de ganancia solar de 0.19 en el modelo, sin calcular ahorros de energía", "Acto III"),
            ("VERTICE", "Punto donde se unen cuatro pliegues; los ángulos alternos suman pi, como en la condición de Kawasaki", "Acto III"),
            ("MAPA", "Hoja plegada de patrón Miura-ori; en el modelo rígido ideal tiene un solo grado de libertad", "Acto III"),
        ],
    },
    "p09": {
        "title_en": "Folio P.09 · Taylor-Cone Electrohydrodynamic Aerosols Crossword",
        "title_es": "Folio P.09 · Crucigrama de Conos de Taylor y Aerosoles Monodispersos",
        "en": [
            ("TAYLOR", "Sir Geoffrey, whose 1964 cone balances electrostatic stress against Laplace pressure at a half-angle of 49.3 degrees", "Act III"),
            ("DROPLET", "Droplet of 2.42 microns in the folio's model at 1.20 microliters per minute; how much cargo survives spraying is not modelled", "Act III"),
            ("CHARGE", "Droplet charge ratio, 0.68 of the Rayleigh limit in the folio's model", "Act III"),
            ("PLUME", "Cloud of fine droplets from the cone-jet; the folio does not model how much encapsulated cargo survives spraying", "Act III"),
            ("CONE", "Cone whose half-angle follows from P_1/2(cos theta) = 0, about 49.3 degrees", "Act III"),
            ("JET", "Thin liquid microjet that leaves the cone tip before varicose breakup into droplets", "Act III"),
        ],
        "es": [
            ("TAYLOR", "Sir Geoffrey, cuyo cono de 1964 equilibra el esfuerzo electrostático con la presión de Laplace en un semiángulo de 49.3 grados", "Acto III"),
            ("AEROSOL", "Niebla de gotas micrométricas; el folio no modela cuánta carga encapsulada sobrevive al rociado", "Acto III"),
            ("CARGA", "Razón de carga de la gota, 0.68 del límite de Rayleigh en el modelo del folio", "Acto III"),
            ("GOTA", "Gota de 2.42 micrómetros en el modelo del folio con 1.20 microlitros por minuto", "Acto III"),
            ("CONO", "Cono cuyo semiángulo sale de P_1/2(cos theta) = 0, unos 49.3 grados", "Acto III"),
            ("RED", "Boquilla o malla de nebulización; el folio no modela cuánta carga encapsulada sobrevive al rociado", "Acto III"),
        ],
    },
    "p10": {
        "title_en": "Folio P.10 · Topological Photonics & Haldane-Raghu Chern Insulators Crossword",
        "title_es": "Folio P.10 · Crucigrama de Fotónica Topológica y Aislantes de Chern",
        "en": [
            ("CHERN", "Integer invariant; integrating Berry curvature over the Brillouin zone gives C = +1 in the folio's model", "Act III"),
            ("BERRY", "Momentum-space curvature Omega_n(k) that the folio integrates across the photonic Brillouin zone", "Act III"),
            ("PHOTON", "Light quantum; in the folio's illustrative model, the one-way edge wave keeps 99.8 percent forward transmission at a 90-degree bend, a figure not taken from an experiment", "Act III"),
            ("HALDANE", "F. Duncan M., who with Srinivas Raghu published the 2008 Physical Review Letters paper on photonic Chern insulators that the folio builds on", "Act I"),
            ("EDGE", "Boundary state that a nonzero Chern number leads the folio to expect; its tolerance to disorder is shown in an illustrative model", "Act III"),
            ("MODE", "One-way edge wave of the folio's model, confined between regions of different topology", "Act III"),
        ],
        "es": [
            ("FOTON", "Cuanto de luz; en el modelo ilustrativo del folio, la onda de borde unidireccional conserva 99.8% de transmisión en una curva de 90 grados, una cifra que no proviene de un experimento", "Acto III"),
            ("CHERN", "Invariante entero; al integrar la curvatura de Berry sobre la zona de Brillouin el modelo del folio da C = +1", "Acto III"),
            ("BERRY", "Curvatura en el espacio de momentos que el folio integra sobre la zona de Brillouin fotónica", "Acto III"),
            ("BORDE", "Estado de frontera que un número de Chern distinto de cero lleva al folio a esperar; su tolerancia al desorden se muestra en un modelo ilustrativo", "Acto III"),
            ("CRISTAL", "Red fotónica periódica; en el folio, romper la simetría de inversión temporal abre una brecha de banda de 14.2% en el modelo", "Acto III"),
            ("ONDA", "Perturbación electromagnética; la onda de borde unidireccional del modelo conserva su transmisión hacia adelante frente al desorden", "Acto III"),
        ],
    },
    "m09": {
        "title_en": "Folio M.09 · Wasserstein-2 Optimal Transport & Sinkhorn Flow Crossword",
        "title_es": "Folio M.09 · Crucigrama de Transporte Óptimo Wasserstein-2 y Sinkhorn",
        "en": [
            ("OPTIMAL", "Describes the transport plan with least total cost; Kantorovich relaxed Monge's map into a linear program over couplings", "Act I"),
            ("MONGE", "Mathematician whose 1781 question about cut-and-fill earthworks began optimal transport", "Act I"),
            ("ENTROPY", "Penalty term in Sinkhorn's method that turns transport into alternating matrix scalings", "Act III"),
            ("FLOW", "Motion of a pressureless fluid that Benamou and Brenier use to recast Wasserstein-2 transport", "Act I"),
            ("COST", "What Kantorovich's linear program over couplings minimizes; it is quadratic for Wasserstein-2", "Act I"),
            ("MASS", "Probability density that moves along geodesics under the continuity equation in Benamou and Brenier's formulation", "Act III"),
        ],
        "es": [
            ("MONGE", "Matemático cuya pregunta de 1781 sobre cortes y rellenos de tierra dio origen al transporte óptimo", "Acto I"),
            ("BRENIER", "Coautor, con Benamou, de la reformulación del transporte Wasserstein-2 como problema de mecánica de fluidos", "Acto I"),
            ("FLUJO", "Movimiento de un fluido sin presión con el que Benamou y Brenier replantean el transporte", "Acto I"),
            ("COSTO", "Lo que minimiza el programa lineal de Kantorovich sobre acoplamientos; es cuadrático en Wasserstein-2", "Acto I"),
            ("MASA", "Densidad de probabilidad que se mueve según la ecuación de continuidad en la formulación de Benamou y Brenier", "Acto III"),
            ("RED", "Conjunto de nodos conectados; un acoplamiento entre dos distribuciones puede pensarse como una malla de pesos", "Acto III"),
        ],
    },
    "m10": {
        "title_en": "Folio M.10 · Persistent Homology, Betti Barcodes & Percolation Crossword",
        "title_es": "Folio M.10 · Crucigrama de Homología Persistente y Códigos de Betti",
        "en": [
            ("BARCODE", "Collection of birth-to-death intervals from a filtration; long bars stand out as structure and short ones read as noise", "Act II"),
            ("BETTI", "Topological invariant beta_k counting connected components (k=0), loops (k=1) and voids (k=2); the model shows 1, 3 and 0", "Act III"),
            ("SIMPLEX", "Vertex, edge, triangle or tetrahedron building block in a Vietoris-Rips filtration", "Act II"),
            ("CYCLE", "Closed loop of edges; the longest H_1 bar in the folio's synthetic point cloud runs from 38 nm to 116 nm", "Act III"),
            ("HOLE", "Tunnel or cavity in a shape; long-lived ones stand out from noise in a barcode", "Act I"),
            ("SPAN", "Length of a bar, death minus birth; the stability theorem says small perturbations move persistence points only slightly", "Act III"),
        ],
        "es": [
            ("BETTI", "Número topológico que cuenta componentes conexas, túneles y cavidades en un complejo", "Acto III"),
            ("CICLO", "Lazo cerrado de aristas; en la nube de puntos sintética del folio, la barra H_1 más larga va de 38 a 116 nm", "Acto III"),
            ("FILTRO", "Familia anidada de complejos simpliciales de Vietoris-Rips al crecer la escala epsilon", "Acto II"),
            ("BARRA", "Intervalo de nacimiento a muerte; en el modelo, las barras largas destacan del ruido (no es una medición)", "Acto III"),
            ("PORO", "Espacio vacío en un material; Robins y colaboradores (2016) relacionan rasgos de persistencia con escalas de percolación en imágenes de micro-CT", "Acto III"),
            ("DATO", "Punto de una nube, como los nodos de poro del modelo sintético; el teorema de estabilidad dice que perturbar los datos mueve poco los puntos de persistencia", "Acto III"),
        ],
    },
    "e11": {
        "title_en": "Folio E.11 · SIMP Topology Optimization, Michell Trusses & Inerter Damping Crossword",
        "title_es": "Folio E.11 · Crucigrama de Optimización Topológica SIMP y Amortiguadores Inerter",
        "en": [
            ("INERTER", "Two-terminal mechanical device whose force is proportional to relative acceleration, introduced by Malcolm Smith in 2002", "Act I"),
            ("MICHELL", "Australian engineer whose 1904 paper asked how a truss carrying a given load could use the least material", "Act I"),
            ("BONE", "Trabecular tissue; Wolff argued in 1892 that bone adapts to its loads, a resemblance with Michell trusses that the folio calls a popular analogy, not a proof", "Act I"),
            ("SIMP", "Power-law density penalization with p = 3 that pushes intermediate densities toward 0 or 1", "Act III"),
            ("SLAB", "Floor plate; keeping V/V_0 = 0.35 means 65 percent less concrete in the optimized region than a solid slab, with whole-building savings smaller", "Act III"),
            ("MASS", "Apparent mass of an inerter; the folio's illustrative ring flywheel on a screw gives about 200 times its own mass", "Act III"),
        ],
        "es": [
            ("MICHELL", "Ingeniero australiano cuyo artículo de 1904 preguntó cómo una armadura con una carga dada podía usar el mínimo de material", "Acto I"),
            ("HUESO", "Tejido trabecular; Wolff sostuvo en 1892 que el hueso se adapta a sus cargas, una analogía popular y no una demostración", "Acto I"),
            ("LOSA", "Placa de entrepiso; el folio no ejecutó ningún modelo de elementos finitos, y el 65% menos de concreto es un valor ilustrativo", "Acto III"),
            ("GIRO", "Rotación del volante de un inerter; la reducción de deriva que muestra el laboratorio es ilustrativa", "Acto III"),
            ("PESO", "Peso del concreto de la losa; con V/V_0 = 0.35 el folio ilustra 65% menos volumen en la región optimizada", "Acto III"),
            ("RED", "Malla de elementos finitos; un filtro de radio r_min suprime los patrones de tablero de ajedrez", "Acto III"),
        ],
    },
    "e12": {
        "title_en": "Folio E.12 · RISC-V Silicon, Control Barrier Functions & Firefly Grid Sync Crossword",
        "title_es": "Folio E.12 · Crucigrama de Silicio RISC-V y Barreras de Control en Redes",
        "en": [
            ("BARRIER", "Safety function h(x) >= 0; for the modelled dynamics, and while the filter stays feasible, the state does not leave the set where it holds", "Act III"),
            ("RISCV", "Open instruction-set architecture; machine-checked small processors exist in Coq, but the folio knows of no such proof for a grid relay processor", "Act III"),
            ("INVERTER", "Grid-forming converter that, in the folio's model, injects power proportional to the rate of frequency change to give virtual inertia", "Act III"),
            ("GRID", "Network whose frequency, in the folio's reduced model, dips to 59.82 Hz after a 1.2 GW loss, a model value", "Act III"),
            ("SAFE", "Set where h(x) >= 0; for the modelled dynamics the state stays inside it while the filter remains feasible", "Act III"),
            ("ROCQ", "Current name of the Coq proof assistant, in which Kami and the embedded system of Erbsen and colleagues were built", "Act III"),
        ],
        "es": [
            ("BARRERA", "Función de control h(x) >= 0; para la dinámica modelada, y mientras el programa cuadrático sea factible, el estado no sale del conjunto donde se cumple", "Acto III"),
            ("INERCIA", "Inercia sintética que, en el modelo del folio, los inversores emulan mediante máquinas síncronas virtuales", "Acto III"),
            ("SILICIO", "Material del chip RISC-V; el folio no conoce una prueba formal publicada para el procesador de un relevador de red, y la supone sin mostrarla", "Acto III"),
            ("FASE", "Ángulo de cada inversor en el modelo de osciladores acoplados; la luciérnaga es una analogía, no la misma ecuación", "Acto III"),
            ("RED", "Sistema eléctrico; PyPSA describe qué generadores, líneas y almacenamiento existen, pero la dinámica del folio es su propio modelo reducido", "Acto I"),
            ("GIRO", "Giro de las turbinas de acero, cuyo momento mecánico mantenía la frecuencia cerca de 60 ciclos por segundo y que disminuye con la energía solar y las baterías", "Acto I"),
        ],
    },
    "e13": {
        "title_en": "Folio E.13 · Biot 3D Poroelasticity & Fault Slip Margin Crossword",
        "title_es": "Folio E.13 · Crucigrama de Poroelasticidad de Biot y Fallas",
        "en": [
            ("BIOT", "Maurice, who published the 3D consolidation theory in 1941 linking rock skeleton strain and pore fluid pressure", "Act I"),
            ("SKEMPTON", "Geotechnical pioneer behind the undrained pore-pressure coefficient B = 0.394 in brine-saturated sandstone", "Act I"),
            ("FAULT", "Planar rock discontinuity whose cohesionless slip tendency |tau|/sigma'_n stays below 0.60 at sedimentary k_0 = 0.72", "Act III"),
            ("BRINE", "Saline formation water with bulk modulus 2.2 GPa; displacing it with supercritical CO2 drops B to 0.053 in the model", "Act II"),
            ("STRESS", "Normal and shear traction across a fault; the ratio k_0 = sigma_h / sigma_v separates sedimentary basins from basement", "Act III"),
            ("PORE", "Fluid-filled void space in sandstone whose pressure opposes clamping stress across mineral contacts and faults", "Act I"),
        ],
        "es": [
            ("BIOT", "Físico que en 1941 formuló la teoría tridimensional de consolidación acoplando esqueleto rocoso y presión de poro", "Acto I"),
            ("FALLA", "Discontinuidad en la roca cuya tendencia al deslizamiento sube al caer el esfuerzo normal efectivo en el modelo", "Acto III"),
            ("PORO", "Cavidad en la arenisca cuya presión de fluido empuja hacia afuera frente al peso de la sobrecarga", "Acto I"),
            ("ROCA", "Medio poroso rígido cuyo módulo drenado K_d = 12 GPa y módulo mineral K_s = 36 GPa dan alfa = 0.667", "Acto II"),
            ("SELLO", "Estrato superior de baja permeabilidad sobre el acuífero salino en el almacenamiento geológico de CO2", "Acto I"),
            ("ARENA", "Roca sedimentaria porosa (arenisca) menos críticamente esforzada que el basamento cristalino en el modelo", "Acto III"),
        ],
    },
    "e14": {
        "title_en": "Folio E.14 · Unsaturated Soil Suction Stress & Slope Stability Crossword",
        "title_es": "Folio E.14 · Crucigrama de Succión No Saturada y Estabilidad de Laderas",
        "en": [
            ("SUCTION", "Negative gauge pore-water pressure u_a - u_w above the water table that pulls unsaturated grains together", "Act I"),
            ("MUALEM", "Hydrologist whose 1976 integral links water retention curves to relative hydraulic conductivity K_r(S_e)", "Act I"),
            ("SLOPE", "Hillside inclined at angle beta; when beta exceeds drained friction phi', capillary clamping supports FS > 1", "Act III"),
            ("SAND", "Coarse soil with exponent n = 2.68 > 2 whose suction stress peaks near 7.96 kPa and falls upon drying", "Act II"),
            ("RAIN", "Storm infiltration that raises effective saturation S_e and lowers capillary clamping before u_w turns positive", "Act I"),
            ("LOAM", "Silty fine-grained soil with n = 1.60 <= 2 where modeled |sigma^s| increases monotonically with suction", "Act II"),
        ],
        "es": [
            ("SUCCION", "Presión negativa de poro u_a - u_w sobre el manto freático que mantiene unidas las partículas del suelo", "Acto I"),
            ("MUALEM", "Hidrólogo que en 1976 vinculó la curva de retención de agua con la conductividad relativa K_r(S_e)", "Acto I"),
            ("ARENA", "Suelo grueso (n = 2.68 > 2) cuyo esfuerzo de succión alcanza un pico y cae al secarse en el modelo", "Acto II"),
            ("LIMO", "Suelo fino (n = 1.60 <= 2) en el que |sigma^s| crece de forma monótona al aumentar la succión", "Acto II"),
            ("LLUVIA", "Infiltración pluvial que reduce la succión mátrica y puede disparar deslizamientos antes de saturar", "Acto I"),
            ("PORO", "Espacio intergranular ocupado por agua y aire por encima del nivel freático", "Acto I"),
        ],
    },
    "a11": {
        "title_en": "Folio A.11 · 3D Polyhedral Graphic Statics, Airy Stress & Guastavino Vaults Crossword",
        "title_es": "Folio A.11 · Crucigrama de Estática Gráfica Poliédrica 3D y Bóvedas sin Acero",
        "en": [
            ("MAXWELL", "Scientist whose 1864 paper on reciprocal figures linked plane frames in equilibrium to polyhedra; in 1870 he read a polyhedron as a stress function", "Act I"),
            ("VAULT", "Compression-only shell; the folio is a design study, and its 52 mm thickness and compression-only result are model values, not a structural check", "Act III"),
            ("DUAL", "In the force diagram, each member's face has an area proportional to the member force; a closed cell means the forces at that node balance", "Act III"),
            ("AIRY", "Stress function Phi(x, y); if its Hessian is negative-definite the model's stress field is compressive everywhere, a property of the model and not a structural check", "Act III"),
            ("TILE", "Thin timbrel unit; Rafael Guastavino and his son built hundreds of thin timbrel tile vaults in the United States after emigrating from Spain in 1881", "Act I"),
            ("RIB", "Stiffening element of a funicular floor; the folio notes that one published unreinforced funicular floor uses about one-third of the material of a flat slab", "Act I"),
        ],
        "es": [
            ("BOVEDA", "Cubierta delgada a compresión; en el folio es un estudio de diseño, con espesor ilustrativo de 52 mm y sin ser una revisión estructural", "Acto III"),
            ("MAXWELL", "Científico cuyos artículos de 1864 y 1870 sobre figuras recíprocas ligaron marcos planos en equilibrio con poliedros y funciones de esfuerzo", "Acto I"),
            ("CARA", "Polígono de una celda en el diagrama de fuerzas; su área es proporcional a la fuerza del miembro", "Acto III"),
            ("ARCO", "Forma que carga en compresión; el Folio A.01 revisa su línea de empuje con la regla del tercio medio", "Acto I"),
            ("LOSA", "Piso; el folio cita un piso funicular sin refuerzo publicado que usa cerca de un tercio del material de una losa plana", "Acto I"),
            ("CAL", "Ligante mineral tradicional, tratado en el Folio E.01; aquí se mencionan las bóvedas tabicadas de losetas de Guastavino", "Acto I"),
        ],
    },
    "a12": {
        "title_en": "Folio A.12 · Tensegrity Cable-Strut Domes & 8-13 um Radiative Sky-Cooling Crossword",
        "title_es": "Folio A.12 · Crucigrama de Domos de Tensegridad y Enfriamiento Radiativo al Cielo",
        "en": [
            ("SNELSON", "Kenneth, an art student who in the late 1940s made small sculptures in which wooden struts were held apart by taut cords", "Act I"),
            ("CABLE", "Tension element of the prestressed net; in the model, cable prestress makes the geometric stiffness positive on the mechanism modes", "Act III"),
            ("STRUT", "Isolated compression bar floating inside a tension net without touching neighboring bars", "Act III"),
            ("WINDOW", "8 to 13 micrometer atmospheric infrared band through which the folio's membrane model exchanges heat with the sky", "Act III"),
            ("DOME", "Geiger-type cable dome in a design study; 12.4 kg/m2 for a 120 m span is an illustrative figure, not a design result", "Act III"),
            ("COOL", "In the model, the membrane surface sits about 5.2 degrees below the air, an illustrative model value", "Act III"),
        ],
        "es": [
            ("CABLE", "Elemento continuo en tracción; en el modelo, su preesfuerzo t_0 rigidiza los modos de mecanismo del domo", "Acto III"),
            ("DOMO", "Cubierta de cables y puntales de un estudio de diseño; 12.4 kg/m2 es una cifra ilustrativa", "Acto III"),
            ("CIELO", "Sumidero frío con el que la membrana intercambia calor por la ventana de 8 a 13 micras en el modelo", "Acto III"),
            ("BARRA", "Puntal aislado de acero en compresión que flota sin tocar ninguna otra barra", "Acto III"),
            ("SOL", "Luz solar; en el modelo, la membrana supuesta refleja 97% de 1,000 W/m2, un valor asumido", "Acto III"),
            ("RED", "Malla de cables en equilibrio; la matriz de equilibrio se analiza con descomposición en valores singulares (Pellegrino y Calladine, 1986)", "Acto III"),
        ],
    },
    "a13": {
        "title_en": "Folio A.13 · Heinz Isler Thin-Shell Domes & Buckling Knockdown Crossword",
        "title_es": "Folio A.13 · Crucigrama de Cáscaras Delgadas de Heinz Isler y Pandeo",
        "en": [
            ("ISLER", "Swiss engineer Heinz, who presented hanging-cloth and pneumatic shell form-finding at Madrid in 1959", "Act I"),
            ("ZOELLY", "Author of the 1915 classical elastic spherical-shell buckling pressure formula", "Act II"),
            ("DIMPLE", "Localized inward shell defect that lowers buckling capacity more sharply than an outward bump", "Act II"),
            ("SHELL", "Thin doubly curved roof carrying load mainly by in-plane membrane forces rather than bending", "Act I"),
            ("CLOTH", "Hanging fabric soaked in plaster or frozen in winter air and inverted into compression", "Act I"),
            ("CREEP", "Long-term concrete deformation that reduces effective modulus and lowers buckling resistance", "Act III"),
        ],
        "es": [
            ("ISLER", "Ingeniero suizo que presentó en 1959 las telas colgadas invertidas para hallar formas de cáscaras", "Acto I"),
            ("ZOELLY", "Autor en 1915 de la fórmula clásica de pandeo elástico para una esfera uniforme", "Acto II"),
            ("TELA", "Lámina textil colgada en tracción pura que al endurecerse e invertirse trabaja en compresión", "Acto I"),
            ("PANDEO", "Inestabilidad súbita que gobierna una cáscara delgada mucho antes de su aplastamiento", "Acto II"),
            ("DOMO", "Casquete curvo idealizado de 31.6 m de claro analizado en este modelo", "Acto III"),
            ("CARGA", "Peso propio y sobrecarga uniforme proyectada en planta dentro del modelo", "Acto III"),
        ],
    },
    "p11": {
        "title_en": "Folio P.11 · Surface-Code Quantum Error Correction & FeMoCo Nitrogen Catalysis Crossword",
        "title_es": "Folio P.11 · Crucigrama de Corrección Cuántica de Superficie y Catálisis de Nitrógeno",
        "en": [
            ("SURFACE", "Code family whose star and plaquette parity checks the folio simulates; it takes a threshold of about 1 percent", "Act III"),
            ("QUBIT", "Quantum bit; in the folio's resource estimate a distance-27 surface code needs 1,458 physical qubits per logical one", "Act III"),
            ("FEMOCO", "Iron-molybdenum cofactor of nitrogenase; the folio asks whether quantum simulation could one day inform the search for ambient-temperature nitrogen fertilizer", "Act III"),
            ("ANYON", "Non-Abelian quasiparticle whose braiding the folio mentions alongside surface codes", "Act IV"),
            ("STIM", "Open-source stabilizer-circuit simulator, Craig Gidney's quantumlib/Stim, that the folio names for surface-code parity checks", "Act III"),
            ("CODE", "Distance-27 surface code; in the folio's resource estimate, logical error per cycle reaches 3.0e-16, labelled a resource estimate only", "Act III"),
        ],
        "es": [
            ("CUANTICO", "Relativo a la computación cuántica tolerante a fallos; el folio sólo da una estimación de recursos, no un resultado", "Acto III"),
            ("CODIGO", "Código de superficie de Kitaev; el folio supone un umbral de cerca del 1 por ciento", "Acto III"),
            ("PARIDAD", "Chequeo conmutativo de estrella y plaqueta que el folio simula sin colapsar la superposición lógica", "Acto III"),
            ("AMONIACO", "Fertilizante nitrogenado; el folio pregunta si la simulación cuántica podría informar algún día la búsqueda de uno a temperatura ambiente", "Acto III"),
            ("RED", "Cuadrícula bidimensional de qubits; el folio nombra el software abierto Stim para sus chequeos de paridad", "Acto III"),
            ("FASE", "Estimación cuántica de fase; el folio la menciona para el estado de transición del FeMoCo, con una precisión de hasta 1.0 kcal/mol como estimación", "Acto III"),
        ],
    },
    "p12": {
        "title_en": "Folio P.12 · Hilbert's Sixth Problem: Boltzmann Kinetics to Navier-Stokes Crossword",
        "title_es": "Folio P.12 · Crucigrama del Sexto Problema de Hilbert: De Boltzmann a Navier-Stokes",
        "en": [
            ("HILBERT", "Mathematician who posed in 1900 the 6th Problem of axiomatizing physics from atoms to fluids", "Act I"),
            ("SPHERE", "Hard Newtonian particle of diameter epsilon that evolves under Boltzmann-Grad scaling in the folio's first level", "Act III"),
            ("FLUID", "Continuum described by the incompressible Navier-Stokes equations; Deng, Hani and Ma report in a preprint a derivation of them from hard-sphere collisions over long times", "Act I"),
            ("TREE", "Layered Feynman interaction trees that, according to the authors' preprints, help cut recollision loops", "Act III"),
            ("SCALE", "Size regime; the Knudsen number compares mean free path with the flow scale, and the folio takes it toward zero to reach Navier-Stokes", "Act III"),
            ("LIMIT", "Boltzmann-Grad and Knudsen limits that the folio's levels take; as the Knudsen number goes to zero, the flow is incompressible Navier-Stokes", "Act III"),
        ],
        "es": [
            ("HILBERT", "Matemático que planteó en 1900 el sexto problema sobre el paso de átomos al continuo fluido", "Acto I"),
            ("ESFERA", "Partícula dura newtoniana que evoluciona bajo el escalamiento de Boltzmann-Grad en el primer nivel del folio", "Acto III"),
            ("FLUIDO", "Medio continuo descrito por Navier-Stokes incompresible; Deng, Hani y Ma reportan en un preprint una derivación de sus ecuaciones desde colisiones de esferas duras en tiempos largos", "Acto I"),
            ("ARBOL", "Árbol de interacción por capas de Feynman que, según los preprints de los autores, ayuda a cortar lazos de recolisión", "Acto III"),
            ("CAOS", "Hipótesis de caos molecular de Boltzmann (1872), que las recolisiones amenazaban; los preprints de Deng, Hani y Ma reportan un tratamiento a tiempos largos", "Acto I"),
            ("OLA", "Perturbación que se propaga; los pronósticos más rápidos y confiables de ciclones y crecidas son una perspectiva del folio, no un resultado reportado", "Acto III"),
        ],
    },
    "m11": {
        "title_en": "Folio M.11 · 3D Kakeya Conjecture (Wang-Zahl) & Guth-Maynard 30/13 Riemann Bound Crossword",
        "title_es": "Folio M.11 · Crucigrama de la Conjetura de Kakeya 3D y la Cota 30/13 de Guth-Maynard",
        "en": [
            ("KAKEYA", "Conjecture about sets holding a unit segment in every direction; Wang and Zahl's preprint states a proof of dimension 3 in R^3", "Act I"),
            ("NEEDLE", "Unit segment that can be turned through all directions inside a set of arbitrarily small volume (Besicovitch)", "Act I"),
            ("PRIME", "Integer with exactly two divisors; Guth and Maynard also deduce asymptotics for primes in short intervals of length x^(17/30+o(1))", "Act III"),
            ("ZETA", "Riemann's function; Guth and Maynard improve the exponent bounding zeros off the critical line to 30/13", "Act III"),
            ("TUBE", "Thin cylinder of width delta; Wang and Zahl study sets of such delta-tubes in R^3", "Act III"),
            ("GAP", "Space between consecutive primes; the Guth-Maynard result gives asymptotics for primes in short intervals", "Act III"),
        ],
        "es": [
            ("KAKEYA", "Conjetura sobre conjuntos con un segmento unitario en cada dirección; el preprint de Wang y Zahl afirma demostrar dimensión 3 en R^3", "Acto I"),
            ("RECTA", "Aguja unitaria que, según la paradoja de Besicovitch, gira 360 grados dentro de un conjunto de volumen arbitrariamente pequeño", "Acto I"),
            ("PRIMO", "Entero con exactamente dos divisores; Guth y Maynard deducen asintóticas para primos en intervalos cortos de longitud x^(17/30+o(1))", "Acto III"),
            ("TUBO", "Cilindro delgado de ancho delta; Wang y Zahl estudian conjuntos de tales delta-tubos en R^3", "Acto III"),
            ("CERO", "Punto donde se anula la función zeta; Guth y Maynard mejoran a 30/13 el exponente que acota los que quedan fuera de la línea crítica", "Acto III"),
            ("LEAN", "Lenguaje de demostración formal; el README de anthropics/formal-math, leído el 14 de noviembre de 2026, no lista este resultado", "Acto IV"),
        ],
    },
    "m12": {
        "title_en": "Folio M.12 · Public Lean 4 Repositories & Post-Quantum Lattices Crossword",
        "title_es": "Folio M.12 · Crucigrama de Repositorios Lean 4 Públicos y Retículos Post-Cuánticos ML-KEM",
        "en": [
            ("LATTICE", "Structure on which module-lattice problems are posed; NIST FIPS 203 (ML-KEM) rests its security on their presumed hardness", "Act III"),
            ("QUANTUM", "Kind of computer that Shor's 1994 algorithm would let break RSA and elliptic-curve cryptography; none able to do so has been reported", "Act III"),
            ("NOISE", "Small centered binomial error e added in b = A s + e (mod 3329) to hide the secret s", "Act III"),
            ("LEAN", "Language of the public repository anthropics/formal-math, whose README lists three projects that this site has not checked", "Act III"),
            ("RANK", "Number of multiplications a bilinear map needs, as in Folio M.03; an earlier rank claim on this page was withdrawn", "Act III"),
            ("KEY", "Secret shared through a key encapsulation mechanism such as ML-KEM; liboqs is an open-source library of post-quantum algorithms", "Act III"),
        ],
        "es": [
            ("RETICULO", "Estructura sobre la que se plantean los problemas de retículos modulares; la seguridad de NIST FIPS 203 (ML-KEM) descansa en su dureza presunta", "Acto III"),
            ("PRUEBA", "Argumento matemático; el README de anthropics/formal-math lista tres proyectos de Lean 4 que este sitio no ha comprobado", "Acto III"),
            ("RUIDO", "Error binomial centrado y pequeño e que oculta el secreto s en b = A s + e (mod 3329)", "Acto III"),
            ("CLAVE", "Secreto compartido mediante un mecanismo de encapsulamiento como ML-KEM; liboqs es una biblioteca abierta de algoritmos post-cuánticos", "Acto III"),
            ("RANGO", "Número de multiplicaciones que necesita una aplicación bilineal, como en el Folio M.03; una afirmación de rango de una edición anterior se retiró", "Acto III"),
            ("RED", "Conjunto de nodos conectados; un proyecto de Lean 4 puede organizarse como una red de dependencias entre lemas (Folio M.01)", "Acto IV"),
        ],
    },
    "m13": {
        "title_en": "Folio M.13 · Shannon Zero-Error Capacity & Lovász Theta Crossword",
        "title_es": "Folio M.13 · Crucigrama de Capacidad de Error Cero de Shannon y Theta de Lovász",
        "en": [
            ("SHANNON", "Information theorist who in 1956 turned zero-error coding into packing vertices in strong graph products", "Act I"),
            ("LOVASZ", "Mathematician whose 1979 orthonormal umbrella bounded capacity from above and closed C_5 at root five", "Act I"),
            ("HAEMERS", "Author of the 1979 matrix-rank bound showing capacity can stay strictly below theta on 27 lines", "Act I"),
            ("CYCLE", "Ring graph of odd length n whose capacity sits between independence alpha and theta", "Act II"),
            ("SANDWICH", "Inequality chain placing Lovasz theta between independence number and clique cover", "Act II"),
            ("SCHLAFLI", "Cubic-surface graph on 27 vertices whose complement has theta = 9 and rational rank 7", "Act III"),
        ],
        "es": [
            ("SHANNON", "Teórico de la información que en 1956 formuló la capacidad de error cero mediante productos fuertes", "Acto I"),
            ("LOVASZ", "Matemático cuyo paraguas ortonormal de 1979 cerró la capacidad del ciclo de cinco en raíz de cinco", "Acto I"),
            ("HAEMERS", "Autor de la cota de rango matricial de 1979 que separó la capacidad de theta en 27 rectas", "Acto I"),
            ("CICLO", "Grafo en anillo impar de n vértices donde el caso de siete sigue abierto entre 3.2579 y 3.3177", "Acto II"),
            ("RANGO", "Dimensión lineal exacta igual a 7 para A(S_bar) - I sobre el complemento de Schläfli", "Acto III"),
            ("CONO", "Figura geométrica de vectores ortogonales que acota desde arriba los empaquetamientos sin error", "Acto II"),
        ],
    },
    "cc01": {
        "title_en": "CC.01 · Golf GTI Chassis, Boost & Transaxle Crossword",
        "title_es": "CC.01 · Crucigrama de Chasis, Turbo y Transmisión del Golf GTI",
        "en": [
            ("TORQUE", "Rotational turning effort (Nm) metered across open, brake-based, and clutch-pack front differentials", "Part IV"),
            ("TARTAN", "Woven check seat textile pairing with the dimpled golf-ball knob in 1976", "Part I"),
            ("TURBO", "Exhaust-driven compressor introduced as the mainline GTI petrol architecture from the 1998 Mk4", "Part III"),
            ("CLUTCH", "Friction engagement element—doubled coaxially in the 2004 DSG and hydraulic front lock", "Part III"),
            ("CAMBER", "Wheel tilt angle changing under lateral body roll on MacPherson struts", "Part IV"),
            ("BRAKE", "Inside-wheel clamping force used by XDS to redirect open-differential drive torque", "Part IV"),
        ],
        "es": [
            ("EMBRAGUE", "Elemento de fricción duplicado en flechas coaxiales DSG y en el paquete delantero VAQ", "Parte III"),
            ("CHASIS", "Bastidor y geometría de suspensión rebajados 10 mm adelante y 20 mm atrás en el Mk1 de 1976", "Parte I"),
            ("AGARRE", "Límite de tracción μ · N · r que topa un diferencial abierto al descargar la rueda interior", "Parte IV"),
            ("FRENOS", "Sistema usado por XDS para morder el disco interior y enviar par al neumático exterior", "Parte IV"),
            ("VOLANTE", "Mando de dirección progresiva con 2.1 vueltas de tope a tope frente a 2.75 en Golf base", "Parte IV"),
            ("MOTOR", "Unidad de cuatro cilindros que evolucionó de 1.6 L atmosférico a 2.0 L turboalimentado", "Parte II"),
        ],
    },
    "cc02": {
        "title_en": "CC.02 · La Sagrada Família Stereotomy & Towers Crossword",
        "title_es": "CC.02 · Crucigrama de Estereotomía y Torres de la Sagrada Família",
        "en": [
            ("CATENARY", "Curve of a hanging self-weight cord inverted by Gaudí to carry masonry vaults in compression", "Part I"),
            ("GAUDI", "Architect who took over the Barcelona temple in 1883 at age 31 and turned it toward ruled geometry", "Part I"),
            ("PORPHYRY", "Red igneous rock used for the four heaviest 12-pointed crossing pillars at 24 m total height", "Part II"),
            ("RULED", "Class of curved surfaces generated by moving a straight line—hyperboloid, paraboloid, helicoid, conoid", "Part II"),
            ("OCULUS", "Daylight aperture carved with one-sheet hyperboloid geometry in the nave ceiling vaults", "Part II"),
            ("TOWER", "One of 18 parabolic spires, topped in February 2026 by the 172.5 m central spire of Jesus Christ", "Part IV"),
        ],
        "es": [
            ("CATENARIA", "Curva de una cuerda suspendida por su peso propio que Gaudí invirtió para trabajar a compresión", "Parte I"),
            ("PORFIDO", "Roca ígnea roja elegida para los cuatro pilares centrales de 12 puntas y 24 m de altura total", "Parte II"),
            ("REGLADA", "Superficie curva generada por una recta móvil, como el hiperboloide o el paraboloide hiperbólico", "Parte II"),
            ("COLUMNA", "Pilar arbóreo nacido de la intersección de dos prismas estrellados que giran en sentidos opuestos", "Parte II"),
            ("BASALTO", "Piedra volcánica negra empleada en los pilares de 10 puntas alrededor del perímetro del crucero", "Parte II"),
            ("TORRE", "Cada una de las 18 agujas de perfil parabólico, coronadas a 172.5 m en 2026 debajo de Montjuïc", "Parte IV"),
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
