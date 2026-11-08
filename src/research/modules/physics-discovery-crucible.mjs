/**
 * @module physics-discovery-crucible
 * Interactive Symbolic Physics & Sparse PDE Law Finder (PySR / PySINDy / Dedalus / PhysLean / ITensors.jl)
 * and Open-Source Physics & Math Discovery Radar for Informatico.ai.
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
    snippet: `# PySINDy + Dedalus Spectral PDE Discovery (Folio P.07 / P.11)
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
    snippet: `# PySR Multi-Population Symbolic Regression (Folio P.05 / M.08)
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
    snippet: `# ITensors.jl + NetKet Critical TFIM Entanglement Scaling (Folio P.11 / P.12)
# Exact Pfeuty ground-state energy density E_0/N = -4/pi = -1.27323954
import math
L, c, chi = 128, 0.5, 64
s_vn = (c / 6.0) * math.log(L) + 0.4785
assert s_vn <= math.log(chi)  # MPS area-law bond dimension verified`,
  },
};

export function initPhysicsDiscoveryCrucible(scope = document) {
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

  // Feature 2: Open-Source Physics & Mathematical Discovery Stack Radar filter
  const radar = scope.querySelector("#tp-oss-physics-radar");
  if (radar && radar.dataset.bound !== "true") {
    radar.dataset.bound = "true";
    const cards = Array.from(radar.querySelectorAll("[data-oss-cat]"));
    const countOut = radar.querySelector("#tp-oss-count-out");

    radar.querySelectorAll("[data-oss-filter]").forEach((btn) => {
      btn.addEventListener("click", () => {
        const filter = btn.getAttribute("data-oss-filter") || "all";
        radar.querySelectorAll("[data-oss-filter]").forEach((b) => {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        let shown = 0;
        cards.forEach((card) => {
          const cat = card.getAttribute("data-oss-cat") || "";
          const match = filter === "all" || cat === filter;
          if (match) {
            card.removeAttribute("hidden");
            shown += 1;
          } else {
            card.setAttribute("hidden", "");
          }
        });
        if (countOut) {
          countOut.textContent = `${shown} / ${cards.length}`;
        }
      });
    });
  }
}
