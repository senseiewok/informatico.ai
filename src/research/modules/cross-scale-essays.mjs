/**
 * @module cross-scale-essays
 * Zero-dependency interactive instruments for the 3 Informatico.ai Cross-Scale Featured Essays (/essays/):
 *  - [data-cs-instrument="mesoscopic"] (ES.01): Fluctuation-dissipation, short-wavelength gas saturation vs R^6 T^9
 *    black-body photon localization in ultra-high vacuum (0.15–4 K), paired with Stokes-Einstein & Ogston-Amsden
 *    hindered nanoparticle diffusion in aqueous hydrogels (310.15 K).
 *  - [data-cs-instrument="epistemic"]  (ES.02): Six-tier Epistemic Lattice & 8-mutant falsification inspector comparing
 *    tabletop quantum-gravity deductions (DERIVED (NOT MEASURED)) with Cryo-EM structural gaps (UNRESOLVED vs DELETED).
 *  - [data-cs-instrument="tur_pores"]  (ES.03): Barato-Seifert Thermodynamic Uncertainty Relation (Q_TUR >= 2) on a
 *    biased Markovian clock/gating ring paired with Brinkman porous screening & Kramers barrier escape.
 *  - [data-cs-predict]: Predict-before-reveal interactive commitment prompt.
 */

const KB = 1.380649e-23;
const HBAR = 1.054571817e-34;
const C_LIGHT = 299792458.0;
const M_HE = 6.6464731e-27;
const ZETA9 = 1.0020083928260822;
const FACT8 = 40320.0;

function lang() {
  return /^es(?:-|$)/i.test(document.documentElement.lang || "") ? "es" : "en";
}

function fmtSci(x) {
  if (!Number.isFinite(x)) return "—";
  if (x === 0) return "0";
  const ax = Math.abs(x);
  if (ax >= 0.01 && ax < 1000) return x.toPrecision(3);
  return x.toExponential(2);
}

function initPredict(root) {
  const answer = root.getAttribute("data-answer");
  const verdict = root.querySelector("[data-cs-verdict]");
  const buttons = root.querySelectorAll("button[data-choice]");
  let chosen = null;

  function renderVerdict() {
    if (!chosen || !verdict) return;
    const isEs = lang() === "es";
    const right = chosen === answer;
    const prefix = right
      ? (isEs ? "Predicción acertada: " : "Prediction confirmed: ")
      : (isEs ? "Contraste instructivo: " : "Instructive contrast: ");
    const explain = root.getAttribute(isEs ? "data-explain-es" : "data-explain-en") || "";
    verdict.hidden = false;
    verdict.setAttribute("data-correct", String(right));
    verdict.textContent = prefix + explain;
  }

  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      chosen = btn.getAttribute("data-choice");
      buttons.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      renderVerdict();
    });
  });
  window.addEventListener("tp-lang-change", renderVerdict);
  root.setAttribute("data-cs-ready", "true");
}

function initMesoscopic(root) {
  const logP = root.querySelector('[data-cs-input="logp"]');
  const tempK = root.querySelector('[data-cs-input="temp"]');
  const splitUm = root.querySelector('[data-cs-input="split"]');
  const meshNm = root.querySelector('[data-cs-input="mesh"]');
  const koBtn = root.querySelector("[data-cs-knockout]");
  const statusEl = root.querySelector("[data-cs-status]");
  const gasBar = root.querySelector('[data-cs-bar="gas"]');
  const photBar = root.querySelector('[data-cs-bar="phot"]');
  const gelBar = root.querySelector('[data-cs-bar="gel"]');
  const reads = {};
  root.querySelectorAll("[data-cs-read]").forEach((el) => { reads[el.getAttribute("data-cs-read")] = el; });
  let knockout = false;

  const MSG = {
    en: {
      ok: "Live regime: in ultra-high vacuum (Kn >> 1), 4 K helium collisions are short-wavelength saturated (independent of split Δx), while thermal photons scale as R⁶T⁹Δx²; at 310 K in hydrogel, Ogston polymer-mesh hindrance suppresses Stokes–Einstein transport.",
      ko: "Planted-defect knockout active: treats polymer hydrogel as pure water (no Ogston fiber hindrance) and falsely scales short-wavelength gas collisions as Δx²—the exact regime confusion the Python verifier rejects.",
    },
    es: {
      ok: "Régimen vivo: en ultra-alto vacío (Kn >> 1), las colisiones de helio a 4 K están saturadas en onda corta (independientes de Δx), mientras los fotones térmicos escalan como R⁶T⁹Δx²; a 310 K en hidrogel, el impedimento de malla de Ogston frena la difusión de Stokes–Einstein.",
      ko: "Apagado / defecto plantado activo: trata el hidrogel como agua pura (sin malla de Ogston) y escala falsamente el gas de onda corta con Δx², la confusión de régimen que el verificador rechaza.",
    },
  };

  function render() {
    const pPa = 10 ** Number(logP ? logP.value : -15);
    const tVac = Number(tempK ? tempK.value : 4.0);
    const dxUm = Number(splitUm ? splitUm.value : 100);
    const xiNm = Number(meshNm ? meshNm.value : 120);
    const dxM = dxUm * 1e-6;

    // 10^-14 kg diamond sphere (rho = 3510 kg/m^3 -> R ≈ 8.79e-7 m)
    const rDiam = Math.cbrt((3 * 1e-14) / (4 * Math.PI * 3510));
    const vTh = Math.sqrt((8 * KB * tVac) / (Math.PI * M_HE));
    const nGas = pPa / (KB * tVac);
    // Kinetic collision saturation rate (independent of dx since lambda_th << dx) vs naive long-wavelength Lambda_gas * dx^2
    const lambdaGasLong = (8 * Math.sqrt(2 * Math.PI) * Math.sqrt(M_HE * KB * tVac) * pPa * rDiam * rDiam) / (3 * HBAR * HBAR);
    const gammaGas = knockout ? (lambdaGasLong * dxM * dxM) : (nGas * Math.PI * rDiam * rDiam * vTh);
    // Dipole scattered black-body photons (Joos-Zeh / Romero-Isart R^6 T^9 dx^2, eps=5.7 diamond)
    const epsRe = (5.7 - 1) / (5.7 + 2);
    const kTherm = (KB * tVac) / (HBAR * C_LIGHT);
    const lambdaSc = ((FACT8 * 8 * ZETA9 * C_LIGHT * (rDiam ** 6)) / (9 * Math.PI)) * (kTherm ** 9) * (epsRe ** 2);
    const gammaPhot = lambdaSc * dxM * dxM;

    // 310.15 K aqueous polymer hydrogel for R_np = 50 nm (100 nm nanoparticle), r_f = 3.5 nm mucin/polymer fiber
    const rNp = 50e-9;
    const rFiber = 3.5e-9;
    const etaWater = 0.691e-3;
    const d0Um2s = ((KB * 310.15) / (6 * Math.PI * etaWater * rNp)) * 1e12;
    const xiM = xiNm * 1e-9;
    const ogston = knockout ? 1.0 : Math.exp(-Math.PI * (((rNp + rFiber) / (xiM + 2 * rFiber)) ** 2));
    const dEffUm2s = d0Um2s * ogston;
    const isEs = lang() === "es";

    if (reads.logp) reads.logp.textContent = `10^${Number(logP.value).toFixed(1)} Pa`;
    if (reads.temp) reads.temp.textContent = `${tVac.toFixed(1)} K`;
    if (reads.split) reads.split.textContent = `${dxUm.toFixed(0)} µm`;
    if (reads.mesh) reads.mesh.textContent = `${xiNm.toFixed(0)} nm`;
    if (reads.gammagas) reads.gammagas.textContent = `${fmtSci(gammaGas)} s⁻¹`;
    if (reads.gammaphot) reads.gammaphot.textContent = `${fmtSci(gammaPhot)} s⁻¹`;
    if (reads.deff) reads.deff.textContent = `${dEffUm2s.toFixed(2)} µm²/s (${(ogston * 100).toFixed(1)}% ${isEs ? "de D₀" : "of D₀"})`;

    // Unified logarithmic scale [10^-12, 10^10 s^-1] across both vacuum decoherence bars so bar length strictly preserves rate ordering
    const mapBar = (val, minLog, maxLog) => {
      const lv = Math.log10(Math.max(val, 10 ** minLog));
      return Math.max(8, Math.min(240, ((lv - minLog) / (maxLog - minLog)) * 240));
    };
    if (gasBar) gasBar.setAttribute("width", mapBar(gammaGas, -12, 10).toFixed(1));
    if (photBar) photBar.setAttribute("width", mapBar(gammaPhot, -12, 10).toFixed(1));
    if (gelBar) gelBar.setAttribute("width", Math.max(8, ogston * 240).toFixed(1));

    if (statusEl) {
      const L = MSG[lang()];
      statusEl.textContent = knockout ? L.ko : L.ok;
      statusEl.setAttribute("data-state", knockout ? "defect" : "pass");
    }
  }

  [logP, tempK, splitUm, meshNm].forEach((el) => { if (el) el.addEventListener("input", render); });
  if (koBtn) {
    koBtn.addEventListener("click", () => {
      knockout = !knockout;
      koBtn.setAttribute("aria-pressed", String(knockout));
      render();
    });
  }
  window.addEventListener("tp-lang-change", render);
  root.setAttribute("data-cs-ready", "true");
  render();
}

function initEpistemic(root) {
  const modeSel = root.querySelectorAll("button[data-ep-case]");
  const koBtn = root.querySelector("[data-cs-knockout]");
  const badgeEl = root.querySelector('[data-cs-read="badge"]');
  const parentEl = root.querySelector('[data-cs-read="parent"]');
  const mutantEl = root.querySelector('[data-cs-read="mutants"]');
  const statusEl = root.querySelector("[data-cs-status]");
  const hiNode = root.querySelector("[data-ep-highlight]");
  let activeCase = "derived_recast";
  let laxMode = false;

  const CASES = {
    derived_recast: {
      y: 134,
      badgeEn: "DERIVED (NOT MEASURED)",
      badgeEs: "DERIVADO (NO MEDIDO)",
      laxEn: "DERIVED WITHOUT MEASURED PARENT (M3 LEAK!)",
      laxEs: "DERIVADO SIN FILA MADRE MEDIDA (¡FUGA M3!)",
      parentEn: "Parent: T05-LEE2020 (52 µm Eöt-Wash inverse-square data)",
      parentEs: "Fila madre: T05-LEE2020 (datos Eöt-Wash a 52 µm)",
      noteEn: "Exact Fourier–Bessel projection excludes σ > 33 µm at 95%, yet no smeared-kernel raw-data refit or entanglement witness has been measured.",
      noteEs: "La proyección exacta de Fourier–Bessel excluye σ > 33 µm al 95 %, pero no se ha medido ningún testigo ni reajustado los datos crudos.",
      laxNoteEn: "Parent gate disabled: mutant M3_DERIVED_PROPOSED_PARENT survives (7/8 killed), letting unbuilt PROPOSED parents masquerade as DERIVED.",
      laxNoteEs: "Compuerta madre apagada: sobrevive el mutante M3_DERIVED_PROPOSED_PARENT (7/8 eliminados), permitiendo derivar desde filas PROPUESTAS.",
    },
    cryo_rdomain: {
      y: 262,
      badgeEn: "OPEN / UNRESOLVED COORDINATES",
      badgeEs: "ABIERTO / COORDENADAS NO RESUELTAS",
      laxEn: "MEASURED (SMOOTHED HALLUCINATION!)",
      laxEs: "MEDIDO (¡ALUCINACIÓN SUAVIZADA!)",
      parentEn: "Structures: 5UAK & 6MSM (Phe508 present; ~200-aa R-domain disordered)",
      parentEs: "Estructuras: 5UAK y 6MSM (Phe508 presente; dominio R ~200 aa desordenado)",
      noteEn: "Wild-type Phe508 is resolved in 5UAK/6MSM (and deleted in 8EIQ ΔF508), while the flexible R-domain smears out in cryo-EM—honest scripts leave unmodeled atoms blank.",
      noteEs: "Phe508 silvestre está resuelto en 5UAK/6MSM (y ausente en 8EIQ ΔF508), mientras el dominio R flexible no tiene coordenadas 3D: el verificador deja el hueco en blanco.",
      laxNoteEn: "Lax prose defect: interpolates disordered ~200-aa cryo-EM density as if resolved—caught in strict mode by M7_CRYOEM_UNRESOLVED_AS_MEASURED.",
      laxNoteEs: "Defecto de prosa laxa: interpola el dominio R desordenado (~200 aa) como si estuviera resuelto, bloqueado en modo estricto por M7.",
    },
    bmv_witness: {
      y: 198,
      badgeEn: "PROPOSED",
      badgeEs: "PROPUESTO",
      laxEn: "DERIVED (UNBUILT PARENT PROMOTED!)",
      laxEs: "DERIVADO (¡PADRE NO CONSTRUIDO PROMOVIDO!)",
      parentEn: "Preprint / Proposal cap: apparatus not yet realized at 10⁻¹⁴ kg",
      parentEs: "Tope de propuesta: aparato aún no construido a 10⁻¹⁴ kg",
      noteEn: "Whether witnessing entanglement experimentally settles quantum gravity vs non-LOCC classical hybrids remains an active 2025–2026 dispute.",
      noteEs: "Si observar el entrelazamiento decide entre gravedad cuántica e híbridos clásicos sigue en disputa activa en 2025–2026.",
      laxNoteEn: "Parent gate disabled: mutant M3_DERIVED_PROPOSED_PARENT survives (7/8 killed), falsely promoting algebra over an unbuilt T05-BOSE2017 apparatus.",
      laxNoteEs: "Compuerta madre apagada: sobrevive el mutante M3 (7/8 eliminados), promoviendo álgebra sobre un aparato T05-BOSE2017 aún no construido.",
    },
    eotwash_law: {
      y: 68,
      badgeEn: "MEASURED",
      badgeEs: "MEDIDO",
      laxEn: "MEASURED (UNAFFECTED; SUITE FAILS M3)",
      laxEs: "MEDIDO (INTACTO; LA BATERÍA FALLA EN M3)",
      parentEn: "≥ 2 independent collaborations (Lee 2020 Eöt-Wash + Tan 2020 HUST, > 24 mo)",
      parentEs: "≥ 2 colaboraciones independientes (Lee 2020 Eöt-Wash + Tan 2020 HUST, > 24 meses)",
      noteEn: "Peer-reviewed, independently replicated across distinct torsion-balance geometries, and past the 24-month replication window.",
      noteEs: "Revisado por pares, replicado por grupos independientes con geometrías distintas y fuera de la ventana de 24 meses.",
      laxNoteEn: "This replicated Eöt-Wash/HUST row remains MEASURED, but the ledger gate as a whole still fails closed because mutant M3 survives (7/8 killed).",
      laxNoteEs: "Esta fila replicada sigue siendo MEDIDA, pero la compuerta global falla en cerrado porque sobrevive el mutante M3 (7/8 eliminados).",
    },
  };

  function render() {
    const isEs = lang() === "es";
    const c = CASES[activeCase] || CASES.derived_recast;
    if (badgeEl) badgeEl.textContent = laxMode ? (isEs ? c.laxEs : c.laxEn) : (isEs ? c.badgeEs : c.badgeEn);
    if (parentEl) parentEl.textContent = isEs ? c.parentEs : c.parentEn;
    if (mutantEl) mutantEl.textContent = laxMode ? (isEs ? "7/8 eliminados · M3 sobrevive (FALLO)" : "7/8 killed · M3 survives (FAIL)") : (isEs ? "8/8 mutantes eliminados (PASA)" : "8/8 mutants killed (PASS)");
    if (hiNode) hiNode.setAttribute("y", String(c.y - 26));
    if (statusEl) {
      statusEl.textContent = laxMode ? (isEs ? c.laxNoteEs : c.laxNoteEn) : (isEs ? c.noteEs : c.noteEn);
      statusEl.setAttribute("data-state", laxMode ? "defect" : "pass");
    }
  }

  modeSel.forEach((btn) => {
    btn.addEventListener("click", () => {
      activeCase = btn.getAttribute("data-ep-case");
      modeSel.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      render();
    });
  });
  if (koBtn) {
    koBtn.addEventListener("click", () => {
      laxMode = !laxMode;
      koBtn.setAttribute("aria-pressed", String(laxMode));
      render();
    });
  }
  window.addEventListener("tp-lang-change", render);
  root.setAttribute("data-cs-ready", "true");
  render();
}

function initTurPores(root) {
  const affInput = root.querySelector('[data-cs-input="affinity"]');
  const statesInput = root.querySelector('[data-cs-input="states"]');
  const ddgInput = root.querySelector('[data-cs-input="ddg"]');
  const koBtn = root.querySelector("[data-cs-knockout]");
  const statusEl = root.querySelector("[data-cs-status]");
  const marker = root.querySelector("[data-tur-point]");
  const reads = {};
  root.querySelectorAll("[data-cs-read]").forEach((el) => { reads[el.getAttribute("data-cs-read")] = el; });
  let knockout = false;

  const MSG = {
    en: {
      ok: "Classical Markovian steady state: Q_TUR = (Var(N)/⟨N⟩²)·(ΔS/k_B) ≥ 2 holds everywhere on and above the bound; lowering a Kramers barrier by ΔΔG‡ multiplies escape/folding rate by exp(ΔΔG‡/k_BT).",
      ko: "Planted-defect knockout: sets thermodynamic affinity A → 0 while claiming directed clock ticks below the 2 k_B floor—a perpetuum-mobile clock rejected by the verifier.",
    },
    es: {
      ok: "Estado estacionario markoviano clásico: Q_TUR = (Var(N)/⟨N⟩²)·(ΔS/k_B) ≥ 2 se cumple siempre; reducir una barrera de Kramers en ΔΔG‡ multiplica la tasa por exp(ΔΔG‡/k_BT).",
      ko: "Apagado / defecto plantado: fija la afinidad termodinámica A → 0 pretendiendo pulsos dirigidos bajo el piso de 2 k_B, rechazado por el verificador.",
    },
  };

  function render() {
    const aff = Number(affInput ? affInput.value : 20);
    const nSt = Number(statesInput ? statesInput.value : 4);
    const ddg = Number(ddgInput ? ddgInput.value : 3.0);

    const aPerStep = Math.max(0.05, aff / nSt);
    const coth = 1 / Math.tanh(0.5 * aPerStep);
    const qTur = knockout ? 0.85 : aPerStep * coth;
    const relVarPerTick = (1 / nSt) * coth;
    const kramersBoost = Math.exp(ddg);

    const isEs = lang() === "es";
    if (reads.affinity) reads.affinity.textContent = `${aff.toFixed(1)} k_B T`;
    if (reads.states) reads.states.textContent = `${nSt}`;
    if (reads.ddg) reads.ddg.textContent = `${ddg.toFixed(1)} k_B T`;
    if (reads.qtur) {
      const okTxt = isEs ? "≥ 2 (PASA)" : "≥ 2 (PASS)";
      const koTxt = isEs ? "< 2 (DEFECTO)" : "< 2 (DEFECT)";
      reads.qtur.textContent = `${qTur.toFixed(3)} ${qTur >= 2.0 ? okTxt : koTxt}`;
    }
    if (reads.relvar) reads.relvar.textContent = relVarPerTick.toFixed(3);
    if (reads.boost) reads.boost.textContent = `${kramersBoost.toFixed(1)}×`;

    if (marker) {
      const x = 70 + Math.min(1, aff / 40) * 340;
      const y = knockout ? 238 : Math.max(55, 210 - Math.min(145, (qTur - 2.0) * 16));
      marker.setAttribute("cx", x.toFixed(1));
      marker.setAttribute("cy", y.toFixed(1));
    }

    if (statusEl) {
      const L = MSG[lang()];
      statusEl.textContent = knockout ? L.ko : L.ok;
      statusEl.setAttribute("data-state", knockout ? "defect" : "pass");
    }
  }

  [affInput, statesInput, ddgInput].forEach((el) => { if (el) el.addEventListener("input", render); });
  if (koBtn) {
    koBtn.addEventListener("click", () => {
      knockout = !knockout;
      koBtn.setAttribute("aria-pressed", String(knockout));
      render();
    });
  }
  window.addEventListener("tp-lang-change", render);
  root.setAttribute("data-cs-ready", "true");
  render();
}

export function initCrossScaleEssays(scope = document) {
  const once = (sel, fn) => scope.querySelectorAll(sel).forEach((el) => {
    if (!el.hasAttribute("data-cs-ready")) fn(el);
  });
  once("[data-cs-predict]", initPredict);
  once('[data-cs-instrument="mesoscopic"]', initMesoscopic);
  once('[data-cs-instrument="epistemic"]', initEpistemic);
  once('[data-cs-instrument="tur_pores"]', initTurPores);
}

initCrossScaleEssays(document);
