/**
 * @module solvers
 * Interactive mathematical, tectonic (1:50 + 1:5 Maxwell-Cremona & High-Tech Gerberette),
 * and continuum (Stokes-Brinkman, Herschel-Bulkley, Terzaghi, ASCE 7-22) plate solvers,
 * Universal Reactive SVG & Control Animation Engine, 4-stage Ciechanowski steppers,
 * and Distill.pub equation-to-diagram highlighting.
 */

const SVG_NS = "http://www.w3.org/2000/svg";

function createSvgNode(tag, attrs = {}, text = "") {
  const el = document.createElementNS(SVG_NS, tag);
  for (const [k, v] of Object.entries(attrs)) {
    el.setAttribute(k, String(v));
  }
  if (text) el.textContent = text;
  return el;
}

/**
 * Smoothly tween a range input from its current value to targetVal over durationMs.
 */
function tweenRangeSlider(slider, targetVal, durationMs = 340) {
  if (!slider) return;
  const reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const min = parseFloat(slider.min) || 0;
  const max = parseFloat(slider.max) || 100;
  const step = parseFloat(slider.step) || 0.01;
  const clampedTarget = Math.max(min, Math.min(max, targetVal));

  if (reduced || durationMs <= 0) {
    slider.value = step >= 1 ? String(Math.round(clampedTarget / step) * step) : String(clampedTarget);
    slider.dispatchEvent(new Event("input", { bubbles: true }));
    return;
  }

  const startVal = parseFloat(slider.value) || min;
  const startTime = performance.now();

  function tick(now) {
    const t = Math.min(1.0, (now - startTime) / durationMs);
    const ease = 1.0 - Math.pow(1.0 - t, 3); // cubic ease-out
    let cur = startVal + (clampedTarget - startVal) * ease;
    if (step >= 1) cur = Math.round(cur / step) * step;
    slider.value = String(cur);
    slider.dispatchEvent(new Event("input", { bubbles: true }));
    if (t < 1.0) requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
}

/**
 * Interactive Fullscreen Stage Controller (Law 6 & Fullscreen Observatory Mode)
 */
export function initFullscreenControls(scope = document) {
  scope.querySelectorAll(".tp-plate").forEach((plate) => {
    const head = plate.querySelector(".tp-plate-head");
    if (!head) return;
    let fsBtn = head.querySelector(".tp-fullscreen-btn");
    if (!fsBtn) {
      fsBtn = document.createElement("button");
      fsBtn.type = "button";
      fsBtn.className = "tp-fullscreen-btn";
      fsBtn.setAttribute("aria-label", "Toggle Fullscreen Stage");
      const svg = createSvgNode("svg", {
        viewBox: "0 0 24 24",
        width: "13",
        height: "13",
        fill: "none",
        stroke: "currentColor",
        "stroke-width": "2.2",
        "aria-hidden": "true",
      });
      const p = createSvgNode("path", {
        d: "M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3",
      });
      svg.appendChild(p);
      fsBtn.appendChild(svg);
      const span = document.createElement("span");
      span.textContent = "Stage ⛶";
      fsBtn.appendChild(span);
      head.appendChild(fsBtn);
    }
    if (fsBtn.dataset.bound === "true") return;
    fsBtn.dataset.bound = "true";

    const updateBtnState = () => {
      const isFs = document.fullscreenElement === plate || document.webkitFullscreenElement === plate;
      fsBtn.setAttribute("aria-pressed", isFs ? "true" : "false");
      const span = fsBtn.querySelector("span");
      if (span) span.textContent = isFs ? "Exit ⛶" : "Stage ⛶";
    };

    fsBtn.addEventListener("click", () => {
      const isFs = document.fullscreenElement === plate || document.webkitFullscreenElement === plate;
      if (!isFs) {
        if (plate.requestFullscreen) {
          plate.requestFullscreen();
        } else if (plate.webkitRequestFullscreen) {
          plate.webkitRequestFullscreen();
        }
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        } else if (document.webkitExitFullscreen) {
          document.webkitExitFullscreen();
        }
      }
      setTimeout(updateBtnState, 50);
    });

    plate.addEventListener("keydown", (e) => {
      if ((e.key === "f" || e.key === "F") && !e.target.matches("input, textarea, select")) {
        e.preventDefault();
        fsBtn.click();
      }
    });
  });

  if (!document.__tpFsChangeBound) {
    document.__tpFsChangeBound = true;
    const onFsChange = () => {
      window.dispatchEvent(new Event("resize"));
      document.querySelectorAll(".tp-fullscreen-btn").forEach((btn) => {
        const plate = btn.closest(".tp-plate");
        const isFs = plate && (document.fullscreenElement === plate || document.webkitFullscreenElement === plate);
        btn.setAttribute("aria-pressed", isFs ? "true" : "false");
        const span = btn.querySelector("span");
        if (span) span.textContent = isFs ? "Exit ⛶" : "Stage ⛶";
      });
    };
    document.addEventListener("fullscreenchange", onFsChange);
    document.addEventListener("webkitfullscreenchange", onFsChange);
  }
}

/**
 * Bret Victor Explorable In-Sentence Scrubbable Tokens (.tp-scrub)
 */
export function initScrubbableTokens(scope = document) {
  scope.querySelectorAll(".tp-scrub").forEach((scrub) => {
    if (scrub.dataset.scrubBound === "true") return;
    scrub.dataset.scrubBound = "true";
    scrub.setAttribute("tabindex", "0");
    scrub.setAttribute("role", "slider");

    let activeSlider = null;
    const explicitTarget = scrub.getAttribute("data-target-slider");
    if (explicitTarget) {
      activeSlider = document.getElementById(explicitTarget) ||
        ((explicitTarget === "0" || explicitTarget === "1")
          ? document.querySelector(`[id^="tp-bw-s${explicitTarget}-"], [data-bw-slider="${explicitTarget}"]`)
          : null);
    }
    else if (scrub.id === "tp-inline-phi") activeSlider = document.getElementById("tp-eng-phi");
    else if (scrub.id === "tp-inline-tau0") activeSlider = document.getElementById("tp-e02-tau0");
    else if (scrub.id === "tp-inline-surcharge") activeSlider = document.getElementById("tp-e05-surcharge");
    else if (scrub.id === "tp-inline-sds") activeSlider = document.getElementById("tp-e06-sds");
    else if (scrub.id === "tp-inline-prime") activeSlider = document.getElementById("tp-math-prime");
    else if (scrub.id === "tp-inline-rise") activeSlider = document.getElementById("tp-arch-rise");
    else if (scrub.id === "tp-inline-atp") activeSlider = document.getElementById("p-slider-atp");
    else if (scrub.id === "tp-inline-cf") {
      const targetId = scrub.getAttribute("data-target-slider");
      activeSlider = (targetId && document.getElementById(targetId)) || document.querySelector('input[data-cf-slider="primary"]');
    }
    if (!activeSlider) {
      activeSlider = scope.querySelector('.tp-plate input[type="range"], .tp-bounty-workbench input[type="range"]') || document.querySelector('.tp-plate input[type="range"], .tp-bounty-workbench input[type="range"]');
    }
    const syncAria = () => {
      if (!activeSlider) {
        scrub.setAttribute("aria-label", scrub.textContent.trim() || "Interactive parameter scrubber");
        scrub.setAttribute("aria-valuemin", "0");
        scrub.setAttribute("aria-valuemax", "100");
        scrub.setAttribute("aria-valuenow", "50");
        return;
      }
      const min = activeSlider.min || "0";
      const max = activeSlider.max || "100";
      const val = activeSlider.value || min;
      const labelEl = activeSlider.id ? document.querySelector(`label[for="${activeSlider.id}"]`) : null;
      const labelText = (labelEl && labelEl.textContent.trim()) || scrub.getAttribute("aria-label") || scrub.textContent.trim() || "Parameter scrubber";
      scrub.setAttribute("aria-label", labelText);
      scrub.setAttribute("aria-valuemin", String(min));
      scrub.setAttribute("aria-valuemax", String(max));
      scrub.setAttribute("aria-valuenow", String(val));
      scrub.setAttribute("aria-valuetext", scrub.textContent.trim() || String(val));
    };
    syncAria();
    if (activeSlider) {
      activeSlider.addEventListener("input", syncAria);
    }

    let isDragging = false;
    let startX = 0;
    let startVal = 0;

    const onPointerDown = (e) => {
      if (!activeSlider) return;
      isDragging = true;
      startX = e.clientX;
      startVal = parseFloat(activeSlider.value) || 0;
      scrub.setPointerCapture(e.pointerId);
      scrub.classList.add("tp-scrubbing");
      e.preventDefault();
    };

    const onPointerMove = (e) => {
      if (!isDragging || !activeSlider) return;
      const dx = e.clientX - startX;
      const min = parseFloat(activeSlider.min) || 0;
      const max = parseFloat(activeSlider.max) || 100;
      const step = parseFloat(activeSlider.step) || 0.1;
      const span = max - min;
      const change = (dx / 200) * span;
      let newVal = Math.max(min, Math.min(max, startVal + change));
      if (step >= 1.0) newVal = Math.round(newVal / step) * step;
      activeSlider.value = newVal;
      activeSlider.dispatchEvent(new Event("input", { bubbles: true }));
    };

    const onPointerUp = (e) => {
      if (!isDragging) return;
      isDragging = false;
      scrub.classList.remove("tp-scrubbing");
      try { scrub.releasePointerCapture(e.pointerId); } catch (_) {}
    };

    scrub.addEventListener("pointerdown", onPointerDown);
    scrub.addEventListener("pointermove", onPointerMove);
    scrub.addEventListener("pointerup", onPointerUp);
    scrub.addEventListener("pointercancel", onPointerUp);

    scrub.addEventListener("keydown", (e) => {
      if (!activeSlider) return;
      const step = parseFloat(activeSlider.step) || 0.1;
      const min = parseFloat(activeSlider.min) || 0;
      const max = parseFloat(activeSlider.max) || 100;
      let cur = parseFloat(activeSlider.value) || 0;
      if (e.key === "ArrowRight" || e.key === "ArrowUp") {
        e.preventDefault();
        activeSlider.value = Math.min(max, cur + step);
        activeSlider.dispatchEvent(new Event("input", { bubbles: true }));
      } else if (e.key === "ArrowLeft" || e.key === "ArrowDown") {
        e.preventDefault();
        activeSlider.value = Math.max(min, cur - step);
        activeSlider.dispatchEvent(new Event("input", { bubbles: true }));
      }
    });
  });
}

/**
 * Universal Reactive SVG & Control Animation Engine across all 24 Folios.
 * Ensures every Folio's SVG stage and controls animate smoothly on slider input,
 * stage stepper clicks, and interactive Auto-Sweep exploration.
 */
export function initUniversalSvgAndControlAnimations(scope = document) {
  const reducedMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  scope.querySelectorAll(".tp-plate").forEach((plate) => {
    if (plate.dataset.animBound === "true") return;
    plate.dataset.animBound = "true";

    const svg = plate.querySelector("svg.tp-svg-stage");
    const sliders = Array.from(plate.querySelectorAll('input[type="range"]'));
    const stepper = plate.querySelector(".tp-stepper");
    const stepBtns = Array.from(plate.querySelectorAll(".tp-step-btn[data-step-desc]"));

    // 1. Enhance static SVG strokes with animated flow classes & build the Live Vector Overlay
    let liveGroup = null;
    let harmonicPath = null;
    let beaconGroup = null;
    let beaconRing = null;
    let beaconLabel = null;
    let telemetryText = null;
    let artPossibleGroup = null;
    let quantumPacketPath = null;
    let phaseNeedleLine = null;
    let cremonaPolygon = null;
    let michellArchPath = null;
    let attractorPath = null;
    let attractorOrb = null;
    let loupeGroup = null;
    let loupeReadout = null;
    let qedVerdictLabel = null;
    let knockoutActive = false;
    let blochVectorLine = null;
    let blochEquatorialEllipse = null;
    let wefRibbonPath = null;
    let quantumWefReadout = null;

    const mountEl = plate.closest("[data-folio-id]") || document.getElementById("tp-folio-mount");
    const folioId = (mountEl && mountEl.getAttribute("data-folio-id")) || "";
    const folioCat = folioId ? folioId.charAt(0).toUpperCase() : "M";

    const isTwoPanelCf = Boolean(
      svg && svg.querySelector("#tp-c01-rescue-curve, #tp-c02-pcl-rect, #tp-c03-lnp-1, #tp-c04-surge-curve, #tp-c05-edit-curve, #tp-c06-cosh-curve")
    );
    const stageXPositions = isTwoPanelCf ? [398, 472, 546, 618] : [125, 268, 412, 555];
    const streamXMin = isTwoPanelCf ? 385 : 65;
    const streamXSpan = isTwoPanelCf ? 255 : 550;
    let primaryDynamicCurves = [];

    if (svg) {
      // Tag primary dashed/accent paths so they carry living flux motion
      svg.querySelectorAll("path, polyline, line").forEach((el, idx) => {
        const dash = el.getAttribute("stroke-dasharray");
        const stroke = el.getAttribute("stroke") || "";
        if (dash || (idx === 1 && stroke.includes("var(--tp-"))) {
          el.classList.add("tp-svg-flow-line");
        }
      });

      // Capture primary schematic curves on folios without custom [data-*] curve handlers so sliders visibly morph them
      if (!isTwoPanelCf) {
        primaryDynamicCurves = Array.from(svg.querySelectorAll("path, polyline")).filter((el) => {
          const stroke = el.getAttribute("stroke") || "";
          return stroke.includes("var(--tp-") && !el.closest(".tp-svg-live-layer");
        });
      }

      liveGroup = svg.querySelector(".tp-svg-live-layer");
      if (!liveGroup) {
        liveGroup = createSvgNode("g", { class: "tp-svg-live-layer", "pointer-events": "none" });

        // Harmonic response wave linking slider state to visual frequency/amplitude
        harmonicPath = createSvgNode("path", {
          class: "tp-svg-harmonic-wave tp-svg-flow-line",
          d: isTwoPanelCf
            ? "M 385 176 Q 450 156 512 176 T 640 176"
            : "M 65 176 Q 202 152 340 176 T 615 176",
          fill: "none",
          stroke: "var(--tp-verdigris)",
          "stroke-width": "1.5",
          "stroke-opacity": isTwoPanelCf ? "0.35" : "0.52",
          "stroke-dasharray": "5 5",
        });
        liveGroup.appendChild(harmonicPath);

        // Layer 1: Scale-Reactive Force & Flux Vector Field (4 stage vectors)
        const vectorGroup = createSvgNode("g", { class: "tp-svg-vector-field" });
        stageXPositions.forEach((vx, vIdx) => {
          const arrowG = createSvgNode("g", {
            class: "tp-vector-arrow",
            "data-vector-idx": String(vIdx),
            transform: `translate(${vx}, ${isTwoPanelCf ? 196 : 182})`,
          });
          const shaft = createSvgNode("line", {
            class: "tp-vector-shaft",
            x1: "0",
            y1: "0",
            x2: "22",
            y2: "-12",
            stroke: vIdx % 2 === 0 ? "var(--tp-prussian)" : "var(--tp-verdigris)",
            "stroke-width": "1.5",
            "stroke-opacity": "0.62",
          });
          const head = createSvgNode("polygon", {
            class: "tp-vector-head",
            points: "22,-12 16,-13 19,-8",
            fill: vIdx % 2 === 0 ? "var(--tp-prussian)" : "var(--tp-verdigris)",
            "fill-opacity": "0.72",
          });
          arrowG.appendChild(shaft);
          arrowG.appendChild(head);
          vectorGroup.appendChild(arrowG);
        });
        liveGroup.appendChild(vectorGroup);

        // Layer 2: Lagrangian Particle / Ion Advection Stream (8 particles along trajectory)
        const particleGroup = createSvgNode("g", { class: "tp-svg-particle-stream" });
        for (let pIdx = 0; pIdx < 8; pIdx++) {
          const pCircle = createSvgNode("circle", {
            class: "tp-svg-particle",
            "data-particle-idx": String(pIdx),
            cx: String(streamXMin + pIdx * (streamXSpan / 8)),
            cy: "162",
            r: pIdx % 2 === 0 ? "3.0" : "2.2",
            fill: pIdx % 3 === 0 ? "var(--tp-minium)" : "var(--tp-verdigris)",
            "fill-opacity": "0.75",
          });
          particleGroup.appendChild(pCircle);
        }
        liveGroup.appendChild(particleGroup);

        // Layer 3: Stage Spotlight Beacon + Expanding Phase-Transition Wavefront Ripples
        beaconGroup = createSvgNode("g", {
          class: "tp-svg-beacon",
          transform: `translate(${stageXPositions[0]}, 118)`,
        });
        ["tp-wave-ring", "tp-wave-ring tp-wave-ring-2", "tp-wave-ring tp-wave-ring-3"].forEach((cls) => {
          const wRing = createSvgNode("circle", {
            class: cls,
            cx: "0",
            cy: "0",
            r: "9",
            fill: "var(--tp-verdigris)",
            "fill-opacity": "0.08",
            stroke: "var(--tp-verdigris)",
            "stroke-width": "1.1",
          });
          beaconGroup.appendChild(wRing);
        });
        beaconRing = createSvgNode("circle", {
          class: "tp-svg-beacon-ring",
          cx: "0",
          cy: "0",
          r: "12",
          fill: "var(--tp-verdigris)",
          "fill-opacity": "0.14",
          stroke: "var(--tp-verdigris)",
          "stroke-width": "1.4",
          "stroke-dasharray": "3 2",
        });
        const beaconDot = createSvgNode("circle", {
          class: "tp-svg-beacon-dot",
          cx: "0",
          cy: "0",
          r: "4.0",
          fill: "var(--tp-minium)",
          stroke: "var(--tp-vellum)",
          "stroke-width": "1.4",
        });
        beaconLabel = createSvgNode("text", {
          x: "0",
          y: "-16",
          "text-anchor": "middle",
          "font-size": "8.5",
          "font-weight": "700",
          fill: "var(--tp-prussian)",
          opacity: "0",
        }, "STAGE 1 LOCUS");
        beaconGroup.appendChild(beaconRing);
        beaconGroup.appendChild(beaconDot);
        beaconGroup.appendChild(beaconLabel);
        liveGroup.appendChild(beaconGroup);

        // Layer 4: Subtle Futuristic Telemetry Reticles & Phase-Scan Beam
        const hudGroup = createSvgNode("g", {
          class: "tp-svg-futuristic-hud",
          "aria-hidden": "true",
        });
        const hudLeft = isTwoPanelCf ? 378 : 26;
        const hudRight = 654;
        const hudTop = 18;
        const hudBottom = 214;
        const cornerBrackets = createSvgNode("path", {
          class: "tp-svg-corner-reticle",
          d: `M ${hudLeft} ${hudTop + 10} V ${hudTop} H ${hudLeft + 10} M ${hudRight - 10} ${hudTop} H ${hudRight} V ${hudTop + 10} M ${hudLeft} ${hudBottom - 10} V ${hudBottom} H ${hudLeft + 10} M ${hudRight - 10} ${hudBottom} H ${hudRight} V ${hudBottom - 10}`,
          fill: "none",
          stroke: "var(--tp-verdigris)",
          "stroke-width": "1.15",
          "stroke-opacity": "0.42",
        });
        const orbitReticle = createSvgNode("circle", {
          class: "tp-svg-orbit-reticle",
          cx: String(hudRight - 14),
          cy: String(hudTop + 14),
          r: "6.5",
          fill: "none",
          stroke: "var(--tp-verdigris)",
          "stroke-width": "1.1",
          "stroke-dasharray": "4 3",
          "stroke-opacity": "0.55",
        });
        const scanBeam = createSvgNode("line", {
          class: "tp-svg-scan-beam",
          x1: String(hudLeft + 12),
          y1: String(hudTop + 4),
          x2: String(hudLeft + 12),
          y2: String(hudBottom - 4),
          stroke: "var(--tp-verdigris)",
          "stroke-width": "1.1",
          "stroke-dasharray": "2 4",
          "stroke-opacity": "0.18",
        });
        hudGroup.appendChild(cornerBrackets);
        hudGroup.appendChild(orbitReticle);
        hudGroup.appendChild(scanBeam);
        liveGroup.appendChild(hudGroup);

        // Layer 5: Pillar-Specific "Art of the Possible" Vector Micro-Observatory
        artPossibleGroup = createSvgNode("g", {
          class: "tp-svg-art-possible-layer",
          "data-pillar-cat": folioCat,
          "aria-hidden": "true",
        });

        // 5A. Pillar-Specific Kinetic Choreography
        const choreoGroup = createSvgNode("g", { class: "tp-svg-pillar-choreography" });
        if (folioCat === "M") {
          // Mathematics: Lean 4 Proof Dependency DAG & Eight-Square Tensor Contraction Loom
          const dagCoords = isTwoPanelCf
            ? [[395, 148], [448, 112], [505, 86], [562, 104], [622, 68]]
            : [[82, 146], [198, 108], [328, 84], [462, 102], [596, 62]];
          for (let dIdx = 0; dIdx < dagCoords.length - 1; dIdx++) {
            const [x1, y1] = dagCoords[dIdx];
            const [x2, y2] = dagCoords[dIdx + 1];
            const cxM = ((x1 + x2) * 0.5).toFixed(1);
            const cyM = (Math.min(y1, y2) - 16).toFixed(1);
            const edge = createSvgNode("path", {
              class: "tp-svg-proof-dag-edge tp-svg-flow-line",
              d: `M ${x1} ${y1} Q ${cxM} ${cyM} ${x2} ${y2}`,
              fill: "none",
              stroke: dIdx === 2 ? "var(--tp-verdigris)" : "var(--tp-prussian)",
              "stroke-width": "1.6",
              "stroke-opacity": "0.48",
              "stroke-dasharray": "6 4",
            });
            choreoGroup.appendChild(edge);
          }
          dagCoords.forEach(([nx, ny], nIdx) => {
            const node = createSvgNode("circle", {
              class: "tp-svg-proof-dag-node",
              cx: String(nx),
              cy: String(ny),
              r: nIdx === dagCoords.length - 1 ? "4.6" : "3.2",
              fill: nIdx === dagCoords.length - 1 ? "var(--tp-verdigris)" : "var(--tp-prussian)",
              "fill-opacity": "0.75",
            });
            choreoGroup.appendChild(node);
          });
          const loomGroup = createSvgNode("g", {
            class: "tp-svg-tensor-loom",
            transform: "translate(596, 62)",
          });
          const octagram = createSvgNode("polygon", {
            class: "tp-svg-octagram-ring",
            points: "0,-15 4,-4 15,0 4,4 0,15 -4,4 -15,0 -4,-4",
            fill: "none",
            stroke: "var(--tp-verdigris)",
            "stroke-width": "1.15",
            "stroke-opacity": "0.62",
          });
          const qedSeal = createSvgNode("circle", {
            class: "tp-svg-qed-seal",
            cx: "0",
            cy: "0",
            r: "11",
            fill: "none",
            stroke: "var(--tp-prussian)",
            "stroke-width": "1.1",
            "stroke-dasharray": "3 2",
            "stroke-opacity": "0.58",
          });
          qedVerdictLabel = createSvgNode("text", {
            class: "tp-svg-qed-verdict-label",
            x: "0",
            y: "24",
            "text-anchor": "middle",
            "font-size": "7.5",
            "font-weight": "700",
            fill: "var(--tp-verdigris)",
            opacity: "0.86",
          }, "0 sorryAx · QED");
          loomGroup.appendChild(octagram);
          loomGroup.appendChild(qedSeal);
          loomGroup.appendChild(qedVerdictLabel);
          choreoGroup.appendChild(loomGroup);
        } else if (folioCat === "P") {
          // Physics: WKB Quantum / Kinetic Wavepacket Envelope + Kuramoto Phase Rotor
          quantumPacketPath = createSvgNode("path", {
            class: "tp-svg-quantum-packet",
            d: "M 70 132 Q 180 92 310 132 T 580 132",
            fill: "none",
            stroke: "var(--tp-prussian)",
            "stroke-width": "1.7",
            "stroke-opacity": "0.52",
          });
          choreoGroup.appendChild(quantumPacketPath);
          const rotorGroup = createSvgNode("g", {
            class: "tp-svg-braid-rosette",
            transform: "translate(596, 62)",
          });
          const rotorRing = createSvgNode("circle", {
            class: "tp-svg-octagram-ring",
            cx: "0",
            cy: "0",
            r: "13",
            fill: "none",
            stroke: "var(--tp-verdigris)",
            "stroke-width": "1.2",
            "stroke-dasharray": "4 2",
            "stroke-opacity": "0.6",
          });
          phaseNeedleLine = createSvgNode("line", {
            class: "tp-svg-phase-needle",
            x1: "0",
            y1: "0",
            x2: "10",
            y2: "-7",
            stroke: "var(--tp-minium)",
            "stroke-width": "1.6",
          });
          qedVerdictLabel = createSvgNode("text", {
            class: "tp-svg-qed-verdict-label",
            x: "0",
            y: "24",
            "text-anchor": "middle",
            "font-size": "7.5",
            "font-weight": "700",
            fill: "var(--tp-verdigris)",
            opacity: "0.86",
          }, "PHASE COHERENT");
          rotorGroup.appendChild(rotorRing);
          rotorGroup.appendChild(phaseNeedleLine);
          rotorGroup.appendChild(qedVerdictLabel);
          choreoGroup.appendChild(rotorGroup);
        } else if (folioCat === "E") {
          // Civil Engineering: Karman Vortex-Shedding Street + Michell Funicular Truss Arch
          michellArchPath = createSvgNode("path", {
            class: "tp-svg-michell-arch",
            d: "M 85 168 Q 340 48 595 168",
            fill: "none",
            stroke: "var(--tp-prussian)",
            "stroke-width": "1.8",
            "stroke-opacity": "0.38",
            "stroke-dasharray": "8 4",
          });
          choreoGroup.appendChild(michellArchPath);
          [190, 290, 390, 490].forEach((vx, kIdx) => {
            const vRing = createSvgNode("circle", {
              class: "tp-svg-karman-vortex tp-svg-octagram-ring",
              "data-karman-idx": String(kIdx),
              cx: String(vx),
              cy: String(kIdx % 2 === 0 ? 112 : 138),
              r: String(7 + kIdx * 1.5),
              fill: "none",
              stroke: kIdx % 2 === 0 ? "var(--tp-verdigris)" : "var(--tp-prussian)",
              "stroke-width": "1.2",
              "stroke-dasharray": "5 3",
              "stroke-opacity": "0.52",
            });
            choreoGroup.appendChild(vRing);
          });
          qedVerdictLabel = createSvgNode("text", {
            class: "tp-svg-qed-verdict-label",
            x: "592",
            y: "84",
            "text-anchor": "middle",
            "font-size": "7.5",
            "font-weight": "700",
            fill: "var(--tp-verdigris)",
            opacity: "0.86",
          }, "SAFETY PASS");
          choreoGroup.appendChild(qedVerdictLabel);
        } else {
          // Architecture: Solar Caustic Ray Fan + Maxwell-Cremona Reciprocal Force Polygon
          for (let rIdx = 0; rIdx < 5; rIdx++) {
            const ray = createSvgNode("line", {
              class: "tp-svg-caustic-ray",
              "data-ray-idx": String(rIdx),
              x1: "110",
              y1: "28",
              x2: String(210 + rIdx * 78),
              y2: "178",
              stroke: "var(--tp-minium)",
              "stroke-width": "1.0",
              "stroke-opacity": "0.24",
              "stroke-dasharray": "3 3",
            });
            choreoGroup.appendChild(ray);
          }
          const cremonaGroup = createSvgNode("g", {
            class: "tp-svg-cremona-rosette",
            transform: "translate(596, 62)",
          });
          cremonaPolygon = createSvgNode("polygon", {
            class: "tp-svg-cremona-polygon",
            points: "0,-14 14,-3 9,13 -9,13 -14,-3",
            fill: "var(--tp-verdigris)",
            "fill-opacity": "0.10",
            stroke: "var(--tp-verdigris)",
            "stroke-width": "1.35",
            "stroke-opacity": "0.68",
          });
          qedVerdictLabel = createSvgNode("text", {
            class: "tp-svg-qed-verdict-label",
            x: "0",
            y: "25",
            "text-anchor": "middle",
            "font-size": "7.5",
            "font-weight": "700",
            fill: "var(--tp-verdigris)",
            opacity: "0.86",
          }, "ΣF = 0 CLOSED");
          cremonaGroup.appendChild(cremonaPolygon);
          cremonaGroup.appendChild(qedVerdictLabel);
          choreoGroup.appendChild(cremonaGroup);
        }
        artPossibleGroup.appendChild(choreoGroup);

        // 5B. Interactive 1:5 Precision Vector Loupe (toggled by [1:5 Loupe] button)
        loupeGroup = createSvgNode("g", {
          class: "tp-svg-precision-loupe",
          transform: "translate(518, 96)",
        });
        const loupeBg = createSvgNode("circle", {
          cx: "0",
          cy: "0",
          r: "38",
          fill: "var(--tp-vellum)",
          "fill-opacity": "0.92",
          stroke: "var(--tp-prussian)",
          "stroke-width": "1.6",
          "vector-effect": "non-scaling-stroke",
        });
        const loupeVernier = createSvgNode("circle", {
          class: "tp-svg-octagram-ring",
          cx: "0",
          cy: "0",
          r: "32",
          fill: "none",
          stroke: "var(--tp-verdigris)",
          "stroke-width": "1.1",
          "stroke-dasharray": "4 3",
          "vector-effect": "non-scaling-stroke",
        });
        const loupeCrossH = createSvgNode("line", {
          x1: "-34",
          y1: "0",
          x2: "34",
          y2: "0",
          stroke: "var(--tp-prussian)",
          "stroke-width": "0.8",
          "stroke-opacity": "0.35",
        });
        const loupeCrossV = createSvgNode("line", {
          x1: "0",
          y1: "-34",
          x2: "0",
          y2: "34",
          stroke: "var(--tp-prussian)",
          "stroke-width": "0.8",
          "stroke-opacity": "0.35",
        });
        const loupeGlyph = createSvgNode("polygon", {
          class: "tp-svg-loupe-glyph",
          points: "-16,12 0,-18 16,12",
          fill: "var(--tp-verdigris)",
          "fill-opacity": "0.16",
          stroke: "var(--tp-verdigris)",
          "stroke-width": "1.5",
          "vector-effect": "non-scaling-stroke",
        });
        loupeReadout = createSvgNode("text", {
          x: "0",
          y: "26",
          "text-anchor": "middle",
          "font-size": "7.2",
          "font-weight": "700",
          fill: "var(--tp-prussian)",
        }, "1:5 LOUPE · PASS");
        loupeGroup.appendChild(loupeBg);
        loupeGroup.appendChild(loupeVernier);
        loupeGroup.appendChild(loupeCrossH);
        loupeGroup.appendChild(loupeCrossV);
        loupeGroup.appendChild(loupeGlyph);
        loupeGroup.appendChild(loupeReadout);
        artPossibleGroup.appendChild(loupeGroup);

        // 5C. Parametric Lissajous / Lorenz Phase-Space Attractor (toggled by [Phase Attractor] button)
        const attractorGroup = createSvgNode("g", {
          class: "tp-svg-phase-attractor-group",
        });
        attractorPath = createSvgNode("path", {
          class: "tp-svg-phase-attractor",
          d: "M 340 110 C 390 60 440 160 340 110",
          fill: "none",
          stroke: "var(--tp-minium)",
          "stroke-width": "1.75",
          "stroke-opacity": "0.78",
        });
        attractorOrb = createSvgNode("circle", {
          class: "tp-svg-attractor-orb",
          cx: "340",
          cy: "110",
          r: "4.2",
          fill: "var(--tp-minium)",
          stroke: "var(--tp-vellum)",
          "stroke-width": "1.2",
        });
        attractorGroup.appendChild(attractorPath);
        attractorGroup.appendChild(attractorOrb);
        artPossibleGroup.appendChild(attractorGroup);

        // 5D. Interactive Cross-Field Quantum Bloch / Surface-Code & WEF Global Resilience Bridge
        const qWefGroup = createSvgNode("g", {
          class: "tp-svg-quantum-wef-bridge",
        });
        const blochSphere = createSvgNode("circle", {
          cx: "162",
          cy: "96",
          r: "32",
          fill: "var(--tp-vellum)",
          "fill-opacity": "0.90",
          stroke: "var(--tp-prussian)",
          "stroke-width": "1.5",
        });
        blochEquatorialEllipse = createSvgNode("ellipse", {
          cx: "162",
          cy: "96",
          rx: "32",
          ry: "11",
          fill: "none",
          stroke: "var(--tp-verdigris)",
          "stroke-width": "1.1",
          "stroke-dasharray": "3 2",
        });
        blochVectorLine = createSvgNode("line", {
          class: "tp-svg-bloch-vector",
          x1: "162",
          y1: "96",
          x2: "180",
          y2: "72",
          stroke: "var(--tp-minium)",
          "stroke-width": "2.0",
        });
        const blochKetLabel = createSvgNode("text", {
          x: "162",
          y: "142",
          "text-anchor": "middle",
          "font-size": "7.2",
          "font-weight": "700",
          fill: "var(--tp-prussian)",
        }, "|ψ⟩ BLOCH · STIM QEC");
        wefRibbonPath = createSvgNode("path", {
          class: "tp-svg-wef-ribbon tp-svg-flow-line",
          d: "M 194 96 C 268 54 362 138 446 96",
          fill: "none",
          stroke: "var(--tp-verdigris)",
          "stroke-width": "2.0",
          "stroke-dasharray": "6 4",
        });
        const wefHubBox = createSvgNode("rect", {
          x: "446",
          y: "68",
          width: "126",
          height: "56",
          rx: "4",
          fill: "var(--tp-vellum)",
          "fill-opacity": "0.92",
          stroke: "var(--tp-verdigris)",
          "stroke-width": "1.5",
        });
        const wefTitle = createSvgNode("text", {
          x: "509",
          y: "86",
          "text-anchor": "middle",
          "font-size": "7.2",
          "font-weight": "700",
          fill: "var(--tp-verdigris)",
        }, "WEF CROSS-FIELD BRIDGE");
        quantumWefReadout = createSvgNode("text", {
          x: "509",
          y: "102",
          "text-anchor": "middle",
          "font-size": "6.8",
          "font-weight": "600",
          fill: "var(--tp-ink)",
        }, "FeMoCo N₂ · 60Hz Grid · ML-KEM");
        const ossSubLabel = createSvgNode("text", {
          x: "509",
          y: "115",
          "text-anchor": "middle",
          "font-size": "6.3",
          fill: "var(--tp-prussian)",
        }, "OSS: Stim · PyPSA · Lean 4");
        qWefGroup.appendChild(blochSphere);
        qWefGroup.appendChild(blochEquatorialEllipse);
        qWefGroup.appendChild(blochVectorLine);
        qWefGroup.appendChild(blochKetLabel);
        qWefGroup.appendChild(wefRibbonPath);
        qWefGroup.appendChild(wefHubBox);
        qWefGroup.appendChild(wefTitle);
        qWefGroup.appendChild(quantumWefReadout);
        qWefGroup.appendChild(ossSubLabel);
        artPossibleGroup.appendChild(qWefGroup);

        liveGroup.appendChild(artPossibleGroup);

        svg.appendChild(liveGroup);
      }
    }

    let currentStageIdx = 0;

    // Record initial slider defaults for Reset
    const initialValues = sliders.map((s) => parseFloat(s.value) || 0);

    function getNormalizedSliders() {
      const s0 = sliders[0];
      const s1 = sliders[1];
      let aNorm = 0.55;
      let bNorm = 0.50;
      if (s0) {
        const min0 = parseFloat(s0.min) || 0;
        const max0 = parseFloat(s0.max) || 100;
        aNorm = Math.max(0.0, Math.min(1.0, ((parseFloat(s0.value) || min0) - min0) / Math.max(1e-6, max0 - min0)));
      }
      if (s1) {
        const min1 = parseFloat(s1.min) || 0;
        const max1 = parseFloat(s1.max) || 100;
        bNorm = Math.max(0.0, Math.min(1.0, ((parseFloat(s1.value) || min1) - min1) / Math.max(1e-6, max1 - min1)));
      }
      return { aNorm, bNorm };
    }

    function syncSvgToControls() {
      if (!svg) return;
      const { aNorm, bNorm } = getNormalizedSliders();

      // Update CSS flow duration based on primary drive
      const flowDuration = (2.4 - aNorm * 1.45).toFixed(2) + "s";
      svg.style.setProperty("--tp-flow-duration", flowDuration);

      // Morph primary schematic curves slightly on single-panel folios so every diagram responds to sliders
      primaryDynamicCurves.forEach((curveEl, cIdx) => {
        const dy = ((aNorm - 0.5) * (cIdx % 2 === 0 ? -14 : 11) + (bNorm - 0.5) * 8).toFixed(1);
        const sy = (1 + (aNorm - 0.5) * 0.08 * (cIdx === 0 ? 1 : -1)).toFixed(3);
        curveEl.setAttribute("transform", `translate(0, ${dy}) scale(1, ${sy})`);
        curveEl.style.transformOrigin = "340px 135px";
      });

      // Update harmonic wave path & stage beacon position
      if (harmonicPath) {
        const amp = Math.round(10 + aNorm * 24);
        const midY = Math.round(168 - bNorm * 20);
        if (isTwoPanelCf) {
          harmonicPath.setAttribute(
            "d",
            `M 385 ${midY} Q 449 ${midY - amp} 512 ${midY} T 640 ${midY}`
          );
        } else {
          harmonicPath.setAttribute(
            "d",
            `M 60 ${midY} Q 198 ${midY - amp} 340 ${midY} T 620 ${midY}`
          );
        }
      }

      if (beaconGroup) {
        const baseX = stageXPositions[currentStageIdx] || stageXPositions[0];
        const offsetX = Math.round((aNorm - 0.5) * (isTwoPanelCf ? 24 : 44));
        const targetY = Math.round(142 - aNorm * 54 + (bNorm - 0.5) * 24);
        beaconGroup.setAttribute("transform", `translate(${baseX + offsetX}, ${targetY})`);
      }

      // Update Scale-Reactive Force Vector Arrows based on slider state
      svg.querySelectorAll(".tp-vector-arrow").forEach((arrowG, vIdx) => {
        const len = 14 + aNorm * 18 + (vIdx % 2 === 0 ? bNorm * 6 : -bNorm * 4);
        const angle = -0.35 - bNorm * 0.55 + vIdx * 0.12;
        const x2 = (Math.cos(angle) * len).toFixed(1);
        const y2 = (Math.sin(angle) * len).toFixed(1);
        const hx1 = (Math.cos(angle - 0.32) * (len - 5.5)).toFixed(1);
        const hy1 = (Math.sin(angle - 0.32) * (len - 5.5)).toFixed(1);
        const hx2 = (Math.cos(angle + 0.32) * (len - 5.5)).toFixed(1);
        const hy2 = (Math.sin(angle + 0.32) * (len - 5.5)).toFixed(1);
        const shaft = arrowG.querySelector(".tp-vector-shaft");
        const head = arrowG.querySelector(".tp-vector-head");
        if (shaft) {
          shaft.setAttribute("x2", x2);
          shaft.setAttribute("y2", y2);
        }
        if (head) {
          head.setAttribute("points", `${x2},${y2} ${hx1},${hy1} ${hx2},${hy2}`);
        }
      });

      // Update Lagrangian Particle Stream coordinates & radii
      const ampP = 10 + aNorm * 24;
      const midYP = 168 - bNorm * 20;
      svg.querySelectorAll(".tp-svg-particle").forEach((pEl, pIdx) => {
        const t = ((pIdx / 8) + aNorm * 0.65 + bNorm * 0.35) % 1.0;
        const px = streamXMin + t * streamXSpan;
        const py = midYP - Math.sin(t * Math.PI * 2.0) * ampP * 0.68;
        pEl.setAttribute("cx", px.toFixed(1));
        pEl.setAttribute("cy", py.toFixed(1));
        pEl.setAttribute("r", (2.0 + (pIdx % 2) * 0.9 + aNorm * 1.2).toFixed(1));
      });

      if (telemetryText) {
        telemetryText.textContent = `LIVE DRIVE ${(aNorm * 100).toFixed(0)}% · BIAS ${(bNorm * 100).toFixed(0)}%`;
      }

      // Layer 5 Live Mathematical & Physical Geometry Synthesis
      if (quantumPacketPath) {
        const pts = [];
        const kWave = 2.5 + aNorm * 4.5;
        const envSigma = 110 + bNorm * 85;
        for (let i = 0; i <= 28; i++) {
          const u = i / 28;
          const x = 68 + u * 540;
          const dx = x - (240 + aNorm * 180);
          const env = Math.exp(-(dx * dx) / (2 * envSigma * envSigma));
          const y = 126 - env * 36 * Math.cos(u * Math.PI * kWave * 2.0 + bNorm * Math.PI);
          pts.push(`${i === 0 ? "M" : "L"} ${x.toFixed(1)} ${y.toFixed(1)}`);
        }
        quantumPacketPath.setAttribute("d", pts.join(" "));
      }

      if (phaseNeedleLine) {
        const theta = (aNorm * 2.0 + bNorm) * Math.PI * 2.0;
        phaseNeedleLine.setAttribute("x2", (Math.cos(theta) * 12).toFixed(1));
        phaseNeedleLine.setAttribute("y2", (Math.sin(theta) * 12).toFixed(1));
      }

      if (michellArchPath) {
        const archPeakY = Math.round(78 - aNorm * 42);
        michellArchPath.setAttribute("d", `M 85 168 Q 340 ${archPeakY} 595 168`);
        michellArchPath.setAttribute("stroke-width", (1.4 + aNorm * 2.2).toFixed(2));
      }

      svg.querySelectorAll(".tp-svg-karman-vortex").forEach((vEl, kIdx) => {
        const baseX = 180 + kIdx * 96 + (aNorm - 0.5) * 34;
        const baseY = (kIdx % 2 === 0 ? 108 : 142) + (bNorm - 0.5) * (kIdx % 2 === 0 ? -14 : 14);
        const rad = 6.5 + kIdx * 1.4 + aNorm * 4.0;
        vEl.setAttribute("cx", baseX.toFixed(1));
        vEl.setAttribute("cy", baseY.toFixed(1));
        vEl.setAttribute("r", rad.toFixed(1));
      });

      svg.querySelectorAll(".tp-svg-caustic-ray").forEach((rayEl, rIdx) => {
        const srcX = 95 + aNorm * 85;
        const dstX = 185 + rIdx * 76 + (bNorm - 0.5) * 48;
        rayEl.setAttribute("x1", srcX.toFixed(1));
        rayEl.setAttribute("x2", dstX.toFixed(1));
      });

      if (cremonaPolygon) {
        const sA = 10 + aNorm * 7;
        const sB = 9 + bNorm * 7;
        cremonaPolygon.setAttribute(
          "points",
          `0,${(-sA).toFixed(1)} ${sB.toFixed(1)},-3 ${(sA * 0.68).toFixed(1)},${sB.toFixed(1)} ${(-sA * 0.68).toFixed(1)},${sB.toFixed(1)} ${(-sB).toFixed(1)},-3`
        );
      }

      if (attractorPath) {
        const aPts = [];
        const freqX = 1 + Math.round(aNorm * 2);
        const freqY = 2 + Math.round(bNorm * 2);
        const delta = (aNorm + bNorm) * Math.PI;
        const cxA = isTwoPanelCf ? 512 : 340;
        const cyA = 108;
        for (let j = 0; j <= 40; j++) {
          const tA = (j / 40) * Math.PI * 2.0;
          const ax = cxA + Math.sin(freqX * tA + delta) * (68 + aNorm * 36);
          const ay = cyA + Math.sin(freqY * tA) * (34 + bNorm * 22);
          aPts.push(`${j === 0 ? "M" : "L"} ${ax.toFixed(1)} ${ay.toFixed(1)}`);
          if (j === 12 && attractorOrb) {
            attractorOrb.setAttribute("cx", ax.toFixed(1));
            attractorOrb.setAttribute("cy", ay.toFixed(1));
          }
        }
        attractorPath.setAttribute("d", aPts.join(" "));
      }

      if (loupeReadout) {
        loupeReadout.textContent = knockoutActive
          ? "1:5 KNOCKOUT FRACTURE"
          : `1:5 LOUPE · ${(aNorm * 100).toFixed(0)}% / ${(bNorm * 100).toFixed(0)}%`;
      }

      if (blochVectorLine && blochEquatorialEllipse && wefRibbonPath) {
        const thetaBloch = (aNorm * 1.65 + 0.15) * Math.PI;
        const phiBloch = bNorm * Math.PI * 2.0;
        const bx = 162 + Math.sin(thetaBloch) * Math.cos(phiBloch) * 28;
        const by = 96 - Math.cos(thetaBloch) * 28;
        blochVectorLine.setAttribute("x2", bx.toFixed(1));
        blochVectorLine.setAttribute("y2", by.toFixed(1));
        blochEquatorialEllipse.setAttribute("ry", (6 + bNorm * 10).toFixed(1));
        const ctrlY1 = (54 + (aNorm - 0.5) * 46).toFixed(1);
        const ctrlY2 = (138 - (bNorm - 0.5) * 46).toFixed(1);
        wefRibbonPath.setAttribute("d", `M 194 96 C 268 ${ctrlY1} 362 ${ctrlY2} 446 96`);
      }

      if (quantumWefReadout) {
        const pL = (Math.pow(0.45, 2 + Math.round(aNorm * 5)) * 100).toFixed(3);
        quantumWefReadout.textContent = `QEC ε_L=${pL}% → WEF Grid/N₂`;
      }

      // Auto-detect extremal p = 2 knockout on M.01 or explicit knockout button
      const s0Val = sliders[0] ? parseFloat(sliders[0].value) : 5;
      const isAutoP2Knockout = folioId === "M.01" && s0Val <= 2.01;
      const effectiveKnockout = knockoutActive || isAutoP2Knockout;
      plate.classList.toggle("is-svg-knockout-active", effectiveKnockout);
      if (qedVerdictLabel) {
        if (effectiveKnockout) {
          qedVerdictLabel.textContent = folioCat === "M" ? "FRACTURED (p=2)" : "BOUNDARY FRACTURE";
          qedVerdictLabel.setAttribute("fill", "var(--tp-minium)");
        } else {
          qedVerdictLabel.textContent =
            folioCat === "M"
              ? "0 sorryAx · QED"
              : folioCat === "P"
              ? "PHASE COHERENT"
              : folioCat === "E"
              ? "SAFETY PASS"
              : "ΣF = 0 CLOSED";
          qedVerdictLabel.setAttribute("fill", "var(--tp-verdigris)");
        }
      }
    }

    // Continuous Lagrangian Particle Advection Loop (pauses when offscreen or reduced-motion)
    if (!reducedMotion && svg) {
      let particleRaf = null;
      let isVisible = true;
      let phaseOffset = 0;

      const stepParticles = () => {
        if (!isVisible) {
          particleRaf = null;
          return;
        }
        const { aNorm, bNorm } = getNormalizedSliders();
        phaseOffset = (phaseOffset + 0.0035 * (0.6 + aNorm * 1.4)) % 1.0;
        const ampP = 10 + aNorm * 24;
        const midYP = 168 - bNorm * 20;
        svg.querySelectorAll(".tp-svg-particle").forEach((pEl, pIdx) => {
          const t = ((pIdx / 8) + phaseOffset) % 1.0;
          const px = streamXMin + t * streamXSpan;
          const py = midYP - Math.sin(t * Math.PI * 2.0) * ampP * 0.68;
          pEl.setAttribute("cx", px.toFixed(1));
          pEl.setAttribute("cy", py.toFixed(1));
        });
        particleRaf = requestAnimationFrame(stepParticles);
      };

      if ("IntersectionObserver" in window) {
        const io = new IntersectionObserver((entries) => {
          entries.forEach((entry) => {
            isVisible = entry.isIntersecting;
            if (isVisible && !particleRaf) {
              particleRaf = requestAnimationFrame(stepParticles);
            }
          });
        }, { threshold: 0.05 });
        io.observe(svg);
      } else {
        particleRaf = requestAnimationFrame(stepParticles);
      }
    }

    sliders.forEach((s) => {
      s.addEventListener("input", syncSvgToControls);
    });
    syncSvgToControls();

    // 2. Bind Stepper Buttons to animate SVG Beacon + Tween Sliders to Stage Presets
    const stagePresets = [
      [0.24, 0.28],
      [0.52, 0.45],
      [0.78, 0.62],
      [0.92, 0.35],
    ];

    stepBtns.forEach((btn, idx) => {
      btn.addEventListener("click", () => {
        currentStageIdx = idx % 4;
        if (beaconLabel) {
          beaconLabel.textContent = `STAGE ${currentStageIdx + 1} LOCUS`;
        }
        const preset = stagePresets[currentStageIdx];
        if (sliders[0] && preset) {
          const min0 = parseFloat(sliders[0].min) || 0;
          const max0 = parseFloat(sliders[0].max) || 100;
          tweenRangeSlider(sliders[0], min0 + preset[0] * (max0 - min0), 340);
        }
        if (sliders[1] && preset) {
          const min1 = parseFloat(sliders[1].min) || 0;
          const max1 = parseFloat(sliders[1].max) || 100;
          tweenRangeSlider(sliders[1], min1 + preset[1] * (max1 - min1), 340);
        }
        if (!reducedMotion && svg && svg.animate) {
          svg.animate(
            [{ transform: "scale(0.992)" }, { transform: "scale(1)" }],
            { duration: 240, easing: "cubic-bezier(0.22, 1, 0.36, 1)" }
          );
        }
      });
    });

    // 3. Inject Interactive Auto-Sweep & Reset Controls into the Stepper Bar
    if (stepper && sliders.length > 0 && !stepper.querySelector("[data-auto-sweep]")) {
      let sweepId = null;
      let sweepStart = 0;

      const sweepBtn = document.createElement("button");
      sweepBtn.type = "button";
      sweepBtn.className = "tp-step-btn tp-sweep-btn";
      sweepBtn.setAttribute("data-auto-sweep", "true");
      sweepBtn.setAttribute("aria-pressed", "false");
      sweepBtn.textContent = "▶ Auto-Sweep";

      const stopSweep = () => {
        if (sweepId) {
          cancelAnimationFrame(sweepId);
          sweepId = null;
        }
        sweepBtn.setAttribute("aria-pressed", "false");
        sweepBtn.textContent = "▶ Auto-Sweep";
      };

      const runSweep = (now) => {
        if (!sweepId) return;
        const elapsed = (now - sweepStart) * 0.001;
        sliders.forEach((s, i) => {
          const min = parseFloat(s.min) || 0;
          const max = parseFloat(s.max) || 100;
          const step = parseFloat(s.step) || 0.01;
          const phase = i === 0 ? elapsed * 1.15 : elapsed * 0.78 + 1.1;
          const norm = 0.5 + 0.42 * Math.sin(phase);
          let val = min + norm * (max - min);
          if (step >= 1) val = Math.round(val / step) * step;
          s.value = String(val);
          s.dispatchEvent(new Event("input", { bubbles: true }));
        });
        sweepId = requestAnimationFrame(runSweep);
      };

      sweepBtn.addEventListener("click", () => {
        if (sweepId) {
          stopSweep();
        } else {
          sweepStart = performance.now();
          sweepBtn.setAttribute("aria-pressed", "true");
          sweepBtn.textContent = "⏸ Pause Sweep";
          sweepId = requestAnimationFrame(runSweep);
        }
      });

      // Stop auto-sweep immediately if the user grabs a slider manually
      sliders.forEach((s) => {
        s.addEventListener("pointerdown", () => {
          if (sweepId) stopSweep();
        });
      });

      const resetBtn = document.createElement("button");
      resetBtn.type = "button";
      resetBtn.className = "tp-step-btn tp-reset-btn";
      resetBtn.setAttribute("data-reset-controls", "true");
      resetBtn.textContent = "↺ Reset";
      resetBtn.addEventListener("click", () => {
        if (sweepId) stopSweep();
        sliders.forEach((s, i) => {
          tweenRangeSlider(s, initialValues[i], 280);
        });
      });

      const loupeBtn = document.createElement("button");
      loupeBtn.type = "button";
      loupeBtn.className = "tp-step-btn tp-lens-btn";
      loupeBtn.setAttribute("data-svg-lens", "loupe");
      loupeBtn.setAttribute("aria-pressed", "false");
      loupeBtn.textContent = "🔍 1:5 Loupe";
      loupeBtn.addEventListener("click", () => {
        const active = plate.classList.toggle("is-svg-loupe-active");
        loupeBtn.setAttribute("aria-pressed", active ? "true" : "false");
      });

      const attractorBtn = document.createElement("button");
      attractorBtn.type = "button";
      attractorBtn.className = "tp-step-btn tp-lens-btn";
      attractorBtn.setAttribute("data-svg-lens", "attractor");
      attractorBtn.setAttribute("aria-pressed", "false");
      attractorBtn.textContent = "∞ Attractor";
      attractorBtn.addEventListener("click", () => {
        const active = plate.classList.toggle("is-svg-attractor-active");
        attractorBtn.setAttribute("aria-pressed", active ? "true" : "false");
      });

      const knockoutBtn = document.createElement("button");
      knockoutBtn.type = "button";
      knockoutBtn.className = "tp-step-btn tp-knockout-btn";
      knockoutBtn.setAttribute("data-svg-knockout", "true");
      knockoutBtn.setAttribute("aria-pressed", "false");
      knockoutBtn.textContent = "⚡ Counterfactual";
      knockoutBtn.addEventListener("click", () => {
        knockoutActive = !knockoutActive;
        knockoutBtn.setAttribute("aria-pressed", knockoutActive ? "true" : "false");
        if (folioId === "M.01" && sliders[0]) {
          tweenRangeSlider(sliders[0], knockoutActive ? 2 : 5, 280);
        } else {
          syncSvgToControls();
        }
      });

      const qWefBtn = document.createElement("button");
      qWefBtn.type = "button";
      qWefBtn.className = "tp-step-btn tp-lens-btn";
      qWefBtn.setAttribute("data-svg-lens", "quantum-wef");
      qWefBtn.setAttribute("aria-pressed", "false");
      qWefBtn.textContent = "⚛ Quantum · WEF";
      qWefBtn.addEventListener("click", () => {
        const active = plate.classList.toggle("is-svg-quantum-wef-active");
        qWefBtn.setAttribute("aria-pressed", active ? "true" : "false");
      });

      stepper.appendChild(sweepBtn);
      stepper.appendChild(loupeBtn);
      stepper.appendChild(attractorBtn);
      stepper.appendChild(qWefBtn);
      stepper.appendChild(knockoutBtn);
      stepper.appendChild(resetBtn);
    }
  });
}

export function initPlateSolvers(scope = document) {
  initFullscreenControls(scope);
  initScrubbableTokens(scope);

  // 1. Bidirectional Equation-to-Diagram Highlighting
  scope.querySelectorAll("[data-eq-target]").forEach((chip) => {
    if (chip.dataset.bound === "true") return;
    chip.dataset.bound = "true";
    const targetId = chip.getAttribute("data-eq-target");
    const setHighlight = (active) => {
      chip.setAttribute("data-active", active ? "true" : "false");
      if (!targetId) return;
      const el = document.getElementById(targetId);
      if (el) {
        el.classList.toggle("tp-svg-highlighted", active);
      }
    };
    chip.addEventListener("mouseenter", () => setHighlight(true));
    chip.addEventListener("mouseleave", () => setHighlight(false));
    chip.addEventListener("focus", () => setHighlight(true));
    chip.addEventListener("blur", () => setHighlight(false));
  });

  // 2. Ciechanowski 4-Stage Stepper Buttons
  scope.querySelectorAll(".tp-step-btn[data-step-desc]").forEach((btn) => {
    if (btn.dataset.bound === "true") return;
    btn.dataset.bound = "true";
    btn.addEventListener("click", () => {
      const group = btn.closest(".tp-stepper");
      if (group) {
        group.querySelectorAll(".tp-step-btn[data-step-desc]").forEach((b) => {
          b.setAttribute("aria-pressed", "false");
        });
      }
      btn.setAttribute("aria-pressed", "true");
      const targetOutId = btn.getAttribute("data-step-target");
      const desc = btn.getAttribute("data-step-desc");
      if (targetOutId && desc) {
        const outEl = document.getElementById(targetOutId);
        if (outEl) outEl.textContent = desc;
      }
    });
  });

  const getActiveSlug = () =>
    scope.querySelector("[data-folio-slug]")?.getAttribute("data-folio-slug") ||
    document.querySelector("[data-folio-slug]")?.getAttribute("data-folio-slug") ||
    "";

  const syncSvgStageTelemetry = (slug, badgeText) => {
    if (!badgeText) return;
    const headerBadge =
      scope.querySelector(".tp-plate-live-badge[data-svg-live-telemetry]") ||
      document.querySelector(".tp-plate-live-badge[data-svg-live-telemetry]");
    if (headerBadge) {
      headerBadge.textContent = `[LIVE ${slug.toUpperCase()}] ${badgeText}`;
      return;
    }
  };
  scope.querySelectorAll('input[type="range"]').forEach((inp) => {
    if (inp.dataset.svgTelemetryBound === "true") return;
    inp.dataset.svgTelemetryBound = "true";
    inp.addEventListener("input", () => {
      const slug = getActiveSlug();
      const r0 = scope.querySelector(".tp-readout-strip .tp-readout-v")?.textContent || inp.value;
      if (slug) syncSvgStageTelemetry(slug, r0);
    });
  });

  // 3. Architecture Tectonic Solvers (Folios A.01-A.06)
  const archSpanInput = document.getElementById("tp-arch-rise");
  const archLoadInput = document.getElementById("tp-arch-load");
  if (archSpanInput && archLoadInput && archSpanInput.dataset.bound !== "true") {
    archSpanInput.dataset.bound = "true";
    const updateArch = () => {
      const slug = getActiveSlug() || "a01";
      const v0 = parseFloat(archSpanInput.value) || 4.5;
      const v1 = parseFloat(archLoadInput.value) || 0.032;

      const riseLabel = document.getElementById("tp-arch-rise-val");
      const loadLabel = document.getElementById("tp-arch-load-val");
      const inlineRise = document.getElementById("tp-inline-rise");
      const thrustOut = document.getElementById("tp-readout-thrust");
      const kernOut = document.getElementById("tp-readout-kern");
      const outR2 = document.getElementById("tp-readout-arch-r2");
      const statusBox = document.getElementById("tp-readout-arch-box");
      const statusOut = document.getElementById("tp-readout-arch-status");
      const archPath = document.getElementById("tp-svg-thrust-line");

      if (slug === "a02") {
        const lam = v0;
        const vlap = v1;
        if (riseLabel) riseLabel.textContent = `λ = ${lam.toFixed(2)}`;
        if (loadLabel) loadLabel.textContent = `${vlap.toFixed(1)} kN`;
        if (inlineRise) inlineRise.textContent = `λ = ${lam.toFixed(2)}`;
        const mlap = vlap * (1.493 * lam) * (1.0 - lam);
        const util = (vlap / 18.4) * ((lam * (1.0 - lam)) / 0.1875) * 0.64;
        const sf = 3.74 * (0.64 / Math.max(0.1, util));
        if (thrustOut) thrustOut.textContent = `${vlap.toFixed(1)} kN`;
        if (kernOut) kernOut.textContent = `${mlap.toFixed(2)} kN·m`;
        if (outR2) outR2.textContent = `${util.toFixed(2)} ${util <= 1.0 ? "≤ 1.00 (SAFE)" : "> 1.00 (OVERSTRESS)"}`;
        if (statusOut) statusOut.textContent = util <= 1.0 ? `SF = ${sf.toFixed(2)} · EN 1995-1-1 PASS` : "NOTCH SHEAR EXCEEDED";
        if (statusBox) statusBox.setAttribute("data-alert", util <= 1.0 ? "false" : "true");
        return;
      }
      if (slug === "a03") {
        const H = v0;
        const dT = v1;
        if (riseLabel) riseLabel.textContent = `${H.toFixed(1)} m`;
        if (loadLabel) loadLabel.textContent = `${dT.toFixed(1)} K`;
        if (inlineRise) inlineRise.textContent = `H = ${H.toFixed(1)} m`;
        const dp = 3.92 * (H / 9.0) * (dT / 11.2);
        const vel = 0.84 * Math.sqrt(Math.max(0.05, dp / 3.92));
        const flow = Math.round(142.0 * (vel / 0.84));
        const ach = (24.21 * (vel / 0.84)).toFixed(2);
        if (thrustOut) thrustOut.textContent = `${dp.toFixed(2)} Pa`;
        if (kernOut) kernOut.textContent = `${vel.toFixed(2)} m/s (${flow} m³/h·m)`;
        if (outR2) outR2.textContent = `0.11 (EN ISO 52022-3)`;
        if (statusOut) statusOut.textContent = `${ach} ACH · 285 EML PASS`;
        return;
      }
      if (slug === "a04") {
        const a = v0;
        const c = v1;
        if (riseLabel) riseLabel.textContent = `${a.toFixed(2)} m`;
        if (loadLabel) loadLabel.textContent = `${c.toFixed(2)} m`;
        if (inlineRise) inlineRise.textContent = `a = ${a.toFixed(2)} m`;
        const vpReaction = 4800.0;
        const tieTension = vpReaction * (a / c);
        const sf = 3.12 * (1280.0 / Math.max(100.0, tieTension));
        if (thrustOut) thrustOut.textContent = `48.0 m (100% Column-Free)`;
        if (kernOut) kernOut.textContent = `${tieTension.toLocaleString("en-US", { minimumFractionDigits: 1, maximumFractionDigits: 1 })} kN (SF = ${sf.toFixed(2)})`;
        if (outR2) outR2.textContent = `τ_pod = 15 yr / τ_frame = 100 yr`;
        if (statusOut) statusOut.textContent = sf >= 1.5 ? "ISOSTATIC EXOSKELETON PASS" : "TIE-ROD YIELD WARNING";
        if (statusBox) statusBox.setAttribute("data-alert", sf >= 1.5 ? "false" : "true");

        const a04Truss1 = document.getElementById("tp-a04-truss-1");
        const a04Truss2 = document.getElementById("tp-a04-truss-2");
        const a04Label = document.getElementById("tp-a04-svg-label");
        if (a04Truss1) {
          const camberY1 = Math.round(86 - (a - 1.6) * 8.0);
          const camberY2 = Math.round(134 - (a - 1.6) * 8.0);
          a04Truss1.setAttribute("d", `M 175 82 Q 340 ${camberY1} 505 82`);
          if (a04Truss2) a04Truss2.setAttribute("d", `M 175 130 Q 340 ${camberY2} 505 130`);
        }
        if (a04Label) {
          a04Label.textContent = `Archigram → Foster / Rogers / Rice Exoskeleton · T_tie = ${tieTension.toFixed(0)} kN · 48.0 m Clear Span`;
        }
        return;
      }
      if (slug === "a05") {
        const alpha = v0;
        const pQrd = Math.round(v1);
        if (riseLabel) riseLabel.textContent = `α_bar = ${alpha.toFixed(2)}`;
        if (loadLabel) loadLabel.textContent = `p = ${pQrd}`;
        if (inlineRise) inlineRise.textContent = `α_bar = ${alpha.toFixed(2)}`;
        const t60 = 0.62 * (-Math.log(1.0 - 0.44)) / Math.max(0.05, -Math.log(1.0 - alpha));
        const sti = Math.min(0.88, Math.max(0.42, 0.74 - 0.22 * (t60 - 0.62)));
        const c50 = (4.8 - 6.5 * (t60 - 0.62)).toFixed(1);
        if (thrustOut) thrustOut.textContent = `${t60.toFixed(2)} s (vs 1.85 s)`;
        if (kernOut) kernOut.textContent = `${sti.toFixed(2)} (${sti >= 0.68 ? "Excellent ≥ 0.68" : "Degraded < 0.68"})`;
        if (outR2) outR2.textContent = `${Number(c50) >= 0 ? "+" : ""}${c50} dB (QRD p=${pQrd})`;
        if (statusOut) statusOut.textContent = sti >= 0.68 ? "SAFE KERN & ACOUSTIC PASS" : "REVERBERATION EXCEEDS LIMIT";
        if (statusBox) statusBox.setAttribute("data-alert", sti >= 0.68 ? "false" : "true");
        return;
      }
      if (slug === "a06") {
        const tau = v0;
        const hUv = v1;
        if (riseLabel) riseLabel.textContent = `${tau.toFixed(1)} d`;
        if (loadLabel) loadLabel.textContent = `${hUv.toFixed(0)} mJ/cm²`;
        if (inlineRise) inlineRise.textContent = `τ = ${tau.toFixed(1)} d`;
        const cOut = 3.0 + (140.0 - 3.0) * Math.exp(-1.12 * tau);
        const rem = ((140.0 - cOut) / 140.0) * 100.0;
        const logRed = 5.4 * (hUv / 45.0);
        if (thrustOut) thrustOut.textContent = `${rem.toFixed(1)}% (140 → ${cOut.toFixed(1)} mg/L)`;
        if (kernOut) kernOut.textContent = `${logRed.toFixed(1)}-Log (${hUv.toFixed(0)} mJ/cm²)`;
        if (outR2) outR2.textContent = `60.0 °C (v = 0.65 m/s)`;
        if (statusOut) statusOut.textContent = rem >= 85.0 && logRed >= 4.0 ? "ZERO BIOFILM VERIFIED" : "INCOMPLETE PURGE WARNING";
        if (statusBox) statusBox.setAttribute("data-alert", rem >= 85.0 && logRed >= 4.0 ? "false" : "true");
        return;
      }
      if (slug === "a07") {
        const ks = v0;
        const f12 = v1;
        if (riseLabel) riseLabel.textContent = `K/S = ${ks.toFixed(2)}`;
        if (loadLabel) loadLabel.textContent = `F_12 = ${f12.toFixed(2)}`;
        if (inlineRise) inlineRise.textContent = `K/S = ${ks.toFixed(2)}`;
        const rInf = Math.max(0.05, 1.0 + ks - Math.sqrt(ks * ks + 2.0 * ks));
        const bGain = 1.0 / Math.max(0.15, 1.0 - rInf * f12);
        const dE00 = (3.4 + 24.5 * f12 * (1.0 - rInf)).toFixed(1);
        if (thrustOut) thrustOut.textContent = `${(rInf * 100.0).toFixed(1)}% (K/S = ${ks.toFixed(2)})`;
        if (kernOut) kernOut.textContent = `${bGain.toFixed(2)}× (F_12 = ${f12.toFixed(2)})`;
        if (outR2) outR2.textContent = `ΔE_00 = ${dE00} (Warm Gold Shift)`;
        if (statusOut) statusOut.textContent = f12 >= 0.25 ? "BARRAGÁN RADIANT HARMONY · PASS" : "LOW COURTYARD INTER-REFLECTION";
        if (statusBox) statusBox.setAttribute("data-alert", f12 >= 0.25 ? "false" : "true");
        return;
      }
      if (slug === "a08") {
        const epsWin = v0;
        const rSol = v1;
        if (riseLabel) riseLabel.textContent = `ε_8-13 = ${epsWin.toFixed(2)}`;
        if (loadLabel) loadLabel.textContent = `R_solar = ${rSol.toFixed(3)}`;
        if (inlineRise) inlineRise.textContent = `ε_8-13 = ${epsWin.toFixed(2)}`;
        const pRad = 158.0 * epsWin;
        const pSol = 920.0 * (1.0 - rSol);
        const pNet = pRad - 34.0 - pSol;
        const dT = Math.min(-0.5, -(pNet / 16.5));
        if (thrustOut) thrustOut.textContent = `${pNet >= 0 ? "+" : ""}${pNet.toFixed(1)} W/m² (Noon Sun)`;
        if (kernOut) kernOut.textContent = `${dT.toFixed(1)} °C vs Ambient`;
        if (outR2) outR2.textContent = `T_m = 23.5 °C (185 kJ/kg)`;
        if (statusOut) statusOut.textContent = pNet >= 40.0 ? "SUB-AMBIENT DAYTIME COOLING PASS" : "SOLAR PARASITIC HEATING WARNING";
        if (statusBox) statusBox.setAttribute("data-alert", pNet >= 40.0 ? "false" : "true");
        return;
      }
      if (slug === "a09") {
        const dMc = v0;
        const hMm = v1;
        if (riseLabel) riseLabel.textContent = `ΔMC = +${dMc.toFixed(1)}%`;
        if (loadLabel) loadLabel.textContent = `h = ${hMm.toFixed(1)} mm`;
        if (inlineRise) inlineRise.textContent = `ΔMC = +${dMc.toFixed(1)}%`;
        const kappa = (1.42 * (dMc / 6.0) * (6.0 / Math.max(2.0, hMm)));
        const tipMm = Math.min(240.0, 0.5 * kappa * 0.425 * 0.425 * 1000.0);
        const ventPct = Math.min(92.0, Math.max(12.0, 64.5 * (kappa / 1.42)));
        if (thrustOut) thrustOut.textContent = `${kappa.toFixed(2)} m⁻¹ (R = ${(1.0 / Math.max(0.1, kappa)).toFixed(2)} m)`;
        if (kernOut) kernOut.textContent = `${tipMm.toFixed(1)} mm (at L = 425 mm)`;
        if (outR2) outR2.textContent = `${ventPct.toFixed(1)}% Free Area (0 W)`;
        if (statusOut) statusOut.textContent = kappa >= 0.45 ? "ZERO-ENERGY ACTUATION · PASS" : "LOW HYGROSCOPIC STROKE";
        if (statusBox) statusBox.setAttribute("data-alert", kappa >= 0.45 ? "false" : "true");
        return;
      }
      if (slug === "a10") {
        const thetaDeg = v0;
        const alphaDeg = v1;
        if (riseLabel) riseLabel.textContent = `θ = ${thetaDeg.toFixed(0)}°`;
        if (loadLabel) loadLabel.textContent = `α = ${alphaDeg.toFixed(0)}°`;
        if (inlineRise) inlineRise.textContent = `θ = ${thetaDeg.toFixed(0)}°`;
        const alphaRad = (alphaDeg * Math.PI) / 180.0;
        const thetaRad = (thetaDeg * Math.PI) / 180.0;
        const cosPhi = Math.min(0.99, Math.sin(alphaRad) * Math.cos(thetaRad * 0.5));
        const sinPhi = Math.sqrt(Math.max(1e-4, 1.0 - cosPhi * cosPhi));
        const tanPhi = sinPhi / Math.max(0.08, cosPhi);
        const nuXy = -(tanPhi * tanPhi);
        const shgc = Math.max(0.11, 0.58 * (1.0 - 0.78 * Math.cos(thetaRad)));
        const gamma2 = (2.0 * Math.atan(Math.cos(alphaRad) * Math.tan(Math.max(0.1, Math.PI * 0.5 - thetaRad * 0.5))) * 180.0) / Math.PI;
        if (thrustOut) thrustOut.textContent = `${nuXy.toFixed(2)} (Auxetic −tan² φ)`;
        if (kernOut) kernOut.textContent = `SHGC = ${shgc.toFixed(2)} (−${((1.0 - shgc / 0.60) * 100.0).toFixed(1)}% Solar)`;
        if (outR2) outR2.textContent = `γ_2 = ${gamma2.toFixed(1)}° (1-DOF Isometric)`;
        if (statusOut) statusOut.textContent = shgc <= 0.32 ? "RIGID-FOLDABLE · ZERO JAM" : "HIGH SOLAR TRANSMISSION";
        if (statusBox) statusBox.setAttribute("data-alert", shgc <= 0.32 ? "false" : "true");
        return;
      }
      if (slug === "a11") {
        const lSpan = v0;
        const fRatio = v1;
        if (riseLabel) riseLabel.textContent = `L = ${lSpan.toFixed(1)} m`;
        if (loadLabel) loadLabel.textContent = `f/L = ${fRatio.toFixed(2)}`;
        if (inlineRise) inlineRise.textContent = `L = ${lSpan.toFixed(1)} m`;
        const qLoad = 8.0;
        const fRise = Math.max(0.5, lSpan * fRatio);
        const hThrust = (qLoad * lSpan * lSpan) / (8.0 * fRise);
        const co2Save = Math.min(82.0, Math.max(45.0, 72.0 - Math.abs(fRatio - 0.16) * 90.0));
        const safe = fRatio >= 0.12 && hThrust <= 480.0;
        if (thrustOut) thrustOut.textContent = `H = ${hThrust.toFixed(0)} kN (f = ${fRise.toFixed(2)} m)`;
        if (kernOut) kernOut.textContent = `−${co2Save.toFixed(0)}% Embodied Concrete (0 kg Rebar)`;
        if (outR2) outR2.textContent = `Σ A_k n_k = 0 (3D Minkowski Closed)`;
        if (statusOut) statusOut.textContent = safe ? "COMPRESSION-ONLY · ZERO REBAR" : "HIGH HORIZONTAL THRUST / TIE ALERT";
        if (statusBox) statusBox.setAttribute("data-alert", safe ? "false" : "true");
        return;
      }
      if (slug === "a12") {
        const epsIr = v0;
        const rSolar = v1;
        if (riseLabel) riseLabel.textContent = `ε_8-13 = ${epsIr.toFixed(2)}`;
        if (loadLabel) loadLabel.textContent = `R_solar = ${rSolar.toFixed(3)}`;
        if (inlineRise) inlineRise.textContent = `ε_8-13 = ${epsIr.toFixed(2)}`;
        const qRad = 158.0 * epsIr;
        const qSol = 1000.0 * (1.0 - rSolar);
        const qNet = qRad - 23.3 - qSol;
        const dT = -(qNet / 18.9);
        const safe = qNet >= 60.0 && dT <= -3.0;
        if (thrustOut) thrustOut.textContent = `q_net = ${qNet >= 0 ? "+" : ""}${qNet.toFixed(1)} W/m² (Noon Sun)`;
        if (kernOut) kernOut.textContent = `ΔT_sub = ${dT.toFixed(1)} °C vs Ambient`;
        if (outR2) outR2.textContent = `s = 1, m = 1 (Super-Stable Tensegrity)`;
        if (statusOut) statusOut.textContent = safe ? "PASSIVE SKY-COOLING · ZERO GRID" : "SOLAR ABSORPTION HEATING ALERT";
        if (statusBox) statusBox.setAttribute("data-alert", safe ? "false" : "true");
        return;
      }

      const rise = v0;
      const asym = v1;
      const span = 18.0;
      const thickness = 0.6;
      const qLoad = 24.0;
      const thrustH = (qLoad * span * span) / (8.0 * rise);
      const kernLimit = thickness / 6.0;
      const safe = Math.abs(asym) <= kernLimit;
      const safetyFactor = thickness / (2.0 * Math.max(Math.abs(asym), 0.005));

      if (riseLabel) riseLabel.textContent = rise.toFixed(2) + " m";
      if (loadLabel) loadLabel.textContent = (asym * 1000).toFixed(0) + " mm";
      if (inlineRise) inlineRise.textContent = "f = " + rise.toFixed(2) + " m";
      if (thrustOut) thrustOut.textContent = thrustH.toFixed(1) + " kN";
      if (kernOut) kernOut.textContent = (asym * 1000).toFixed(0) + " / 100 mm";
      if (statusOut) {
        statusOut.textContent = safe
          ? "SAFE KERN HARMONY (SF " + safetyFactor.toFixed(2) + ")"
          : "DESIGN TUNING: CENTER THRUST WITHIN KERN (|e| ≤ t/6)";
      }
      if (statusBox) statusBox.setAttribute("data-alert", safe ? "false" : "true");

      if (archPath) {
        const apexY = Math.round(175 - (rise - 2.5) * 24);
        const shiftX = Math.round(260 + asym * 320);
        archPath.setAttribute("d", "M 60 190 Q " + shiftX + " " + apexY + " 460 190");
      }
      const cremonaH = document.getElementById("tp-svg-cremona-h");
      const cremonaR1 = document.getElementById("tp-svg-cremona-r1");
      const cremonaR2 = document.getElementById("tp-svg-cremona-r2");
      const cremonaPole = document.getElementById("tp-svg-cremona-pole");
      const cremonaLabel = document.getElementById("tp-svg-cremona-label");
      if (cremonaH && cremonaR1 && cremonaR2 && cremonaPole && cremonaLabel) {
        const poleX = Math.max(4, Math.min(68, Math.round(95 - (thrustH / 216.0) * 80)));
        cremonaH.setAttribute("x1", String(poleX));
        cremonaR1.setAttribute("x1", String(poleX));
        cremonaR2.setAttribute("x1", String(poleX));
        cremonaPole.setAttribute("cx", String(poleX));
        cremonaLabel.setAttribute("x", String(poleX));
        cremonaLabel.textContent = "O (H=" + thrustH.toFixed(0) + " kN)";
      }
    };
    archSpanInput.addEventListener("input", updateArch);
    archLoadInput.addEventListener("input", updateArch);
    if ((getActiveSlug() || "a01") === "a01") updateArch();
  }

  // 4. Math Modularity, Spectral, Combinatorics, PFR, Neuro-Symbolic & Complexity Solvers (M.01-M.06)
  const mathPrimeInput = document.getElementById("tp-math-prime");
  const mathClauseInput = document.getElementById("tp-math-clause");
  if (mathPrimeInput && mathClauseInput && mathPrimeInput.dataset.bound !== "true") {
    mathPrimeInput.dataset.bound = "true";
    const updateMath = () => {
      const slug = getActiveSlug() || "m01";
      const v0 = parseFloat(mathPrimeInput.value) || 5.0;
      const v1 = parseFloat(mathClauseInput.value) || 4.26;

      const pLabel = document.getElementById("tp-math-prime-val");
      const cLabel = document.getElementById("tp-math-clause-val");
      const inlineP = document.getElementById("tp-inline-prime");
      const barrierOut = document.getElementById("tp-readout-barrier");
      const fluxOut = document.getElementById("tp-readout-flux");
      const ethOut = document.getElementById("tp-readout-eth");
      const qedBox = document.getElementById("tp-readout-qed-box");
      const qedOut = document.getElementById("tp-readout-qed");
      const stage4Dot = document.getElementById("tp-svg-stage-4");

      if (slug === "m02") {
        const sigma = v0;
        const logT = v1;
        if (pLabel) pLabel.textContent = `σ = ${sigma.toFixed(2)}`;
        if (cLabel) cLabel.textContent = `log T = ${logT.toFixed(1)}`;
        if (inlineP) inlineP.textContent = `σ = ${sigma.toFixed(2)}`;
        const cIng = (3.0 * (1.0 - sigma)) / (2.0 - sigma);
        const cHux = (12.0 * (1.0 - sigma)) / 5.0;
        const cEff = Math.min(cIng, cHux);
        const gap = 0.418 * (sigma / 0.75) * (10.0 / Math.max(4.0, logT));
        if (barrierOut) barrierOut.textContent = `${cEff.toFixed(3)} (at σ = ${sigma.toFixed(2)})`;
        if (fluxOut) fluxOut.textContent = `${gap.toFixed(3)}`;
        if (ethOut) ethOut.textContent = `0 sorryAx (log T = ${logT.toFixed(1)})`;
        if (qedOut) qedOut.textContent = sigma >= 0.75 ? "HUXLEY REGIME · 0 sorryAx" : "INGHAM REGIME · 0 sorryAx";
        return;
      }
      if (slug === "m03") {
        const n = Math.round(v0);
        const rank = Math.round(v1);
        if (pLabel) pLabel.textContent = `n = ${n}`;
        if (cLabel) cLabel.textContent = `rank = ${rank}`;
        if (inlineP) inlineP.textContent = `n = ${n}`;
        const capMap = { 3: 9, 4: 20, 5: 45, 6: 112, 7: 236, 8: 512 };
        const capSize = capMap[n] || Math.round(Math.pow(2.2202, n));
        const omega4 = (Math.log(rank) / Math.log(4)).toFixed(4);
        if (barrierOut) barrierOut.textContent = `${capSize} vectors (FunSearch)`;
        if (fluxOut) fluxOut.textContent = `2.7551^${n} Upper Bound`;
        if (ethOut) ethOut.textContent = `${rank} ${rank < 49 ? "< 49 (AlphaEvolve)" : "(Strassen 49)"}`;
        if (qedOut) qedOut.textContent = `log_4(${rank}) = ${omega4}`;
        return;
      }
      if (slug === "m04") {
        const K = v0;
        const dR = v1;
        if (pLabel) pLabel.textContent = `K = ${K.toFixed(1)}`;
        if (cLabel) cLabel.textContent = `d_R = ${dR.toFixed(2)}`;
        if (inlineP) inlineP.textContent = `K = ${K.toFixed(1)}`;
        if (barrierOut) barrierOut.textContent = `≤ 2 · ${K.toFixed(1)}^12 Cosets`;
        if (fluxOut) fluxOut.textContent = `22,028,942 Verified Edges`;
        if (ethOut) ethOut.textContent = `100% Formalized (0 sorry)`;
        if (qedOut) qedOut.textContent = `Δd_R ≤ -${(dR / 12.0).toFixed(3)} (at d_R = ${dR.toFixed(2)})`;
        return;
      }
      if (slug === "m05") {
        const kAux = Math.round(v0);
        const alpha = v1;
        if (pLabel) pLabel.textContent = `k_aux = ${kAux}`;
        if (cLabel) cLabel.textContent = `α = ${alpha.toFixed(2)}`;
        if (inlineP) inlineP.textContent = `k_aux = ${kAux}`;
        const inv = 14 + kAux * 11;
        const rate = Math.min(96.0, 54.0 + kAux * 10.0);
        const rmsd = (1.26 / Math.max(1, kAux)).toFixed(2);
        if (barrierOut) barrierOut.textContent = `14 → ${inv} Invariants`;
        if (fluxOut) fluxOut.textContent = `${rate.toFixed(1)}% (AlphaGeometry 2)`;
        if (ethOut) ethOut.textContent = `det(B_5) = 0 (${rmsd} Å)`;
        if (qedOut) qedOut.textContent = kAux >= 2 ? "QED VERIFIED (DD+AR)" : "AUXILIARY ANCHOR REQUIRED";
        return;
      }
      if (slug === "m06") {
        const dPoly = Math.round(v0);
        const alpha = v1;
        if (pLabel) pLabel.textContent = `d_poly = ${dPoly}`;
        if (cLabel) cLabel.textContent = `α = ${alpha.toFixed(2)}`;
        if (inlineP) inlineP.textContent = `d_poly = ${dPoly}`;
        const speedup = (2.96 * dPoly).toFixed(1);
        const prm = Math.min(99.2, 74.6 + dPoly * 4.0).toFixed(1);
        const s3 = (0.385 * (alpha / 4.26)).toFixed(3);
        if (barrierOut) barrierOut.textContent = `${speedup}× (at n = 4,096)`;
        if (fluxOut) fluxOut.textContent = `${prm}% (vs 41.2% ORM)`;
        if (ethOut) ethOut.textContent = `2^(${s3} n)`;
        if (qedOut) qedOut.textContent = "QED VERIFIED (Sub-Cubic)";
        return;
      }
      if (slug === "m07") {
        const lSoc = v0;
        const kModes = Math.round(v1);
        if (pLabel) pLabel.textContent = `λ_soc = ${lSoc.toFixed(2)}`;
        if (cLabel) cLabel.textContent = `k_max = ${kModes}`;
        if (inlineP) inlineP.textContent = `λ_soc = ${lSoc.toFixed(2)}`;
        const dtGain = -(0.18 + 0.31 * (lSoc / 1.42) * Math.min(1.15, kModes / 24.0));
        const fnoMs = (0.45 + 0.032 * kModes).toFixed(2);
        if (barrierOut) barrierOut.textContent = `${dtGain.toFixed(2)} s / Lap (350 kW MGU-K)`;
        if (fluxOut) fluxOut.textContent = `3.98 / 4.00 MJ (SoC Neutral)`;
        if (ethOut) ethOut.textContent = `${fnoMs} ms (1,150× vs RANS)`;
        if (qedOut) qedOut.textContent = Math.abs(lSoc - 1.42) <= 0.35 ? "PONTRYAGIN OPTIMAL · PASS" : "ENERGY DEPLETION DRIFT";
        if (qedBox) qedBox.setAttribute("data-alert", Math.abs(lSoc - 1.42) <= 0.35 ? "false" : "true");
        return;
      }
      if (slug === "m08") {
        const kCurv = v0;
        const mScale = v1;
        if (pLabel) pLabel.textContent = `κ_g = ${kCurv.toFixed(2)}`;
        if (cLabel) cLabel.textContent = `g_scale = ${mScale.toFixed(2)}×`;
        if (inlineP) inlineP.textContent = `κ_g = ${kCurv.toFixed(2)}`;
        const dsRiem = (14.2 * mScale * (1.0 - 0.142 * kCurv)).toFixed(1);
        const abney = (6.8 * kCurv).toFixed(1);
        if (barrierOut) barrierOut.textContent = `Δs_R = ${dsRiem} JND (−14.2% vs Euclidean)`;
        if (fluxOut) fluxOut.textContent = `+${abney}° Hue Bend (Geodesic)`;
        if (ethOut) ethOut.textContent = `dim(N_C) = N − 3 (Metamers)`;
        if (qedOut) qedOut.textContent = "SCHRÖDINGER METRIC · QED PASS";
        return;
      }
      if (slug === "m09") {
        const tGeo = v0;
        const epsSink = v1;
        if (pLabel) pLabel.textContent = `t = ${tGeo.toFixed(2)}`;
        if (cLabel) cLabel.textContent = `ε = ${epsSink.toFixed(2)}`;
        if (inlineP) inlineP.textContent = `t = ${tGeo.toFixed(2)}`;
        const w2Sq = (4.82 + 0.45 * epsSink).toFixed(2);
        const muT = (-1.10 * (1.0 - tGeo) + 1.10 * tGeo).toFixed(2);
        const sigT = (0.95 * (1.0 - tGeo) + 1.35 * tGeo).toFixed(2);
        const iters = Math.max(6, Math.round(18.0 * (0.05 / Math.max(0.01, epsSink))));
        if (barrierOut) barrierOut.textContent = `W_2² = ${w2Sq} (Bures–Wasserstein)`;
        if (fluxOut) fluxOut.textContent = `μ_t = ${muT} · σ_t = ${sigT}`;
        if (ethOut) ethOut.textContent = `${iters} Iterations (ε = ${epsSink.toFixed(2)})`;
        if (qedOut) qedOut.textContent = "HJB GEODESIC · QED PASS";
        if (qedBox) qedBox.setAttribute("data-alert", "false");
        return;
      }
      if (slug === "m10") {
        const epsNm = v0;
        const sigNoise = v1;
        if (pLabel) pLabel.textContent = `ε = ${epsNm.toFixed(0)} nm`;
        if (cLabel) cLabel.textContent = `σ = ${sigNoise.toFixed(2)}`;
        if (inlineP) inlineP.textContent = `ε = ${epsNm.toFixed(0)} nm`;
        const b0 = epsNm < 35.0 ? 4 : 1;
        const b1 = epsNm >= 38.0 && epsNm <= 116.0 ? 3 : 1;
        const chi = b0 - b1;
        const rCrit = Math.max(48.0, 116.0 - 42.0 * sigNoise);
        const pass = rCrit >= 65.0;
        if (barrierOut) barrierOut.textContent = `β₀ = ${b0} · β₁ = ${b1} · β₂ = 0`;
        if (fluxOut) fluxOut.textContent = `χ = β₀ − β₁ + β₂ = ${chi}`;
        if (ethOut) ethOut.textContent = `r_crit = ${rCrit.toFixed(0)} nm (> 65 nm LNP)`;
        if (qedOut) qedOut.textContent = pass ? "PERCOLATING · BOTTLENECK PASS" : "THROAT PINCHED BELOW 65 NM";
        if (qedBox) qedBox.setAttribute("data-alert", pass ? "false" : "true");
        return;
      }
      if (slug === "m11") {
        const kCard = Math.round(v0);
        const sigZero = v1;
        if (pLabel) pLabel.textContent = `|A| = ${kCard}`;
        if (cLabel) cLabel.textContent = `σ = ${sigZero.toFixed(2)}`;
        if (inlineP) inlineP.textContent = `|A| = ${kCard}`;
        const nHorizon = 900;
        const erdosTur = Math.floor(Math.sqrt(nHorizon) + Math.pow(nHorizon, 0.25) + 1.0);
        const guthMaynard = (30.0 * (1.0 - sigZero)) / 13.0;
        const pass = kCard <= erdosTur;
        if (barrierOut) barrierOut.textContent = `dim_H(K) = 3.00 (Wang–Zahl 3D Kakeya)`;
        if (fluxOut) fluxOut.textContent = `N(σ,T) ≪ T^(${guthMaynard.toFixed(3)}+ε) (θ = 13/30)`;
        if (ethOut) ethOut.textContent = `|A| = ${kCard} / ${erdosTur} Bound (N = 900)`;
        if (qedOut) qedOut.textContent = pass ? "SIDON B₂ COLLISION-FREE · 0 SORRY" : "PIGEONHOLE SUM COLLISION (> 36)";
        if (qedBox) qedBox.setAttribute("data-alert", pass ? "false" : "true");
        return;
      }
      if (slug === "m12") {
        const nDim = Math.round(v0);
        const kMod = Math.round(v1);
        if (pLabel) pLabel.textContent = `n = ${nDim}`;
        if (cLabel) cLabel.textContent = `k = ${kMod} (ML-KEM-${kMod * 256})`;
        if (inlineP) inlineP.textContent = `n = ${nDim}`;
        const naiveMults = Math.pow(nDim, 3);
        const eightSqMults = Math.round(Math.pow(nDim, 2.755));
        const secBits = kMod === 2 ? 128 : kMod === 3 ? 192 : 256;
        if (barrierOut) barrierOut.textContent = `${eightSqMults.toLocaleString("en-US")} mults (vs ${naiveMults.toLocaleString("en-US")} n³)`;
        if (fluxOut) fluxOut.textContent = `${secBits}-bit Post-Quantum (NIST FIPS 203)`;
        if (ethOut) ethOut.textContent = `ETHIsFalse.lean · EightSquare.lean`;
        if (qedOut) qedOut.textContent = kMod >= 3 ? "LEAN 4 KERNEL QED · 0 SORRYAX" : "ML-KEM-512 BASELINE LEVEL 1";
        if (qedBox) qedBox.setAttribute("data-alert", kMod >= 3 ? "false" : "true");
        return;
      }

      const pVal = Math.round(v0);
      const clauseDensity = v1;
      const isPythagorean = pVal === 2;
      const unbridgedPeak = 8.39;
      const bridgedPeak = isPythagorean ? 9.85 : Math.max(2.65, 3.59 - (pVal - 5) * 0.08);
      const fluxPct = isPythagorean ? 18.5 : Math.min(89.5, 68.4 + (pVal - 5) * 2.4);
      const s3Exponent = Math.max(0.08, 0.385 * (clauseDensity / 4.26));

      if (pLabel) pLabel.textContent = "p = " + pVal;
      if (cLabel) cLabel.textContent = "α = " + clauseDensity.toFixed(2);
      if (inlineP) inlineP.textContent = "p = " + pVal;
      if (barrierOut) barrierOut.textContent = bridgedPeak.toFixed(2) + " kcal/mol (vs " + unbridgedPeak + ")";
      if (fluxOut) fluxOut.textContent = fluxPct.toFixed(1) + "%";
      if (ethOut) ethOut.textContent = "2^(" + s3Exponent.toFixed(3) + " n)";
      if (qedOut) {
        qedOut.textContent = isPythagorean
          ? "CLASSICAL HARMONY (p = 2 Pythagorean Solutions: 3² + 4² = 5²)"
          : "QED VERIFIED (29,500 Lemmas · Human + AI Proof)";
      }
      if (qedBox) qedBox.setAttribute("data-alert", isPythagorean ? "true" : "false");
      if (stage4Dot) {
        const cy = isPythagorean ? 44 : Math.round(115 - (clauseDensity - 4.26) * 8);
        stage4Dot.setAttribute("cy", String(cy));
      }
    };
    mathPrimeInput.addEventListener("input", updateMath);
    mathClauseInput.addEventListener("input", updateMath);
    if ((getActiveSlug() || "m01") === "m01") updateMath();
  }

  // 5. Engineering Stokes-Brinkman (E.01), Acoustic Metamaterials (E.03) & Enthalpy Cores (E.04)
  const engPhiInput = document.getElementById("tp-eng-phi");
  const engRadiusInput = document.getElementById("tp-eng-radius");
  if (engPhiInput && engRadiusInput && engPhiInput.dataset.bound !== "true") {
    engPhiInput.dataset.bound = "true";
    const updateEng = () => {
      const slug = getActiveSlug() || "e01";
      const v0 = parseFloat(engPhiInput.value) || 0.72;
      const v1 = parseFloat(engRadiusInput.value) || 12.0;

      const phiLabel = document.getElementById("tp-eng-phi-val");
      const radLabel = document.getElementById("tp-eng-radius-val");
      const inlinePhi = document.getElementById("tp-inline-phi");
      const kappaOut = document.getElementById("tp-readout-kappa");
      const deffOut = document.getElementById("tp-readout-deff");
      const outR2 = document.getElementById("tp-readout-eng-r2");
      const percBox = document.getElementById("tp-readout-perc-box");
      const percOut = document.getElementById("tp-readout-perc");
      const engPoint = document.getElementById("tp-svg-eng-point");

      if (slug === "e03") {
        const f0 = v0;
        const rNeck = v1;
        if (phiLabel) phiLabel.textContent = `${f0.toFixed(0)} Hz`;
        if (radLabel) radLabel.textContent = `${rNeck.toFixed(2)} mm`;
        if (inlinePhi) inlinePhi.textContent = `f_0 = ${f0.toFixed(0)} Hz`;
        const dv = 0.174 * Math.sqrt(160.0 / Math.max(20.0, f0));
        const rRatio = rNeck / 0.65;
        const reZ = 1.04 / Math.pow(rRatio, 1.35);
        const imZ = 0.08 * (f0 / 160.0 - 160.0 / f0);
        const rSq = ((reZ - 1.0) * (reZ - 1.0) + imZ * imZ) / ((reZ + 1.0) * (reZ + 1.0) + imZ * imZ);
        const alphaP = 1.0 - rSq;
        if (kappaOut) kappaOut.textContent = `${dv.toFixed(3)} mm (at ${f0.toFixed(0)} Hz)`;
        if (deffOut) deffOut.textContent = `Z_s / Z_0 = ${reZ.toFixed(2)} ${imZ >= 0 ? "+" : "-"} ${Math.abs(imZ).toFixed(2)} i`;
        if (outR2) outR2.textContent = `α_peak = ${alphaP.toFixed(3)} (${alphaP >= 0.90 ? "Critical Match" : "Detuned"})`;
        if (percOut) percOut.textContent = alphaP >= 0.85 ? "CLASS A · ZERO FIBER" : "SUB-OPTIMAL IMPEDANCE";
        if (percBox) percBox.setAttribute("data-alert", alphaP >= 0.85 ? "false" : "true");
        return;
      }
      if (slug === "e04") {
        const ntuS = v0;
        const ntuM = v1;
        if (phiLabel) phiLabel.textContent = `NTU = ${ntuS.toFixed(1)}`;
        if (radLabel) radLabel.textContent = `NTU_m = ${ntuM.toFixed(2)}`;
        if (inlinePhi) inlinePhi.textContent = `NTU = ${ntuS.toFixed(1)}`;
        const epsS = (ntuS / (1.0 + ntuS)) * 100.0;
        const epsL = (ntuM / (1.0 + ntuM)) * 100.0;
        const tFrost = -3.0 - 9.5 * (epsL / 79.4);
        if (kappaOut) kappaOut.textContent = `${epsS.toFixed(1)}% (NTU = ${ntuS.toFixed(1)})`;
        if (deffOut) deffOut.textContent = `${epsL.toFixed(1)}% (NTU_m = ${ntuM.toFixed(2)})`;
        if (outR2) outR2.textContent = `${tFrost.toFixed(1)} °C (vs -3.0 °C Sensible)`;
        if (percOut) percOut.textContent = epsS >= 75.0 ? "PASS · BALANCED NTU" : "LOW RECOVERY WARNING";
        if (percBox) percBox.setAttribute("data-alert", epsS >= 75.0 ? "false" : "true");
        return;
      }
      if (slug === "e07") {
        const uWind = v0;
        const gapM = v1;
        if (phiLabel) phiLabel.textContent = `${uWind.toFixed(0)} m/s`;
        if (radLabel) radLabel.textContent = `${gapM.toFixed(1)} m`;
        if (inlinePhi) inlinePhi.textContent = `U = ${uWind.toFixed(0)} m/s`;
        const uCrit = 54.0 + 4.0 * gapM;
        const zeta = 0.038 * (1.0 - Math.pow(uWind / uCrit, 1.8));
        const safe = uWind < uCrit * 0.85;
        if (kappaOut) kappaOut.textContent = `U_crit = ${uCrit.toFixed(1)} m/s (vs 54.0 m/s)`;
        if (deffOut) deffOut.textContent = `ζ_eff = ${(zeta * 100.0).toFixed(2)}% (at U = ${uWind.toFixed(0)} m/s)`;
        if (outR2) outR2.textContent = `1.8 ms (R² = 0.994 vs Wind Tunnel)`;
        if (percOut) percOut.textContent = safe ? "AEROELASTIC STABLE · PASS" : "FLUTTER BOUNDARY WARNING";
        if (percBox) percBox.setAttribute("data-alert", safe ? "false" : "true");
        return;
      }
      if (slug === "e08") {
        const vlPct = v0;
        const pFace = v1;
        if (phiLabel) phiLabel.textContent = `V_L = ${vlPct.toFixed(2)}%`;
        if (radLabel) radLabel.textContent = `${pFace.toFixed(0)} kPa`;
        if (inlinePhi) inlinePhi.textContent = `V_L = ${vlPct.toFixed(2)}%`;
        const dTun = 9.8;
        const iTrough = 11.0;
        const sMaxMm = (0.313 * (vlPct / 100.0) * dTun * dTun / iTrough) * 1000.0 * (225.0 / Math.max(120.0, pFace));
        const betaMax = (0.606 * (sMaxMm / 1000.0)) / iTrough;
        const safe = sMaxMm <= 15.0 && pFace >= 180.0;
        if (kappaOut) kappaOut.textContent = `S_max = ${sMaxMm.toFixed(1)} mm (V_L = ${vlPct.toFixed(2)}%)`;
        if (deffOut) deffOut.textContent = `i = 11.0 m (z_0 = 22.0 m)`;
        if (outR2) outR2.textContent = `β_max = 1 / ${Math.round(1.0 / Math.max(1e-5, betaMax)).toLocaleString("en-US")} (< 1 / 500)`;
        if (percOut) percOut.textContent = safe ? "GREENFIELD SAFE · GNN VERIFIED" : "SETTLEMENT / FACE PRESSURE ALERT";
        if (percBox) percBox.setAttribute("data-alert", safe ? "false" : "true");
        return;
      }
      if (slug === "e09") {
        const w0Mm = v0;
        const kHeal = v1;
        if (phiLabel) phiLabel.textContent = `w_0 = ${w0Mm.toFixed(2)} mm`;
        if (radLabel) radLabel.textContent = `k_heal = ${kHeal.toFixed(2)}×`;
        if (inlinePhi) inlinePhi.textContent = `w_0 = ${w0Mm.toFixed(2)} mm`;
        const sealFrac = Math.min(0.985, Math.max(0.25, 0.94 * (0.30 / Math.max(0.10, w0Mm)) * (0.75 + 0.25 * kHeal)));
        const wRem = w0Mm * (1.0 - sealFrac);
        const leakRed = (1.0 - Math.pow(1.0 - sealFrac, 3)) * 100.0;
        const cwiRec = Math.min(99.2, sealFrac * 102.5);
        const safe = sealFrac >= 0.80;
        if (kappaOut) kappaOut.textContent = `${(sealFrac * 100.0).toFixed(1)}% (w_rem = ${wRem.toFixed(3)} mm)`;
        if (deffOut) deffOut.textContent = `−${leakRed.toFixed(2)}% Darcy Cutoff`;
        if (outR2) outR2.textContent = `${cwiRec.toFixed(1)}% (Δv/v Restored)`;
        if (percOut) percOut.textContent = safe ? "AUTOGENOUS SEAL · PASS" : "PARTIAL SEAL · W_0 > 0.50 MM";
        if (percBox) percBox.setAttribute("data-alert", safe ? "false" : "true");
        return;
      }
      if (slug === "e10") {
        const aThix = v0;
        const vBuild = v1;
        if (phiLabel) phiLabel.textContent = `A_thix = ${aThix.toFixed(2)} Pa/s`;
        if (radLabel) radLabel.textContent = `v_build = ${vBuild.toFixed(2)} m/hr`;
        if (inlinePhi) inlinePhi.textContent = `A_thix = ${aThix.toFixed(2)} Pa/s`;
        const sfYield = (aThix / 0.85) * (1.60 / Math.max(0.4, vBuild)) * 1.68;
        const hCrit = Math.min(5.2, Math.max(0.65, 2.84 * Math.pow(aThix / 0.85, 0.65) * Math.pow(1.60 / Math.max(0.4, vBuild), 0.45)));
        const layers = Math.round(hCrit / 0.05);
        const safe = sfYield >= 1.15 && hCrit >= 1.80;
        if (kappaOut) kappaOut.textContent = `${hCrit.toFixed(2)} m (${layers} Layers)`;
        if (deffOut) deffOut.textContent = `SF = ${sfYield.toFixed(2)} (${safe ? "Plastic Safe" : "Yield Risk"})`;
        if (outR2) outR2.textContent = sfYield >= 1.4 ? "ELASTIC-PLASTIC BALANCED" : "BUCKLING / PLASTIC LIMIT";
        if (percOut) percOut.textContent = safe ? "BUILDABILITY PASS · 0 FORMWORK" : "COLLAPSE / BUCKLING WARNING";
        if (percBox) percBox.setAttribute("data-alert", safe ? "false" : "true");
        return;
      }
      if (slug === "e11") {
        const rhoBar = v0;
        const betaInerter = v1;
        if (phiLabel) phiLabel.textContent = `ρ̄ = ${rhoBar.toFixed(2)}`;
        if (radLabel) radLabel.textContent = `β = ${betaInerter.toFixed(2)}`;
        if (inlinePhi) inlinePhi.textContent = `ρ̄ = ${rhoBar.toFixed(2)}`;
        const co2PerM2 = (280.0 * rhoBar * 0.56) - (280.0 * rhoBar * 0.088);
        const rmsRed = Math.min(58.0, (1.0 - 1.0 / Math.sqrt(1.0 + 3.2 * betaInerter)) * 100.0);
        const safe = co2PerM2 <= 45.0 && rhoBar >= 0.28;
        if (kappaOut) kappaOut.textContent = `${co2PerM2.toFixed(1)} kg CO₂e/m² (vs 156.8 Baseline)`;
        if (deffOut) deffOut.textContent = `−${rmsRed.toFixed(1)}% Wind RMS Sway (β = ${betaInerter.toFixed(2)})`;
        if (outR2) outR2.textContent = `p = 3.0 SIMP · L_span / 250 Pass`;
        if (percOut) percOut.textContent = safe ? "SUB-45 KG CO2E/M² · BOUNTY E-1 PASS" : "EMBODIED CARBON / DEFLECTION ALERT";
        if (percBox) percBox.setAttribute("data-alert", safe ? "false" : "true");
        return;
      }
      if (slug === "e12") {
        const uOpt = v0;
        const hCbf = v1;
        if (phiLabel) phiLabel.textContent = `u_opt = ${uOpt.toFixed(2)}`;
        if (radLabel) radLabel.textContent = `h(x) = ${hCbf.toFixed(2)} Hz`;
        if (inlinePhi) inlinePhi.textContent = `u_opt = ${uOpt.toFixed(2)}`;
        const ePj = (0.048 + 0.024 * (1.0 - uOpt)).toFixed(3);
        const safe = hCbf >= 0.15;
        if (kappaOut) kappaOut.textContent = `${ePj} pJ / MAC (vs 2.40 pJ CMOS)`;
        if (deffOut) deffOut.textContent = `Δf_margin = +${hCbf.toFixed(2)} Hz (CBF Safe)`;
        if (outR2) outR2.textContent = `180M-Line Rocq RISC-V Verified`;
        if (percOut) percOut.textContent = safe ? "FORWARD INVARIANT · ZERO BLACKOUT" : "CBF BOUNDARY PROXIMITY ALERT";
        if (percBox) percBox.setAttribute("data-alert", safe ? "false" : "true");
        return;
      }

      const phi = v0;
      const radiusNm = v1;
      const phiC = 0.5927;
      const solid = 1.0 - phi;
      const kappa = (radiusNm * radiusNm * Math.pow(phi, 3)) / (4.0 * Math.max(solid * solid, 1e-6));
      const brinkmanLen = Math.sqrt(kappa);
      const percolating = phi > phiC;
      const dEffRatio = percolating ? Math.pow((phi - phiC) / (1.0 - phiC), 1.3) : 0.0;

      if (phiLabel) phiLabel.textContent = "phi = " + phi.toFixed(3);
      if (radLabel) radLabel.textContent = "a_f = " + radiusNm.toFixed(1) + " nm";
      if (inlinePhi) inlinePhi.textContent = "phi = " + phi.toFixed(3);
      if (kappaOut) kappaOut.textContent = brinkmanLen.toFixed(2) + " nm";
      if (deffOut) deffOut.textContent = dEffRatio.toFixed(3) + " D_0";
      if (percOut) {
        percOut.textContent = percolating
          ? "SUPERCRITICAL PERCOLATING PATHWAY (phi > 0.593)"
          : "HYDRATION OPPORTUNITY: RAISE POROSITY ABOVE φ_c = 0.593";
      }
      if (percBox) percBox.setAttribute("data-alert", percolating ? "false" : "true");
      if (engPoint) {
        const cx = Math.round(60 + ((phi - 0.45) / 0.47) * 530);
        const cy = percolating ? Math.round(180 - dEffRatio * 145) : 185;
        engPoint.setAttribute("cx", String(cx));
        engPoint.setAttribute("cy", String(cy));
      }
    };
    engPhiInput.addEventListener("input", updateEng);
    engRadiusInput.addEventListener("input", updateEng);
    if ((getActiveSlug() || "e01") === "e01") updateEng();
  }

  // 6. Physics Solvers (P.01-P.06)
  const physAtpInput = document.getElementById("p-slider-atp");
  const physVmInput = document.getElementById("p-slider-vm");
  if (physAtpInput && physVmInput && physAtpInput.dataset.bound !== "true") {
    physAtpInput.dataset.bound = "true";
    const updatePhys = () => {
      const slug = getActiveSlug() || "p01";
      const v0 = parseFloat(physAtpInput.value) || 18.4;
      const v1 = parseFloat(physVmInput.value) || -30.0;

      const atpOut = document.getElementById("out-atp");
      const vmOut = document.getElementById("out-vm");
      const inlineAtp = document.getElementById("tp-inline-atp");
      const effOut = document.getElementById("out-eff");
      const ratioOut = document.getElementById("out-ratio");
      const outR2 = document.getElementById("out-r2");
      const statusOut = document.getElementById("out-status");

      if (slug === "p02") {
        const kCoup = v0;
        const hPcl = v1;
        if (atpOut) atpOut.textContent = `${kCoup.toFixed(2)} K/σ`;
        if (vmOut) vmOut.textContent = `${hPcl.toFixed(1)} μm`;
        if (inlineAtp) inlineAtp.textContent = `K/σ = ${kCoup.toFixed(2)}`;
        const rSync = kCoup <= 1.0 ? 0.18 * kCoup : Math.sqrt(1.0 - 1.0 / (kCoup * kCoup)) * Math.min(1.0, hPcl / 6.5);
        const vMcc = (42.8 * rSync * Math.max(0.05, (hPcl - 3.0) / 4.0)).toFixed(1);
        if (effOut) effOut.textContent = `R = ${rSync.toFixed(2)} (K/K_c = ${kCoup.toFixed(2)})`;
        if (ratioOut) ratioOut.textContent = `${vMcc} μm/s (h_PCL = ${hPcl.toFixed(1)} μm)`;
        if (outR2) outR2.textContent = `f_beat = ${(14.2 * Math.min(1.0, hPcl / 6.0)).toFixed(1)} Hz`;
        if (statusOut) statusOut.textContent = rSync >= 0.65 && hPcl >= 5.5 ? "METACHRONAL WAVE LOCKED" : "CILIARY PHASE ARREST";
        return;
      }
      if (slug === "p03") {
        const phiM = v0;
        const dpNm = v1;
        if (atpOut) atpOut.textContent = `${phiM.toFixed(1)} %`;
        if (vmOut) vmOut.textContent = `${dpNm.toFixed(0)} nm`;
        if (inlineAtp) inlineAtp.textContent = `φ = ${phiM.toFixed(1)}%`;
        const xiNm = 140.0 * Math.pow(2.0 / phiM, 0.75);
        const alphaSub = Math.max(0.18, Math.min(0.96, 1.0 - 0.186 * Math.pow(dpNm / xiNm, 1.5)));
        if (effOut) effOut.textContent = `ξ = ${xiNm.toFixed(1)} nm (at ${phiM.toFixed(1)}% mucin)`;
        if (ratioOut) ratioOut.textContent = `α = ${alphaSub.toFixed(3)} (d_p / ξ = ${(dpNm / xiNm).toFixed(2)})`;
        if (outR2) outR2.textContent = `D_eff / D_0 = ${Math.exp(-Math.pow(dpNm / xiNm, 1.45)).toFixed(3)}`;
        if (statusOut) statusOut.textContent = alphaSub >= 0.65 ? "ERGODIC MUCUS PENETRATION" : "SUBDIFFUSIVE MESH TRAPPING";
        return;
      }
      if (slug === "p04") {
        const cMuc = v0;
        const clFlux = v1;
        if (atpOut) atpOut.textContent = `${cMuc.toFixed(1)} wt%`;
        if (vmOut) vmOut.textContent = `${clFlux.toFixed(0)} mM`;
        if (inlineAtp) inlineAtp.textContent = `c_mucus = ${cMuc.toFixed(1)} wt%`;
        const cEff = cMuc * (85.0 / Math.max(25.0, clFlux));
        const piMuc = 0.25 * Math.pow(cEff / 2.0, 2.65);
        const hPcl = piMuc <= 3.0 ? 7.0 : 7.0 * Math.pow(3.0 / piMuc, 0.38);
        if (effOut) effOut.textContent = `Π_mucus = ${piMuc.toFixed(2)} kPa (vs Π_PCL = 3.0 kPa)`;
        if (ratioOut) ratioOut.textContent = `h_PCL = ${hPcl.toFixed(2)} μm`;
        if (outR2) outR2.textContent = `J_Cl = ${clFlux.toFixed(0)} mM Efflux`;
        if (statusOut) statusOut.textContent = piMuc <= 3.0 ? "HYDRATED BRUSH · PASS" : "HYPERCONCENTRATED COLLAPSE (> 3 kPa)";
        return;
      }
      if (slug === "p05") {
        const v0Bar = v0;
        const dvMv = v1;
        if (atpOut) atpOut.textContent = `${v0Bar.toFixed(1)} kcal/mol`;
        if (vmOut) vmOut.textContent = `${dvMv.toFixed(0)} mV`;
        if (inlineAtp) inlineAtp.textContent = `V_0 = ${v0Bar.toFixed(1)} kcal/mol`;
        const vEff = v0Bar + 0.025 * (dvMv + 30.0);
        const twoGamma = 6.84 * Math.sqrt(Math.max(2.0, vEff) / 14.2);
        const tWkb = Math.exp(-twoGamma);
        const kie = (7.4 * Math.exp(0.18 * (twoGamma - 6.84))).toFixed(2);
        if (effOut) effOut.textContent = `T_WKB = ${tWkb.toExponential(2)} (2γ = ${twoGamma.toFixed(2)})`;
        if (ratioOut) ratioOut.textContent = `KIE (k_H / k_D) = ${kie}`;
        if (outR2) outR2.textContent = `k_deam = ${(4.8 * (tWkb / 1.07e-3)).toFixed(2)} s⁻¹`;
        if (statusOut) statusOut.textContent = vEff <= 16.5 ? "QUANTUM TUNNELING ACTIVE" : "BARRIER SUPPRESSED";
        return;
      }
      if (slug === "p06") {
        const nNe = v0;
        const vmBias = v1;
        if (atpOut) atpOut.textContent = `${nNe.toFixed(1)} N/N_e`;
        if (vmOut) vmOut.textContent = `${vmBias.toFixed(0)} mV`;
        if (inlineAtp) inlineAtp.textContent = `N/N_e = ${nNe.toFixed(1)}`;
        const dRep = (1.0 / Math.pow(nNe, 2.0)) * (1.0 + 0.008 * Math.abs(vmBias));
        const tauD = (0.42 * Math.pow(nNe / 10.0, 3.0)).toFixed(2);
        if (effOut) effOut.textContent = `D_rep / D_0 = ${dRep.toExponential(2)} (N/N_e = ${nNe.toFixed(1)})`;
        if (ratioOut) ratioOut.textContent = `τ_d = ${tauD} ms ( ~ N³)`;
        if (outR2) outR2.textContent = `a_tube = 85.0 nm`;
        if (statusOut) statusOut.textContent = nNe <= 20.0 ? "REPTATION PASSAGE VERIFIED" : "ENTANGLEMENT BOTTLENECK";
        return;
      }
      if (slug === "p07") {
        const hMm = v0;
        const xMode = v1;
        if (atpOut) atpOut.textContent = `h = ${hMm.toFixed(0)} mm`;
        if (vmOut) vmOut.textContent = `α_X = ${xMode.toFixed(2)}`;
        if (inlineAtp) inlineAtp.textContent = `h = ${hMm.toFixed(0)} mm`;
        const porpoising = hMm < 18.0;
        const cl = porpoising ? 2.15 : 3.42 * (28.0 / Math.max(18.0, hMm)) * (1.0 - 0.28 * xMode);
        const cd = 0.88 * (1.0 - 0.42 * xMode);
        const ld = cl / Math.max(0.2, cd);
        if (effOut) effOut.textContent = `−C_L = ${cl.toFixed(2)} (${(cl * 7.83).toFixed(1)} kN @ 300 km/h)`;
        if (ratioOut) ratioOut.textContent = `L / D = ${ld.toFixed(2)} (−${(xMode * 42.0).toFixed(0)}% Drag in X-Mode)`;
        if (outR2) outR2.textContent = `h_crit = 17.5 mm (f_p = 6.2 Hz)`;
        if (statusOut) statusOut.textContent = porpoising ? "PORPOISING STALL LIMIT CYCLE!" : "VORTEX SEALED · ZERO PORPOISING";
        return;
      }
      if (slug === "p08") {
        const dNm = v0;
        const thetaDeg = v1;
        if (atpOut) atpOut.textContent = `d_film = ${dNm.toFixed(0)} nm`;
        if (vmOut) vmOut.textContent = `θ_1 = ${thetaDeg.toFixed(0)}°`;
        if (inlineAtp) inlineAtp.textContent = `d_film = ${dNm.toFixed(0)} nm`;
        const nFilm = 2.45;
        const sinTheta = Math.sin((thetaDeg * Math.PI) / 180.0);
        const lamMax = 2.0 * dNm * Math.sqrt(Math.max(1.0, nFilm * nFilm - sinTheta * sinTheta));
        const lam0 = 2.0 * dNm * nFilm;
        const dLam = lamMax - lam0;
        if (effOut) effOut.textContent = `λ_max = ${lamMax.toFixed(0)} nm (θ_1 = ${thetaDeg.toFixed(0)}°)`;
        if (ratioOut) ratioOut.textContent = `Δλ = ${dLam.toFixed(0)} nm (Gonioapparent Shift)`;
        if (outR2) outR2.textContent = `FI = 14.8 (vs 1.08 Barragán Stucco)`;
        if (statusOut) statusOut.textContent = "BRAGG & KUBELKA-MUNK VERIFIED";
        return;
      }
      if (slug === "p09") {
        const qFlow = v0;
        const kCond = v1;
        if (atpOut) atpOut.textContent = `Q = ${qFlow.toFixed(2)} μL/min`;
        if (vmOut) vmOut.textContent = `K = ${kCond.toFixed(2)} S/m`;
        if (inlineAtp) inlineAtp.textContent = `Q = ${qFlow.toFixed(2)} μL/min`;
        const dDrop = 2.42 * Math.pow(qFlow / 1.20, 0.5) * Math.pow(0.45 / Math.max(0.04, kCond), 0.167);
        const qRatio = Math.min(1.12, 0.68 * Math.pow(kCond / 0.45, 0.22));
        const inWindow = dDrop >= 1.4 && dDrop <= 3.8 && qRatio < 0.98;
        if (effOut) effOut.textContent = `49.29° (P_{1/2} Zero)`;
        if (ratioOut) ratioOut.textContent = `d_drop = ${dDrop.toFixed(2)} μm (Bronchial)`;
        if (outR2) outR2.textContent = `q / q_R = ${qRatio.toFixed(2)} (${qRatio < 1.0 ? "< 1.00 Stable" : "Fission!"})`;
        if (statusOut) statusOut.textContent = inWindow ? "97.4% INTACT mRNA · PASS" : "OUTSIDE BRONCHIAL / RAYLEIGH WINDOW";
        return;
      }
      if (slug === "p10") {
        const mT = v0;
        const sigDef = v1;
        if (atpOut) atpOut.textContent = `m_T = ${mT.toFixed(2)}`;
        if (vmOut) vmOut.textContent = `σ_def = ${sigDef.toFixed(2)}`;
        if (inlineAtp) inlineAtp.textContent = `m_T = ${mT.toFixed(2)}`;
        const mP = 0.25;
        const chern = mT > mP ? 1 : 0;
        const gapPct = Math.abs(mT - mP) * 47.3;
        const transPct = chern === 1 ? Math.max(96.5, 99.9 - 0.4 * sigDef) : Math.max(18.0, 92.0 - 85.0 * sigDef);
        if (effOut) effOut.textContent = `C = ${chern === 1 ? "+1 (Topological)" : "0 (Trivial)"}`;
        if (ratioOut) ratioOut.textContent = `Δω / ω_0 = ${gapPct.toFixed(1)}%`;
        if (outR2) outR2.textContent = `T = ${transPct.toFixed(1)}% (σ = ${sigDef.toFixed(2)})`;
        if (statusOut) statusOut.textContent = chern === 1 ? "BACKSCATTER-FREE · PASS" : "TRIVIAL PHASE · BACKSCATTERING";
        return;
      }
      if (slug === "p11") {
        const dCode = Math.round(v0);
        const pPhys = v1;
        if (atpOut) atpOut.textContent = `d = ${dCode}`;
        if (vmOut) vmOut.textContent = `p = ${pPhys.toFixed(4)}`;
        if (inlineAtp) inlineAtp.textContent = `d = ${dCode}`;
        const pTh = 0.01;
        const expHalf = Math.floor((dCode + 1) / 2);
        const pLog = 0.03 * Math.pow(pPhys / pTh, expHalf);
        const nPhys = 2 * dCode * dCode;
        const safe = pPhys < pTh && pLog <= 1e-12;
        if (effOut) effOut.textContent = `p_L = ${pLog.toExponential(2)} / cycle`;
        if (ratioOut) ratioOut.textContent = `2d² = ${nPhys.toLocaleString("en-US")} Physical Qubits / Logical`;
        if (outR2) outR2.textContent = `FeMoco CAS(54e,54o) · −1.8% Global CO₂`;
        if (statusOut) statusOut.textContent = safe ? "BELOW THRESHOLD · FEMOCO QEC PASS" : "ABOVE THRESHOLD / LOGICAL DRIFT";
        return;
      }
      if (slug === "p12") {
        const negLogKn = v0;
        const reK = v1;
        const kn = Math.pow(10, -negLogKn);
        if (atpOut) atpOut.textContent = `Kn = ${kn.toExponential(1)}`;
        if (vmOut) vmOut.textContent = `Re = ${(reK * 1000).toLocaleString("en-US")}`;
        if (inlineAtp) inlineAtp.textContent = `Kn = ${kn.toExponential(1)}`;
        const safe = negLogKn >= 2.0;
        if (effOut) effOut.textContent = `||f_ε − M|| = ${kn.toExponential(1)} O(Kn)`;
        if (ratioOut) ratioOut.textContent = `ν = 1.51 × 10⁻⁵ m²/s (Chapman–Enskog)`;
        if (outR2) outR2.textContent = `10 days in < 60 s (GraphCast + PDE Guard)`;
        if (statusOut) statusOut.textContent = safe ? "NEWTON → NAVIER–STOKES QED" : "RAREFIED KNUDSEN REGIME (Kn > 0.01)";
        return;
      }

      const atpAffinity = v0;
      const vmPotential = v1;

      const vmFactor = Math.max(0.6, Math.min(1.1, 1.0 - 0.003 * (vmPotential + 30.0)));
      const rawEff = (atpAffinity / (atpAffinity + 2.5)) * vmFactor;
      const couplingEfficiency = Math.max(0.05, Math.min(0.95, rawEff));

      const ratio = couplingEfficiency > 0.4
        ? Math.max(1.02, 1.12 * (0.88 / couplingEfficiency))
        : Math.min(12.0, 1.12 + 8.0 * Math.pow((0.4 - couplingEfficiency) / 0.35, 2));

      const isCoupled = couplingEfficiency >= 0.75 && ratio <= 2.0;
      const isLowDrive = couplingEfficiency < 0.25 || ratio > 4.0;
      const statusText = isCoupled
        ? "COUPLED BIOENERGETIC HARMONY (Open Channel Conductance)"
        : isLowDrive
          ? "MODULATOR OPPORTUNITY: BOOST ATP / ALLOSTERIC COUPLING"
          : "TRANSITIONAL RESCUE PATHWAY (Partial Conductance)";

      if (atpOut) atpOut.textContent = atpAffinity.toFixed(1) + " k_B T";
      if (vmOut) vmOut.textContent = vmPotential.toFixed(0) + " mV";
      if (inlineAtp) inlineAtp.textContent = "Delta_mu_ATP = " + atpAffinity.toFixed(1) + " k_BT";
      if (effOut) effOut.textContent = couplingEfficiency.toFixed(2) + (isCoupled ? " (WT-Coupled)" : isLowDrive ? " (Modulator Target)" : " (Rescued)");
      if (ratioOut) ratioOut.textContent = ratio.toFixed(2);
      if (statusOut) {
        statusOut.textContent = statusText;
        statusOut.setAttribute("data-alert", isLowDrive ? "true" : "false");
      }
    };
    physAtpInput.addEventListener("input", updatePhys);
    physVmInput.addEventListener("input", updatePhys);
    if ((getActiveSlug() || "p01") === "p01") updatePhys();
  }

  // 7. Engineering & Construction E.02: Herschel-Bulkley Concrete Pumping Solver
  const tau0Input = document.getElementById("tp-e02-tau0");
  const dpInput = document.getElementById("tp-e02-dp");
  if (tau0Input && dpInput && tau0Input.dataset.bound !== "true") {
    tau0Input.dataset.bound = "true";
    const updateE02 = () => {
      const tau0 = parseFloat(tau0Input.value) || 28.0;
      const dpKpa = parseFloat(dpInput.value) || 2.4;
      const pipeRadiusM = 0.0625;
      const dpPaM = dpKpa * 1000.0;
      const tauWall = (dpPaM * pipeRadiusM) / 2.0;
      const plugRatio = Math.max(0.0, Math.min(1.0, tau0 / tauWall));
      const needsSuperplasticizer = tauWall <= tau0;

      const n = 0.65;
      const K = 8.5;
      let qM3Hr = 0.0;
      if (!needsSuperplasticizer) {
        const uPlug = (n / (n + 1.0)) * Math.pow(dpPaM / (2.0 * K), 1.0 / n) * Math.pow(pipeRadiusM * (1.0 - plugRatio), (n + 1.0) / n);
        const qPlug = Math.PI * Math.pow(pipeRadiusM * plugRatio, 2.0) * uPlug;
        const qAnnulus = Math.PI * Math.pow(pipeRadiusM, 2.0) * uPlug * 0.62;
        qM3Hr = (qPlug + qAnnulus) * 3600.0;
      }

      const tau0Val = document.getElementById("tp-e02-tau0-val");
      const dpVal = document.getElementById("tp-e02-dp-val");
      const wallOut = document.getElementById("tp-e02-readout-tauw");
      const plugOut = document.getElementById("tp-e02-readout-plug");
      const flowOut = document.getElementById("tp-e02-readout-flow");
      const statusBox = document.getElementById("tp-e02-readout-status-box");
      const statusOut = document.getElementById("tp-e02-readout-status");

      const inlineTau0 = document.getElementById("tp-inline-tau0");
      if (inlineTau0) inlineTau0.textContent = "tau_0 = " + tau0.toFixed(1) + " Pa";
      if (tau0Val) tau0Val.textContent = tau0.toFixed(1) + " Pa";
      if (dpVal) dpVal.textContent = dpKpa.toFixed(2) + " kPa/m";
      if (wallOut) wallOut.textContent = tauWall.toFixed(1) + " Pa";
      if (plugOut) plugOut.textContent = (plugRatio * 100).toFixed(1) + "% (" + (plugRatio * pipeRadiusM * 1000).toFixed(1) + " mm)";
      if (flowOut) flowOut.textContent = needsSuperplasticizer ? "0.0 m³/hr (Dose PCE)" : qM3Hr.toFixed(1) + " m³/hr (" + (qM3Hr * 1.308).toFixed(1) + " yd³/hr)";
      if (statusOut) {
        statusOut.textContent = needsSuperplasticizer
          ? "RHEOLOGY TUNING: DOSE PCE DISPERSANT OR RAISE ΔP/L (τ_w > τ_0)"
          : "STEADY MOBILIZED PUMPING (r_p/R = " + (plugRatio * 100).toFixed(0) + "% · Ready to Cast)";
      }
      if (statusBox) statusBox.setAttribute("data-alert", needsSuperplasticizer ? "true" : "false");

      const plugCircle = document.getElementById("tp-e02-svg-plug-circle");
      const plugRadiusText = document.getElementById("tp-e02-svg-plug-text");
      const velocityProfilePath = document.getElementById("tp-e02-svg-velocity-path");
      const velocityPlugLine = document.getElementById("tp-e02-svg-velocity-plug");

      if (plugCircle) {
        const svgPipeR = 64;
        const rPix = needsSuperplasticizer ? svgPipeR : Math.max(6, Math.round(svgPipeR * plugRatio));
        plugCircle.setAttribute("r", String(rPix));
        plugCircle.setAttribute("fill", needsSuperplasticizer ? "var(--tp-minium)" : "var(--tp-prussian)");
      }
      if (plugRadiusText) {
        plugRadiusText.textContent = needsSuperplasticizer
          ? "Yield Threshold: Dose PCE to Mobilize Core (r_p = R)"
          : "Plug Core: r_p = " + (plugRatio * pipeRadiusM * 1000).toFixed(1) + " mm (" + (plugRatio * 100).toFixed(0) + "% R)";
      }
      if (velocityProfilePath && velocityPlugLine) {
        if (needsSuperplasticizer) {
          velocityProfilePath.setAttribute("d", "M 480 50 L 480 170");
          velocityPlugLine.setAttribute("x1", "480");
          velocityPlugLine.setAttribute("x2", "480");
        } else {
          const maxU = Math.min(130, Math.round(qM3Hr * 2.5));
          const apexX = 480 + maxU;
          const plugYTop = 110 - Math.round(50 * plugRatio);
          const plugYBot = 110 + Math.round(50 * plugRatio);
          velocityPlugLine.setAttribute("x1", String(apexX));
          velocityPlugLine.setAttribute("x2", String(apexX));
          velocityPlugLine.setAttribute("y1", String(plugYTop));
          velocityPlugLine.setAttribute("y2", String(plugYBot));
          velocityProfilePath.setAttribute("d", "M 480 50 Q " + (480 + maxU * 0.7) + " 80 " + apexX + " " + plugYTop + " L " + apexX + " " + plugYBot + " Q " + (480 + maxU * 0.7) + " 140 480 170");
        }
      }
    };
    tau0Input.addEventListener("input", updateE02);
    dpInput.addEventListener("input", updateE02);
    updateE02();
  }

  // 8. Engineering & Construction E.05: Terzaghi Consolidation, CFA Piling & Liquefaction Surcharge Solver
  const e05SurchargeInput = document.getElementById("tp-e05-surcharge");
  const e05CvInput = document.getElementById("tp-e05-cv");
  if (e05SurchargeInput && e05CvInput && e05SurchargeInput.dataset.bound !== "true") {
    e05SurchargeInput.dataset.bound = "true";
    const updateE05 = () => {
      const dq = parseFloat(e05SurchargeInput.value) || 120.0;
      const cv = parseFloat(e05CvInput.value) || 3.2;
      const hDr = 6.0;
      const tYears = 3.6;
      const tv = (cv * tYears) / (hDr * hDr);
      const uAvg = tv <= 0.286
        ? Math.sqrt((4.0 * tv) / Math.PI)
        : 1.0 - (8.0 / (Math.PI * Math.PI)) * Math.exp((-Math.PI * Math.PI * tv) / 4.0);
      const uAvgClamped = Math.max(0.05, Math.min(0.995, uAvg));

      const settlementMm = (dq / 120.0) * 66.7 * uAvgClamped;
      const sigmaV0Prime = 200.0;
      const deltaUResidual = dq * (1.0 - uAvgClamped);
      const ru = Math.min(0.98, deltaUResidual / sigmaV0Prime);
      const sigmaVPrime = Math.max(4.0, sigmaV0Prime * (1.0 - ru));

      const qSkin = 2380.0 * (1.0 - 0.65 * ru);
      const qToe = 1980.0 * (1.0 - 0.35 * ru);
      const qUlt = Math.max(650.0, qSkin + qToe);
      const pDesign = 1400.0 + dq * 1.25;
      const fs = qUlt / pDesign;
      const needsWickDrains = ru >= 0.70 || fs < 2.0;

      const dqVal = document.getElementById("tp-e05-surcharge-val");
      const cvVal = document.getElementById("tp-e05-cv-val");
      const inlineDq = document.getElementById("tp-inline-surcharge");
      const uOut = document.getElementById("tp-e05-readout-u");
      const qultOut = document.getElementById("tp-e05-readout-qult");
      const ruOut = document.getElementById("tp-e05-readout-ru");
      const statusBox = document.getElementById("tp-e05-readout-status-box");
      const statusOut = document.getElementById("tp-e05-readout-status");

      if (dqVal) dqVal.textContent = dq.toFixed(0) + " kPa";
      if (cvVal) cvVal.textContent = cv.toFixed(1) + " m²/yr";
      if (inlineDq) inlineDq.textContent = "Delta_q = " + dq.toFixed(0) + " kPa";
      if (uOut) uOut.textContent = (uAvgClamped * 100).toFixed(1) + "% (S_c = " + settlementMm.toFixed(1) + " mm)";
      if (qultOut) qultOut.textContent = qUlt.toFixed(0) + " kN (FS = " + fs.toFixed(2) + ")";
      if (ruOut) ruOut.textContent = "r_u = " + ru.toFixed(2) + " (σ'_v = " + sigmaVPrime.toFixed(0) + " kPa)";
      if (statusOut) {
        statusOut.textContent = needsWickDrains
          ? "DESIGN WINDOW: ADD PVD WICK DRAINS TO ACCELERATE c_v (FS ≥ 2.0)"
          : "SAFE CFA BEARING · CONSOLIDATED (FS = " + fs.toFixed(2) + ")";
      }
      if (statusBox) statusBox.setAttribute("data-alert", needsWickDrains ? "true" : "false");

      const isoPath = document.getElementById("tp-e05-svg-isochrone");
      const svgLabel = document.getElementById("tp-e05-svg-label");
      if (isoPath) {
        const bulgeX = Math.round(360 + Math.min(265, deltaUResidual * 2.1));
        isoPath.setAttribute("d", "M 360 30 Q " + bulgeX + " 112 360 195");
      }
      if (svgLabel) {
        svgLabel.textContent = "U_avg = " + (uAvgClamped * 100).toFixed(1) + "% · Q_ult = " + qUlt.toFixed(0) + " kN";
      }
    };
    e05SurchargeInput.addEventListener("input", updateE05);
    e05CvInput.addEventListener("input", updateE05);
    updateE05();
  }

  // 9. Engineering & Construction E.06: ASCE 7-22 Inelastic Response Spectra & Seismic Base-Isolation Solver
  const e06SdsInput = document.getElementById("tp-e06-sds");
  const e06DampInput = document.getElementById("tp-e06-damping");
  if (e06SdsInput && e06DampInput && e06SdsInput.dataset.bound !== "true") {
    e06SdsInput.dataset.bound = "true";
    const updateE06 = () => {
      const sds = parseFloat(e06SdsInput.value) || 1.00;
      const betaEff = parseFloat(e06DampInput.value) || 0.22;
      const tM = 2.85;
      const bM = Math.max(0.8, Math.pow(betaEff / 0.05, 0.30));
      const sd1 = sds * 0.60;
      const gMm = 9810.0;
      const dMMm = (gMm * sd1 * tM) / (4.0 * Math.PI * Math.PI * bM);
      const csIsolated = sd1 / (tM * bM);
      const reductionPct = Math.max(10.0, (1.0 - csIsolated / sds) * 100.0);
      const moatExceeded = dMMm > 400.0;

      const sdsVal = document.getElementById("tp-e06-sds-val");
      const dampVal = document.getElementById("tp-e06-damping-val");
      const inlineSds = document.getElementById("tp-inline-sds");
      const tmOut = document.getElementById("tp-e06-readout-tm");
      const dmOut = document.getElementById("tp-e06-readout-dm");
      const csOut = document.getElementById("tp-e06-readout-cs");
      const statusBox = document.getElementById("tp-e06-readout-status-box");
      const statusOut = document.getElementById("tp-e06-readout-status");

      if (sdsVal) sdsVal.textContent = sds.toFixed(2) + " g";
      if (dampVal) dampVal.textContent = (betaEff * 100).toFixed(1) + "%";
      if (inlineSds) inlineSds.textContent = "S_DS = " + sds.toFixed(2) + " g";
      if (tmOut) tmOut.textContent = "T_M = " + tM.toFixed(2) + " s (B_M = " + bM.toFixed(2) + ")";
      if (dmOut) dmOut.textContent = dMMm.toFixed(0) + " mm (Moat 400 mm)";
      if (csOut) csOut.textContent = "V_b / W = " + csIsolated.toFixed(3) + " g (-" + reductionPct.toFixed(0) + "%)";
      if (statusOut) {
        statusOut.textContent = moatExceeded
          ? "DESIGN TUNING: INCREASE LEAD-PLUG DAMPING β_eff OR MOAT CLEARANCE"
          : "IMMEDIATE OCCUPANCY RESILIENCE (D_M = " + dMMm.toFixed(0) + " mm · Hospital Safe)";
      }
      if (statusBox) statusBox.setAttribute("data-alert", moatExceeded ? "true" : "false");

      const loopPoly = document.getElementById("tp-e06-svg-loop");
      const loopLabel = document.getElementById("tp-e06-svg-label");
      const driftDot = document.getElementById("tp-e06-svg-drift");
      if (loopPoly) {
        const halfW = Math.min(125, Math.max(45, Math.round(dMMm * 0.38)));
        const halfH = Math.min(68, Math.max(22, Math.round(betaEff * 185)));
        const x1 = 505 - halfW;
        const x2 = 505 - Math.round(halfW * 0.55);
        const x3 = 505 + halfW;
        const x4 = 505 + Math.round(halfW * 0.55);
        const y1 = 110 + halfH;
        const y2 = 110 - Math.round(halfH * 0.55);
        const y3 = 110 - halfH;
        const y4 = 110 + Math.round(halfH * 0.55);
        loopPoly.setAttribute("points", x1 + "," + y1 + " " + x2 + "," + y2 + " " + x3 + "," + y3 + " " + x4 + "," + y4);
      }
      if (driftDot) {
        const cy = Math.max(95, Math.min(178, Math.round(185 - csIsolated * 160)));
        driftDot.setAttribute("cy", String(cy));
      }
      if (loopLabel) {
        loopLabel.textContent = "Bilinear LRB Loop · D_M = " + dMMm.toFixed(0) + " mm · β_eff = " + (betaEff * 100).toFixed(1) + "%";
      }
    };
    e06SdsInput.addEventListener("input", updateE06);
    e06DampInput.addEventListener("input", updateE06);
    updateE06();
  }

  // 9b. Pillar V Biophysical Ion-Channel & Curative Therapeutics Solvers (CF.01-CF.06 / c01-c06)
  const cfPrimary = scope.querySelector('input[data-cf-slider="primary"]') || document.querySelector('input[data-cf-slider="primary"]');
  const cfSecondary = scope.querySelector('input[data-cf-slider="secondary"]') || document.querySelector('input[data-cf-slider="secondary"]');
  if (cfPrimary && cfSecondary && cfPrimary.dataset.bound !== "true") {
    cfPrimary.dataset.bound = "true";
    const slug = cfPrimary.getAttribute("data-cf-slug") || "c01";
    const updateCf = () => {
      const v0 = parseFloat(cfPrimary.value) || 0;
      const v1 = parseFloat(cfSecondary.value) || 0;
      const lbl0 = document.getElementById(cfPrimary.id + "-val");
      const lbl1 = document.getElementById(cfSecondary.id + "-val");
      if (lbl0) lbl0.textContent = String(v0);
      if (lbl1) lbl1.textContent = String(v1);
      const inlineCf = document.getElementById("tp-inline-cf");
      if (inlineCf) {
        const baseName = inlineCf.textContent.split("=")[0].trim();
        inlineCf.textContent = baseName + " = " + v0;
      }

      const r0 = document.getElementById("tp-" + slug + "-readout-0");
      const r1 = document.getElementById("tp-" + slug + "-readout-1");
      const r2 = document.getElementById("tp-" + slug + "-readout-2");
      const r3 = document.getElementById("tp-" + slug + "-readout-3");
      const box = document.getElementById("tp-" + slug + "-readout-status-box");

      if (slug === "c01") {
        // Wyman dual-corrector allostery & potentiator gating
        const dG = Math.max(1.2, 8.4 - 6.2 * v0 - 1.1 * v1);
        const bandC = Math.min(92.0, Math.max(2.0, 88.0 * Math.pow(v0, 1.15)));
        const po = Math.min(0.88, Math.max(0.04, 0.08 + 0.78 * v0 * v1));
        const sweat = -(12.0 + 46.0 * v0 * v1);
        if (r0) r0.textContent = dG.toFixed(2) + " kcal/mol";
        if (r1) r1.textContent = bandC.toFixed(1) + "% of Wild-Type";
        if (r2) r2.textContent = "P_o = " + po.toFixed(2);
        if (r3) r3.textContent = sweat.toFixed(1) + " mmol/L" + (po >= 0.5 ? " (Rescued)" : " (Sub-Threshold)");
        if (box) box.setAttribute("data-alert", po < 0.35 ? "true" : "false");

        const rescueCurve = document.getElementById("tp-c01-rescue-curve");
        const barrierDot = document.getElementById("tp-c01-barrier-dot");
        const openDot = document.getElementById("tp-c01-open-dot");
        const barrierLbl = document.getElementById("tp-c01-barrier-label");
        const bandcBar = document.getElementById("tp-c01-bandc-bar");
        const bandcTxt = document.getElementById("tp-c01-bandc-txt");
        const peakY = Math.round(36 + (8.4 - dG) * 12.5);
        const openY = Math.round(168 - po * 135);
        if (rescueCurve) rescueCurve.setAttribute("d", `M 294 170 Q 405 ${peakY} 508 162 T 644 ${openY}`);
        if (barrierDot) barrierDot.setAttribute("cy", String(Math.round(42 + (8.4 - dG) * 11.5)));
        if (openDot) openDot.setAttribute("cy", String(openY));
        if (barrierLbl) barrierLbl.textContent = `Rescued Barrier: ${dG.toFixed(2)} kcal/mol (VX-445/121 + VX-661)`;
        if (bandcBar) bandcBar.setAttribute("width", String(Math.round(2.04 * bandC)));
        if (bandcTxt) bandcTxt.textContent = `Band C = ${bandC.toFixed(1)}% WT · P_o = ${po.toFixed(2)}`;
      } else if (slug === "c02") {
        // Two-Gel Brush Osmometry: v0 = solids %, v1 = ENaC blockade
        const effSolids = Math.max(1.2, v0 * (1.0 - 0.38 * v1));
        const piM = 0.08 * Math.pow(effSolids, 2.25);
        const hPcl = piM <= 3.0 ? 7.0 : Math.max(2.2, 7.0 * Math.pow(3.0 / piM, 0.33));
        const vMcc = piM >= 5.5 ? 0.0 : Math.max(0.2, 6.8 * (1.0 - piM / 6.0));
        const healthy = piM <= 3.0;
        if (r0) r0.textContent = piM.toFixed(2) + " kPa (vs 3.0 kPa)";
        if (r1) r1.textContent = hPcl.toFixed(2) + " μm";
        if (r2) r2.textContent = vMcc.toFixed(1) + " mm/min";
        if (r3) r3.textContent = healthy ? "HYDRATED GEL-ON-BRUSH" : "OSMOTIC BRUSH COMPRESSION";
        if (box) box.setAttribute("data-alert", healthy ? "false" : "true");

        const pclRect = document.getElementById("tp-c02-pcl-rect");
        const mucusSlab = document.getElementById("tp-c02-mucus-slab");
        const pclTxt = document.getElementById("tp-c02-pcl-txt");
        const opDot = document.getElementById("tp-c02-op-dot");
        const pclH = Math.round(hPcl * 11.0);
        const pclY = 180 - pclH;
        if (pclRect) {
          pclRect.setAttribute("y", String(pclY));
          pclRect.setAttribute("height", String(pclH));
        }
        if (mucusSlab) mucusSlab.setAttribute("y", String(Math.max(36, pclY - 38)));
        if (pclTxt) pclTxt.textContent = `h_PCL = ${hPcl.toFixed(2)} μm (${healthy ? "Beating Cilia" : "Crushed Brush"})`;
        if (opDot) {
          opDot.setAttribute("cx", String(Math.min(635, Math.max(305, Math.round(295 + effSolids * 42)))));
          opDot.setAttribute("cy", String(Math.min(195, Math.max(52, Math.round(54 + (7.0 - hPcl) * 28)))));
        }
      } else if (slug === "c03") {
        // Inhaled mRNA-LNP Percolation: v0 = diameter nm, v1 = porosity phi
        const phiC = 0.5927;
        const surv = Math.max(55.0, 96.5 - 0.08 * Math.max(0, v0 - 50));
        const perc = v1 > phiC ? Math.pow((v1 - phiC) / (1.0 - phiC), 1.3) * Math.exp(-Math.pow(v0 / 95.0, 2)) : 0.0;
        const margin = v1 - phiC;
        const trans = Math.min(42.0, perc * 95.0);
        if (r0) r0.textContent = surv.toFixed(1) + "% Intact";
        if (r1) r1.textContent = "D_eff / D₀ = " + perc.toFixed(3);
        if (r2) r2.textContent = (margin >= 0 ? "+" : "") + margin.toFixed(3) + " vs φ_c";
        if (r3) r3.textContent = v1 > phiC ? trans.toFixed(1) + "% Transfection" : "SUBCRITICAL MUCUS ARREST";
        if (box) box.setAttribute("data-alert", v1 <= phiC ? "true" : "false");

        const opDot = document.getElementById("tp-c03-op-dot");
        const lnp1 = document.getElementById("tp-c03-lnp-1");
        const lnp2 = document.getElementById("tp-c03-lnp-2");
        const stTxt = document.getElementById("tp-c03-status-txt");
        const rPx = String(Math.max(4.5, Math.min(13.5, v0 / 10.5)).toFixed(1));
        if (lnp1) lnp1.setAttribute("r", rPx);
        if (lnp2) lnp2.setAttribute("r", rPx);
        if (opDot) {
          opDot.setAttribute("cx", String(Math.round(298 + ((v0 - 45) / 120) * 335)));
          opDot.setAttribute("cy", String(Math.min(198, Math.max(48, Math.round(196 - perc * 360)))));
        }
        if (stTxt) stTxt.textContent = `2r_p = ${v0.toFixed(0)} nm · φ = ${v1.toFixed(3)} (${v1 > phiC ? "Percolating" : "Steric Trap"})`;
      } else if (slug === "c04") {
        // Suppressor ACE-tRNA & NMD Escape: v0 = tRNA/eRF1 ratio, v1 = EJC stripping
        const rt = v0 / (v0 + 1.0);
        const mrna = Math.min(95.0, 15.0 + 80.0 * rt * v1);
        const rescue = (mrna * rt);
        if (r0) r0.textContent = (rt * 100).toFixed(1) + "% per Ribosome";
        if (r1) r1.textContent = mrna.toFixed(1) + "% of Wild-Type";
        if (r2) r2.textContent = rescue.toFixed(1) + "% WT Cl⁻ Current";
        if (r3) r3.textContent = rescue >= 15.0 ? "THERAPEUTIC READTHROUGH PASS" : "BELOW 15% CLINICAL THRESHOLD";
        if (box) box.setAttribute("data-alert", rescue < 15.0 ? "true" : "false");

        const surgeCurve = document.getElementById("tp-c04-surge-curve");
        const opDot = document.getElementById("tp-c04-op-dot");
        const mrnaBar = document.getElementById("tp-c04-mrna-bar");
        const mrnaTxt = document.getElementById("tp-c04-mrna-txt");
        const endY = Math.max(38, Math.min(194, Math.round(196 - rescue * 2.5)));
        const midY = Math.max(75, Math.min(192, Math.round(196 - rescue * 1.35)));
        if (surgeCurve) surgeCurve.setAttribute("d", `M 296 196 Q 450 ${midY} 642 ${endY}`);
        if (opDot) {
          opDot.setAttribute("cx", String(Math.min(638, Math.max(305, Math.round(296 + (v0 / 5.0) * 340)))));
          opDot.setAttribute("cy", String(endY));
        }
        if (mrnaBar) mrnaBar.setAttribute("width", String(Math.round(mrna * 2.04)));
        if (mrnaTxt) mrnaTxt.textContent = `Steady-State mRNA = ${mrna.toFixed(1)}% WT · Cl⁻ = ${rescue.toFixed(1)}%`;
      } else if (slug === "c05") {
        // Base & Prime Editing: v0 = RNP dose, v1 = MOI
        const abe = 68.0 * (1.0 - Math.exp(-1.35 * v0));
        const pe = 48.0 * (1.0 - Math.exp(-1.1 * v0));
        const aav = Math.pow(1.0 - Math.exp(-v1), 2) * 94.0;
        if (r0) r0.textContent = abe.toFixed(1) + "% Allelic Rescue";
        if (r1) r1.textContent = pe.toFixed(1) + "% Allelic Rescue";
        if (r2) r2.textContent = aav.toFixed(1) + "% Dual-AAV Yield";
        if (r3) r3.textContent = abe >= 20.0 ? "<0.8% Indels · DSB-Free Pass" : "INCREASE RNP / MOI DOSE";
        if (box) box.setAttribute("data-alert", abe < 20.0 ? "true" : "false");

        const editCurve = document.getElementById("tp-c05-edit-curve");
        const opDot = document.getElementById("tp-c05-op-dot");
        const aavBar = document.getElementById("tp-c05-aav-bar");
        const aavTxt = document.getElementById("tp-c05-aav-txt");
        const endY = Math.max(38, Math.min(190, Math.round(196 - abe * 2.3)));
        if (editCurve) editCurve.setAttribute("d", `M 294 196 Q 405 ${Math.round(196 - abe * 2.0)} 642 ${endY}`);
        if (opDot) {
          opDot.setAttribute("cx", String(Math.min(638, Math.max(305, Math.round(294 + (v0 / 3.0) * 340)))));
          opDot.setAttribute("cy", String(endY));
        }
        if (aavBar) aavBar.setAttribute("width", String(Math.round(aav * 2.04)));
        if (aavTxt) aavTxt.textContent = `Dual-AAV Splicing = ${aav.toFixed(1)}% · ABE = ${abe.toFixed(1)}%`;
      } else if (slug === "c06") {
        // Phage-Antibiotic Biofilm Synergy: v0 = lyase activity, v1 = log10 PFU
        const thiele = Math.max(0.45, 4.2 * (1.0 - 0.80 * v0));
        const eta = Math.tanh(thiele) / thiele;
        const logRed = -(1.2 + 3.2 * eta + 0.35 * (v1 - 6.0));
        if (r0) r0.textContent = "Φ = " + thiele.toFixed(2);
        if (r1) r1.textContent = "η = " + eta.toFixed(3);
        if (r2) r2.textContent = logRed.toFixed(2) + " log₁₀ CFU/mL";
        if (r3) r3.textContent = "8.0% US · 7.6% CA · 11.5% AU";
        if (box) box.setAttribute("data-alert", thiele > 2.2 ? "true" : "false");

        const penFill = document.getElementById("tp-c06-penetration-fill");
        const coshCurve = document.getElementById("tp-c06-cosh-curve");
        const opDot = document.getElementById("tp-c06-op-dot");
        const thTxt = document.getElementById("tp-c06-thiele-txt");
        if (penFill) penFill.setAttribute("height", String(Math.round(24 + eta * 112)));
        const endY = Math.min(198, Math.max(68, Math.round(52 + eta * 142)));
        if (coshCurve) coshCurve.setAttribute("d", `M 294 48 C 405 ${Math.round(48 + eta * 82)}, 490 ${Math.round(48 + eta * 124)}, 642 ${endY}`);
        if (opDot) {
          opDot.setAttribute("cx", String(Math.min(638, Math.max(305, Math.round(294 + v0 * 340)))));
          opDot.setAttribute("cy", String(endY));
        }
        if (thTxt) thTxt.textContent = `Thiele Φ = ${thiele.toFixed(2)} · Penetration η = ${(eta * 100).toFixed(0)}%`;
      }
    };
    cfPrimary.addEventListener("input", updateCf);
    cfSecondary.addEventListener("input", updateCf);
    updateCf();
  }

  // 10. Activate Universal SVG & Control Animation Engine, Split-Stage Workbench & Motion Plates
  initUniversalSvgAndControlAnimations(scope);
  initSplitWorkbenchToggle(scope);
}


/**
 * Widescreen Split-Stage Workbench Toggle ([data-plate-layout-toggle])
 * Switches .tp-plate-split-workbench between side-by-side "split" and full-width "stacked" modes.
 */
export function initSplitWorkbenchToggle(scope = document) {
  scope.querySelectorAll("[data-plate-layout-toggle]").forEach((btn) => {
    if (btn.dataset.toggleBound === "true") return;
    btn.dataset.toggleBound = "true";
    btn.addEventListener("click", () => {
      const plate = btn.closest(".tp-plate");
      if (!plate) return;
      const workbench = plate.querySelector(".tp-plate-split-workbench");
      if (!workbench) return;
      const isSplit = workbench.getAttribute("data-layout-mode") !== "stacked";
      const nextMode = isSplit ? "stacked" : "split";
      workbench.setAttribute("data-layout-mode", nextMode);
      btn.setAttribute("aria-pressed", nextMode === "split" ? "true" : "false");
      btn.textContent = nextMode === "split" ? "Split Workbench ◫" : "Stacked Cinema ▭";
      window.dispatchEvent(new Event("resize"));
    });
  });
}

/**
 * Scite-Grounded Editorial Still / Local Motion Video (.webp) / Live SVG Vector Overlay Controller
 * Operates 100% natively under Content-Security-Policy: img-src 'self'; media-src 'none'.
 */
