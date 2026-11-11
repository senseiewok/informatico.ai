/**
 * @module folio-puzzle
 * Newspaper-inspired Interactive Bilingual Crossword Atelier & Collector's Passport
 * for Informatico.ai (/).
 *
 * Features:
 * - Independent English (`en`) and Mexican Spanish (`es-MX`) 10x10 crosswords per Folio (66 total puzzles).
 * - Persistent `localStorage` cell state (`informatico.puzzle.v1.<slug>.<lang>`) + cross-tab sync.
 * - Global Collector's Passport (`informatico.passport.v1`) stamping solved seals (`EN ✓` / `ES-MX ✓`)
 *   onto the Issue Rack cards and the 32-Folio Index Matrix.
 * - WAI-ARIA `role="grid"` / `role="gridcell"` roving `tabindex="0"`, full keyboard navigation
 *   (Arrows, Space to toggle Across/Down, A-Z entry with auto-advance, Backspace smart step-back).
 * - Strict CSP compliance: zero DOM string injection and zero inline style mutations.
 */

const PASSPORT_STORAGE_KEY = "informatico.passport.v1";
const PUZZLE_KEY_PREFIX = "informatico.puzzle.v1.";
const TOTAL_PUZZLE_TARGETS = 49; // Cover Hub + 40 Folios (82 bilingual puzzles total)

const memoryFallbackStore = new Map();

function safeGetStorage(key) {
  try {
    if (typeof window !== "undefined" && window.localStorage) {
      const raw = window.localStorage.getItem(key);
      if (raw !== null) return raw;
    }
  } catch (_err) {
    // Fallback to in-memory map when storage is blocked
  }
  return memoryFallbackStore.get(key) || null;
}

function safeSetStorage(key, value) {
  memoryFallbackStore.set(key, value);
  try {
    if (typeof window !== "undefined" && window.localStorage) {
      window.localStorage.setItem(key, value);
    }
  } catch (_err) {
    // Ignore storage quota or private mode errors
  }
}

export function loadPassport() {
  const raw = safeGetStorage(PASSPORT_STORAGE_KEY);
  if (raw) {
    try {
      const parsed = JSON.parse(raw);
      if (parsed && typeof parsed === "object" && parsed.solved && typeof parsed.solved === "object") {
        return parsed;
      }
    } catch (_err) {
      // Fall through to default
    }
  }
  return { version: 1, solved: {} };
}

export function recordPassportSolved(slug, lang) {
  const passport = loadPassport();
  if (!passport.solved[slug] || typeof passport.solved[slug] !== "object") {
    passport.solved[slug] = {};
  }
  if (!passport.solved[slug][lang]) {
    passport.solved[slug][lang] = new Date().toISOString();
    safeSetStorage(PASSPORT_STORAGE_KEY, JSON.stringify(passport));
  }
  return passport;
}

export function clearPassportSolved(slug, lang) {
  const passport = loadPassport();
  if (passport.solved[slug] && typeof passport.solved[slug] === "object" && passport.solved[slug][lang]) {
    delete passport.solved[slug][lang];
    if (Object.keys(passport.solved[slug]).length === 0) {
      delete passport.solved[slug];
    }
    safeSetStorage(PASSPORT_STORAGE_KEY, JSON.stringify(passport));
  }
  return passport;
}

function loadPuzzleState(slug, lang) {
  const key = `${PUZZLE_KEY_PREFIX}${slug}.${lang}`;
  const raw = safeGetStorage(key);
  if (raw) {
    try {
      const parsed = JSON.parse(raw);
      if (parsed && typeof parsed === "object" && parsed.cells && typeof parsed.cells === "object") {
        return {
          version: 1,
          slug,
          lang,
          cells: parsed.cells,
          solved: Boolean(parsed.solved),
          solvedAt: parsed.solvedAt || null,
          hintsUsed: Number(parsed.hintsUsed) || 0,
        };
      }
    } catch (_err) {
      // Fall through to fresh state
    }
  }
  return {
    version: 1,
    slug,
    lang,
    cells: {},
    solved: false,
    solvedAt: null,
    hintsUsed: 0,
  };
}

function savePuzzleState(slug, lang, state) {
  const key = `${PUZZLE_KEY_PREFIX}${slug}.${lang}`;
  safeSetStorage(key, JSON.stringify(state));
}

function getActiveLanguageCode() {
  const docLang = (document.documentElement.getAttribute("lang") || "en").toLowerCase();
  return docLang.startsWith("es") ? "es" : "en";
}

function clearElementChildren(el) {
  while (el && el.firstChild) {
    el.removeChild(el.firstChild);
  }
}

/**
 * Synchronizes Collector's Passport counters, progress bars, Issue Rack badges,
 * and 32-Folio Index Matrix solved seals across the page.
 */
export function syncPassportUI(scope = document) {
  const passport = loadPassport();
  const solvedMap = passport.solved || {};
  let enCount = 0;
  let esCount = 0;
  let anyFolioCount = 0;

  for (const slug of Object.keys(solvedMap)) {
    const entry = solvedMap[slug];
    if (!entry || typeof entry !== "object") continue;
    const hasEn = Boolean(entry.en);
    const hasEs = Boolean(entry.es);
    if (hasEn) enCount += 1;
    if (hasEs) esCount += 1;
    if (hasEn || hasEs) anyFolioCount += 1;
  }

  const totalBilingualSolved = enCount + esCount;
  const lang = getActiveLanguageCode();

  const progressBars = document.querySelectorAll(".tp-passport-progress");
  progressBars.forEach((bar) => {
    bar.setAttribute("max", String(TOTAL_PUZZLE_TARGETS * 2));
    bar.setAttribute("value", String(totalBilingualSolved));
  });

  const countReadouts = document.querySelectorAll(".tp-passport-count");
  countReadouts.forEach((node) => {
    const enText = `${anyFolioCount} / ${TOTAL_PUZZLE_TARGETS} Folios Sealed (EN: ${enCount} · ES-MX: ${esCount})`;
    const esText = `${anyFolioCount} / ${TOTAL_PUZZLE_TARGETS} Folios Sellados (EN: ${enCount} · ES-MX: ${esCount})`;
    node.setAttribute("data-en", enText);
    node.setAttribute("data-es", esText);
    node.textContent = lang === "es" ? esText : enText;
  });

  // Stamp solved seals onto Issue Rack cards and Index Matrix rows
  const rackCards = scope.querySelectorAll(".tp-rack-card[data-folio-slug], tr[data-folio-slug]");
  rackCards.forEach((card) => {
    const fSlug = (card.getAttribute("data-folio-slug") || "").toLowerCase();
    if (!fSlug) return;
    const entry = solvedMap[fSlug] || {};
    const hasEn = Boolean(entry.en);
    const hasEs = Boolean(entry.es);
    let badge = card.querySelector(".tp-rack-solved-seal");
    if (!hasEn && !hasEs) {
      if (badge && badge.parentNode) {
        badge.parentNode.removeChild(badge);
      }
      card.classList.remove("has-solved-crossword");
      return;
    }
    card.classList.add("has-solved-crossword");
    if (!badge) {
      badge = document.createElement("span");
      badge.className = "tp-rack-solved-seal";
      const targetContainer = card.querySelector(".tp-rack-card-meta") || card.querySelector("td:first-child") || card;
      targetContainer.appendChild(badge);
    }
    const tags = [];
    if (hasEn) tags.push("EN ✓");
    if (hasEs) tags.push("ES-MX ✓");
    const labelText = `❖ ${tags.join(" · ")}`;
    badge.textContent = labelText;
    badge.setAttribute(
      "title",
      lang === "es"
        ? `Crucigrama resuelto (${tags.join(", ")})`
        : `Crossword solved (${tags.join(", ")})`
    );
  });
}

function mountSingleFolioPuzzle(section) {
  if (!section || section.dataset.puzzleMounted === "true") return;
  section.dataset.puzzleMounted = "true";

  const slug = (section.getAttribute("data-puzzle-slug") || "hub").toLowerCase();
  const payloadScript = section.querySelector("script.tp-puzzle-payload");
  if (!payloadScript) return;

  let payload = null;
  try {
    payload = JSON.parse(payloadScript.textContent || "{}");
  } catch (_err) {
    return;
  }
  if (!payload || !payload.en || !payload.es) return;

  const gridContainer = section.querySelector(".tp-crossword-grid");
  const acrossList = section.querySelector(".tp-cw-clues-across");
  const downList = section.querySelector(".tp-cw-clues-down");
  const activeClueBanner = section.querySelector(".tp-cw-active-clue-text");
  const activeClueDirBadge = section.querySelector(".tp-cw-active-clue-dir");
  const statusBanner = section.querySelector(".tp-cw-status-readout");
  const langEditionBadge = section.querySelector(".tp-cw-edition-badge");
  const titleHeading = section.querySelector(".tp-cw-puzzle-title");
  const wordProgressEl = section.querySelector(".tp-cw-word-progress");

  if (!gridContainer || !acrossList || !downList) return;

  let currentLang = getActiveLanguageCode();
  let puzzleData = payload[currentLang] || payload.en;
  let state = loadPuzzleState(slug, currentLang);

  // Runtime interactive state
  let activeRow = 0;
  let activeCol = 0;
  let activeDir = "across"; // "across" | "down"
  let cellButtons = []; // 2D array [r][c] -> HTMLButtonElement | null
  let clueElements = { across: new Map(), down: new Map() };

  function getWordsForDirection(dir) {
    return dir === "down" ? puzzleData.down || [] : puzzleData.across || [];
  }

  function findWordContainingCell(r, c, dir) {
    const list = getWordsForDirection(dir);
    for (const w of list) {
      if (dir === "across") {
        if (w.row === r && c >= w.col && c < w.col + w.length) return w;
      } else {
        if (w.col === c && r >= w.row && r < w.row + w.length) return w;
      }
    }
    return null;
  }

  function getActiveWord() {
    let w = findWordContainingCell(activeRow, activeCol, activeDir);
    if (w) return { word: w, dir: activeDir };
    const altDir = activeDir === "across" ? "down" : "across";
    w = findWordContainingCell(activeRow, activeCol, altDir);
    if (w) {
      activeDir = altDir;
      return { word: w, dir: activeDir };
    }
    const firstAcross = (puzzleData.across || [])[0];
    if (firstAcross) {
      activeDir = "across";
      activeRow = firstAcross.row;
      activeCol = firstAcross.col;
      return { word: firstAcross, dir: "across" };
    }
    return null;
  }

  function getWordCells(word, dir) {
    const coords = [];
    for (let i = 0; i < word.length; i += 1) {
      const r = dir === "across" ? word.row : word.row + i;
      const c = dir === "across" ? word.col + i : word.col;
      coords.push([r, c]);
    }
    return coords;
  }

  function isCellSolvedCorrectly(r, c) {
    const sol = puzzleData.grid[r] && puzzleData.grid[r][c];
    if (!sol || sol === "#") return true;
    const entered = (state.cells[`${r},${c}`] || "").toUpperCase();
    return entered === sol.toUpperCase();
  }

  function isWordCompleteAndCorrect(word, dir) {
    const coords = getWordCells(word, dir);
    return coords.every(([r, c]) => isCellSolvedCorrectly(r, c));
  }

  function countCompletedWords() {
    const allAcross = puzzleData.across || [];
    const allDown = puzzleData.down || [];
    let done = 0;
    const total = allAcross.length + allDown.length;
    for (const w of allAcross) {
      if (isWordCompleteAndCorrect(w, "across")) done += 1;
    }
    for (const w of allDown) {
      if (isWordCompleteAndCorrect(w, "down")) done += 1;
    }
    return { done, total };
  }

  function checkFullPuzzleSolved() {
    for (let r = 0; r < puzzleData.rows; r += 1) {
      for (let c = 0; c < puzzleData.cols; c += 1) {
        const sol = puzzleData.grid[r][c];
        if (sol !== "#") {
          const entered = (state.cells[`${r},${c}`] || "").toUpperCase();
          if (entered !== sol.toUpperCase()) {
            return false;
          }
        }
      }
    }
    return true;
  }

  function setStatusMessage(enMsg, esMsg, tone = "neutral") {
    if (!statusBanner) return;
    statusBanner.setAttribute("data-en", enMsg);
    statusBanner.setAttribute("data-es", esMsg);
    statusBanner.textContent = currentLang === "es" ? esMsg : enMsg;
    statusBanner.classList.remove("is-status-ok", "is-status-warn");
    if (tone === "ok") statusBanner.classList.add("is-status-ok");
    if (tone === "warn") statusBanner.classList.add("is-status-warn");
  }

  function updateVisualHighlights(focusActiveDom = false) {
    const activeInfo = getActiveWord();
    const highlightSet = new Set();
    if (activeInfo && activeInfo.word) {
      for (const [hr, hc] of getWordCells(activeInfo.word, activeInfo.dir)) {
        highlightSet.add(`${hr},${hc}`);
      }
    }

    for (let r = 0; r < puzzleData.rows; r += 1) {
      for (let c = 0; c < puzzleData.cols; c += 1) {
        const btn = cellButtons[r] && cellButtons[r][c];
        if (!btn) continue;
        const key = `${r},${c}`;
        const letter = (state.cells[key] || "").toUpperCase();
        const charSpan = btn.querySelector(".tp-cw-char");
        if (charSpan) {
          charSpan.textContent = letter;
        }
        const isCurrent = r === activeRow && c === activeCol;
        const isInWord = highlightSet.has(key);

        btn.classList.toggle("is-active-cell", isCurrent);
        btn.classList.toggle("is-word-highlight", isInWord && !isCurrent);
        btn.classList.toggle("has-letter", Boolean(letter));
        btn.setAttribute("tabindex", isCurrent ? "0" : "-1");
        btn.setAttribute("aria-selected", isCurrent ? "true" : "false");

        const num = puzzleData.numbers[r] && puzzleData.numbers[r][c];
        const numPrefix = num ? (currentLang === "es" ? `Pista ${num}, ` : `Clue ${num}, `) : "";
        const valDesc = letter
          ? (currentLang === "es" ? `Letra ${letter}` : `Letter ${letter}`)
          : (currentLang === "es" ? "Vacía" : "Empty");
        btn.setAttribute(
          "aria-label",
          currentLang === "es"
            ? `Fila ${r + 1} Columna ${c + 1}, ${numPrefix}${valDesc}`
            : `Row ${r + 1} Column ${c + 1}, ${numPrefix}${valDesc}`
        );

        if (isCurrent && focusActiveDom) {
          btn.focus({ preventScroll: true });
        }
      }
    }

    // Highlight active clue & mark solved words in clue columns
    for (const dir of ["across", "down"]) {
      const list = getWordsForDirection(dir);
      const map = clueElements[dir];
      for (const w of list) {
        const li = map.get(w.number);
        if (!li) continue;
        const isCurrentClue = Boolean(
          activeInfo && activeInfo.dir === dir && activeInfo.word.number === w.number
        );
        const isSolvedWord = isWordCompleteAndCorrect(w, dir);
        li.classList.toggle("is-active-clue", isCurrentClue);
        li.classList.toggle("is-clue-complete", isSolvedWord);
      }
    }

    // Update Active Clue Banner
    if (activeInfo && activeInfo.word) {
      const w = activeInfo.word;
      const dirLabel =
        activeInfo.dir === "across"
          ? currentLang === "es"
            ? `${w.number} HORIZONTAL`
            : `${w.number} ACROSS`
          : currentLang === "es"
          ? `${w.number} VERTICAL`
          : `${w.number} DOWN`;
      if (activeClueDirBadge) {
        activeClueDirBadge.textContent = dirLabel;
      }
      if (activeClueBanner) {
        activeClueBanner.textContent = `${w.clue} (${w.length}) · [${w.act}]`;
      }
    }

    const { done, total } = countCompletedWords();
    if (wordProgressEl) {
      wordProgressEl.setAttribute("max", String(Math.max(1, total)));
      wordProgressEl.setAttribute("value", String(done));
    }

    const solvedNow = checkFullPuzzleSolved();
    section.classList.toggle("is-puzzle-solved", solvedNow);
    if (solvedNow && !state.solved) {
      state.solved = true;
      state.solvedAt = new Date().toISOString();
      savePuzzleState(slug, currentLang, state);
      recordPassportSolved(slug, currentLang);
      syncPassportUI(document);
      setStatusMessage(
        `❖ Folio Crossword Sealed! All ${total} scientific terms verified and stamped in your Collector's Passport.`,
        `❖ ¡Crucigrama del Folio Sellado! Los ${total} términos científicos fueron verificados y sellados en tu Pasaporte.`,
        "ok"
      );
    } else if (!solvedNow && state.solved) {
      state.solved = false;
      savePuzzleState(slug, currentLang, state);
    }
  }

  function advanceAlongActiveWord(step = 1) {
    const activeInfo = getActiveWord();
    if (!activeInfo || !activeInfo.word) return;
    const coords = getWordCells(activeInfo.word, activeInfo.dir);
    const idx = coords.findIndex(([r, c]) => r === activeRow && c === activeCol);
    if (idx === -1) return;

    if (step > 0) {
      // First look for next empty cell in the current word
      for (let i = idx + 1; i < coords.length; i += 1) {
        const [nr, nc] = coords[i];
        if (!state.cells[`${nr},${nc}`]) {
          activeRow = nr;
          activeCol = nc;
          return;
        }
      }
      // Otherwise step to immediate next cell in word if within bounds
      if (idx + 1 < coords.length) {
        activeRow = coords[idx + 1][0];
        activeCol = coords[idx + 1][1];
      }
    } else if (step < 0 && idx - 1 >= 0) {
      activeRow = coords[idx - 1][0];
      activeCol = coords[idx - 1][1];
    }
  }

  function moveByArrow(dr, dc) {
    const desiredDir = dr !== 0 ? "down" : "across";
    if (activeDir !== desiredDir && findWordContainingCell(activeRow, activeCol, desiredDir)) {
      activeDir = desiredDir;
    }
    let r = activeRow + dr;
    let c = activeCol + dc;
    while (r >= 0 && r < puzzleData.rows && c >= 0 && c < puzzleData.cols) {
      if (puzzleData.grid[r][c] !== "#") {
        activeRow = r;
        activeCol = c;
        updateVisualHighlights(true);
        return;
      }
      r += dr;
      c += dc;
    }
  }

  function handleCellKeyDown(event) {
    const key = event.key;
    if (key === "ArrowRight") {
      event.preventDefault();
      moveByArrow(0, 1);
      return;
    }
    if (key === "ArrowLeft") {
      event.preventDefault();
      moveByArrow(0, -1);
      return;
    }
    if (key === "ArrowDown") {
      event.preventDefault();
      moveByArrow(1, 0);
      return;
    }
    if (key === "ArrowUp") {
      event.preventDefault();
      moveByArrow(-1, 0);
      return;
    }
    if (key === " " || key === "Spacebar") {
      event.preventDefault();
      const altDir = activeDir === "across" ? "down" : "across";
      if (findWordContainingCell(activeRow, activeCol, altDir)) {
        activeDir = altDir;
        updateVisualHighlights(true);
      }
      return;
    }
    if (key === "Home" || key === "End") {
      event.preventDefault();
      const activeInfo = getActiveWord();
      if (activeInfo && activeInfo.word) {
        const coords = getWordCells(activeInfo.word, activeInfo.dir);
        const target = key === "Home" ? coords[0] : coords[coords.length - 1];
        if (target) {
          activeRow = target[0];
          activeCol = target[1];
          updateVisualHighlights(true);
        }
      }
      return;
    }
    if (key === "Backspace" || key === "Delete") {
      event.preventDefault();
      const cellKey = `${activeRow},${activeCol}`;
      const btn = cellButtons[activeRow] && cellButtons[activeRow][activeCol];
      if (btn) btn.classList.remove("is-wrong", "is-correct");

      if (state.cells[cellKey]) {
        delete state.cells[cellKey];
      } else if (key === "Backspace") {
        advanceAlongActiveWord(-1);
        const prevKey = `${activeRow},${activeCol}`;
        const prevBtn = cellButtons[activeRow] && cellButtons[activeRow][activeCol];
        if (prevBtn) prevBtn.classList.remove("is-wrong", "is-correct");
        delete state.cells[prevKey];
      }
      savePuzzleState(slug, currentLang, state);
      updateVisualHighlights(true);
      return;
    }

    if (/^[a-zA-ZñÑ]$/.test(key) && !event.ctrlKey && !event.metaKey && !event.altKey) {
      event.preventDefault();
      const upper = key.toUpperCase();
      const cellKey = `${activeRow},${activeCol}`;
      const btn = cellButtons[activeRow] && cellButtons[activeRow][activeCol];
      if (btn) btn.classList.remove("is-wrong", "is-correct");
      state.cells[cellKey] = upper;
      savePuzzleState(slug, currentLang, state);
      advanceAlongActiveWord(1);
      updateVisualHighlights(true);
    }
  }

  function renderPuzzleBoard() {
    currentLang = getActiveLanguageCode();
    puzzleData = payload[currentLang] || payload.en;
    state = loadPuzzleState(slug, currentLang);

    if (titleHeading) {
      titleHeading.setAttribute("data-en", payload.en.title || "");
      titleHeading.setAttribute("data-es", payload.es.title || "");
      titleHeading.textContent = puzzleData.title || "";
    }

    if (langEditionBadge) {
      const enBadge = "EN · INDEPENDENT ENGLISH EDITION (10×10)";
      const esBadge = "ES-MX · EDICIÓN INDEPENDIENTE EN ESPAÑOL (10×10)";
      langEditionBadge.setAttribute("data-en", enBadge);
      langEditionBadge.setAttribute("data-es", esBadge);
      langEditionBadge.textContent = currentLang === "es" ? esBadge : enBadge;
    }

    // Set initial active cell to first Across word start
    const firstAcross = (puzzleData.across || [])[0];
    if (firstAcross) {
      activeRow = firstAcross.row;
      activeCol = firstAcross.col;
      activeDir = "across";
    } else {
      activeRow = 0;
      activeCol = 0;
      activeDir = "across";
    }

    clearElementChildren(gridContainer);
    cellButtons = [];

    for (let r = 0; r < puzzleData.rows; r += 1) {
      const rowEl = document.createElement("div");
      rowEl.className = "tp-cw-row";
      rowEl.setAttribute("role", "row");
      const rowBtns = [];

      for (let c = 0; c < puzzleData.cols; c += 1) {
        const cellVal = puzzleData.grid[r][c];
        if (cellVal === "#") {
          const blockEl = document.createElement("div");
          blockEl.className = "tp-cw-cell is-block";
          blockEl.setAttribute("role", "gridcell");
          blockEl.setAttribute("aria-disabled", "true");
          rowEl.appendChild(blockEl);
          rowBtns.push(null);
        } else {
          const btn = document.createElement("button");
          btn.type = "button";
          btn.className = "tp-cw-cell is-letter";
          btn.setAttribute("role", "gridcell");
          btn.dataset.row = String(r);
          btn.dataset.col = String(c);

          const num = puzzleData.numbers[r] && puzzleData.numbers[r][c];
          if (num) {
            const numSpan = document.createElement("span");
            numSpan.className = "tp-cw-num";
            numSpan.setAttribute("aria-hidden", "true");
            numSpan.textContent = String(num);
            btn.appendChild(numSpan);
          }

          const charSpan = document.createElement("span");
          charSpan.className = "tp-cw-char";
          charSpan.textContent = (state.cells[`${r},${c}`] || "").toUpperCase();
          btn.appendChild(charSpan);

          btn.addEventListener("click", () => {
            if (activeRow === r && activeCol === c) {
              const altDir = activeDir === "across" ? "down" : "across";
              if (findWordContainingCell(r, c, altDir)) {
                activeDir = altDir;
              }
            } else {
              activeRow = r;
              activeCol = c;
              if (!findWordContainingCell(r, c, activeDir)) {
                const altDir = activeDir === "across" ? "down" : "across";
                if (findWordContainingCell(r, c, altDir)) {
                  activeDir = altDir;
                }
              }
            }
            updateVisualHighlights(true);
          });

          btn.addEventListener("keydown", handleCellKeyDown);
          rowEl.appendChild(btn);
          rowBtns.push(btn);
        }
      }
      gridContainer.appendChild(rowEl);
      cellButtons.push(rowBtns);
    }

    // Render Across & Down Clue Lists
    clueElements = { across: new Map(), down: new Map() };
    const renderClueColumn = (listEl, words, dir) => {
      clearElementChildren(listEl);
      for (const w of words) {
        const li = document.createElement("li");
        li.className = "tp-cw-clue-item";
        li.dataset.clueNumber = String(w.number);
        li.dataset.clueDir = dir;

        const clueBtn = document.createElement("button");
        clueBtn.type = "button";
        clueBtn.className = "tp-cw-clue-btn";

        const numTag = document.createElement("span");
        numTag.className = "tp-cw-clue-num";
        numTag.textContent = `${w.number}.`;

        const textSpan = document.createElement("span");
        textSpan.className = "tp-cw-clue-copy";
        textSpan.textContent = `${w.clue} `;

        const metaSpan = document.createElement("span");
        metaSpan.className = "tp-cw-clue-meta";
        metaSpan.textContent = `(${w.length} · ${w.act})`;

        clueBtn.appendChild(numTag);
        clueBtn.appendChild(textSpan);
        clueBtn.appendChild(metaSpan);

        clueBtn.addEventListener("click", () => {
          activeDir = dir;
          const coords = getWordCells(w, dir);
          const firstEmpty = coords.find(([cr, cc]) => !state.cells[`${cr},${cc}`]);
          if (firstEmpty) {
            activeRow = firstEmpty[0];
            activeCol = firstEmpty[1];
          } else {
            activeRow = w.row;
            activeCol = w.col;
          }
          updateVisualHighlights(true);
        });

        li.appendChild(clueBtn);
        listEl.appendChild(li);
        clueElements[dir].set(w.number, li);
      }
    };

    renderClueColumn(acrossList, puzzleData.across || [], "across");
    renderClueColumn(downList, puzzleData.down || [], "down");

    if (state.solved && checkFullPuzzleSolved()) {
      recordPassportSolved(slug, currentLang);
      setStatusMessage(
        "❖ Solved & Sealed in Collector's Passport. Switch EN / ES-MX anytime for the companion crossword.",
        "❖ Resuelto y sellado en el Pasaporte de Coleccionista. Cambia entre EN y ES-MX para el crucigrama hermano.",
        "ok"
      );
    } else {
      setStatusMessage(
        "Select any cell or clue and type A–Z. Space toggles Across/Down; progress auto-saves to localStorage.",
        "Selecciona una celda o pista y escribe A–Z. Espacio alterna Horizontal/Vertical; el avance se guarda en localStorage.",
        "neutral"
      );
    }

    updateVisualHighlights(false);
    syncPassportUI(document);
  }

  // Wire toolbar action buttons
  const actionButtons = section.querySelectorAll("[data-cw-action]");
  actionButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const action = btn.getAttribute("data-cw-action");
      if (action === "check-cell") {
        const curBtn = cellButtons[activeRow] && cellButtons[activeRow][activeCol];
        if (!curBtn) return;
        const entered = (state.cells[`${activeRow},${activeCol}`] || "").toUpperCase();
        if (!entered) {
          setStatusMessage(
            "Type a letter in the active cell first to verify it.",
            "Escribe primero una letra en la celda activa para verificarla.",
            "warn"
          );
          return;
        }
        const ok = isCellSolvedCorrectly(activeRow, activeCol);
        curBtn.classList.toggle("is-correct", ok);
        curBtn.classList.toggle("is-wrong", !ok);
        setStatusMessage(
          ok ? "✓ Active cell matches the primary specification." : "✕ Cell mismatch — try another term.",
          ok ? "✓ La celda activa coincide con la especificación." : "✕ La letra no coincide — intenta otro término.",
          ok ? "ok" : "warn"
        );
      } else if (action === "check-puzzle") {
        let checked = 0;
        let errors = 0;
        for (let r = 0; r < puzzleData.rows; r += 1) {
          for (let c = 0; c < puzzleData.cols; c += 1) {
            const cBtn = cellButtons[r] && cellButtons[r][c];
            if (!cBtn) continue;
            const entered = (state.cells[`${r},${c}`] || "").toUpperCase();
            if (!entered) continue;
            checked += 1;
            const ok = isCellSolvedCorrectly(r, c);
            cBtn.classList.toggle("is-correct", ok);
            cBtn.classList.toggle("is-wrong", !ok);
            if (!ok) errors += 1;
          }
        }
        if (checked === 0) {
          setStatusMessage(
            "No letters entered yet — pick an Across or Down clue to begin.",
            "Aún no hay letras ingresadas — elige una pista Horizontal o Vertical para comenzar.",
            "warn"
          );
        } else if (errors === 0) {
          setStatusMessage(
            `✓ All ${checked} entered letters are verified accurate!`,
            `✓ ¡Las ${checked} letras ingresadas son correctas!`,
            "ok"
          );
        } else {
          setStatusMessage(
            `Checked ${checked} cells: ${errors} mismatch(es) highlighted.`,
            `Verificadas ${checked} celdas: ${errors} discrepancia(s) marcada(s).`,
            "warn"
          );
        }
      } else if (action === "reveal-cell") {
        const sol = puzzleData.grid[activeRow] && puzzleData.grid[activeRow][activeCol];
        if (!sol || sol === "#") return;
        state.cells[`${activeRow},${activeCol}`] = sol.toUpperCase();
        state.hintsUsed = (state.hintsUsed || 0) + 1;
        const curBtn = cellButtons[activeRow] && cellButtons[activeRow][activeCol];
        if (curBtn) {
          curBtn.classList.remove("is-wrong");
          curBtn.classList.add("is-correct");
        }
        savePuzzleState(slug, currentLang, state);
        advanceAlongActiveWord(1);
        updateVisualHighlights(true);
      } else if (action === "reveal-word") {
        const activeInfo = getActiveWord();
        if (!activeInfo || !activeInfo.word) return;
        for (const [wr, wc] of getWordCells(activeInfo.word, activeInfo.dir)) {
          const sol = puzzleData.grid[wr][wc];
          if (sol && sol !== "#") {
            state.cells[`${wr},${wc}`] = sol.toUpperCase();
            const cBtn = cellButtons[wr] && cellButtons[wr][wc];
            if (cBtn) {
              cBtn.classList.remove("is-wrong");
              cBtn.classList.add("is-correct");
            }
          }
        }
        state.hintsUsed = (state.hintsUsed || 0) + 1;
        savePuzzleState(slug, currentLang, state);
        updateVisualHighlights(true);
      } else if (action === "reset-puzzle") {
        state.cells = {};
        state.solved = false;
        state.solvedAt = null;
        savePuzzleState(slug, currentLang, state);
        clearPassportSolved(slug, currentLang);
        syncPassportUI(document);
        for (let r = 0; r < puzzleData.rows; r += 1) {
          for (let c = 0; c < puzzleData.cols; c += 1) {
            const cBtn = cellButtons[r] && cellButtons[r][c];
            if (cBtn) cBtn.classList.remove("is-wrong", "is-correct");
          }
        }
        setStatusMessage(
          "Grid reset for this language edition.",
          "Cuadrícula reiniciada para esta edición de idioma.",
          "neutral"
        );
        updateVisualHighlights(true);
      }
    });
  });

  renderPuzzleBoard();

  window.addEventListener("tp-lang-change", () => {
    const nextLang = getActiveLanguageCode();
    if (nextLang !== currentLang) {
      renderPuzzleBoard();
    } else {
      syncPassportUI(document);
    }
  });
}

let storageListenerAttached = false;

export function initFolioPuzzles(scope = document) {
  const sections = scope.querySelectorAll(".tp-puzzle-atelier[data-puzzle-slug]");
  sections.forEach((section) => {
    mountSingleFolioPuzzle(section);
  });
  syncPassportUI(scope);

  if (!storageListenerAttached && typeof window !== "undefined") {
    storageListenerAttached = true;
    window.addEventListener("storage", (e) => {
      if (!e.key || e.key === PASSPORT_STORAGE_KEY || e.key.startsWith(PUZZLE_KEY_PREFIX)) {
        syncPassportUI(document);
      }
    });
  }
}
