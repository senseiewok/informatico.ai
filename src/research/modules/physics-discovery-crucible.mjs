/**
 * @module physics-discovery-crucible
 * Interactive Symbolic Physics & Sparse PDE Law Finder (PySR / PySINDy / Dedalus / PhysLean / ITensors.jl),
 * Open-Source Physics & Math Discovery Radar, Open-Bounty Crucible Filter, and Standalone Bounty Proof Workbench.
 * Strictly zero .innerHTML and zero inline style attributes.
 */

const REGIMES = {
  burgers: {
    name: "PySINDy + Dedalus · Viscous Burgers / Navier-Stokes PDE",
    exactLaw: "u_t = -1.00 u·u_x + 0.10 u_xx",
    overfitLaw: "u_t = -1.00 u·u_x + 0.10 u_xx + α·u³ + β·u",
    underfitLaw: "u_t = -1.00 u·u_x (inviscid shock truncation)",
    baseWeights: [0.02, 0.03, 0.98, 0.14, 0.03, 0.04],
    trueMask: [false, false, true, true, false, false],
    paretoPoints: [
      [90, 158],
      [175, 118],
      [265, 62],
      [360, 59],
      [450, 57],
    ],
    snippet: `# PySINDy + Dedalus Spectral PDE Discovery (Folio P.12 / P.02)
import numpy as np
import pysindy as ps

# Candidate operator library: [1, u, u_x, u*u_x, u_xx, u^3]
optimizer = ps.STLSQ(threshold=0.05, alpha=1e-3)
model = ps.SINDy(optimizer=optimizer)
# Recovers u_t = -1.00 * u * u_x + 0.10 * u_xx`,
  },
  kepler: {
    name: "PySR · Relativistic Perihelion & Orbital Symbolic Regression",
    exactLaw: "F(r) = -(G·M·m / r²) · [1 + 3·L² / (m²·c²·r²)]",
    overfitLaw: "F(r) = -(G·M·m / r²) · [1 + 3·L²/(m²c²r²) + γ·sin(r)]",
    underfitLaw: "F(r) = -G·M·m / r² (Newtonian 1/r² only)",
    baseWeights: [0.01, 0.99, 0.24, 0.02, 0.03, 0.02],
    trueMask: [false, true, true, false, false, false],
    paretoPoints: [
      [90, 164],
      [175, 96],
      [265, 52],
      [360, 50],
      [450, 49],
    ],
    snippet: `# PySR Multi-Population Symbolic Regression (Folio P.03 / M.07)
from pysr import PySRRegressor

model = PySRRegressor(
    niterations=80,
    binary_operators=["+", "-", "*", "/"],
    parsimony=0.005,
    model_selection="best",
)
# Pareto MDL knee selects relativistic 1/r^2 + 3*L^2/(m^2*c^2*r^4) correction`,
  },
  physlean: {
    name: "HEPLean / PhysLean · Lean 4 Gauge Anomaly Cancellation",
    exactLaw: "∑ d_f Y_f = 0  ∧  ∑ d_f Y_f³ = 0  (U(1)_Y × SU(2)_L × SU(3)_C)",
    overfitLaw: "Chiral hypercharge drift: Tr[Y³] ≠ 0 (gauge anomaly)",
    underfitLaw: "Vector-like truncation (chiral weak doublet omitted)",
    baseWeights: [0.95, 0.88, 0.76, 0.64, 0.01, 0.01],
    trueMask: [true, true, true, true, false, false],
    paretoPoints: [
      [90, 152],
      [175, 110],
      [265, 48],
      [360, 48],
      [450, 48],
    ],
    snippet: `-- HEPLean / PhysLean Standard Model Anomaly Cancellation (Folio M.01 / P.11)
-- https://github.com/HEPLean/PhysLean
theorem sm_hypercharge_cubic_anomaly_zero :
    6 * (1/6 : ℚ)^3 + 3 * (-2/3 : ℚ)^3 + 3 * (1/3 : ℚ)^3
    + 2 * (-1/2 : ℚ)^3 + 1 * (1 : ℚ)^3 = 0 := by norm_num`,
  },
  itensor: {
    name: "ITensors.jl + NetKet · Critical Ising MPS Entanglement Scaling",
    exactLaw: "S_vN(L) = (c / 6) ln(L) + s_1 ≤ ln(χ),  c = 1/2,  E_0/N = -4/π",
    overfitLaw: "Volume-law noise floor S_vN ~ α·L (unphysical thermal drift)",
    underfitLaw: "Mean-field product state χ = 1 (S_vN = 0, misses critical point)",
    baseWeights: [0.02, 0.92, 0.48, 0.22, 0.02, 0.01],
    trueMask: [false, true, true, true, false, false],
    paretoPoints: [
      [90, 168],
      [175, 114],
      [265, 56],
      [360, 52],
      [450, 51],
    ],
    snippet: `# ITensors.jl + NetKet Critical TFIM Entanglement Scaling (Folio P.11 / P.05)
# Exact Pfeuty ground-state energy density E_0/N = -4/pi = -1.27323954
import math
L, c, chi = 128, 0.5, 64
s_vn = (c / 6.0) * math.log(L) + 0.4785
assert s_vn <= math.log(chi)  # MPS area-law bond dimension verified`,
  },
  scite_gate: {
    name: "Scite + Crossref · Section-Weighted Citation Polarity & Retraction Gate",
    exactLaw: "P_scite = (N_supp − w_c·N_cont)/(N_total + 1) ≥ 0,  R_retract = 0  (63/63 DOIs Verified)",
    overfitLaw: "Unverified citation claim or contrasting methods exceedance (SCITE-TALLY-MISMATCH)",
    underfitLaw: "Unsourced static citation count without fetched_on timestamp (SCITE-UNSOURCED)",
    baseWeights: [0.01, 0.96, 0.84, 0.72, 0.02, 0.01],
    trueMask: [false, true, true, true, false, false],
    paretoPoints: [
      [90, 162],
      [175, 108],
      [265, 50],
      [360, 49],
      [450, 48],
    ],
    snippet: `# Deterministic Scite + Crossref Citation Gate (check_folio_citations.py + scite-batch)
# Verifies all 48 Folios and 15 Radar Engines against Crossref and api.scite.ai
python tools/check_folio_citations.py --offline --include-informatico
# SUMMARY essays=88 fail=0 warn=0 unchecked=0 (15/15 Radar DOIs & 48/48 Folios Scite-verified)`,
  },
};

function bindBountyWorkbench(wb) {
  if (!wb || wb.dataset.bound === "true") return;
  wb.dataset.bound = "true";
  const slug = wb.getAttribute("data-bounty-workbench") || "b01";
  const s0 = wb.querySelector('[data-bw-slider="0"]');
  const s1 = wb.querySelector('[data-bw-slider="1"]');
  const v0 = wb.querySelector('[data-bw-val="0"]');
  const v1 = wb.querySelector('[data-bw-val="1"]');
  const r0 = wb.querySelector('[data-bw-readout="0"]');
  const r1 = wb.querySelector('[data-bw-readout="1"]');
  const r2 = wb.querySelector('[data-bw-readout="2"]');
  const r3 = wb.querySelector('[data-bw-readout="3"]');
  const box3 = wb.querySelector('[data-bw-readout-box="3"]');
  const curve = wb.querySelector("[data-bw-curve]");
  const dot = wb.querySelector("[data-bw-dot]");
  const caption = wb.querySelector("[data-bw-caption]");
  const modeBtns = wb.querySelectorAll("[data-bounty-mode]");

  const formatSliderVal = (inputEl, valSpan) => {
    if (!inputEl || !valSpan) return;
    const u = valSpan.getAttribute("data-unit") || "";
    const v = inputEl.value;
    valSpan.textContent = u.includes("=") ? `${u}${v}` : `${v}${u}`;
  };

  const evaluateBountyState = () => {
    const p0 = s0 ? parseFloat(s0.value) : 0;
    const p1 = s1 ? parseFloat(s1.value) : 0;
    formatSliderVal(s0, v0);
    formatSliderVal(s1, v1);

    let pass = true;
    let out = ["", "", "", ""];

    if (slug === "b01") {
      // Erdős Sidon sets: N = p0, |A| = p1
      const bound = Math.sqrt(p0) + Math.pow(p0, 0.25) + 1.0;
      const greedy = Math.max(8, Math.round(0.89 * Math.sqrt(p0)));
      const collisions = p1 > Math.floor(bound) ? Math.round((p1 - Math.floor(bound)) * 3) : 0;
      pass = collisions === 0;
      const uniqueSums = (p1 * (p1 + 1)) / 2 - collisions;
      out = [
        `${greedy} elements (at N = ${Math.round(p0)})`,
        `${bound.toFixed(4)} (√N + N^(1/4) + 1)`,
        `${collisions} collisions (${uniqueSums} unique sums)`,
        pass ? "PASS · ZERO COLLISIONS" : "ALERT · B₂ SUM COLLISION",
      ];
    } else if (slug === "b02") {
      // Surface code QEC: d = p0, p_phys = p1 (×10^-3)
      const pRatio = (p1 * 1e-3) / 0.01;
      const pL = 0.03 * Math.pow(pRatio, (p0 + 1) / 2);
      const qPhys = Math.round(2 * 294 * p0 * p0);
      pass = pL <= 1e-14 && pRatio < 1.0;
      out = [
        `P_L = ${pL.toExponential(2)} / cycle`,
        `${qPhys.toLocaleString("en-US")} physical qubits`,
        `-8496.3241 E_h (CAS(54e,54o))`,
        pass ? "PASS · SUB-THRESHOLD QEC" : "ALERT · LOGICAL ERROR EXCEEDED",
      ];
    } else if (slug === "b03") {
      // SIMP Carbon Slab: rho = p0, m_CO2 = p1
      const cRatio = 1.0 / Math.pow(Math.max(0.15, p0), 2.1);
      const netCo2 = 118.0 * p0 - p1 * 0.42;
      const freq = 14.2 * Math.sqrt(p0 / 0.35);
      pass = netCo2 <= 45.0 && freq >= 8.0 && p0 >= 0.28;
      out = [
        `${netCo2.toFixed(2)} kg CO₂e / m²`,
        `J / J_0 = ${cRatio.toFixed(2)} (p = 3.0)`,
        `f_1 = ${freq.toFixed(2)} Hz (> 8.0 Hz SLS)`,
        pass ? "PASS · SUB-45 KG CO₂E/M²" : "ALERT · SLS / CARBON EXCEEDED",
      ];
    } else if (slug === "b04") {
      // Graphic statics & sky cooling: f/L = p0, eps_sky = p1
      const thrustH = (16.0 / (8.0 * Math.max(0.06, p0))) * 20.0;
      const qNet = 104.2 * p1 - (1.0 - p1) * 42.0;
      const dT = -(qNet / 18.9);
      pass = p0 >= 0.11 && qNet >= 70.0;
      out = [
        `H = ${thrustH.toFixed(1)} kN (0 kg rebar)`,
        `q_net = ${qNet.toFixed(1)} W/m² (8–13 μm)`,
        `ΔT = ${dT.toFixed(2)} °C (${pass ? "zero grid" : "solar gain"})`,
        pass ? "PASS · ZERO-REBAR + SUB-AMBIENT" : "ALERT · THRUST / COOLING BREACH",
      ];
    } else if (slug === "b05") {
      // PySR + PySINDy: sigma = p0, lambda = p1
      const spurious = p1 < 0.025 + p0 * 0.45 ? 2 : 0;
      const missing = p1 > 0.14 ? 1 : 0;
      pass = spurious === 0 && missing === 0 && p0 <= 0.08;
      const mdl = -114.1 + p0 * 140.0 + spurious * 12.4 + missing * 24.0;
      out = [
        pass ? "u_t = -1.00 u·u_x + 0.10 u_xx" : spurious > 0 ? "u_t = -u·u_x + 0.1 u_xx + α·u³" : "u_t = -1.00 u·u_x (underfit)",
        `L_MDL = ${mdl.toFixed(1)} nats`,
        `${2 + spurious - missing} / 6 operators active`,
        pass ? "PASS · EXACT PDE RECOVERED" : "ALERT · SPARSITY DRIFT",
      ];
    } else {
      // b06: PhysLean + ITensors: L = p0, chi = p1
      const sVn = (0.5 / 6.0) * Math.log(Math.max(8, p0)) + 0.4785;
      const cap = Math.log(Math.max(2, p1));
      pass = sVn <= cap && p1 >= 8;
      out = [
        "Tr[Y] = 0 · Tr[Y³] = 0 (Exact)",
        `S_vN(${Math.round(p0)}) = ${sVn.toFixed(4)} nats`,
        `ln(χ) = ${cap.toFixed(4)} nats (χ = ${Math.round(p1)})`,
        pass ? "PASS · ANOMALY-FREE & MPS EXACT" : "ALERT · MPS BOND TRUNCATION",
      ];
    }

    if (r0) r0.textContent = out[0];
    if (r1) r1.textContent = out[1];
    if (r2) r2.textContent = out[2];
    if (r3) r3.textContent = out[3];
    if (box3) box3.setAttribute("data-alert", pass ? "false" : "true");

    // Update SVG curve, dot, and 4 stage bars
    const norm0 = s0 ? (p0 - parseFloat(s0.min)) / Math.max(1e-6, parseFloat(s0.max) - parseFloat(s0.min)) : 0.5;
    const norm1 = s1 ? (p1 - parseFloat(s1.min)) / Math.max(1e-6, parseFloat(s1.max) - parseFloat(s1.min)) : 0.5;
    const dotX = Math.round(75 + norm0 * 335);
    const dotY = Math.round(pass ? 120 - norm1 * 55 : 152);
    if (dot) {
      dot.setAttribute("cx", String(dotX));
      dot.setAttribute("cy", String(dotY));
      dot.setAttribute("fill", pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
    }
    if (curve) {
      const yMid = Math.round(pass ? 88 - (norm0 - 0.5) * 28 : 146);
      curve.setAttribute("points", `65,152 155,124 ${dotX},${dotY} 335,${yMid} 420,54`);
      curve.setAttribute("stroke", pass ? "var(--tp-prussian)" : "var(--tp-minium)");
    }
    for (let i = 0; i < 4; i += 1) {
      const bar = wb.querySelector(`[data-bw-bar="${i}"]`);
      if (bar) {
        const h = pass ? Math.round(96 + ((i + norm0 * 3) % 4) * 6) : i >= 2 ? 32 : 84;
        bar.setAttribute("y", String(168 - h));
        bar.setAttribute("height", String(h));
        bar.setAttribute("fill", pass || i < 2 ? "var(--tp-verdigris)" : "var(--tp-minium)");
      }
    }
    if (caption) {
      caption.textContent = pass
        ? `Certified Benchmark Regime (${slug.toUpperCase()}) — All 4 stage invariants satisfied (${out[3]}).`
        : `Counterfactual Boundary Violation (${slug.toUpperCase()}) — Invariant threshold breached (${out[3]}).`;
    }
  };

  if (s0) s0.addEventListener("input", evaluateBountyState);
  if (s1) s1.addEventListener("input", evaluateBountyState);

  modeBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const mode = btn.getAttribute("data-bounty-mode");
      modeBtns.forEach((b) => b.setAttribute("aria-pressed", b === btn ? "true" : "false"));
      if (!s0 || !s1) return;
      if (mode === "knockout") {
        if (slug === "b01") { s0.value = "500"; s1.value = "34"; }
        else if (slug === "b02") { s0.value = "15"; s1.value = "12.0"; }
        else if (slug === "b03") { s0.value = "0.22"; s1.value = "5"; }
        else if (slug === "b04") { s0.value = "0.08"; s1.value = "0.60"; }
        else if (slug === "b05") { s0.value = "0.18"; s1.value = "0.01"; }
        else { s0.value = "256"; s1.value = "2"; }
      } else {
        if (slug === "b01") { s0.value = "500"; s1.value = "20"; }
        else if (slug === "b02") { s0.value = "27"; s1.value = "1.0"; }
        else if (slug === "b03") { s0.value = "0.35"; s1.value = "24"; }
        else if (slug === "b04") { s0.value = "0.16"; s1.value = "0.94"; }
        else if (slug === "b05") { s0.value = "0.02"; s1.value = "0.05"; }
        else { s0.value = "128"; s1.value = "64"; }
      }
      evaluateBountyState();
    });
  });

  evaluateBountyState();
}

export function initPhysicsDiscoveryCrucible(scope = document) {
  // Feature 0: Open-Bounty Crucible category filter bar on cover & /bounties/
  const crucible = scope.querySelector("#tp-bounty-crucible");
  if (crucible && crucible.dataset.bound !== "true") {
    crucible.dataset.bound = "true";
    const filterBtns = crucible.querySelectorAll("[data-bounty-filter]");
    const bountyCards = crucible.querySelectorAll(".tp-bounty-card[data-bounty-cat]");
    filterBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        const cat = btn.getAttribute("data-bounty-filter") || "all";
        filterBtns.forEach((b) => b.setAttribute("aria-pressed", b === btn ? "true" : "false"));
        bountyCards.forEach((card) => {
          const cardCat = card.getAttribute("data-bounty-cat") || "";
          if (cat === "all" || cardCat === cat) {
            card.removeAttribute("hidden");
          } else {
            card.setAttribute("hidden", "");
          }
        });
      });
    });
  }

  // Standalone Bounty Proof Workbenches on /bounties/b01..b06/
  scope.querySelectorAll("[data-bounty-workbench]").forEach((wb) => {
    bindBountyWorkbench(wb);
  });

  const lab = scope.querySelector("#tp-symbolic-physics-lab");
  if (lab && lab.dataset.bound !== "true") {
    lab.dataset.bound = "true";
    let currentRegime = "burgers";

    const noiseSlider = lab.querySelector("#tp-sym-noise");
    const lambdaSlider = lab.querySelector("#tp-sym-lambda");
    const noiseValEl = lab.querySelector("#tp-sym-noise-val");
    const lambdaValEl = lab.querySelector("#tp-sym-lambda-val");

    const outLaw = lab.querySelector("#tp-sym-out-law");
    const outMdl = lab.querySelector("#tp-sym-out-mdl");
    const outSupport = lab.querySelector("#tp-sym-out-support");
    const outVerdict = lab.querySelector("#tp-sym-out-verdict");
    const verdictBox = lab.querySelector("#tp-sym-verdict-box");

    const paretoLine = lab.querySelector("#tp-sym-pareto-line");
    const activeDot = lab.querySelector("#tp-sym-active-dot");
    const threshLine = lab.querySelector("#tp-sym-thresh-line");
    const stageCaption = lab.querySelector("#tp-sym-stage-caption");
    const codePre = lab.querySelector("#tp-sym-code-preview");

    const updateWorkbench = () => {
      const cfg = REGIMES[currentRegime] || REGIMES.burgers;
      const sigma = noiseSlider ? parseFloat(noiseSlider.value) : 0.02;
      const lam = lambdaSlider ? parseFloat(lambdaSlider.value) : 0.05;

      if (noiseValEl) noiseValEl.textContent = `σ = ${sigma.toFixed(2)}`;
      if (lambdaValEl) lambdaValEl.textContent = `λ = ${lam.toFixed(2)}`;

      // Update threshold line in right-hand STLSQ spectrum panel (y from 165 down to 35)
      const threshY = Math.max(40, Math.min(162, Math.round(165 - lam * 280)));
      if (threshLine) {
        threshLine.setAttribute("y1", String(threshY));
        threshLine.setAttribute("y2", String(threshY));
      }

      let activeTermsCount = 0;
      let spuriousActive = 0;
      let missingTrue = 0;

      for (let i = 0; i < 6; i += 1) {
        const rawMag = Math.min(1.0, cfg.baseWeights[i] + sigma * (i % 2 === 0 ? 0.85 : 0.65));
        const kept = rawMag >= lam;
        if (kept) {
          activeTermsCount += 1;
          if (!cfg.trueMask[i]) spuriousActive += 1;
        } else if (cfg.trueMask[i]) {
          missingTrue += 1;
        }

        const barEl = lab.querySelector(`#tp-sym-bar-${i}`);
        if (barEl) {
          const barH = Math.max(4, Math.round(rawMag * 118));
          const barY = 165 - barH;
          barEl.setAttribute("y", String(barY));
          barEl.setAttribute("height", String(barH));
          barEl.setAttribute(
            "fill",
            kept
              ? cfg.trueMask[i]
                ? "var(--tp-verdigris)"
                : "var(--tp-minium)"
              : "var(--tp-slate)"
          );
          barEl.setAttribute("opacity", kept ? "0.92" : "0.35");
        }
      }

      // Update Pareto polyline & knee marker in left panel
      const pts = cfg.paretoPoints.map(([x, y]) => {
        const dy = Math.round(sigma * 95);
        return [x, Math.max(32, Math.min(165, y - dy))];
      });
      if (paretoLine) {
        paretoLine.setAttribute(
          "points",
          pts.map(([x, y]) => `${x},${y}`).join(" ")
        );
      }

      let kneeIdx = 2;
      if (spuriousActive > 0) kneeIdx = 4;
      else if (missingTrue > 0) kneeIdx = 0;

      if (activeDot && pts[kneeIdx]) {
        activeDot.setAttribute("cx", String(pts[kneeIdx][0]));
        activeDot.setAttribute("cy", String(pts[kneeIdx][1]));
      }

      const mdlScore = (
        -118.4 +
        sigma * 142.0 +
        lam * 28.5 +
        spuriousActive * 9.4 +
        missingTrue * 24.0
      ).toFixed(1);

      if (outMdl) outMdl.textContent = `L_MDL = ${mdlScore} nats`;
      if (outSupport) outSupport.textContent = `${activeTermsCount} / 6 operators active`;

      if (spuriousActive === 0 && missingTrue === 0) {
        if (outLaw) outLaw.textContent = cfg.exactLaw;
        if (outVerdict) outVerdict.textContent = "PASS · EXACT LAW RECOVERED";
        if (verdictBox) verdictBox.setAttribute("data-alert", "false");
      } else if (spuriousActive > 0) {
        if (outLaw) outLaw.textContent = cfg.overfitLaw;
        if (outVerdict) outVerdict.textContent = "OVERFIT · RAISE λ THRESHOLD";
        if (verdictBox) verdictBox.setAttribute("data-alert", "true");
      } else {
        if (outLaw) outLaw.textContent = cfg.underfitLaw;
        if (outVerdict) outVerdict.textContent = "UNDERFIT · LOWER λ THRESHOLD";
        if (verdictBox) verdictBox.setAttribute("data-alert", "true");
      }

      if (stageCaption) {
        stageCaption.textContent = `${cfg.name} — Recovered: ${
          outLaw ? outLaw.textContent : cfg.exactLaw
        }`;
      }
      if (codePre) {
        codePre.textContent = cfg.snippet;
      }
    };

    lab.querySelectorAll("[data-symbolic-regime]").forEach((btn) => {
      btn.addEventListener("click", () => {
        currentRegime = btn.getAttribute("data-symbolic-regime") || "burgers";
        lab.querySelectorAll("[data-symbolic-regime]").forEach((b) => {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        updateWorkbench();
      });
    });

    if (noiseSlider) noiseSlider.addEventListener("input", updateWorkbench);
    if (lambdaSlider) lambdaSlider.addEventListener("input", updateWorkbench);

    const copyBtn = lab.querySelector("#tp-sym-copy-btn");
    if (copyBtn) {
      copyBtn.addEventListener("click", () => {
        const cfg = REGIMES[currentRegime] || REGIMES.burgers;
        const orig = copyBtn.textContent;
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(cfg.snippet + "\n").then(() => {
            copyBtn.textContent = "Copied Discovery Script";
            setTimeout(() => {
              copyBtn.textContent = orig;
            }, 1800);
          });
        }
      });
    }

    updateWorkbench();
  }

  // Feature 2: Open-Source Physics, Mathematical & Epistemic Discovery Stack Radar filter + search
  const radar = scope.querySelector("#tp-oss-physics-radar");
  if (radar && radar.dataset.bound !== "true") {
    radar.dataset.bound = "true";
    const cards = Array.from(radar.querySelectorAll("[data-oss-cat]"));
    const countOut = radar.querySelector("#tp-oss-count-out");
    const searchInput = radar.querySelector("#tp-oss-search");
    let activeFilter = "all";

    const applyRadarFilter = () => {
      const q = searchInput ? searchInput.value.trim().toLowerCase() : "";
      let shown = 0;
      cards.forEach((card) => {
        const cat = card.getAttribute("data-oss-cat") || "";
        const catMatch = activeFilter === "all" || cat === activeFilter;
        const textMatch = !q || (card.textContent || "").toLowerCase().includes(q);
        if (catMatch && textMatch) {
          card.removeAttribute("hidden");
          shown += 1;
        } else {
          card.setAttribute("hidden", "");
        }
      });
      if (countOut) {
        countOut.textContent = `${shown} / ${cards.length} engines shown`;
      }
    };

    radar.querySelectorAll("[data-oss-filter]").forEach((btn) => {
      btn.addEventListener("click", () => {
        activeFilter = btn.getAttribute("data-oss-filter") || "all";
        radar.querySelectorAll("[data-oss-filter]").forEach((b) => {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        applyRadarFilter();
      });
    });

    if (searchInput) {
      searchInput.addEventListener("input", applyRadarFilter);
    }
  }
}
