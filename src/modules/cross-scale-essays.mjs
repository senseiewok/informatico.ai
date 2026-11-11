/**
 * @module cross-scale-essays
 * Zero-dependency interactive instruments for the 6 Informatico.ai Cross-Scale Featured Essays (/essays/):
 *  - [data-cs-instrument="mesoscopic"]  (ES.01): Fluctuation-dissipation, short-wavelength gas saturation vs R^6 T^9
 *    black-body photon localization in ultra-high vacuum (0.15–4 K), paired with Stokes-Einstein & Ogston-Amsden
 *    hindered nanoparticle diffusion in aqueous hydrogels (310.15 K).
 *  - [data-cs-instrument="epistemic"]   (ES.02): Six-tier Epistemic Lattice & 8-mutant falsification inspector comparing
 *    tabletop quantum-gravity deductions (DERIVED (NOT MEASURED)) with Cryo-EM structural gaps (UNRESOLVED vs DELETED).
 *  - [data-cs-instrument="tur_pores"]   (ES.03): Barato-Seifert Thermodynamic Uncertainty Relation (Q_TUR >= 2) on a
 *    biased Markovian clock/gating ring paired with Brinkman porous screening & Kramers barrier escape.
 *  - [data-cs-instrument="kinematic"]   (ES.04): Maxwell-Calladine rank-nullity rigidity vs su(4) microcausality normalizer.
 *  - [data-cs-instrument="island_page"] (ES.05): Unitary QES saddle switch vs subalgebra coarse-graining vs Doob h-transform.
 *  - [data-cs-instrument="wdw_clock"]   (ES.06): 64x64 Page-Wootters clock/branch conditioner & bilateral CPMG parity filter.
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

function initKinematic(root) {
  const bracesInput = root.querySelector('[data-cs-input="braces"]');
  const pinInput = root.querySelector('[data-cs-input="pinrank"]');
  const koBtn = root.querySelector("[data-cs-knockout]");
  const statusEl = root.querySelector("[data-cs-status]");
  const barTruss = root.querySelector('[data-cs-bar="truss"]');
  const barSu4 = root.querySelector('[data-cs-bar="su4"]');
  const barDrift = root.querySelector('[data-cs-bar="drift"]');
  const reads = {};
  root.querySelectorAll("[data-cs-read]").forEach((el) => { reads[el.getAttribute("data-cs-read")] = el; });
  let knockout = false;

  const MSG = {
    en: {
      ok: "Rank–nullity locked: 6 diagonal braces collapse all 6 shear zero-modes of a cubic space frame (18 − 18 = 0), while 9 spatial microcausality commutators [A_A, A_B] = 0 restrict su(4) (dim 15) to su(2)_A ⊕ su(2)_B (dim 6), keeping BMV negativity N = 0.078 gauge-invariant.",
      ko: "Non-local refactorization defect active: unlocks Cartan–Weyl σ_i ⊗ σ_j rotations in su(4) across spacelike-separated arms, allowing arbitrary entanglement drift ΔN = 0.422—violating spatial microcausality.",
    },
    es: {
      ok: "Rango-nulidad bloqueado: 6 diagonales eliminan los 6 modos blandos de corte en una celosía cúbica (18 − 18 = 0), mientras 9 conmutadores de microcausalidad [A_A, A_B] = 0 restringen su(4) (dim 15) a su(2)_A ⊕ su(2)_B (dim 6), fijando la negatividad BMV N = 0.078.",
      ko: "Defecto de refactorización no local activo: desbloquea generadores Cartan–Weyl σ_i ⊗ σ_j en su(4) entre brazos espacialmente separados, induciendo una deriva ΔN = 0.422 que viola la microcausalidad.",
    },
  };

  function render() {
    const braces = Number(bracesInput ? bracesInput.value : 6);
    const pinRank = knockout ? 0 : Number(pinInput ? pinInput.value : 9);
    const isEs = lang() === "es";

    const nFloppyTruss = Math.max(0, 6 - braces);
    const nSelfStress = Math.max(0, braces - 6);
    const nNonlocalZero = 9 - pinRank;
    const gaugeDrift = nNonlocalZero === 0 ? 0.0 : Number((0.0469 * nNonlocalZero).toFixed(3));

    if (reads.braces) reads.braces.textContent = `${braces} / 6`;
    if (reads.pinrank) reads.pinrank.textContent = `${pinRank} / 9`;
    if (reads.trussmodes) {
      reads.trussmodes.textContent = isEs
        ? `${nFloppyTruss} blandos · ${nSelfStress} autotensión`
        : `${nFloppyTruss} floppy · ${nSelfStress} self-stress`;
    }
    if (reads.su4modes) {
      reads.su4modes.textContent = isEs
        ? `${nNonlocalZero} no locales libres (núcleo local = 6)`
        : `${nNonlocalZero} free non-local (local kernel = 6)`;
    }
    if (reads.bmvdrift) {
      reads.bmvdrift.textContent = nNonlocalZero === 0
        ? (isEs ? "ΔN = 0.000 (N = 0.078 invariante)" : "ΔN = 0.000 (N = 0.078 invariant)")
        : (isEs ? `ΔN = ${gaugeDrift.toFixed(3)} (ambiguo)` : `ΔN = ${gaugeDrift.toFixed(3)} (ambiguous)`);
    }

    if (barTruss) barTruss.setAttribute("width", Math.max(8, (nFloppyTruss / 6) * 230).toFixed(1));
    if (barSu4) barSu4.setAttribute("width", Math.max(8, (nNonlocalZero / 9) * 230).toFixed(1));
    if (barDrift) barDrift.setAttribute("width", Math.max(8, (gaugeDrift / 0.43) * 230).toFixed(1));

    if (statusEl) {
      const L = MSG[lang()];
      if (knockout) {
        statusEl.textContent = L.ko;
        statusEl.setAttribute("data-state", "defect");
      } else if (nFloppyTruss > 0 || nNonlocalZero > 0) {
        statusEl.textContent = isEs
          ? `Restricción parcial activa: ${nFloppyTruss} modos blandos mecánicos (${braces}/6 diagonales) y ${nNonlocalZero} generadores no locales libres en su(4) (${pinRank}/9 conmutadores [A_A, A_B] = 0; deriva ΔN = ${gaugeDrift.toFixed(3)}).`
          : `Under-constrained regime active: ${nFloppyTruss} mechanical floppy modes (${braces}/6 diagonal braces) and ${nNonlocalZero} free non-local su(4) generators (${pinRank}/9 [A_A, A_B] = 0 commutators; BMV drift ΔN = ${gaugeDrift.toFixed(3)}).`;
        statusEl.setAttribute("data-state", "defect");
      } else {
        statusEl.textContent = L.ok;
        statusEl.setAttribute("data-state", "pass");
      }
    }
  }

  [bracesInput, pinInput].forEach((el) => { if (el) el.addEventListener("input", render); });
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

function initIslandPage(root) {
  const stepInput = root.querySelector('[data-cs-input="stepk"]');
  const hazInput = root.querySelector('[data-cs-input="hazard"]');
  const modeBtns = root.querySelectorAll("button[data-ip-mode]");
  const koBtn = root.querySelector("[data-cs-knockout]");
  const statusEl = root.querySelector("[data-cs-status]");
  const ptEl = root.querySelector("[data-ip-point]");
  const reads = {};
  root.querySelectorAll("[data-cs-read]").forEach((el) => { reads[el.getAttribute("data-cs-read")] = el; });
  let mode = "qes_unitary";
  let knockout = false;

  const LN2 = Math.LN2;
  const MSG = {
    en: {
      qes_unitary: "Regime 1 (Unitary QES Saddle Switch, DERIVED model): S_gen(k) = min(k, 6−k) ln 2 nats crosses from the empty Hawking saddle to the interior Island saddle at k = 3 and returns to 0 nats at k = 6 with zero discarded runs (V_Doob = 0 nats).",
      blinder_cptp: "Regime 2 (Subalgebra Coarse-Graining / 'Blinders', PROPOSED arXiv:2602.06543): trace-preserving CPTP restriction omitting asymptotic gravitational dressing (0% discarded runs, V_Doob = 0 nats); global purity holds, but undressed radiation entropy climbs as k ln 2.",
      doob_postselect: "Regime 3 (Doob h-Transform Conditional Survival, DERIVED theorem): conditioning an absorbing barrier chain on survival tilts transitions with zero post-selected variance at the terminal boundary ONLY by discarding 1 − (1−γ)⁶ of trajectories (V_Doob = −6 ln(1−γ) nats).",
      ko: "Ensemble-conflation defect active: omits the interior Island saddle while falsely equating path-space KL post-selection discard cost with fine-grained von Neumann radiation entropy.",
    },
    es: {
      qes_unitary: "Régimen 1 (Cambio de Silla QES Unitario, modelo DERIVADO): S_gen(k) = mín(k, 6−k) ln 2 nats cruza de la silla de Hawking a la silla de Isla en k = 3 y vuelve a 0 nats en k = 6 sin descartar corridas (V_Doob = 0 nats).",
      blinder_cptp: "Régimen 2 (Grano Grueso de Subálgebra / 'Anteojeras', PROPUESTO arXiv:2602.06543): restricción CPTP que conserva la traza omitiendo el vestido gravitatorio (0 % descartado, V_Doob = 0 nats); la entropía restringida sube como k ln 2.",
      doob_postselect: "Régimen 3 (Transformada h de Doob, teorema DERIVADO): condicionar una cadena absorbente a sobrevivir alcanza el borde final solo descartando 1 − (1−γ)⁶ de las trayectorias con costo KL exacto V_Doob = −6 ln(1−γ) nats.",
      ko: "Defecto de confusión de ensambles activo: omite la silla interior de Isla e iguala falsamente el costo KL de postselección en espacio de trayectorias con la entropía fina de von Neumann.",
    },
  };

  function render() {
    const k = Number(stepInput ? stepInput.value : 3);
    const gamma = Number(hazInput ? hazInput.value : 0.25);
    const isEs = lang() === "es";

    let sNats = Math.min(k, 6 - k) * LN2;
    let vDoob = 0.0;
    let discardPct = 0.0;

    if (knockout) {
      sNats = k * LN2;
      vDoob = -6 * Math.log(1 - gamma);
      discardPct = (1 - ((1 - gamma) ** 6)) * 100;
    } else if (mode === "blinder_cptp") {
      sNats = k * LN2;
      vDoob = 0.0;
      discardPct = 0.0;
    } else if (mode === "doob_postselect") {
      sNats = Math.min(k, 6 - k) * LN2;
      vDoob = -6 * Math.log(1 - gamma);
      discardPct = (1 - ((1 - gamma) ** 6)) * 100;
    }

    if (reads.stepk) reads.stepk.textContent = `k = ${k} / 6`;
    if (reads.hazard) reads.hazard.textContent = `γ = ${gamma.toFixed(2)}`;
    if (reads.snats) reads.snats.textContent = `${sNats.toFixed(3)} nats`;
    if (reads.vdoob) reads.vdoob.textContent = `${vDoob.toFixed(3)} nats`;
    if (reads.discard) reads.discard.textContent = isEs ? `${discardPct.toFixed(1)} % descartado` : `${discardPct.toFixed(1)}% discarded`;

    if (ptEl) {
      // x maps k in [0..6] -> [64..496], y maps sNats in [0..6*ln2=4.159] -> [224..44]
      const cx = 64 + (k / 6) * 432;
      const cy = 224 - (sNats / (6 * LN2)) * 180;
      ptEl.setAttribute("cx", cx.toFixed(1));
      ptEl.setAttribute("cy", cy.toFixed(1));
    }

    if (statusEl) {
      const L = MSG[lang()];
      statusEl.textContent = knockout ? L.ko : L[mode];
      statusEl.setAttribute("data-state", knockout ? "defect" : "pass");
    }
  }

  [stepInput, hazInput].forEach((el) => { if (el) el.addEventListener("input", render); });
  modeBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      mode = btn.getAttribute("data-ip-mode") || "qes_unitary";
      knockout = false;
      if (koBtn) koBtn.setAttribute("aria-pressed", "false");
      modeBtns.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      render();
    });
  });
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

function initWdwClock(root) {
  const tickInput = root.querySelector('[data-cs-input="tickn"]');
  const nddInput = root.querySelector('[data-cs-input="ndd"]');
  const echoBtns = root.querySelectorAll("button[data-wdw-echo]");
  const koBtn = root.querySelector("[data-cs-knockout]");
  const statusEl = root.querySelector("[data-cs-status]");
  const barVis = root.querySelector('[data-cs-bar="vis"]');
  const barNegQ = root.querySelector('[data-cs-bar="negq"]');
  const barNegH = root.querySelector('[data-cs-bar="negh"]');
  const reads = {};
  root.querySelectorAll("[data-cs-read]").forEach((el) => { reads[el.getAttribute("data-cs-read")] = el; });
  let echoMode = "bilateral";
  let knockout = false;

  const MSG = {
    en: {
      bilateral: "Timeless kernel ker(C) verified (||C|Ψ⟩⟩|| < 10⁻¹³): conditioning on |t_n⟩ yields Zych–Brukner proper-time beats (η = 0), while synchronous bilateral X_A ⊗ X_B pulses preserve (−Z_A)(−Z_B) = +Z_A Z_B gravitational entanglement under 1/f stray gradients and σ ≤ 33 µm excludes hybrid entanglement.",
      unilateral: "Unilateral X_A ⊗ I echo warning: flipping arm A alone sends Z_A Z_B → −Z_A Z_B midway through the hold, refocusing the gravitational cross-phase itself to zero (N_quantum = 0.000) alongside local gradient noise!",
      ko: "Retired-bound / Markovian-echo defect active: substitutes the superseded 44.07 µm single-gap edge match for the 33 µm recast and falsely applies 1/N_dd² CPMG suppression to memoryless white Lindblad noise.",
    },
    es: {
      bilateral: "Núcleo atemporal ker(C) verificado (||C|Ψ⟩⟩|| < 10⁻¹³): condicionar en |t_n⟩ extrae el batido de tiempo propio de Zych–Brukner (η = 0), mientras pulsos bilaterales síncronos X_A ⊗ X_B preservan (−Z_A)(−Z_B) = +Z_A Z_B ante gradientes 1/f y σ ≤ 33 µm excluye al canal híbrido.",
      unilateral: "Advertencia de eco unilateral X_A ⊗ I: invertir solo el brazo A envía Z_A Z_B → −Z_A Z_B a mitad de espera, cancelando la propia fase gravitatoria a cero (N_cuántico = 0.000) junto con el ruido local.",
      ko: "Defecto de cota retirada / ruido blanco activo: sustituye el recast de 33 µm por el antiguo ajuste de 44.07 µm y aplica falsamente supresión 1/N_dd² a ruido blanco markoviano sin memoria.",
    },
  };

  function render() {
    const nTick = Number(tickInput ? tickInput.value : 4);
    const nDd = Number(nddInput ? nddInput.value : 4);
    const isEs = lang() === "es";

    const tn = (2 * Math.PI * nTick) / 16.0;
    // Integer-mode bandwidth-scaled model [-3, -1, 1, 5] -> deltaOmega = (5 - 1) - (-1 - (-3)) = 2
    const deltaOmega = 2.0;
    const vis = Math.abs(Math.cos(0.5 * deltaOmega * tn));
    // Low-frequency gradient noise gamma_0 = 0.012 s^-1 vs Schut 2024 threshold 0.00983 s^-1
    const gammaEff = 0.012 / (nDd * nDd);
    let negQ = Math.max(0, 0.402 * Math.exp(-2.0 * gammaEff * 52.0) - 0.015);
    if (echoMode === "unilateral") negQ = 0.0;
    const negHyb = knockout ? 0.064 : 0.0;
    const sigmaBoundTxt = knockout
      ? (isEs ? "44.1 µm (DEFECTO)" : "44.1 µm (DEFECT)")
      : (isEs ? "33 µm (95 % NC)" : "33 µm (95% CL)");

    if (reads.tickn) reads.tickn.textContent = `n = ${nTick} (t_n = ${(tn / Math.PI).toFixed(2)}π)`;
    if (reads.ndd) reads.ndd.textContent = `N_dd = ${nDd} (γ_eff = ${gammaEff.toExponential(2)} s⁻¹)`;
    if (reads.vis) reads.vis.textContent = `V(t_n) = ${vis.toFixed(3)} · η = 0`;
    if (reads.negq) reads.negq.textContent = `N_Q = ${negQ.toFixed(3)}`;
    if (reads.negh) {
      reads.negh.textContent = knockout
        ? (isEs ? `N_hyb = ${negHyb.toFixed(3)} (${sigmaBoundTxt})` : `N_hyb = ${negHyb.toFixed(3)} (${sigmaBoundTxt})`)
        : (isEs ? "N_hyb = 0.000 (σ ≤ 33 µm excluido)" : "N_hyb = 0.000 (σ ≤ 33 µm excluded)");
    }

    if (barVis) barVis.setAttribute("width", Math.max(8, vis * 230).toFixed(1));
    if (barNegQ) barNegQ.setAttribute("width", Math.max(8, (negQ / 0.42) * 230).toFixed(1));
    if (barNegH) barNegH.setAttribute("width", Math.max(8, (negHyb / 0.42) * 230).toFixed(1));

    if (statusEl) {
      const L = MSG[lang()];
      statusEl.textContent = knockout ? L.ko : L[echoMode];
      statusEl.setAttribute("data-state", (knockout || echoMode === "unilateral") ? "defect" : "pass");
    }
  }

  [tickInput, nddInput].forEach((el) => { if (el) el.addEventListener("input", render); });
  echoBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      echoMode = btn.getAttribute("data-wdw-echo") || "bilateral";
      knockout = false;
      if (koBtn) koBtn.setAttribute("aria-pressed", "false");
      echoBtns.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      render();
    });
  });
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

function erfApprox(x) {
  const s = x < 0 ? -1 : 1;
  const ax = Math.abs(x);
  const t = 1.0 / (1.0 + 0.3275911 * ax);
  const poly = (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t;
  return s * (1.0 - poly * Math.exp(-ax * ax));
}

function smearedF(r, sigma) {
  if (r <= 1e-15) return 1.0 / (sigma * Math.sqrt(Math.PI));
  return erfApprox(r / (2.0 * sigma)) / r;
}

function parallelHybridNegClosed(splitM, gapM, massKg, sigmaM, tS, thetaRad) {
  const ct = Math.cos(thetaRad);
  if (Math.abs(ct) < 1e-14) return 0.0;
  const rSame = Math.sqrt(gapM * gapM + 0.5 * splitM * splitM * (1.0 - ct));
  const rDiff = Math.sqrt(gapM * gapM + 0.5 * splitM * splitM * (1.0 + ct));
  const a = smearedF(0.0, sigmaM) - smearedF(splitM, sigmaM);
  const b = Math.abs(smearedF(rSame, sigmaM) - smearedF(rDiff, sigmaM));
  const tau = (6.67430e-11 * massKg * massKg * tS) / (2.0 * HBAR);
  const eMinus = Math.exp(-Math.max(0.0, 4.0 * (a - b) * tau));
  const ePlus = Math.exp(-4.0 * (a + b) * tau);
  const uPlus = 0.5 * (eMinus + ePlus);
  const uMinus = 0.5 * (eMinus - ePlus);
  const s = Math.sin(2.0 * b * tau);
  const rad = Math.sqrt(uMinus * uMinus + 4.0 * Math.exp(-4.0 * a * tau) * s * s);
  return Math.max(0.0, 0.25 * (uPlus + rad - 1.0));
}

function parallelCriticalSigmaM(splitM, gapM, thetaRad) {
  const ct = Math.cos(thetaRad);
  if (Math.abs(ct) < 1e-14) return Infinity;
  let lo = 1e-8;
  let hi = 2e-2;
  for (let i = 0; i < 60; i += 1) {
    const mid = 0.5 * (lo + hi);
    const rSame = Math.sqrt(gapM * gapM + 0.5 * splitM * splitM * (1.0 - ct));
    const rDiff = Math.sqrt(gapM * gapM + 0.5 * splitM * splitM * (1.0 + ct));
    const a = smearedF(0.0, mid) - smearedF(splitM, mid);
    const b = Math.abs(smearedF(rSame, mid) - smearedF(rDiff, mid));
    if (Math.SQRT2 * b > a) hi = mid;
    else lo = mid;
  }
  return 0.5 * (lo + hi);
}

function initParallelHorizon(root) {
  const gapInput = root.querySelector('[data-cs-input="gap"]');
  const splitInput = root.querySelector('[data-cs-input="split"]');
  const tempInput = root.querySelector('[data-cs-input="temp"]');
  const thetaBtns = root.querySelectorAll("button[data-ph-theta]");
  const ensBtns = root.querySelectorAll("button[data-ph-ens]");
  const koBtn = root.querySelector("[data-cs-knockout]");
  const statusEl = root.querySelector("[data-cs-status]");
  const barSigma = root.querySelector('[data-cs-bar="sigmac"]');
  const barNegQ = root.querySelector('[data-cs-bar="negq"]');
  const barNegH = root.querySelector('[data-cs-bar="negh"]');
  const reads = {};
  root.querySelectorAll("[data-cs-read]").forEach((el) => { reads[el.getAttribute("data-cs-read")] = el; });
  let thetaDeg = 0;
  let ensMode = "isobaric";
  let knockout = false;

  const SIGMA_95_UM = 33.08;
  const MASS_KG = 1.0e-14;
  const HOLD_S = 2.5;
  // Exact 1 K benchmark prefactors from timegravity_kernel_decoherence at P = 2.7e-16 Pa, dx = 250 um, m = 10^-14 kg
  const A_GAS_1K = 0.0290064;
  const B_EM_1K = 2.32101e-5;
  const B_SC_1K = 2.14194e-8;

  const MSG = {
    en: {
      island: "Loophole-free quantum island verified: σ_c(D, Δx, θ) > 33.08 µm forces classical-hybrid negativity N_hyb(t) = 0 identically for all hold times t ≥ 0, while the unitary Newtonian channel retains strong macroscopic negativity N_Q.",
      leak: "Hybrid leakage warning: at this (D, Δx, θ) geometry, σ_c < 33.08 µm! Even when D > 51.18 µm (such as D = 60 µm at Δx = 250 µm), Diósi–Penrose smeared gravity still produces a positive classical negativity pulse before self-decohering.",
      null90: "Midpoint '+' orthogonal null control (θ = 90°): r_same = r_diff = √(D² + ½Δx²) exactly, cancelling Newtonian, Yukawa, and erf-smeared pair potentials to every multipole order while keeping apparatus, lasers, and screen unchanged.",
      ko: "Naive small-split / uncentred-corner defect active: falsely extrapolates the 51.18 µm small-split horizon to large splits (hiding the D = 60 µm leak) and rotates 90° about an endpoint ('L' corner), creating a spurious multipole phase!",
    },
    es: {
      island: "Isla cuántica sin resquicios verificada: σ_c(D, Δx, θ) > 33.08 µm fuerza N_hyb(t) = 0 idénticamente para todo t ≥ 0, mientras el canal newtoniano unitario preserva una fuerte negatividad macroscópica N_Q.",
      leak: "Advertencia de fuga híbrida: en esta geometría (D, Δx, θ) resulta σ_c < 33.08 µm. Aun con D > 51.18 µm (como D = 60 µm con Δx = 250 µm), la gravedad difuminada genera un pulso positivo de negatividad clásica.",
      null90: "Control nulo ortogonal centrado '+' (θ = 90°): r_same = r_diff = √(D² + ½Δx²) de forma exacta, anulando potenciales newtonianos, de Yukawa y erf en todo orden multipolar sin alterar láseres ni pantalla.",
      ko: "Defecto de extrapolación corta / esquina 'L' activo: extrapola falsamente el umbral de 51.18 µm a divisiones grandes (ocultando la fuga en D = 60 µm) y gira 90° sobre un extremo en 'L', induciendo una fase espuria.",
    },
  };

  function render() {
    const dUm = Number(gapInput ? gapInput.value : 75);
    const dxUm = Number(splitInput ? splitInput.value : 250);
    const tempK = Number(tempInput ? tempInput.value : 2.0);
    const isEs = lang() === "es";

    const dM = dUm * 1e-6;
    const dxM = dxUm * 1e-6;
    const thRad = (thetaDeg * Math.PI) / 180.0;

    let sigmaCUm = parallelCriticalSigmaM(dxM, dM, thRad) * 1e6;
    if (knockout && thetaDeg !== 90) {
      sigmaCUm = dUm / 1.547134;
    }

    const dxRatio = (dxUm / 250.0) * (dxUm / 250.0);
    const gammaPhot = (B_EM_1K * Math.pow(tempK, 6) + B_SC_1K * Math.pow(tempK, 9)) * dxRatio;
    const gammaGas = ensMode === "isobaric"
      ? A_GAS_1K * Math.pow(tempK, -0.5)
      : A_GAS_1K * Math.pow(tempK, 0.5);
    const gammaTot = gammaGas + gammaPhot;

    let dPhi = 0.0;
    if (thetaDeg === 90 && knockout) {
      const rLL = dM;
      const rLR = Math.hypot(dM, dxM);
      const rRR = Math.sqrt(dM * dM + 2.0 * dxM * dxM);
      dPhi = ((6.67430e-11 * MASS_KG * MASS_KG * HOLD_S) / HBAR) * Math.abs((2.0 / rLR) - (1.0 / rLL) - (1.0 / rRR));
    } else if (thetaDeg !== 90) {
      const ct = Math.cos(thRad);
      const rSame = Math.sqrt(dM * dM + 0.5 * dxM * dxM * (1.0 - ct));
      const rDiff = Math.sqrt(dM * dM + 0.5 * dxM * dxM * (1.0 + ct));
      dPhi = ((6.67430e-11 * MASS_KG * MASS_KG * HOLD_S) / HBAR) * 2.0 * Math.abs((1.0 / rSame) - (1.0 / rDiff));
    }

    const eta = Math.exp(-gammaTot * HOLD_S);
    const negQ = Math.max(0.0, 0.25 * (eta * eta + 2.0 * eta * Math.abs(Math.sin(0.5 * dPhi)) - 1.0));

    let negHybMax = 0.0;
    if (!knockout && Number.isFinite(sigmaCUm) && sigmaCUm < SIGMA_95_UM) {
      for (let k = -20; k <= 32; k += 1) {
        const tProbe = Math.pow(10.0, k / 16.0);
        const nh = parallelHybridNegClosed(dxM, dM, MASS_KG, SIGMA_95_UM * 1e-6, tProbe, thRad);
        if (nh > negHybMax) negHybMax = nh;
      }
    }

    if (reads.gap) {
      const tag = dUm >= 73.14
        ? (isEs ? "Isla ≥ 73.14 µm" : "Island ≥ 73.14 µm")
        : (isEs ? "Bajo techo 73.14 µm" : "Below 73.14 µm ceiling");
      reads.gap.textContent = `D = ${dUm} µm (${tag})`;
    }
    if (reads.split) reads.split.textContent = `Δx = ${dxUm} µm`;
    if (reads.temp) reads.temp.textContent = `T = ${tempK.toFixed(1)} K (γ = ${gammaTot.toExponential(2)} s⁻¹)`;

    if (reads.sigmac) {
      if (!Number.isFinite(sigmaCUm)) {
        reads.sigmac.textContent = isEs ? "σ_c = ∞ (Nulo exacto 90°)" : "σ_c = ∞ (Exact 90° Null)";
      } else {
        const cmp = sigmaCUm > SIGMA_95_UM ? ">" : "<";
        reads.sigmac.textContent = `σ_c = ${sigmaCUm.toFixed(2)} µm ${cmp} 33.08 µm`;
      }
    }
    if (reads.negq) reads.negq.textContent = `N_Q = ${negQ.toFixed(3)} · Δφ = ${dPhi.toFixed(2)} rad`;
    if (reads.negh) {
      reads.negh.textContent = negHybMax > 0
        ? (isEs ? `N_hyb = ${negHybMax.toFixed(4)} (Fuga Clásica)` : `N_hyb = ${negHybMax.toFixed(4)} (Classical Leak)`)
        : (isEs ? "N_hyb = 0.0000 (Clásicamente Oscuro)" : "N_hyb = 0.0000 (Classically Dark)");
    }

    const sigBarFrac = !Number.isFinite(sigmaCUm) ? 1.0 : Math.min(1.0, sigmaCUm / 60.0);
    if (barSigma) barSigma.setAttribute("width", Math.max(8, sigBarFrac * 230).toFixed(1));
    if (barNegQ) barNegQ.setAttribute("width", Math.max(8, (negQ / 0.50) * 230).toFixed(1));
    if (barNegH) barNegH.setAttribute("width", Math.max(8, Math.min(1.0, negHybMax * 18.0) * 230).toFixed(1));

    if (statusEl) {
      const L = MSG[lang()];
      if (knockout) {
        statusEl.textContent = L.ko;
        statusEl.setAttribute("data-state", "defect");
      } else if (thetaDeg === 90) {
        statusEl.textContent = L.null90;
        statusEl.setAttribute("data-state", "pass");
      } else if (sigmaCUm < SIGMA_95_UM) {
        statusEl.textContent = L.leak;
        statusEl.setAttribute("data-state", "defect");
      } else {
        statusEl.textContent = L.island;
        statusEl.setAttribute("data-state", "pass");
      }
    }
  }

  [gapInput, splitInput, tempInput].forEach((el) => { if (el) el.addEventListener("input", render); });
  thetaBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      thetaDeg = Number(btn.getAttribute("data-ph-theta") || 0);
      thetaBtns.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      render();
    });
  });
  ensBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      ensMode = btn.getAttribute("data-ph-ens") || "isobaric";
      ensBtns.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      render();
    });
  });
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

function erfcScaled(x) {
  if (x >= 0) {
    const t = 1.0 / (1.0 + 0.3275911 * x);
    return (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t;
  }
  return 2.0 * Math.exp(x * x) - erfcScaled(-x);
}

function sheetSmearedRatio(q, s, sigma) {
  if (sigma <= 0) return 1.0;
  const a = q * sigma;
  const b = s / (2.0 * sigma);
  const d1 = a - b;
  const d2 = a + b;
  const term1 = d1 >= 0 ? Math.exp(-d1 * d1) * erfcScaled(d1) : 1.0 - erfApprox(d1);
  const term2 = Math.exp(-d1 * d1) * erfcScaled(d2);
  return 0.5 * (term1 + term2);
}

function initSchurRecast(root) {
  const sigmaInput = root.querySelector('[data-cs-input="sigma"]');
  const sminInput = root.querySelector('[data-cs-input="smin"]');
  const weightBtns = root.querySelectorAll("button[data-sr-weight]");
  const projBtns = root.querySelectorAll("button[data-sr-proj]");
  const koBtn = root.querySelector("[data-cs-knockout]");
  const statusEl = root.querySelector("[data-cs-status]");
  const barRet = root.querySelector('[data-cs-bar="ret"]');
  const barAlign = root.querySelector('[data-cs-bar="align"]');
  const barGain = root.querySelector('[data-cs-bar="gain"]');
  const reads = {};
  root.querySelectorAll("[data-cs-read]").forEach((el) => { reads[el.getAttribute("data-cs-read")] = el; });
  let weightMode = "equal";
  let projMode = "schur";
  let knockout = false;

  // Compact 3-mode radial + 3x3 Gauss-Legendre thick-foil surrogate (t1 = 54 um, t2 = 99 um) matching the 120-fold Eot-Wash kernel
  const K_MODES = [
    [6000.0, 0.25],
    [7600.0, 0.48],
    [9800.0, 0.27],
  ];
  const GL3_U = [0.11270166537925831, 0.5, 0.8872983346207417];
  const GL3_W = [5.0 / 18.0, 8.0 / 18.0, 5.0 / 18.0];
  const T_DET = 54e-6;
  const T_ATT = 99e-6;
  // Lee (2020) Table 11.4 rows (lambda_um, alpha95_minus)
  const TABLE_ROWS = [
    [10.0, -520.0], [11.0, -232.0], [13.0, -63.5], [14.0, -37.3],
    [16.0, -15.2], [18.0, -7.36], [20.0, -4.02], [22.0, -2.41],
    [25.0, -1.27], [28.0, -0.886], [32.0, -0.507], [35.0, -0.36],
  ];

  function foilTorque(s, kind, paramM) {
    let sum = 0.0;
    for (let m = 0; m < K_MODES.length; m += 1) {
      const k = K_MODES[m][0];
      const wk = K_MODES[m][1];
      const kap = kind === "yukawa" ? Math.sqrt(k * k + 1.0 / (paramM * paramM)) : k;
      let zSum = 0.0;
      for (let i1 = 0; i1 < 3; i1 += 1) {
        const z1 = GL3_U[i1] * T_DET;
        for (let i2 = 0; i2 < 3; i2 += 1) {
          const sz = s + z1 + GL3_U[i2] * T_ATT;
          const wt = GL3_W[i1] * GL3_W[i2];
          if (kind === "newton") {
            zSum += wt * (Math.exp(-k * sz) / k);
          } else if (kind === "smeared") {
            zSum += wt * (Math.exp(-k * sz) / k) * sheetSmearedRatio(k, sz, paramM);
          } else {
            zSum += wt * (Math.exp(-kap * sz) / kap);
          }
        }
      }
      sum += wk * zSum;
    }
    return sum;
  }

  function mgsProject(vec, q1, q2, w) {
    let c1 = 0.0;
    let c2 = 0.0;
    for (let i = 0; i < vec.length; i += 1) {
      c1 += w[i] * q1[i] * vec[i];
      c2 += w[i] * q2[i] * vec[i];
    }
    return vec.map((x, i) => x - c1 * q1[i] - c2 * q2[i]);
  }

  function det3(r0, r1, r2) {
    return (
      r0[0] * (r1[1] * r2[2] - r1[2] * r2[1])
      - r0[1] * (r1[0] * r2[2] - r1[2] * r2[0])
      + r0[2] * (r1[0] * r2[1] - r1[1] * r2[0])
    );
  }

  function dOptimalMidUm(sMinM, sigmaM) {
    const nG = 25;
    const sMaxM = 3.0e-3;
    const ds = 0.25e-6;
    const grid = [];
    const rows = [];
    for (let i = 0; i < nG; i += 1) {
      const s = sMinM * Math.pow(sMaxM / sMinM, i / (nG - 1));
      grid.push(s);
      const tn = foilTorque(s, "newton", 0);
      const v2 = (sMinM * (foilTorque(s + ds, "newton", 0) - foilTorque(s - ds, "newton", 0))) / (2.0 * ds * tn);
      const d = 1.0 - foilTorque(s, "smeared", sigmaM) / tn;
      rows.push([1.0, v2, d]);
    }
    let bestDet = -1.0;
    let bestMid = grid[7];
    for (let i1 = 1; i1 < nG - 1; i1 += 1) {
      const v = Math.abs(det3(rows[0], rows[i1], rows[nG - 1]));
      if (v > bestDet) {
        bestDet = v;
        bestMid = grid[i1];
      }
    }
    return Math.round(bestMid * 1e6);
  }

  function computeGrid(sMinM, sigmaM, wMode, useSchur) {
    const n = 12;
    const sMaxM = 3.0e-3;
    const seps = [];
    for (let i = 0; i < n; i += 1) {
      seps.push(sMinM * Math.pow(sMaxM / sMinM, i / (n - 1)));
    }
    const tN = seps.map((s) => foilTorque(s, "newton", 0));
    const w = wMode === "abs_torque" ? tN.map((t) => t * t) : seps.map(() => 1.0);
    const ds = 0.25e-6;
    const v1 = seps.map(() => 1.0);
    const v2 = seps.map((s, i) => (sMinM * (foilTorque(s + ds, "newton", 0) - foilTorque(s - ds, "newton", 0))) / (2.0 * ds * tN[i]));
    let n1 = 0.0;
    for (let i = 0; i < n; i += 1) n1 += w[i] * v1[i] * v1[i];
    n1 = Math.sqrt(Math.max(n1, 1e-300));
    const q1 = v1.map((x) => x / n1);
    let r12 = 0.0;
    for (let i = 0; i < n; i += 1) r12 += w[i] * q1[i] * v2[i];
    const u2 = v2.map((x, i) => x - r12 * q1[i]);
    let n2 = 0.0;
    for (let i = 0; i < n; i += 1) n2 += w[i] * u2[i] * u2[i];
    n2 = Math.sqrt(Math.max(n2, 1e-300));
    const q2 = u2.map((x) => x / n2);

    const dRaw = seps.map((s, i) => 1.0 - foilTorque(s, "smeared", sigmaM) / tN[i]);
    const dPerp = mgsProject(dRaw, q1, q2, w);
    let rawSq = 0.0;
    let perpSq = 0.0;
    for (let i = 0; i < n; i += 1) {
      rawSq += w[i] * dRaw[i] * dRaw[i];
      perpSq += w[i] * dPerp[i] * dPerp[i];
    }
    const dUse = useSchur ? dPerp : dRaw;
    let best = null;
    for (let r = 0; r < TABLE_ROWS.length; r += 1) {
      const lamUm = TABLE_ROWS[r][0];
      const a95Minus = TABLE_ROWS[r][1];
      const yRaw = seps.map((s, i) => foilTorque(s, "yukawa", lamUm * 1e-6) / tN[i]);
      const yUse = useSchur ? mgsProject(yRaw, q1, q2, w) : yRaw;
      let den = 0.0;
      let dot = 0.0;
      let dNorm = 0.0;
      for (let i = 0; i < n; i += 1) {
        den += w[i] * yUse[i] * yUse[i];
        dot += w[i] * dUse[i] * yUse[i];
        dNorm += w[i] * dUse[i] * dUse[i];
      }
      const aEff = -dot / Math.max(den, 1e-300);
      let errSq = 0.0;
      for (let i = 0; i < n; i += 1) {
        const diff = dUse[i] + aEff * yUse[i];
        errSq += w[i] * diff * diff;
      }
      const resid = Math.sqrt(errSq / Math.max(dNorm, 1e-300));
      if (!best || resid < best.resid) {
        best = { lamUm, a95Minus, aEff, resid, cosTheta: Math.sqrt(Math.max(0.0, 1.0 - resid * resid)) };
      }
    }
    return { fisherRet: perpSq / Math.max(rawSq, 1e-300), normRet: Math.sqrt(perpSq / Math.max(rawSq, 1e-300)), perpSq, best };
  }

  const MSG = {
    en: {
      excluded: "Schur-complement exclusion verified: after projecting out floating calibration scale γ and separation offset s₀ via Modified Gram–Schmidt (P_⊥), the orthogonal smeared residual still aligns with Yukawa y_λ (cos θ_⊥ > 0.999) and violates α_95,−!",
      allowed: "Inside 95% allowed region: at this smaller smearing width σ, even the Schur-projected short-range deficit stays milder than Lee et al. (2020) Table 11.4 α_95,−; pushing s_min below 50 µm boosts Schur Fisher leverage sharply.",
      ko: "Nuisance-washout fallacy active: falsely assumes floating (γ, s₀) absorbs 100% of the Gaussian-smeared deficit without projecting onto P_⊥, hiding an excluded smearing width behind a rank-deficient algebra mistake!",
    },
    es: {
      excluded: "Exclusión por complemento de Schur verificada: tras proyectar la escala flotante γ y el desplazamiento s₀ mediante Gram–Schmidt modificado (P_⊥), el residuo ortogonal se alinea con Yukawa y_λ (cos θ_⊥ > 0.999) y viola α_95,−.",
      allowed: "Dentro de la región permitida al 95 %: para este ancho menor σ, incluso el déficit proyectado por Schur es más suave que α_95,− de la Tabla 11.4; reducir s_min bajo 50 µm multiplica la información de Fisher.",
      ko: "Falacia de borrado parásito activa: supone falsamente que (γ, s₀) absorben el 100 % del déficit gaussiano sin calcular P_⊥, ocultando un ancho excluido tras un error algebraico.",
    },
  };

  function render() {
    const sigmaUm = Number(sigmaInput ? sigmaInput.value : 33.0);
    const sMinUm = Number(sminInput ? sminInput.value : 52);
    const isEs = lang() === "es";

    const base52 = computeGrid(52e-6, sigmaUm * 1e-6, weightMode, projMode === "schur");
    const curS = computeGrid(sMinUm * 1e-6, sigmaUm * 1e-6, weightMode, true);
    const baseSchur52 = computeGrid(52e-6, sigmaUm * 1e-6, weightMode, true);
    const gain = curS.perpSq / Math.max(baseSchur52.perpSq, 1e-300);

    const fisherPct = knockout ? 0.0 : base52.fisherRet * 100.0;
    const normFrac = knockout ? 0.0 : base52.normRet;
    const best = base52.best;
    const aEff = knockout ? 0.0 : best.aEff;
    const cosTh = knockout ? 0.0 : best.cosTheta;
    const excluded = !knockout && aEff < best.a95Minus;
    const midSupportUm = dOptimalMidUm(sMinUm * 1e-6, sigmaUm * 1e-6);

    if (reads.sigma) reads.sigma.textContent = `σ = ${sigmaUm.toFixed(1)} µm (λ_mimic = ${best.lamUm.toFixed(1)} µm)`;
    if (reads.smin) {
      reads.smin.textContent = isEs
        ? `s_min = ${sMinUm} µm (soporte 3-pt: ${sMinUm}, ${midSupportUm}, 3000 µm)`
        : `s_min = ${sMinUm} µm (3-pt support: ${sMinUm}, ${midSupportUm}, 3000 µm)`;
    }
    if (reads.ret) {
      reads.ret.textContent = knockout
        ? (isEs ? "0.0% Fisher (DEFECTO DE BORRADO)" : "0.0% Fisher (WASHOUT DEFECT)")
        : `${fisherPct.toFixed(1)}% Fisher (||P_⊥d||/||d|| = ${normFrac.toFixed(3)})`;
    }
    if (reads.align) {
      const cmp = aEff < best.a95Minus ? "<" : "≥";
      reads.align.textContent = `cos θ_⊥ = ${cosTh.toFixed(4)} · α_eff = ${aEff.toFixed(2)} ${cmp} ${best.a95Minus}`;
    }
    if (reads.gain) {
      reads.gain.textContent = `${gain.toFixed(2)}× (max_s d(s) = 3.000 D-opt)`;
    }

    if (barRet) barRet.setAttribute("width", Math.max(8, (fisherPct / 100.0) * 230).toFixed(1));
    if (barAlign) barAlign.setAttribute("width", Math.max(8, cosTh * 230).toFixed(1));
    if (barGain) barGain.setAttribute("width", Math.max(20, Math.min(1.0, Math.log10(Math.max(1.0, gain)) / 1.25 + 0.1) * 230).toFixed(1));

    if (statusEl) {
      const L = MSG[lang()];
      if (knockout) {
        statusEl.textContent = L.ko;
        statusEl.setAttribute("data-state", "defect");
      } else if (excluded) {
        statusEl.textContent = L.excluded;
        statusEl.setAttribute("data-state", "pass");
      } else {
        statusEl.textContent = L.allowed;
        statusEl.setAttribute("data-state", "pass");
      }
    }
  }

  [sigmaInput, sminInput].forEach((el) => { if (el) el.addEventListener("input", render); });
  weightBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      weightMode = btn.getAttribute("data-sr-weight") || "equal";
      weightBtns.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      render();
    });
  });
  projBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      projMode = btn.getAttribute("data-sr-proj") || "schur";
      projBtns.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      render();
    });
  });
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

function initMultipartiteWitness(root) {
  const holdInput = root.querySelector('[data-cs-input="holdt"]');
  const tempInput = root.querySelector('[data-cs-input="temp"]');
  const chanBtns = root.querySelectorAll("button[data-mw-chan]");
  const compBtns = root.querySelectorAll("button[data-mw-comp]");
  const koBtn = root.querySelector("[data-cs-knockout]");
  const statusEl = root.querySelector("[data-cs-status]");
  const barMermin = root.querySelector('[data-cs-bar="mermin"]');
  const barComp = root.querySelector('[data-cs-bar="comp"]');
  const barClock = root.querySelector('[data-cs-bar="clock"]');
  const reads = {};
  root.querySelectorAll("[data-cs-read]").forEach((el) => { reads[el.getAttribute("data-cs-read")] = el; });
  let chanMode = "quantum";
  let compMode = "diamond";
  let knockout = false;

  const G = 6.67430e-11;
  const MASS_KG = 1.0e-14;
  const D_M = 75e-6;
  const DX_M = 250e-6;
  const SIGMA_95_M = 33.08e-6;
  const OMEGA_PAIR = ((2.0 * G * MASS_KG * MASS_KG) / HBAR) * ((1.0 / D_M) - (1.0 / Math.hypot(D_M, DX_M)));
  const A_GAS_1K = 0.0290064;
  const B_EM_1K = 2.32101e-5;
  const B_SC_1K = 2.14194e-8;
  const BISEP_BOUND = 2.0 * Math.SQRT2;

  const MSG = {
    en: {
      gte: "Genuine tripartite entanglement (GTE) verified: ⟨M₃(t)⟩ clears BOTH the local-hidden-variable ceiling (2.0) AND the Seevinck–Svetlichny biseparable ceiling (2√2 ≈ 2.828) without extra local rotation gates because cryogenic Z-pointer localization leaves Z_j undamped!",
      sub: "Below biseparable GTE ceiling (2√2 ≈ 2.828): adjust hold time toward t_π = 2.61 s or stay near the 2.04 K cryogenic valley so ⟨M₃(t)⟩ = η³ + (3/2)η(1 − cos Δφ) crosses 2.828.",
      hybrid: "3-body Diósi–Penrose hybrid channel at σ_95 = 33.08 µm: two-neighbour collective damping lowers the 1|23 critical width to σ_c^(1|23) = 34.93 µm > 33.08 µm, locking N_1|23^hyb = 0 identically and capping ⟨M₃⟩_hyb < 1.0!",
      ko: "Biseparable-conflation defect active: falsely claims genuine 3-body quantum gravity entanglement whenever ⟨M₃⟩ > 2.0, ignoring that a single 2-body Bell pair tensored with a separable third mass reaches ⟨M₃⟩ = 2√2 = 2.828!",
    },
    es: {
      gte: "Entrelazamiento genuino tripartito (GTE) verificado: ⟨M₃(t)⟩ supera TANTO el techo de variables ocultas locales (2.0) COMO el techo biseparable de Seevinck–Svetlichny (2√2 ≈ 2.828) porque la localización criogénica en Z deja a Z_j sin amortiguar.",
      sub: "Bajo el techo GTE biseparable (2√2 ≈ 2.828): acerca el tiempo de espera a t_π = 2.61 s o mantén el baño cerca del valle criogénico de 2.04 K para que ⟨M₃(t)⟩ = η³ + (3/2)η(1 − cos Δφ) supere 2.828.",
      hybrid: "Canal híbrido Diósi–Penrose de 3 cuerpos en σ_95 = 33.08 µm: el amortiguamiento colectivo de dos vecinos reduce el umbral crítico 1|23 a σ_c^(1|23) = 34.93 µm > 33.08 µm, fijando N_1|23^hyb = 0 y ⟨M₃⟩_hyb < 1.0.",
      ko: "Defecto de confusión biseparable activo: declara falsamente entrelazamiento genuino de 3 cuerpos apenas ⟨M₃⟩ > 2.0, ignorando que un solo par de Bell de 2 cuerpos alcanza ⟨M₃⟩ = 2√2 = 2.828.",
    },
  };

  function render() {
    const tHold = Number(holdInput ? holdInput.value : 2.61);
    const tempK = Number(tempInput ? tempInput.value : 2.0);
    const isEs = lang() === "es";

    // Density adjust for surface area R^2 when switching diamond (3500 kg/m^3) vs Yb (6900 kg/m^3) at fixed mass M
    const rhoScale = compMode === "yb173" ? Math.pow(3500.0 / 6900.0, 2.0 / 3.0) : 1.0;
    const gammaGas = A_GAS_1K * rhoScale * Math.pow(tempK, -0.5);
    const gammaPhot = (B_EM_1K * Math.pow(tempK, 6) + B_SC_1K * Math.pow(tempK, 9));
    const etaEnv = Math.exp(-(gammaGas + gammaPhot) * tHold);

    let dPhi = OMEGA_PAIR * tHold;
    let m3Val = 0.0;
    if (chanMode === "quantum") {
      m3Val = Math.pow(etaEnv, 3) + 1.5 * etaEnv * (1.0 - Math.cos(dPhi));
    } else {
      const a = smearedF(0.0, SIGMA_95_M) - smearedF(DX_M, SIGMA_95_M);
      const b = smearedF(D_M, SIGMA_95_M) - smearedF(Math.hypot(D_M, DX_M), SIGMA_95_M);
      const tau = (G * MASS_KG * MASS_KG * tHold) / (2.0 * HBAR);
      const phiHyb = 2.0 * b * tau;
      dPhi = phiHyb;
      const xxx = 0.25 * Math.pow(etaEnv, 3) * (
        Math.exp(-6.0 * (a + 2.0 * b) * tau) + 3.0 * Math.exp(-2.0 * (3.0 * a - 2.0 * b) * tau)
      );
      const xzzSum = 3.0 * etaEnv * Math.exp(-2.0 * a * tau) * Math.pow(Math.sin(phiHyb), 2);
      m3Val = xxx + xzzSum;
    }

    const ahAmpRatio = compMode === "yb173" ? Math.pow(173.04 / 12.0, 2) * Math.pow(3500.0 / 6900.0, 1.0 / 3.0) : 1.0;
    // Active optical Sr-like clock proper-time visibility benchmark (scaled coherent array parameter)
    const vClock = Math.abs(Math.cos(0.245 * tHold));

    if (reads.holdt) reads.holdt.textContent = `t = ${tHold.toFixed(2)} s (Δφ = ${dPhi.toFixed(2)} rad)`;
    if (reads.temp) reads.temp.textContent = `T = ${tempK.toFixed(1)} K (η = ${etaEnv.toFixed(3)})`;
    if (reads.mermin) {
      if (knockout) {
        reads.mermin.textContent = isEs ? `⟨M₃⟩ = ${m3Val.toFixed(3)} vs 2.0 (DEFECTO)` : `⟨M₃⟩ = ${m3Val.toFixed(3)} vs 2.0 (DEFECT)`;
      } else if (m3Val > BISEP_BOUND) {
        reads.mermin.textContent = `⟨M₃⟩ = ${m3Val.toFixed(3)} > 2√2 (GTE PASS)`;
      } else {
        reads.mermin.textContent = `⟨M₃⟩ = ${m3Val.toFixed(3)} ≤ 2.828`;
      }
    }
    if (reads.comp) {
      reads.comp.textContent = compMode === "yb173"
        ? `WEP 1.00× · √ϑ_AH ${ahAmpRatio.toFixed(1)}× (¹⁷³Yb)`
        : (isEs ? "WEP 1.00× · √ϑ_AH 1.00× (ref ¹²C)" : "WEP 1.00× · √ϑ_AH 1.00× (¹²C ref)");
    }
    if (reads.clock) {
      reads.clock.textContent = `V_clock = ${vClock.toFixed(3)} · 1|23 σ_c = 34.93 µm`;
    }

    if (barMermin) barMermin.setAttribute("width", Math.max(8, (Math.max(0, m3Val) / 4.0) * 230).toFixed(1));
    if (barComp) barComp.setAttribute("width", (compMode === "yb173" ? 226.0 : 28.0).toFixed(1));
    if (barClock) barClock.setAttribute("width", Math.max(8, vClock * 230).toFixed(1));

    if (statusEl) {
      const L = MSG[lang()];
      if (knockout) {
        statusEl.textContent = L.ko;
        statusEl.setAttribute("data-state", "defect");
      } else if (chanMode === "hybrid") {
        statusEl.textContent = L.hybrid;
        statusEl.setAttribute("data-state", "pass");
      } else if (m3Val > BISEP_BOUND) {
        statusEl.textContent = L.gte;
        statusEl.setAttribute("data-state", "pass");
      } else {
        statusEl.textContent = L.sub;
        statusEl.setAttribute("data-state", "defect");
      }
    }
  }

  [holdInput, tempInput].forEach((el) => { if (el) el.addEventListener("input", render); });
  chanBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      chanMode = btn.getAttribute("data-mw-chan") || "quantum";
      chanBtns.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      render();
    });
  });
  compBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      compMode = btn.getAttribute("data-mw-comp") || "diamond";
      compBtns.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      render();
    });
  });
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

const SVG_NS = "http://www.w3.org/2000/svg";
const EULER_GAMMA = 0.5772156649015329;

function svgEl(tag, attrs = {}, text = null) {
  const el = document.createElementNS(SVG_NS, tag);
  Object.entries(attrs).forEach(([k, v]) => el.setAttribute(k, String(v)));
  if (text !== null) el.textContent = text;
  return el;
}

function closedFormCombined(r, sigma, lb, knockout = false) {
  let first = 1.0;
  let second = 0.0;
  if (sigma <= 1e-9) {
    first = 1.0;
    second = lb > 1e-9 ? Math.exp(-r / lb) : 0.0;
  } else if (lb <= 1e-9) {
    first = erfApprox(r / (2.0 * sigma));
    second = 0.0;
  } else {
    first = erfApprox(r / (2.0 * sigma));
    const a = sigma / lb;
    const b = r / (2.0 * sigma);
    const d1 = a - b;
    const d2 = a + b;
    const termB = Math.exp(-b * b) * erfcScaled(d2);
    const termA = d1 >= 0.0
      ? Math.exp(-b * b) * erfcScaled(d1)
      : 2.0 * Math.exp(a * a - r / lb) - Math.exp(-b * b) * erfcScaled(-d1);
    second = 0.5 * (termA - termB);
  }
  return knockout ? (first + second) : (first - second);
}

function besselI0(x) {
  const ax = Math.abs(x);
  if (ax < 3.75) {
    const y = (x / 3.75) * (x / 3.75);
    return 1.0 + y * (3.5156229 + y * (3.0899424 + y * (1.2067492 + y * (0.2659732 + y * (0.0360768 + y * 0.0045813)))));
  }
  const y = 3.75 / ax;
  return (Math.exp(ax) / Math.sqrt(ax)) * (
    0.39894228 + y * (0.01328592 + y * (0.00225319 + y * (-0.00157565 + y * (
      0.00916281 + y * (-0.02057706 + y * (0.02635537 + y * (-0.01647633 + y * 0.00392377)))
    ))))
  );
}

function besselK0(x) {
  if (x <= 1e-12) return 0.0;
  if (x <= 2.0) {
    const y = (x * x) / 4.0;
    return -Math.log(x / 2.0) * besselI0(x) - 0.57721566 + y * (
      0.42278420 + y * (0.23069756 + y * (0.03488590 + y * (0.00262698 + y * (0.00010750 + y * 0.00000740))))
    );
  }
  const y = 2.0 / x;
  return (Math.exp(-x) / Math.sqrt(x)) * (
    1.25331414 + y * (-0.07832358 + y * (0.02189568 + y * (-0.01062446 + y * (
      0.00587872 + y * (-0.00251540 + y * 0.00053208)
    ))))
  );
}

function helfrichGreenReg(rNm, lbNm) {
  return Math.log(rNm / (2.0 * lbNm)) + EULER_GAMMA + besselK0(rNm / lbNm);
}

function initFourGateSieve(root) {
  const sigmaInput = root.querySelector('[data-cs-input="sigma"]');
  const lbInput = root.querySelector('[data-cs-input="lb"]');
  const valSigma = root.querySelector('[data-cs-val="sigma"]');
  const valLb = root.querySelector('[data-cs-val="lb"]');
  const scaleBtn = root.querySelector("[data-fgs-scale]");
  const koBtn = root.querySelector("[data-cs-knockout]");
  const statusEl = root.querySelector("[data-cs-status]");
  const leftG = root.querySelector("[data-fgs-left]");
  const rightG = root.querySelector("[data-fgs-right]");
  const reads = {};
  root.querySelectorAll("[data-cs-read]").forEach((el) => { reads[el.getAttribute("data-cs-read")] = el; });
  const cells = {};
  root.querySelectorAll("[data-fgs-cell]").forEach((el) => { cells[el.getAttribute("data-fgs-cell")] = el; });

  let scale = "brane";
  let knockout = false;

  const SIGNED_CONTOUR = [
    [0.0, 27.22], [10.0, 25.47], [18.0, 23.34], [24.0, 20.01],
    [28.0, 16.22], [32.0, 7.83], [33.01, 0.0],
  ];
  const UNSIGNED_CONTOUR = [
    [0.0, 38.47], [18.0, 36.24], [32.0, 28.69], [40.4, 0.0],
  ];

  const G_NEWTON = 6.67430e-11;
  const MASS_KG = 1.0e-14;
  const D_M = 75.0e-6;
  const DX_M = 250.0e-6;
  const DIAG_M = Math.hypot(D_M, DX_M);
  const OMEGA_N = ((2.0 * G_NEWTON * MASS_KG * MASS_KG) / HBAR) * ((1.0 / D_M) - (1.0 / DIAG_M));
  const T_PI = Math.PI / OMEGA_N;
  const GAMMA_2K = 0.021965;
  const ETA_2K = Math.exp(-GAMMA_2K * T_PI);
  const BISEP_BOUND = 2.0 * Math.SQRT2;
  const DP_SIGMA_M = 33.08e-6;

  // Precompute classical 3-body DP Mermin benchmark at sigma_95 = 33.08 um (0.3227)
  const dpA = smearedF(0.0, DP_SIGMA_M) - smearedF(DX_M, DP_SIGMA_M);
  const dpB = smearedF(D_M, DP_SIGMA_M) - smearedF(DIAG_M, DP_SIGMA_M);
  const dpTau = (G_NEWTON * MASS_KG * MASS_KG * T_PI) / (2.0 * HBAR);
  const M3_DP_REF = 0.25 * Math.pow(ETA_2K, 3) * (
    Math.exp(-6.0 * (dpA + 2.0 * dpB) * dpTau) + 3.0 * Math.exp(-2.0 * (3.0 * dpA - 2.0 * dpB) * dpTau)
  ) + 3.0 * ETA_2K * Math.exp(-2.0 * dpA * dpTau) * Math.pow(Math.sin(2.0 * dpB * dpTau), 2);

  function contourLimit(pts, sig) {
    if (sig < 0.0) return pts[0][1];
    const last = pts[pts.length - 1];
    if (sig > last[0]) return -1.0;
    for (let i = 0; i < pts.length - 1; i += 1) {
      const [x0, y0] = pts[i];
      const [x1, y1] = pts[i + 1];
      if (sig >= x0 && sig <= x1) {
        const t = (sig - x0) / Math.max(x1 - x0, 1e-9);
        return y0 + t * (y1 - y0);
      }
    }
    return 0.0;
  }

  function renderLeftQuadrant(sigma, lb, insideSigned, insideUnsigned, isEs) {
    if (!leftG) return;
    leftG.replaceChildren();
    const x0 = 38;
    const y0 = 266;
    const w = 212;
    const h = 216;
    const maxS = 44.0;
    const maxL = 44.0;
    const sx = (s) => x0 + (s / maxS) * w;
    const sy = (l) => y0 - (l / maxL) * h;

    leftG.appendChild(svgEl("text", {
      x: x0 - 4,
      y: 30,
      fill: "var(--tp-ink)",
      "font-size": "11.2",
      "font-weight": "700",
    }, isEs ? "1 · Cuadrante 95 % (σ, ℓ_b)" : "1 · 95% Quadrant (σ, ℓ_b)"));

    leftG.appendChild(svgEl("rect", {
      x: x0,
      y: y0 - h,
      width: w,
      height: h,
      rx: 6,
      fill: "var(--tp-minium-soft)",
      stroke: "var(--tp-rule)",
    }));

    const uPoly = [[x0, y0], ...UNSIGNED_CONTOUR.map(([s, l]) => [sx(s), sy(l)]), [sx(40.4), y0]]
      .map(([px, py]) => `${px.toFixed(1)},${py.toFixed(1)}`).join(" ");
    leftG.appendChild(svgEl("polygon", { points: uPoly, fill: "var(--tp-vellum)", opacity: "0.92" }));

    const sPoly = [[x0, y0], ...SIGNED_CONTOUR.map(([s, l]) => [sx(s), sy(l)]), [sx(33.01), y0]]
      .map(([px, py]) => `${px.toFixed(1)},${py.toFixed(1)}`).join(" ");
    leftG.appendChild(svgEl("polygon", { points: sPoly, fill: "var(--tp-verdigris)", opacity: "0.18" }));

    const uLine = UNSIGNED_CONTOUR.map(([s, l]) => `${sx(s).toFixed(1)},${sy(l).toFixed(1)}`).join(" ");
    leftG.appendChild(svgEl("polyline", {
      points: uLine,
      fill: "none",
      stroke: "var(--tp-sienna)",
      "stroke-width": "2.2",
      "stroke-dasharray": "5 3",
    }));

    const sLine = SIGNED_CONTOUR.map(([s, l]) => `${sx(s).toFixed(1)},${sy(l).toFixed(1)}`).join(" ");
    leftG.appendChild(svgEl("polyline", {
      points: sLine,
      fill: "none",
      stroke: "var(--tp-minium)",
      "stroke-width": "2.8",
    }));

    leftG.appendChild(svgEl("line", { x1: x0, y1: y0, x2: x0 + w, y2: y0, stroke: "var(--tp-ink)", "stroke-width": "1.5" }));
    leftG.appendChild(svgEl("line", { x1: x0, y1: y0 - h, x2: x0, y2: y0, stroke: "var(--tp-ink)", "stroke-width": "1.5" }));

    [0, 18, 33, 40].forEach((tk) => {
      const tx = sx(tk);
      leftG.appendChild(svgEl("line", { x1: tx, y1: y0, x2: tx, y2: y0 + 4, stroke: "var(--tp-ink)" }));
      leftG.appendChild(svgEl("text", { x: tx - 6, y: y0 + 15, fill: "var(--tp-ink)", "font-size": "9.5" }, String(tk)));
    });
    [0, 18, 27, 38].forEach((tk) => {
      const ty = sy(tk);
      leftG.appendChild(svgEl("line", { x1: x0 - 4, y1: ty, x2: x0, y2: ty, stroke: "var(--tp-ink)" }));
      leftG.appendChild(svgEl("text", { x: 14, y: ty + 3.5, fill: "var(--tp-ink)", "font-size": "9.5" }, String(tk)));
    });
    leftG.appendChild(svgEl("text", { x: x0 + 74, y: 298, fill: "var(--tp-ink)", "font-size": "10.2", "font-weight": "700" }, "σ (µm)"));
    leftG.appendChild(svgEl("text", { x: x0 + 6, y: y0 - h + 14, fill: "var(--tp-minium)", "font-size": "9.4", "font-weight": "700" }, isEs ? "Sólida: con signo 27.2 µm" : "Solid: signed 27.2 µm"));
    leftG.appendChild(svgEl("text", { x: x0 + 6, y: y0 - h + 26, fill: "var(--tp-sienna)", "font-size": "9.2" }, isEs ? "Guiones: sin signo 38.5 µm" : "Dashed: unsigned 38.5 µm"));

    const cx = sx(Math.min(maxS, sigma));
    const cy = sy(Math.min(maxL, lb));
    const dotCol = knockout
      ? "var(--tp-minium)"
      : (insideSigned ? "var(--tp-verdigris)" : (insideUnsigned ? "var(--tp-sienna)" : "var(--tp-minium)"));
    leftG.appendChild(svgEl("line", { x1: x0, y1: cy, x2: cx, y2: cy, stroke: dotCol, "stroke-width": "1.2", "stroke-dasharray": "3 2" }));
    leftG.appendChild(svgEl("line", { x1: cx, y1: cy, x2: cx, y2: y0, stroke: dotCol, "stroke-width": "1.2", "stroke-dasharray": "3 2" }));
    leftG.appendChild(svgEl("circle", { cx: cx.toFixed(1), cy: cy.toFixed(1), r: "9.5", fill: "none", stroke: "var(--tp-prussian)", "stroke-width": "1.8" }));
    leftG.appendChild(svgEl("circle", { cx: cx.toFixed(1), cy: cy.toFixed(1), r: "5.8", fill: dotCol, stroke: "var(--tp-vellum)", "stroke-width": "1.6" }));
  }

  function renderRightPanel(sigma, lb, isEs) {
    if (!rightG) return;
    rightG.replaceChildren();
    const x0 = 294;
    const yTop = 50;
    const w = 248;
    const h = 216;
    const yBot = yTop + h;

    rightG.appendChild(svgEl("rect", {
      x: x0,
      y: yTop,
      width: w,
      height: h,
      rx: 6,
      fill: "var(--tp-vellum)",
      stroke: "var(--tp-rule)",
    }));

    if (scale === "brane") {
      rightG.appendChild(svgEl("text", {
        x: x0,
        y: 30,
        fill: "var(--tp-ink)",
        "font-size": "11.2",
        "font-weight": "700",
      }, isEs ? "2 · ΔV(r)/V_N (%) · Brana 2.0 K (d = 3)" : "2 · ΔV(r)/V_N (%) · 2.0 K Brane (d = 3)"));

      const rMin = 35.0;
      const rMax = 120.0;
      const vMin = -35.0;
      const vMax = 45.0;
      const rx = (r) => x0 + ((r - rMin) / (rMax - rMin)) * w;
      const ry = (pct) => {
        const cl = Math.max(vMin, Math.min(vMax, pct));
        return yBot - ((cl - vMin) / (vMax - vMin)) * h;
      };
      const yZero = ry(0.0);

      rightG.appendChild(svgEl("line", { x1: x0, y1: yZero, x2: x0 + w, y2: yZero, stroke: "var(--tp-ink)", "stroke-width": "1.4" }));
      [52, 75].forEach((rm) => {
        const xm = rx(rm);
        rightG.appendChild(svgEl("line", { x1: xm, y1: yTop, x2: xm, y2: yBot, stroke: "var(--tp-rule)", "stroke-dasharray": "3 3" }));
        rightG.appendChild(svgEl("text", { x: xm - 8, y: yBot + 15, fill: "var(--tp-ink)", "font-size": "9.5" }, `${rm}`));
      });
      rightG.appendChild(svgEl("text", { x: x0 + w - 26, y: yBot + 15, fill: "var(--tp-ink)", "font-size": "9.5" }, "120"));
      rightG.appendChild(svgEl("text", { x: x0 + 82, y: 298, fill: "var(--tp-ink)", "font-size": "10.2", "font-weight": "700" }, "r (µm)"));

      const rsPts = [];
      const branePts = [];
      for (let i = 0; i <= 48; i += 1) {
        const r = rMin + (i / 48.0) * (rMax - rMin);
        const pctRs = (2.0 / 3.0) * Math.pow(30.0 / r, 2) * 100.0;
        const pctBrane = (closedFormCombined(r, sigma, lb, knockout) - 1.0) * 100.0;
        rsPts.push(`${rx(r).toFixed(1)},${ry(pctRs).toFixed(1)}`);
        branePts.push(`${rx(r).toFixed(1)},${ry(pctBrane).toFixed(1)}`);
      }
      rightG.appendChild(svgEl("polyline", {
        points: rsPts.join(" "),
        fill: "none",
        stroke: "var(--tp-prussian)",
        "stroke-width": "2.5",
      }));
      rightG.appendChild(svgEl("polyline", {
        points: branePts.join(" "),
        fill: "none",
        stroke: knockout ? "var(--tp-sienna)" : "var(--tp-minium)",
        "stroke-width": "2.8",
        ...(knockout ? { "stroke-dasharray": "5 2" } : {}),
      }));

      const v52Rs = (2.0 / 3.0) * Math.pow(30.0 / 52.0, 2) * 100.0;
      const v52Br = (closedFormCombined(52.0, sigma, lb, knockout) - 1.0) * 100.0;
      rightG.appendChild(svgEl("circle", { cx: rx(52).toFixed(1), cy: ry(v52Rs).toFixed(1), r: "4.4", fill: "var(--tp-prussian)" }));
      rightG.appendChild(svgEl("circle", { cx: rx(52).toFixed(1), cy: ry(v52Br).toFixed(1), r: "4.8", fill: knockout ? "var(--tp-sienna)" : "var(--tp-minium)" }));

      rightG.appendChild(svgEl("text", {
        x: x0 + 36,
        y: yTop + 15,
        fill: "var(--tp-prussian)",
        "font-family": "monospace",
        "font-size": "9.0",
      }, `RS-II +(2/3)(30/r)²: +${v52Rs.toFixed(2)}% @52µm`));
      rightG.appendChild(svgEl("text", {
        x: x0 + 8,
        y: yBot - 8,
        fill: knockout ? "var(--tp-sienna)" : "var(--tp-minium)",
        "font-family": "monospace",
        "font-size": "9.4",
      }, `${knockout ? "DEFECT (+second)" : "Brane (−second)"}: ${v52Br >= 0 ? "+" : ""}${v52Br.toFixed(2)}% @52µm`));
    } else {
      rightG.appendChild(svgEl("text", {
        x: x0,
        y: 30,
        fill: "var(--tp-ink)",
        "font-size": "11.0",
        "font-weight": "700",
      }, isEs ? "2 · Bicapa 310.15 K (d = 2, ℓ_b = 65.44 nm)" : "2 · 310.15 K Bilayer (d = 2, ℓ_b = 65.44 nm)"));

      const lbNm = 65.44;
      const rMin = 2.0;
      const rMax = 150.0;
      const gMin = -3.4;
      const gMax = 0.8;
      const rx = (r) => x0 + ((r - rMin) / (rMax - rMin)) * w;
      const ry = (g) => {
        const cl = Math.max(gMin, Math.min(gMax, g));
        return yBot - ((cl - gMin) / (gMax - gMin)) * h;
      };
      const yZero = ry(0.0);
      rightG.appendChild(svgEl("line", { x1: x0, y1: yZero, x2: x0 + w, y2: yZero, stroke: "var(--tp-ink)", "stroke-width": "1.3" }));

      const barePts = [];
      const regPts = [];
      for (let i = 0; i <= 50; i += 1) {
        const r = rMin + (i / 50.0) * (rMax - rMin);
        const gBare = Math.log(r / (2.0 * lbNm)) + EULER_GAMMA;
        const gReg = helfrichGreenReg(r, lbNm);
        barePts.push(`${rx(r).toFixed(1)},${ry(gBare).toFixed(1)}`);
        regPts.push(`${rx(r).toFixed(1)},${ry(gReg).toFixed(1)}`);
      }
      rightG.appendChild(svgEl("polyline", {
        points: barePts.join(" "),
        fill: "none",
        stroke: "var(--tp-sienna)",
        "stroke-width": "2.0",
        "stroke-dasharray": "4 3",
      }));
      rightG.appendChild(svgEl("polyline", {
        points: regPts.join(" "),
        fill: "none",
        stroke: "var(--tp-verdigris)",
        "stroke-width": "2.8",
      }));

      const g75 = helfrichGreenReg(7.5, lbNm);
      rightG.appendChild(svgEl("circle", { cx: rx(7.5).toFixed(1), cy: ry(g75).toFixed(1), r: "5.2", fill: "var(--tp-verdigris)", stroke: "var(--tp-prussian)", "stroke-width": "1.5" }));
      rightG.appendChild(svgEl("text", { x: x0 + 68, y: 298, fill: "var(--tp-ink)", "font-size": "10.2", "font-weight": "700" }, "r (nm · Helfrich d = 2)"));
      rightG.appendChild(svgEl("text", {
        x: x0 + 8,
        y: yTop + 16,
        fill: "var(--tp-verdigris)",
        "font-family": "monospace",
        "font-size": "9.2",
      }, "ln(r/2ℓ_b)+γ_E+K₀(r/ℓ_b) · F = 1.31 pN"));
      rightG.appendChild(svgEl("text", {
        x: x0 + 8,
        y: yBot - 20,
        fill: "var(--tp-prussian)",
        "font-family": "monospace",
        "font-size": "9.1",
      }, "U_GBP(7.5 nm) = −0.0741 k_B T"));
      rightG.appendChild(svgEl("text", {
        x: x0 + 8,
        y: yBot - 7,
        fill: "var(--tp-ink)",
        "font-family": "monospace",
        "font-size": "9.1",
      }, "F_EH / F_lipid = 3.68e54"));
    }
  }

  function render() {
    const sigma = Number(sigmaInput ? sigmaInput.value : 18.0);
    const lb = Number(lbInput ? lbInput.value : 18.0);
    const isEs = lang() === "es";

    if (valSigma) valSigma.textContent = `${sigma.toFixed(1)} µm`;
    if (valLb) valLb.textContent = `${lb.toFixed(1)} µm`;

    if (scaleBtn) {
      scaleBtn.setAttribute("aria-pressed", String(scale === "bilayer"));
      scaleBtn.textContent = scale === "brane"
        ? (isEs
          ? "Escala activa: Brana Espaciotemporal 2.0 K (d = 3) → Cambiar a Bicapa 310.15 K"
          : "Active: 2.0 K Spacetime Brane (d = 3) → Switch to 310.15 K Lipid Bilayer")
        : (isEs
          ? "Escala activa: Bicapa Lipídica 310.15 K (d = 2, ℓ_b = 65.44 nm, F = 1.31 pN)"
          : "Active: 310.15 K Lipid Bilayer (d = 2, l_b = 65.44 nm, F = 1.31 pN)");
    }

    const insideSigned = sigma <= 33.01 && lb <= contourLimit(SIGNED_CONTOUR, sigma);
    const insideUnsigned = sigma <= 40.4 && lb <= contourLimit(UNSIGNED_CONTOUR, sigma);

    const dUm = 75.0;
    const dxUm = 250.0;
    const diagUm = Math.hypot(dUm, dxUm);
    const dPhiRatio = (
      (closedFormCombined(dUm, sigma, lb, knockout) / dUm)
      - (closedFormCombined(diagUm, sigma, lb, knockout) / diagUm)
    ) / ((1.0 / dUm) - (1.0 / diagUm));
    const phaseShiftPct = (dPhiRatio - 1.0) * 100.0;
    const m3Live = Math.pow(ETA_2K, 3) + 3.0 * ETA_2K * Math.pow(Math.sin(0.5 * Math.PI * dPhiRatio), 2);
    const gtePass = m3Live > BISEP_BOUND;

    renderLeftQuadrant(sigma, lb, insideSigned, insideUnsigned, isEs);
    renderRightPanel(sigma, lb, isEs);

    if (reads.mermin) {
      reads.mermin.textContent = knockout
        ? `PLANTED DEFECT ACTIVE · ⟨M₃⟩ = ${m3Live.toFixed(4)}`
        : `⟨M₃⟩ = ${m3Live.toFixed(4)} ${gtePass ? ">" : "≤"} ${BISEP_BOUND.toFixed(4)} (DP ${M3_DP_REF.toFixed(4)})`;
    }
    if (reads.edge) {
      if (knockout) {
        reads.edge.textContent = "PLANTED DEFECT ACTIVE (−second → +second)";
      } else if (scale === "bilayer") {
        reads.edge.textContent = "l_b = 65.44 nm · U_GBP = −0.0741 k_B T · F_EH/F_lip = 3.68e54";
      } else {
        const edgeTag = insideSigned
          ? (isEs ? "PERMITIDO" : "ALLOWED")
          : (insideUnsigned ? (isEs ? "TRAMPA SIN SIGNO" : "UNSIGNED TRAP") : (isEs ? "EXCLUIDO" : "EXCLUDED"));
        reads.edge.textContent = `${edgeTag} · Δφ/Δφ_N = ${phaseShiftPct >= 0 ? "+" : ""}${phaseShiftPct.toFixed(2)}% (D = 75 µm)`;
      }
    }

    const passTxt = isEs ? "PASA" : "PASS";
    const failTxt = isEs ? "FALLA" : "FAIL";
    const condTxt = "COND";
    const gateState = {
      scalar_sheet: [insideSigned ? passTxt : failTxt, failTxt, gtePass ? passTxt : failTxt, failTxt],
      stelle_box2: [lb <= 27.22 ? passTxt : failTxt, failTxt, failTxt, passTxt],
      classical_dp: [sigma <= 33.01 ? passTxt : failTxt, condTxt, failTxt, failTxt],
      horava_nabla4: [insideSigned ? passTxt : failTxt, condTxt, gtePass ? passTxt : failTxt, passTxt],
      warped_rs2: [passTxt, passTxt, passTxt, passTxt],
      canonical_qg: [passTxt, passTxt, passTxt, passTxt],
    };
    Object.entries(gateState).forEach(([modelKey, labels]) => {
      labels.forEach((lbl, idx) => {
        const cell = cells[`${modelKey}:${idx}`];
        if (!cell) return;
        if (knockout) {
          cell.textContent = idx === 0 ? "PLANTED DEFECT ACTIVE" : (isEs ? "DEFECTO" : "DEFECT");
        } else {
          cell.textContent = lbl;
        }
      });
    });

    if (statusEl) {
      if (knockout) {
        statusEl.textContent = isEs
          ? "PLANTED DEFECT ACTIVE — Defecto de signo activo: invierte el ablandamiento espacial (−second) a (+second), confundiendo la elasticidad biarmónica espacial con el refuerzo de Kaluza–Klein en RS-II."
          : "PLANTED DEFECT ACTIVE — Sign-conflation defect flips spatial bending softening (−second) to (+second), confusing spatial biharmonic elasticity with warped RS-II Kaluza–Klein gravitational enhancement!";
        statusEl.setAttribute("data-state", "defect");
      } else if (scale === "bilayer") {
        statusEl.textContent = isEs
          ? "Modo bicapa lipídica a 310.15 K (d = 2): el operador de Helfrich (−σ_ten Δ + κ Δ²) regulariza el logaritmo infrarrojo mediante K₀(r/ℓ_b) en ℓ_b = 65.44 nm (F = 1.31 pN, U_GBP = −0.0741 k_B T en 7.5 nm; razón de rigidez F_EH / F_lip = 3.68×10⁵⁴)."
          : "310.15 K Lipid Bilayer mode (d = 2): the Helfrich operator (−σ_ten Δ + κ Δ²) UV-regularizes the 2D logarithmic sheet via K₀(r/ℓ_b) at l_b = 65.44 nm (F = 1.31 pN, U_GBP = −0.0741 k_B T at 7.5 nm; stiffness ratio F_EH / F_lipid = 3.68×10⁵⁴).";
        statusEl.setAttribute("data-state", "pass");
      } else if (insideSigned) {
        statusEl.textContent = isEs
          ? `Dentro del contorno con signo al 95 %: (σ, ℓ_b) = (${sigma.toFixed(1)}, ${lb.toFixed(1)}) µm produce ablandamiento gravitatorio (${phaseShiftPct.toFixed(2)} % en D = 75 µm), preserva ⟨M₃⟩ = ${m3Live.toFixed(4)} > 2√2 y deja exactamente 2 sobrevivientes en las cuatro compuertas (RS-II Alabeada y TCE Cuántica Canónica).`
          : `Inside signed 95% contour: (σ, ℓ_b) = (${sigma.toFixed(1)}, ${lb.toFixed(1)}) µm yields genuine spatial softening (${phaseShiftPct.toFixed(2)}% phase shift at D = 75 µm), preserves ⟨M₃⟩ = ${m3Live.toFixed(4)} > 2√2, and leaves exact 2 four-gate survivors (Warped RS-II Brane & Canonical QG EFT).`;
        statusEl.setAttribute("data-state", "pass");
      } else if (insideUnsigned) {
        statusEl.textContent = isEs
          ? `Excluido por la cota con signo (pero dentro del arco ingenuo sin signo de 38.47 µm): ignorar el signo negativo de −exp(−r/ℓ_b) sobreestima ℓ_b; la Tabla 11.4 de Eöt-Wash descarta (${sigma.toFixed(1)}, ${lb.toFixed(1)}) µm en la Compuerta G1.`
          : `Excluded by signed Eöt-Wash bound (inside naive 38.47 µm unsigned arc): ignoring the negative sign of −exp(−r/ℓ_b) overestimates ℓ_b; signed Table 11.4 excludes (${sigma.toFixed(1)}, ${lb.toFixed(1)}) µm at Gate G1!`;
        statusEl.setAttribute("data-state", "defect");
      } else {
        statusEl.textContent = isEs
          ? `Excluido tanto con signo como sin signo: (${sigma.toFixed(1)}, ${lb.toFixed(1)}) µm viola los límites de par submilimétrico de Eöt-Wash en r ≥ 52 µm (Compuerta G1).`
          : `Excluded under both signed and unsigned contours: (${sigma.toFixed(1)}, ${lb.toFixed(1)}) µm violates Eöt-Wash sub-millimetre torsion-balance bounds at r ≥ 52 µm (Gate G1).`;
        statusEl.setAttribute("data-state", "defect");
      }
    }
  }

  [sigmaInput, lbInput].forEach((el) => { if (el) el.addEventListener("input", render); });
  if (scaleBtn) {
    scaleBtn.addEventListener("click", () => {
      scale = scale === "brane" ? "bilayer" : "brane";
      scaleBtn.setAttribute("data-fgs-scale", scale);
      render();
    });
  }
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

function initSevenGateCrown(root) {
  const lstarInput = root.querySelector("[data-crown-lstar]");
  const dqInput = root.querySelector("[data-crown-dq]");
  const gravSelect = root.querySelector("[data-crown-grav]");
  const valLstar = root.querySelector('[data-crown-val="lstar"]');
  const valDq = root.querySelector('[data-crown-val="dq"]');
  const curveEnt = root.querySelector('[data-crown-curve="entire"]');
  const curveSt = root.querySelector('[data-crown-curve="stelle"]');
  const curveFat = root.querySelector('[data-crown-curve="fat"]');
  const lstarLine = root.querySelector("[data-crown-lstar-line]");
  const lstarDot = root.querySelector("[data-crown-lstar-dot]");
  const m75Dot = root.querySelector("[data-crown-m75-dot]");
  const badgeBg = root.querySelector("[data-crown-badge-bg]");
  const statusEl = root.querySelector("[data-cs-status]");

  const reads = {};
  root.querySelectorAll("[data-crown-read]").forEach((el) => {
    reads[el.getAttribute("data-crown-read")] = el;
  });
  const bars = {};
  root.querySelectorAll("[data-crown-bar]").forEach((el) => {
    bars[el.getAttribute("data-crown-bar")] = el;
  });
  const cells = {};
  root.querySelectorAll("[data-crown-cell]").forEach((el) => {
    cells[el.getAttribute("data-crown-cell")] = el;
  });
  const scores = {};
  root.querySelectorAll("[data-crown-score]").forEach((el) => {
    scores[el.getAttribute("data-crown-score")] = el;
  });
  const rows = {};
  root.querySelectorAll("[data-crown-row]").forEach((el) => {
    rows[el.getAttribute("data-crown-row")] = el;
  });

  const L_SCHUR = 32.98;
  const L_VAC = 88.11;
  const L_KAPNER = 84.89;
  const X0_P = 56.0;
  const W_P = 396.0;
  const Y_BOT = 348.0;
  const H_P = 214.0;

  const G_NEWTON = 6.67430e-11;
  const MASS_KG = 1.0e-14;
  const D_M = 75.0e-6;
  const DX_M = 250.0e-6;
  const DIAG_M = Math.hypot(D_M, DX_M);
  const OMEGA_N = ((2.0 * G_NEWTON * MASS_KG * MASS_KG) / HBAR) * ((1.0 / D_M) - (1.0 / DIAG_M));
  const T_PI = Math.PI / OMEGA_N;
  const ETA_2K = Math.exp(-0.021965 * T_PI);

  const BASE_MATRIX = {
    scalarSheet: [true, false, true, false, false, false, false],
    stelleBox2: [true, false, false, true, false, true, false],
    classicalDPHybrid: [true, false, false, false, false, false, false],
    fatGraviton85um: [false, true, true, true, true, false, true],
    pureGaugeIrrationalSM: [true, true, true, true, false, true, false],
    flatCircleKK5D: [false, true, true, true, false, false, false],
    canonicalQuantumGREFT: [true, true, true, true, true, true, false],
    nonlocalChiralHorizonCrown: [true, true, true, true, true, true, true],
  };

  function cpx(rUm) {
    return X0_P + ((rUm - 5.0) / 105.0) * W_P;
  }

  function cpy(vRatio) {
    return Y_BOT - Math.max(0.0, Math.min(1.0, vRatio)) * H_P;
  }

  function fmtSigned(val, digits = 2) {
    const clean = Math.abs(val) < 1e-9 ? 0.0 : val;
    return `${clean >= 0.0 ? "+" : "−"}${Math.abs(clean).toFixed(digits)}`;
  }

  function updateSignedBar(barEl, val, maxScale) {
    if (!barEl) return;
    const xMid = 691.5;
    const halfW = 196.5;
    if (Math.abs(val) < 1e-5) {
      barEl.setAttribute("x", (xMid - 6.0).toFixed(1));
      barEl.setAttribute("width", "12.0");
      barEl.setAttribute("fill", "var(--tp-verdigris)");
      return;
    }
    const span = Math.max(5.0, Math.min(1.0, Math.abs(val) / maxScale) * halfW);
    barEl.setAttribute("x", (val >= 0.0 ? xMid : xMid - span).toFixed(1));
    barEl.setAttribute("width", span.toFixed(1));
    barEl.setAttribute("fill", "var(--tp-minium)");
  }

  function setRead(key, text, ok) {
    const el = reads[key];
    if (!el) return;
    el.textContent = text;
    el.setAttribute("fill", ok ? "var(--tp-verdigris)" : "var(--tp-minium)");
  }

  function render() {
    const lstar = Number(lstarInput ? lstarInput.value : 18);
    const dq = Number(dqInput ? dqInput.value : 0.0);
    const mode = gravSelect ? gravSelect.value : "with_grav";
    const isEs = lang() === "es";

    if (valLstar) valLstar.textContent = `${lstar.toFixed(0)} µm`;
    if (valDq) valDq.textContent = fmtSigned(dq, 2);

    // 1. Update Left Panel radial potential curves across r = 5..110 um
    const entPts = [];
    const stPts = [];
    const fatPts = [];
    for (let i = 0; i <= 70; i += 1) {
      const rUm = 5.0 + (i / 70.0) * 105.0;
      const rx = cpx(rUm).toFixed(1);
      entPts.push(`${rx},${cpy(erfApprox(rUm / (2.0 * lstar))).toFixed(1)}`);
      stPts.push(`${rx},${cpy(1.0 - Math.exp(-rUm / lstar)).toFixed(1)}`);
      fatPts.push(`${rx},${cpy(erfApprox(rUm / (2.0 * L_VAC))).toFixed(1)}`);
    }
    if (curveEnt) curveEnt.setAttribute("points", entPts.join(" "));
    if (curveSt) curveSt.setAttribute("points", stPts.join(" "));
    if (curveFat) curveFat.setAttribute("points", fatPts.join(" "));

    const g1Pass = lstar < L_SCHUR;
    if (curveEnt) {
      curveEnt.setAttribute("stroke", g1Pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
    }
    const xls = cpx(lstar);
    const yls = cpy(erfApprox(0.5));
    if (lstarLine) {
      lstarLine.setAttribute("x1", xls.toFixed(1));
      lstarLine.setAttribute("x2", xls.toFixed(1));
      lstarLine.setAttribute("y1", yls.toFixed(1));
      lstarLine.setAttribute("stroke", g1Pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
    }
    if (lstarDot) {
      lstarDot.setAttribute("cx", xls.toFixed(1));
      lstarDot.setAttribute("cy", yls.toFixed(1));
      lstarDot.setAttribute("fill", g1Pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
    }
    const v52 = erfApprox(52.0 / (2.0 * lstar));
    const v75 = erfApprox(75.0 / (2.0 * lstar));
    const diagUm = Math.hypot(75.0, 250.0);
    const vDiag = erfApprox(diagUm / (2.0 * lstar));
    if (m75Dot) {
      m75Dot.setAttribute("cy", cpy(v75).toFixed(1));
    }
    if (reads.left_foot) {
      reads.left_foot.textContent = isEs
        ? `r (µm) · ℓ_* = ${lstar.toFixed(0)} µm · V(52 µm)/V_N = ${v52.toFixed(4)} (0 fantasmas)`
        : `r (µm) · ℓ_* = ${lstar.toFixed(0)} µm · V(52 µm)/V_N = ${v52.toFixed(4)} (0 ghosts)`;
    }

    const dPhiRatio = ((v75 / 75.0) - (vDiag / diagUm)) / ((1.0 / 75.0) - (1.0 / diagUm));
    const m3Live = Math.pow(ETA_2K, 3) + 3.0 * ETA_2K * Math.pow(Math.sin(0.5 * Math.PI * dPhiRatio), 2);
    const g3Pass = m3Live > 2.0;

    // 2. Chiral hypercharge & mixed gravitational anomaly equations (scaled by 6)
    let q;
    let u;
    let d;
    let l;
    let e;
    if (mode === "with_grav") {
      q = 1.0 + 2.0 * dq;
      u = -4.0 - 2.0 * dq;
      d = 2.0 - 2.0 * dq;
      l = -3.0;
      e = 6.0;
    } else {
      const tParam = 3.0 * dq;
      q = 1.0;
      l = -3.0;
      u = -1.0 - tParam;
      d = -1.0 + tParam;
      e = Math.cbrt(18.0 * (tParam * tParam + 3.0));
    }

    const resSu3 = 2.0 * q + u + d;
    const resSu2 = 3.0 * q + l;
    const resGrav = 6.0 * q + 3.0 * u + 3.0 * d + 2.0 * l + e;
    const resFermat = Math.pow(u + 4.0, 3) + Math.pow(d + 4.0, 3) - Math.pow(e, 3);
    const resHatom = (3.0 + 3.0 * q) - e;

    const okSu3 = Math.abs(resSu3) < 1e-5;
    const okSu2 = Math.abs(resSu2) < 1e-5;
    const okGrav = Math.abs(resGrav) < 1e-4;
    const okFermat = Math.abs(resFermat) < 1e-4;
    const okHatom = Math.abs(resHatom) < 1e-4;
    const g5Pass = okSu3 && okSu2 && okGrav && okFermat && okHatom;

    const passWord = isEs ? "PASA" : "PASS";
    const failWord = isEs ? "FALLA" : "FAIL";

    if (reads.tuple) {
      reads.tuple.textContent = `6Y = (q, u, d, ℓ, e) = (${fmtSigned(q)}, ${fmtSigned(u)}, ${fmtSigned(d)}, ${fmtSigned(l)}, ${fmtSigned(e)})`;
    }
    setRead("su3", `${resSu3.toFixed(3)} · ${okSu3 ? passWord : failWord}`, okSu3);
    setRead("su2", `${resSu2.toFixed(3)} · ${okSu2 ? passWord : failWord}`, okSu2);
    setRead("grav", `${resGrav.toFixed(3)} (e=${e.toFixed(2)}) · ${okGrav ? passWord : failWord}`, okGrav);
    setRead("fermat", `${resFermat.toFixed(3)} · ${okFermat ? passWord : failWord}`, okFermat);
    setRead(
      "hatom",
      `${resHatom.toFixed(3)} · ${okHatom ? (isEs ? "CUANTIZADO" : "QUANTIZED") : (isEs ? "DECUANTIZADO" : "DEQUANTIZED")}`,
      okHatom,
    );
    setRead("uv", `${lstar.toFixed(0)} µm ${g1Pass ? "<" : "≥"} ${L_SCHUR} · ${g1Pass ? passWord : failWord}`, g1Pass);

    updateSignedBar(bars.su3, resSu3, 6.0);
    updateSignedBar(bars.su2, resSu2, 6.0);
    updateSignedBar(bars.grav, resGrav, 6.0);
    updateSignedBar(bars.fermat, resFermat, 220.0);
    updateSignedBar(bars.hatom, resHatom, 6.0);

    if (bars.uv) {
      bars.uv.setAttribute("width", ((lstar / 95.0) * 393.0).toFixed(1));
      bars.uv.setAttribute("fill", g1Pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
    }

    const crownAllPass = g1Pass && g3Pass && g5Pass;
    if (badgeBg) {
      badgeBg.setAttribute("stroke", crownAllPass ? "var(--tp-verdigris)" : "var(--tp-minium)");
    }
    if (reads.crown_verdict) {
      reads.crown_verdict.setAttribute("fill", crownAllPass ? "var(--tp-verdigris)" : "var(--tp-minium)");
      if (crownAllPass) {
        reads.crown_verdict.textContent = isEs
          ? "CORONA: 7/7 COMPUERTAS PASAN · ÚNICO SOBREVIVIENTE"
          : "CROWN STATUS: 7/7 GATES PASS · UNIQUE SURVIVOR";
      } else {
        const broken = [];
        if (!g1Pass) broken.push("G1");
        if (!g3Pass) broken.push("G3");
        if (!g5Pass) broken.push("G5");
        reads.crown_verdict.textContent = isEs
          ? `FUERA DE VENTANA CORONA · FALLA EN ${broken.join(", ")}`
          : `OUTSIDE CROWN WINDOW · FAILS ${broken.join(", ")}`;
      }
    }
    if (reads.crown_sub) {
      reads.crown_sub.textContent = isEs
        ? `G6 rayo nulo: ℓ_Λ = ${L_VAC} / ${L_KAPNER} µm · ⟨M₃(75µm)⟩ = ${m3Live.toFixed(3)} > 2`
        : `G6 null-ray: ℓ_Λ = ${L_VAC} / ${L_KAPNER} µm · ⟨M₃(75µm)⟩ = ${m3Live.toFixed(3)} > 2`;
    }

    // 3. Update 8x7 Elimination Table cells & row states
    const liveMatrix = {
      ...BASE_MATRIX,
      canonicalQuantumGREFT: [g1Pass, true, g3Pass, true, g5Pass, true, false],
      nonlocalChiralHorizonCrown: [g1Pass, true, g3Pass, true, g5Pass, true, true],
    };

    Object.entries(liveMatrix).forEach(([rowKey, vec]) => {
      let countPass = 0;
      vec.forEach((ok, idx) => {
        if (ok) countPass += 1;
        const cell = cells[`${rowKey}:${idx}`];
        if (cell) {
          cell.textContent = ok ? passWord : failWord;
        }
      });
      const scoreEl = scores[rowKey];
      if (scoreEl) {
        if (rowKey === "nonlocalChiralHorizonCrown") {
          scoreEl.textContent = countPass === 7
            ? (isEs ? "7/7 Corona" : "7/7 Crown")
            : `${countPass}/7`;
        } else if (rowKey === "canonicalQuantumGREFT") {
          scoreEl.textContent = countPass === 6
            ? (isEs ? "6/7 TCE" : "6/7 EFT")
            : `${countPass}/7`;
        } else {
          scoreEl.textContent = `${countPass}/7`;
        }
      }
      const rowEl = rows[rowKey];
      if (rowEl) {
        const isActive = (rowKey === "nonlocalChiralHorizonCrown" && crownAllPass)
          || (rowKey === "pureGaugeIrrationalSM" && mode === "omit_grav_sym" && !okGrav);
        rowEl.setAttribute("data-crown-highlight", isActive ? "true" : "false");
      }
    });

    if (statusEl) {
      if (crownAllPass) {
        statusEl.textContent = isEs
          ? `Ventana Corona 7/7 activa: ℓ_* = ${lstar.toFixed(0)} µm < 32.98 µm (muro con signo de Eöt-Wash) y ℓ_* ≪ ℓ_Λ = 88.11 µm (desacoplo en horizonte nulo G6), mientras [Grav]²U(1)_Y = 0 y la reducción cúbica de Fermat fijan e = 6, Q(p + e⁻) = 0 y dejan a UV Entera + Corona Quiral como único sobreviviente 7/7.`
          : `7/7 Crown window active: ℓ_* = ${lstar.toFixed(0)} µm < 32.98 µm (signed Eöt-Wash Schur wall) and ℓ_* ≪ ℓ_Λ = 88.11 µm (G6 null-horizon vacuum decoupling), while [Grav]²U(1)_Y = 0 plus the Fermat cubic reduction lock e = 6, Q(p + e⁻) = 0, leaving Entire UV + Chiral Crown as the unique 7/7 survivor.`;
        statusEl.setAttribute("data-state", "pass");
      } else if (mode === "omit_grav_sym" && !okGrav) {
        statusEl.textContent = isEs
          ? `Rama irracional pura de norma activa (omitiendo [Grav]²U(1)_Y): las anomalías puras de norma se anulan con e = (18(t²+3))^(1/3) = ${e.toFixed(4)}, pero la anomalía gravitatoria mixta deja residuo ${resGrav.toFixed(3)} ≠ 0 y decuantiza el átomo de hidrógeno (6 Q(p + e⁻) = ${resHatom.toFixed(3)}), eliminada en la Compuerta G5.`
          : `Pure-gauge irrational U(1) branch active (omitting [Grav]²U(1)_Y): pure-gauge anomalies vanish at irrational e = (18(t²+3))^(1/3) = ${e.toFixed(4)}, but the mixed gravitational anomaly leaves residual ${resGrav.toFixed(3)} ≠ 0 and dequantizes hydrogen (6 Q(p + e⁻) = ${resHatom.toFixed(3)})—eliminated at Gate G5.`;
        statusEl.setAttribute("data-state", "defect");
      } else if (!g5Pass) {
        statusEl.textContent = isEs
          ? `Perturbación quiral δ(3Y_Q) = ${fmtSigned(dq)} viola la cancelación de anomalías en la Compuerta G5: [SU(2)]²U(1)_Y = ${resSu2.toFixed(3)}, residuo cúbico de Fermat = ${resFermat.toFixed(3)} y carga de hidrógeno 6 Q(p + e⁻) = ${resHatom.toFixed(3)}.`
          : `Chiral quark shift δ(3Y_Q) = ${fmtSigned(dq)} breaks Gate G5 anomaly cancellation: [SU(2)]²U(1)_Y = ${resSu2.toFixed(3)}, Fermat cubic residual = ${resFermat.toFixed(3)}, and hydrogen charge 6 Q(p + e⁻) = ${resHatom.toFixed(3)}.`;
        statusEl.setAttribute("data-state", "defect");
      } else {
        statusEl.textContent = isEs
          ? `Excluido en la Compuerta G1: ℓ_* = ${lstar.toFixed(0)} µm excede el muro de Schur con signo de Eöt-Wash (32.98 µm), suprimiendo V(52 µm)/V_N a ${v52.toFixed(4)} aunque ⟨M₃(75 µm)⟩ = ${m3Live.toFixed(4)} permanezca sobre 2.`
          : `Excluded at Gate G1: ℓ_* = ${lstar.toFixed(0)} µm exceeds the signed Eöt-Wash Schur wall (32.98 µm), suppressing V(52 µm)/V_N to ${v52.toFixed(4)} even though ⟨M₃(75 µm)⟩ = ${m3Live.toFixed(4)} remains above 2.`;
        statusEl.setAttribute("data-state", "defect");
      }
    }
  }

  [lstarInput, dqInput].forEach((el) => {
    if (el) {
      el.addEventListener("input", render);
      el.addEventListener("change", render);
    }
  });
  if (gravSelect) {
    gravSelect.addEventListener("change", render);
    gravSelect.addEventListener("input", render);
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
  once('[data-cs-instrument="kinematic"]', initKinematic);
  once('[data-cs-instrument="island_page"]', initIslandPage);
  once('[data-cs-instrument="wdw_clock"]', initWdwClock);
  once('[data-cs-instrument="parallel_horizon"]', initParallelHorizon);
  once('[data-cs-instrument="schur_recast"]', initSchurRecast);
  once('[data-cs-instrument="multipartite_witness"]', initMultipartiteWitness);
  once('[data-cs-instrument="four_gate_sieve"]', initFourGateSieve);
  once('[data-cs-instrument="seven_gate_crown"]', initSevenGateCrown);
}

initCrossScaleEssays(document);
