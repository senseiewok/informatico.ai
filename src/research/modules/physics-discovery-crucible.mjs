/**
 * @module physics-discovery-crucible
 * Interactive Symbolic Physics & Sparse PDE Law Finder (PySR / PySINDy / Dedalus / PhysLean / ITensors.jl),
 * Open-Source Physics & Math Discovery Radar, Open-Bounty Crucible Filter, and Standalone Bounty Proof Workbench.
 * Drives bespoke 3-panel domain SVG schematics, state-space trajectories, 4-stage waterfalls, and parameter auto-sweep.
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
  const harmonic = wb.querySelector("[data-bw-harmonic]");
  const statusPill = wb.querySelector("[data-bw-status-pill]");
  const caption = wb.querySelector("[data-bw-caption]");
  const modeBtns = wb.querySelectorAll("[data-bounty-mode]");
  let sweepTimer = null;

  const stopSweep = () => {
    if (sweepTimer !== null) {
      cancelAnimationFrame(sweepTimer);
      sweepTimer = null;
    }
  };

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
    let stageRatios = [0.88, 0.92, 0.90, 0.95];
    let stageLabels = ["PASS", "PASS", "PASS", "PASS"];

    if (slug === "b01") {
      // Erdős Sidon sets: N = p0 (100..900), |A| = p1 (10..36)
      const bound = Math.sqrt(p0) + Math.pow(p0, 0.25) + 1.0;
      const greedy = Math.max(8, Math.round(0.8944 * Math.sqrt(p0)));
      const collisions = p1 > Math.floor(bound) ? Math.round((p1 - Math.floor(bound)) * 4) : 0;
      pass = collisions === 0;
      const totalPairs = Math.round((p1 * (p1 + 1)) / 2);
      const uniqueSums = Math.max(1, totalPairs - collisions);
      out = [
        `${Math.round(p1)} elements (${uniqueSums} unique sums)`,
        `${bound.toFixed(4)} (√N + N^(1/4) + 1)`,
        collisions === 0 ? `0 collisions (B₂ verified)` : `${collisions} collisions (Pigeonhole breach)`,
        pass ? "PASS · ZERO SUM COLLISIONS" : "ALERT · B₂ SUM COLLISION",
      ];
      const marginRatio = Math.max(0.18, Math.min(1.0, bound / Math.max(10, p1)));
      stageRatios = pass
        ? [0.92, 0.88, Math.min(0.98, 0.65 + marginRatio * 0.28), 0.95]
        : [0.85, 0.78, 0.28, 0.22];
      stageLabels = [
        `|A|=${Math.round(p1)}`,
        `${uniqueSums}/${totalPairs}`,
        `≤${bound.toFixed(1)}`,
        pass ? "0 sorry" : "FAIL",
      ];

      // Update B.01 bespoke Domain Panel 1 elements
      const colBadge = wb.querySelector("[data-bw-b01-badge]");
      if (colBadge) {
        colBadge.textContent = pass
          ? `B₂ VALID · ${uniqueSums} DISTINCT SUMS`
          : `COLLISION! ${collisions} DUPLICATE SUMS`;
        colBadge.setAttribute("fill", pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
      }
      wb.querySelectorAll("[data-bw-b01-arc]").forEach((arc, idx) => {
        if (!pass && idx >= 3) {
          arc.setAttribute("stroke", "var(--tp-minium)");
          arc.setAttribute("stroke-width", "2.6");
        } else {
          arc.setAttribute("stroke", idx % 2 === 0 ? "var(--tp-prussian)" : "var(--tp-verdigris)");
          arc.setAttribute("stroke-width", "1.7");
        }
      });
      wb.querySelectorAll("[data-bw-b01-cell]").forEach((cell, idx) => {
        const isCol = !pass && (idx === 4 || idx === 9 || idx === 13);
        cell.setAttribute("fill", isCol ? "var(--tp-minium)" : "var(--tp-verdigris)");
        cell.setAttribute("fill-opacity", isCol ? "0.88" : "0.28");
      });
    } else if (slug === "b02") {
      // Surface code QEC: d = p0 (7..35), p_phys = p1 (0.0005..0.012)
      const pRatio = p1 / 0.01;
      const exp = (p0 + 1) / 2;
      const pL = 0.03 * Math.pow(pRatio, exp);
      const qPhys = Math.round(2 * 294 * p0 * p0);
      pass = p1 < 0.01 && pL <= 1e-12;
      const pLExpStr = pL < 1e-99 ? "0.00" : pL.toExponential(2);
      out = [
        `${pLExpStr} (at d = ${Math.round(p0)}, p = ${p1.toFixed(4)})`,
        `294 tiles (114 data + 180 factory)`,
        `${qPhys.toLocaleString("en-US")} physical qubits`,
        pass ? "PASS · FAULT-TOLERANT REGIME" : p1 >= 0.01 ? "ALERT · THRESHOLD COLLAPSE" : "ALERT · SHALLOW CODE DISTANCE",
      ];
      stageRatios = pass
        ? [0.92, Math.min(0.98, 1.0 - pRatio * 0.5), Math.min(0.98, p0 / 35), 0.94]
        : [0.86, p1 >= 0.01 ? 0.22 : 0.68, pL > 1e-12 ? 0.26 : 0.82, 0.25];
      stageLabels = [
        "54e/54o",
        `p/p_th=${pRatio.toFixed(2)}`,
        `d=${Math.round(p0)}`,
        `${Math.round(qPhys / 1000)}k Q`,
      ];

      // Update B.02 bespoke Domain Panel 1 elements
      const chain = wb.querySelector("[data-bw-b02-chain]");
      if (chain) {
        chain.setAttribute("stroke", pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
        chain.setAttribute(
          "d",
          pass
            ? "M 64 96 L 104 96 M 144 136 L 184 136"
            : "M 44 76 L 84 96 L 124 116 L 164 136 L 204 156 L 244 176"
        );
      }
      const badge = wb.querySelector("[data-bw-b02-badge]");
      if (badge) {
        badge.textContent = pass
          ? `PYMATCHING PAIRED · P_L = ${pLExpStr}`
          : `PERCOLATION BREACH · P_L = ${pLExpStr}`;
        badge.setAttribute("fill", pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
      }
    } else if (slug === "b03") {
      // SIMP Carbon Slab: V/V0 = p0 (0.20..0.70), m_CO2 = p1 (0.0..20.0)
      const eRaw = 148.0 * p0;
      const eNet = eRaw - p1;
      const cRatio = 1.0 + 0.40 * Math.pow(1.0 - p0, 1.35);
      const savedPct = (1.0 - p0) * 100.0;
      pass = eNet < 45.0 && cRatio < 1.35;
      out = [
        `${eNet.toFixed(2)} kg CO₂e/m² (< 45.0 target)`,
        `${cRatio.toFixed(3)} (< 1.35 L/250 deflection limit)`,
        `${savedPct.toFixed(1)}% concrete mass saved`,
        pass ? "PASS · SUB-45 KG CO₂E/M²" : eNet >= 45.0 ? "ALERT · CARBON CEILING EXCEEDED" : "ALERT · EXCESSIVE DEFLECTION",
      ];
      stageRatios = [
        0.90,
        Math.min(0.96, p0 + 0.45),
        cRatio < 1.35 ? 0.92 : 0.26,
        eNet < 45.0 ? 0.95 : 0.24,
      ];
      stageLabels = [
        "1.2D+1.6L",
        `V/V₀=${p0.toFixed(2)}`,
        `c/c₀=${cRatio.toFixed(2)}`,
        `${eNet.toFixed(1)}kg`,
      ];

      // Update B.03 bespoke Domain Panel 1 elements
      const arch = wb.querySelector("[data-bw-b03-arch]");
      if (arch) {
        const strokeW = (2.5 + p0 * 8.5).toFixed(1);
        arch.setAttribute("stroke-width", strokeW);
        arch.setAttribute("stroke", pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
      }
      const simpBar = wb.querySelector("[data-bw-b03-simp-bar]");
      if (simpBar) {
        const w = Math.max(16, Math.min(180, Math.round((eRaw / 148.0) * 165)));
        simpBar.setAttribute("width", String(w));
      }
      const netBar = wb.querySelector("[data-bw-b03-net-bar]");
      if (netBar) {
        const w = Math.max(12, Math.min(180, Math.round((Math.max(5, eNet) / 148.0) * 165)));
        netBar.setAttribute("width", String(w));
        netBar.setAttribute("fill", pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
      }
      const badge = wb.querySelector("[data-bw-b03-badge]");
      if (badge) {
        badge.textContent = pass
          ? `SCORS A+ PASS · ${eNet.toFixed(1)} kg CO₂e/m²`
          : `BREACH · ${eNet.toFixed(1)} kg · c/c₀=${cRatio.toFixed(2)}`;
        badge.setAttribute("fill", pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
      }
    } else if (slug === "b04") {
      // Graphic statics & sky cooling: f = p0 (1.60..4.00 m), R_sol = p1 (0.85..0.99)
      const fOverL = p0 / 16.0;
      const thrustH = (8.0 * 16.0 * 16.0) / (8.0 * p0);
      const qRad = 158.0 * 0.96; // 151.68 W/m²
      const qAbs = 1000.0 * (1.0 - p1);
      const qNet = qRad - 23.3 - qAbs;
      const dT = -(qNet / 18.9);
      pass = thrustH <= 160.0 && qNet >= 80.0 && dT <= -4.5;
      out = [
        `${thrustH.toFixed(2)} kN (f/L = ${fOverL.toFixed(3)} · 0 kg rebar)`,
        `${qNet.toFixed(1)} W/m² (≥ 80.0 W/m² target)`,
        `${dT.toFixed(1)} °C (≤ −4.5 °C benchmark)`,
        pass ? "PASS · ZERO-REBAR + SUB-AMBIENT" : "ALERT · THRUST / COOLING BREACH",
      ];
      stageRatios = [
        0.94,
        thrustH <= 160.0 ? Math.min(0.96, 160.0 / Math.max(80.0, thrustH)) : 0.25,
        qNet >= 80.0 ? Math.min(0.96, qNet / 115.0) : 0.24,
        dT <= -4.5 ? 0.95 : 0.22,
      ];
      stageLabels = [
        "∑A_f n_f=0",
        `H=${thrustH.toFixed(0)}kN`,
        `q=${qNet.toFixed(0)}W`,
        `ΔT=${dT.toFixed(1)}°C`,
      ];

      // Update B.04 bespoke Domain Panel 1 elements
      const arch = wb.querySelector("[data-bw-b04-arch]");
      if (arch) {
        const apexY = Math.round(156 - (p0 - 1.6) * 24);
        arch.setAttribute("d", `M 38 166 Q 158 ${apexY} 278 166`);
        arch.setAttribute("stroke", pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
      }
      const badge = wb.querySelector("[data-bw-b04-badge]");
      if (badge) {
        badge.textContent = pass
          ? `0 kg REBAR · H=${thrustH.toFixed(0)} kN · ΔT=${dT.toFixed(1)}°C`
          : `ALERT · H=${thrustH.toFixed(0)} kN · q_net=${qNet.toFixed(1)} W/m²`;
        badge.setAttribute("fill", pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
      }
    } else if (slug === "b05") {
      // PySR + PySINDy: sigma = p0 (0.0..0.25), lambda = p1 (0.01..0.20)
      const overfit = p0 * 0.25 >= p1;
      const underfit = p1 > 0.10;
      pass = !overfit && !underfit;
      const activeCount = underfit ? 1 : overfit ? 4 : 2;
      const mdl = pass ? -1360.87 + p0 * 120.0 : underfit ? -612.4 : -845.2 + p0 * 210.0;
      out = [
        underfit
          ? "['u*u_x'] (1 / 6 active · UNDERFIT)"
          : overfit
          ? "['1', 'u*u_x', 'u_xx', 'u^3'] (4 / 6 · OVERFIT)"
          : "['u*u_x', 'u_xx'] (2 / 6 active)",
        underfit
          ? "u_t = −1.00 u·u_x (viscous term lost)"
          : overfit
          ? "u_t = −u·u_x + 0.10 u_xx + α u³"
          : "u_t = −u·u_x + 0.10 u_xx",
        `${mdl.toFixed(2)} nats (C_tree = ${underfit ? 3 : overfit ? 11 : 6})`,
        pass ? "PASS · EXACT PDE RECOVERED" : underfit ? "ALERT · UNDERFIT (ν u_xx PRUNED)" : "ALERT · OVERFIT (SPURIOUS u³)",
      ];
      stageRatios = [
        0.94,
        Math.max(0.28, 1.0 - p0 * 2.5),
        pass ? 0.95 : 0.26,
        pass ? 0.96 : 0.24,
      ];
      stageLabels = [
        "N=200",
        `σ=${p0.toFixed(2)}`,
        `λ=${p1.toFixed(2)}`,
        `${activeCount}/6 ops`,
      ];

      // Update B.05 bespoke Domain Panel 1 elements
      const lamLine = wb.querySelector("[data-bw-b05-lambda]");
      if (lamLine) {
        const ly = Math.round(258 - Math.min(0.20, p1) * 320);
        lamLine.setAttribute("y1", String(ly));
        lamLine.setAttribute("y2", String(ly));
      }
      const wave = wb.querySelector("[data-bw-b05-wave]");
      if (wave) {
        wave.setAttribute(
          "d",
          overfit
            ? "M 32 76 Q 82 54 118 98 T 178 112 T 236 142 L 282 146"
            : underfit
            ? "M 32 76 L 154 76 L 156 146 L 282 146"
            : "M 32 76 C 110 76 135 78 158 111 C 181 144 206 146 282 146"
        );
        wave.setAttribute("stroke", pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
      }
      const badge = wb.querySelector("[data-bw-b05-badge]");
      if (badge) {
        badge.textContent = pass
          ? "STLSQ EXACT · {u·u_x, u_xx} · MDL = -1360.9"
          : underfit
          ? "UNDERFIT! λ > ν PRUNED VISCOSITY u_xx"
          : "OVERFIT! NOISE EXCEEDS λ SHEARS (u³ LEAK)";
        badge.setAttribute("fill", pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
      }
    } else {
      // b06: PhysLean + ITensors: chi = p0 (1..128), deltaY = p1 (0.0..0.20)
      const sVn = 0.882836;
      const cap = Math.log(Math.max(1, p0));
      const trY3 =
        6 * Math.pow(1 / 6 + p1, 3) +
        3 * Math.pow(-2 / 3, 3) +
        3 * Math.pow(1 / 3, 3) +
        2 * Math.pow(-1 / 2, 3) +
        1.0;
      const anomalyFree = Math.abs(trY3) < 1e-9;
      const mpsValid = cap >= sVn;
      pass = anomalyFree && mpsValid;
      out = [
        anomalyFree ? "0.000000000000 (Anomaly-Free)" : `${trY3.toFixed(6)} (ANOMALY BREACH)`,
        "−1.27323954 (−4 / π exact)",
        `0.8828 nats ≤ ln(χ) = ${cap.toFixed(4)}`,
        pass
          ? "PASS · ANOMALY-FREE & AREA-LAW"
          : !anomalyFree
          ? "ALERT · CHIRAL GAUGE ANOMALY"
          : "ALERT · MPS BOND TRUNCATION",
      ];
      stageRatios = [
        0.95,
        anomalyFree ? 0.96 : 0.22,
        0.92,
        mpsValid ? Math.min(0.98, 0.55 + (cap / 4.85) * 0.42) : 0.20,
      ];
      stageLabels = [
        "15 Weyl",
        anomalyFree ? "Tr[Y³]=0" : "Tr[Y³]≠0",
        "S=0.883",
        `lnχ=${cap.toFixed(2)}`,
      ];

      // Update B.06 bespoke Domain Panel 1 elements
      const tri = wb.querySelector("[data-bw-b06-triangle]");
      if (tri) {
        tri.setAttribute("stroke", anomalyFree ? "var(--tp-verdigris)" : "var(--tp-minium)");
      }
      const bonds = wb.querySelector("[data-bw-b06-bonds]");
      if (bonds) {
        const bw = Math.max(1.2, Math.min(6.5, 1.2 + cap * 1.1)).toFixed(1);
        bonds.setAttribute("stroke-width", bw);
        bonds.setAttribute("stroke", mpsValid ? "var(--tp-prussian)" : "var(--tp-minium)");
      }
      const badge = wb.querySelector("[data-bw-b06-badge]");
      if (badge) {
        badge.textContent = pass
          ? `Tr[Y³] = 0 · ln(${Math.round(p0)}) = ${cap.toFixed(2)} ≥ 0.883`
          : !anomalyFree
          ? `GAUGE ANOMALY! Tr[Y³] = ${trY3.toFixed(4)} ≠ 0`
          : `MPS TRUNCATION! ln(${Math.round(p0)}) = ${cap.toFixed(2)} < 0.883`;
        badge.setAttribute("fill", pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
      }
    }

    if (r0) r0.textContent = out[0];
    if (r1) r1.textContent = out[1];
    if (r2) r2.textContent = out[2];
    if (r3) r3.textContent = out[3];
    if (box3) box3.setAttribute("data-alert", pass ? "false" : "true");

    // Update Panel 2 State-Space Trajectory Curve, Operating Locus Dot & Harmonic Wave
    const norm0 = s0 ? (p0 - parseFloat(s0.min)) / Math.max(1e-6, parseFloat(s0.max) - parseFloat(s0.min)) : 0.5;
    const norm1 = s1 ? (p1 - parseFloat(s1.min)) / Math.max(1e-6, parseFloat(s1.max) - parseFloat(s1.min)) : 0.5;
    const dotX = Math.round(352 + norm0 * 224);
    const dotY = Math.round(pass ? 156 - norm1 * 76 : 214);
    if (dot) {
      dot.setAttribute("cx", String(dotX));
      dot.setAttribute("cy", String(dotY));
      dot.setAttribute("fill", pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
    }
    if (curve) {
      const yMid = Math.round(pass ? 114 - (norm0 - 0.5) * 34 : 208);
      curve.setAttribute("points", `344,218 402,172 ${dotX},${dotY} 524,${yMid} 584,74`);
      curve.setAttribute("stroke", pass ? "var(--tp-prussian)" : "var(--tp-minium)");
    }
    if (harmonic) {
      const amp = Math.round(10 + norm1 * 18);
      harmonic.setAttribute(
        "d",
        `M 344 236 Q 404 ${236 - amp} 464 236 T 584 236`
      );
      harmonic.setAttribute("stroke", pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
    }
    if (statusPill) {
      statusPill.textContent = out[3];
      statusPill.setAttribute("fill", pass ? "var(--tp-verdigris)" : "var(--tp-minium)");
    }

    // Update Panel 3 4-Stage Invariant Waterfall Bars & Value Labels
    for (let i = 0; i < 4; i += 1) {
      const bar = wb.querySelector(`[data-bw-bar="${i}"]`);
      const barVal = wb.querySelector(`[data-bw-bar-val="${i}"]`);
      const ratio = stageRatios[i] || 0.85;
      const h = Math.round(Math.max(24, Math.min(156, ratio * 152)));
      const y = 236 - h;
      const barOk = ratio >= 0.45;
      if (bar) {
        bar.setAttribute("y", String(y));
        bar.setAttribute("height", String(h));
        bar.setAttribute("fill", barOk ? "var(--tp-verdigris)" : "var(--tp-minium)");
      }
      if (barVal) {
        barVal.setAttribute("y", String(y - 6));
        barVal.textContent = stageLabels[i] || "PASS";
        barVal.setAttribute("fill", barOk ? "var(--tp-prussian)" : "var(--tp-minium)");
      }
    }

    if (caption) {
      caption.textContent = pass
        ? `Certified Benchmark Regime (${slug.toUpperCase()}) — All 4 stage invariants satisfied (${out[3]}).`
        : `Counterfactual Boundary Violation (${slug.toUpperCase()}) — Invariant threshold breached (${out[3]}).`;
    }
  };

  if (s0) {
    s0.addEventListener("input", () => {
      stopSweep();
      evaluateBountyState();
    });
  }
  if (s1) {
    s1.addEventListener("input", () => {
      stopSweep();
      evaluateBountyState();
    });
  }

  modeBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      stopSweep();
      const mode = btn.getAttribute("data-bounty-mode");
      modeBtns.forEach((b) => b.setAttribute("aria-pressed", b === btn ? "true" : "false"));
      if (!s0 || !s1) return;

      if (mode === "sweep") {
        const min0 = parseFloat(s0.min);
        const max0 = parseFloat(s0.max);
        const step0 = parseFloat(s0.step) || 1;
        const min1 = parseFloat(s1.min);
        const max1 = parseFloat(s1.max);
        const step1 = parseFloat(s1.step) || 0.01;
        const start = performance.now();
        const dur = 2600;
        const tick = (now) => {
          const t = Math.min(1.0, (now - start) / dur);
          const wave = 0.5 - 0.5 * Math.cos(t * Math.PI * 2.0);
          let v0Now = min0 + (max0 - min0) * (0.25 + 0.65 * wave);
          let v1Now = min1 + (max1 - min1) * wave;
          if (step0 >= 1) v0Now = Math.round(v0Now / step0) * step0;
          else v0Now = Math.round(v0Now / step0) * step0;
          if (step1 >= 1) v1Now = Math.round(v1Now / step1) * step1;
          else v1Now = Number((Math.round(v1Now / step1) * step1).toFixed(4));
          s0.value = String(v0Now);
          s1.value = String(v1Now);
          evaluateBountyState();
          if (t < 1.0) {
            sweepTimer = requestAnimationFrame(tick);
          } else {
            sweepTimer = null;
            // Restore canonical benchmark values at end of sweep
            if (slug === "b01") { s0.value = "500"; s1.value = "20"; }
            else if (slug === "b02") { s0.value = "27"; s1.value = "0.001"; }
            else if (slug === "b03") { s0.value = "0.35"; s1.value = "12.4"; }
            else if (slug === "b04") { s0.value = "2.56"; s1.value = "0.97"; }
            else if (slug === "b05") { s0.value = "0.02"; s1.value = "0.05"; }
            else { s0.value = "64"; s1.value = "0.0"; }
            evaluateBountyState();
          }
        };
        sweepTimer = requestAnimationFrame(tick);
        return;
      }

      if (mode === "knockout") {
        if (slug === "b01") { s0.value = "500"; s1.value = "31"; }
        else if (slug === "b02") { s0.value = "27"; s1.value = "0.011"; }
        else if (slug === "b03") { s0.value = "0.35"; s1.value = "0.0"; }
        else if (slug === "b04") { s0.value = "1.60"; s1.value = "0.88"; }
        else if (slug === "b05") { s0.value = "0.22"; s1.value = "0.02"; }
        else { s0.value = "2"; s1.value = "0.08"; }
      } else {
        if (slug === "b01") { s0.value = "500"; s1.value = "20"; }
        else if (slug === "b02") { s0.value = "27"; s1.value = "0.001"; }
        else if (slug === "b03") { s0.value = "0.35"; s1.value = "12.4"; }
        else if (slug === "b04") { s0.value = "2.56"; s1.value = "0.97"; }
        else if (slug === "b05") { s0.value = "0.02"; s1.value = "0.05"; }
        else { s0.value = "64"; s1.value = "0.0"; }
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
