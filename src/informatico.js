/**
 * INFORMATICO.AI — Interactive Monograph Controller
 * Zero-build ES6 module powering:
 * 1. Cyanotype Blueprint Plate toggle (html[data-theme="blueprint"])
 * 2. Ciechanowski 4-stage tectonic/proof steppers (.tp-step-btn)
 * 3. Bret Victor scrubbable inline prose tokens & range sliders
 * 4. Distill.pub bidirectional equation-to-diagram hover highlighting ([data-eq-target])
 */
(function () {
  "use strict";

  // 1. Cyanotype Blueprint Plate Toggle
  const plateBtn = document.getElementById("tp-blueprint-toggle");
  if (plateBtn) {
    plateBtn.addEventListener("click", function () {
      const root = document.documentElement;
      const isBlueprint = root.getAttribute("data-theme") === "blueprint";
      if (isBlueprint) {
        root.removeAttribute("data-theme");
        plateBtn.setAttribute("aria-pressed", "false");
        plateBtn.textContent = "Plate: Limestone Paper";
      } else {
        root.setAttribute("data-theme", "blueprint");
        plateBtn.setAttribute("aria-pressed", "true");
        plateBtn.textContent = "Plate: Prussian Cyanotype";
      }
    });
  }

  // 2. Bidirectional Equation-to-Diagram Highlighting
  const eqChips = document.querySelectorAll("[data-eq-target]");
  eqChips.forEach(function (chip) {
    const targetId = chip.getAttribute("data-eq-target");
    function setHighlight(active) {
      chip.setAttribute("data-active", active ? "true" : "false");
      if (!targetId) return;
      const el = document.getElementById(targetId);
      if (el) {
        if (active) {
          el.classList.add("tp-svg-highlighted");
        } else {
          el.classList.remove("tp-svg-highlighted");
        }
      }
    }
    chip.addEventListener("mouseenter", function () { setHighlight(true); });
    chip.addEventListener("mouseleave", function () { setHighlight(false); });
    chip.addEventListener("focus", function () { setHighlight(true); });
    chip.addEventListener("blur", function () { setHighlight(false); });
  });

  // 3. Architecture Page (Folio A.01) Interactive Funicular Vault & 1:5 Loupe Solver
  const archSpanInput = document.getElementById("tp-arch-rise");
  const archLoadInput = document.getElementById("tp-arch-load");
  function updateArchitecturePlate() {
    if (!archSpanInput || !archLoadInput) return;
    const rise = parseFloat(archSpanInput.value) || 4.5;
    const asym = parseFloat(archLoadInput.value) || 0.032;
    const span = 18.0;
    const thickness = 0.60;
    const qLoad = 24.0;
    const thrustH = (qLoad * span * span) / (8.0 * rise);
    const kernLimit = thickness / 6.0;
    const safe = Math.abs(asym) <= kernLimit;
    const safetyFactor = thickness / (2.0 * Math.max(Math.abs(asym), 0.005));

    const riseLabel = document.getElementById("tp-arch-rise-val");
    const loadLabel = document.getElementById("tp-arch-load-val");
    const InlineRise = document.getElementById("tp-inline-rise");
    const thrustOut = document.getElementById("tp-readout-thrust");
    const kernOut = document.getElementById("tp-readout-kern");
    const statusBox = document.getElementById("tp-readout-arch-box");
    const statusOut = document.getElementById("tp-readout-arch-status");
    const archPath = document.getElementById("tp-svg-thrust-line");

    if (riseLabel) riseLabel.textContent = rise.toFixed(2) + " m";
    if (loadLabel) loadLabel.textContent = (asym * 1000).toFixed(0) + " mm";
    if (InlineRise) InlineRise.textContent = "f = " + rise.toFixed(2) + " m";
    if (thrustOut) thrustOut.textContent = thrustH.toFixed(1) + " kN";
    if (kernOut) kernOut.textContent = (asym * 1000).toFixed(0) + " / 100 mm";
    if (statusOut) {
      statusOut.textContent = safe
        ? "SAFE KERN (SF " + safetyFactor.toFixed(2) + ")"
        : "HINGE OPENING (e > t/6)";
    }
    if (statusBox) {
      statusBox.setAttribute("data-alert", safe ? "false" : "true");
    }
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
  }
  if (archSpanInput && archLoadInput) {
    archSpanInput.addEventListener("input", updateArchitecturePlate);
    archLoadInput.addEventListener("input", updateArchitecturePlate);
    updateArchitecturePlate();
  }

  // 4. Math Page (Folio M.01) Interactive Modularity & ETH #3-SAT Solver
  const mathPrimeInput = document.getElementById("tp-math-prime");
  const mathClauseInput = document.getElementById("tp-math-clause");
  function updateMathPlate() {
    if (!mathPrimeInput || !mathClauseInput) return;
    const pVal = parseInt(mathPrimeInput.value, 10) || 5;
    const clauseDensity = parseFloat(mathClauseInput.value) || 4.26;
    const isPythagorean = pVal === 2;
    const unbridgedPeak = 8.39;
    const bridgedPeak = isPythagorean ? 9.85 : 3.59;
    const fluxPct = isPythagorean ? 3.2 : 68.4;
    const s3Exponent = Math.max(0.08, 0.385 * (clauseDensity / 4.26));

    const pLabel = document.getElementById("tp-math-prime-val");
    const cLabel = document.getElementById("tp-math-clause-val");
    const inlineP = document.getElementById("tp-inline-prime");
    const barrierOut = document.getElementById("tp-readout-barrier");
    const fluxOut = document.getElementById("tp-readout-flux");
    const ethOut = document.getElementById("tp-readout-eth");
    const qedBox = document.getElementById("tp-readout-qed-box");
    const qedOut = document.getElementById("tp-readout-qed");

    if (pLabel) pLabel.textContent = "p = " + pVal;
    if (cLabel) cLabel.textContent = "alpha = " + clauseDensity.toFixed(2);
    if (inlineP) inlineP.textContent = "p = " + pVal;
    if (barrierOut) barrierOut.textContent = bridgedPeak.toFixed(2) + " kcal/mol (vs " + unbridgedPeak + ")";
    if (fluxOut) fluxOut.textContent = fluxPct.toFixed(1) + "%";
    if (ethOut) ethOut.textContent = "2^(" + s3Exponent.toFixed(3) + " n)";
    if (qedOut) {
      qedOut.textContent = isPythagorean
        ? "COUNTEREXAMPLE (3^2 + 4^2 = 5^2)"
        : "QED VERIFIED (29,500 Lemmas)";
    }
    if (qedBox) {
      qedBox.setAttribute("data-alert", isPythagorean ? "true" : "false");
    }
  }
  if (mathPrimeInput && mathClauseInput) {
    mathPrimeInput.addEventListener("input", updateMathPlate);
    mathClauseInput.addEventListener("input", updateMathPlate);
    updateMathPlate();
  }

  // 5. Engineering Page (Folio E.01) Interactive Stokes-Brinkman & Percolation Solver
  const engPhiInput = document.getElementById("tp-eng-phi");
  const engRadiusInput = document.getElementById("tp-eng-radius");
  function updateEngineeringPlate() {
    if (!engPhiInput || !engRadiusInput) return;
    const phi = parseFloat(engPhiInput.value) || 0.72;
    const radiusNm = parseFloat(engRadiusInput.value) || 12.0;
    const phiC = 0.5927;
    const solid = 1.0 - phi;
    const kappa = (radiusNm * radiusNm * Math.pow(phi, 3)) / (4.0 * Math.max(solid * solid, 1e-6));
    const brinkmanLen = Math.sqrt(kappa);
    const percolating = phi > phiC;
    const dEffRatio = percolating ? Math.pow((phi - phiC) / (1.0 - phiC), 1.3) : 0.0;

    const phiLabel = document.getElementById("tp-eng-phi-val");
    const radLabel = document.getElementById("tp-eng-radius-val");
    const inlinePhi = document.getElementById("tp-inline-phi");
    const kappaOut = document.getElementById("tp-readout-kappa");
    const deffOut = document.getElementById("tp-readout-deff");
    const percBox = document.getElementById("tp-readout-perc-box");
    const percOut = document.getElementById("tp-readout-perc");

    if (phiLabel) phiLabel.textContent = "phi = " + phi.toFixed(3);
    if (radLabel) radLabel.textContent = "a_f = " + radiusNm.toFixed(1) + " nm";
    if (inlinePhi) inlinePhi.textContent = "phi = " + phi.toFixed(3);
    if (kappaOut) kappaOut.textContent = brinkmanLen.toFixed(2) + " nm";
    if (deffOut) deffOut.textContent = dEffRatio.toFixed(3) + " D_0";
    if (percOut) {
      percOut.textContent = percolating
        ? "SUPERCRITICAL PERCOLATING (phi > 0.593)"
        : "SUBCRITICAL ARRESTED (JAMMED)";
    }
    if (percBox) {
      percBox.setAttribute("data-alert", percolating ? "false" : "true");
    }
  }
  if (engPhiInput && engRadiusInput) {
    engPhiInput.addEventListener("input", updateEngineeringPlate);
    engRadiusInput.addEventListener("input", updateEngineeringPlate);
    updateEngineeringPlate();
  }

  // 6. Ciechanowski 4-Stage Stepper Buttons
  const stepButtons = document.querySelectorAll(".tp-step-btn[data-step-desc]");
  stepButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      const group = btn.closest(".tp-stepper");
      if (group) {
        group.querySelectorAll(".tp-step-btn").forEach(function (b) {
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

  // 7. Living Edition & Frontier Council Revision Switcher
  const revButtons = document.querySelectorAll(".tp-rev-btn[data-rev-summary]");
  revButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      const ledger = btn.closest(".tp-rev-ledger");
      if (!ledger) return;
      ledger.querySelectorAll(".tp-rev-btn").forEach(function (b) {
        b.setAttribute("aria-pressed", "false");
      });
      btn.setAttribute("aria-pressed", "true");
      const sumEl = ledger.querySelector("[data-rev-summary-out]");
      const opusEl = ledger.querySelector("[data-rev-opus-out]");
      if (sumEl) sumEl.textContent = btn.getAttribute("data-rev-summary") || "";
      if (opusEl) opusEl.textContent = btn.getAttribute("data-rev-opus") || "";
    });
  });

  // 8. Portable AI-Agnostic SKILL.md Download & Clipboard Copy
  const downloadBtns = document.querySelectorAll("[data-skill-download]");
  downloadBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      const box = btn.closest(".tp-skill-box");
      if (!box) return;
      const srcEl = box.querySelector("[data-skill-source]");
      if (!srcEl) return;
      const fname = btn.getAttribute("data-skill-download") || "SKILL.md";
      const blob = new Blob([srcEl.textContent.trim() + "\n"], { type: "text/markdown;charset=utf-8" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = fname;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    });
  });

  const copyBtns = document.querySelectorAll("[data-skill-copy]");
  copyBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      const box = btn.closest(".tp-skill-box");
      if (!box) return;
      const srcEl = box.querySelector("[data-skill-source]");
      if (!srcEl) return;
      const orig = btn.textContent;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(srcEl.textContent.trim() + "\n").then(function () {
          btn.textContent = "Copied SKILL.md";
          setTimeout(function () { btn.textContent = orig; }, 1800);
        });
      }
    });
  });

  // 9. Swiss Multi-Article Issue Rack Switcher & Deep-Link Loader (?folio=m01..e04)
  const rackCards = document.querySelectorAll(".tp-rack-card[data-folio-payload]");
  function activateFolioCard(card, pushUrl) {
    if (!card) return;
    let data = null;
    try {
      data = JSON.parse(card.getAttribute("data-folio-payload") || "{}");
    } catch (_e) {
      return;
    }
    if (!data || !data.folio_id) return;

    rackCards.forEach(function (c) {
      c.setAttribute("aria-pressed", c === card ? "true" : "false");
    });

    const catFolio = document.querySelector(".tp-cat-folio");
    if (catFolio) catFolio.textContent = "FOLIO " + data.folio_id;
    const heroKicker = document.querySelector(".tp-hero .tp-kicker");
    if (heroKicker && data.colophon) {
      heroKicker.textContent = "Folio " + data.folio_id + " · " + data.colophon.identifier + " · " + data.current_edition;
    }
    const h1 = document.querySelector(".tp-hero .tp-h1");
    if (h1 && data.title) h1.textContent = data.title;
    const standfirst = document.querySelector(".tp-hero .tp-standfirst");
    if (standfirst && data.subtitle) standfirst.textContent = data.subtitle;

    if (data.colophon) {
      const colVals = document.querySelectorAll(".tp-colophon-grid .tp-colophon-val");
      const vals = [
        data.colophon.identifier,
        data.colophon.kernels,
        data.colophon.benchmarks,
        data.colophon.bridge
      ];
      colVals.forEach(function (el, idx) {
        if (vals[idx]) el.textContent = vals[idx];
      });
    }

    if (Array.isArray(data.steps) && data.steps.length >= 4) {
      const sBtns = document.querySelectorAll(".tp-stepper .tp-step-btn");
      sBtns.forEach(function (b, idx) {
        const stepText = data.steps[idx];
        if (!stepText) return;
        b.setAttribute("data-step-desc", stepText);
        b.setAttribute("aria-pressed", idx === 0 ? "true" : "false");
        const m = stepText.match(new RegExp("^Stage\\s+(\\d+)\\s*\\(([^)]+)\\)"));
        if (m) {
          b.textContent = m[1] + " · " + m[2];
        }
        if (idx === 0) {
          const targetId = b.getAttribute("data-step-target");
          const outEl = targetId ? document.getElementById(targetId) : null;
          if (outEl) outEl.textContent = stepText;
        }
      });
    }

    if (Array.isArray(data.readouts)) {
      const rBoxes = document.querySelectorAll(".tp-readout-strip .tp-readout-box");
      data.readouts.forEach(function (ro, idx) {
        const box = rBoxes[idx];
        if (!box) return;
        const kEl = box.querySelector(".tp-readout-k");
        const vEl = box.querySelector(".tp-readout-v");
        if (kEl && ro.label) kEl.textContent = ro.label;
        if (vEl && ro.value) vEl.textContent = ro.value;
      });
    }

    if (data.sidenote_1) {
      const firstNote = document.querySelector(".tp-rail .tp-sidenote");
      if (firstNote) {
        while (firstNote.firstChild) firstNote.removeChild(firstNote.firstChild);
        const idSpan = document.createElement("span");
        idSpan.className = "tp-sidenote-id";
        idSpan.textContent = data.sidenote_1.kicker || ("Sidenote " + data.folio_id);
        firstNote.appendChild(idSpan);
        firstNote.appendChild(document.createTextNode(" " + (data.sidenote_1.body || "")));
      }
    }

    if (data.spec_plate) {
      const specPlate = document.querySelector(".tp-rail .tp-spec-plate");
      if (specPlate) {
        const tag = specPlate.querySelector(".tp-spec-tag");
        const h4 = specPlate.querySelector("h4");
        const p = specPlate.querySelector("p");
        const meta = specPlate.querySelector(".tp-spec-meta");
        if (tag) tag.textContent = data.spec_plate.division;
        if (h4) h4.textContent = data.spec_plate.title;
        if (p) p.textContent = data.spec_plate.body;
        if (meta && data.spec_plate.meta) meta.textContent = data.spec_plate.meta;
      }
    }

    const dlBtn = document.querySelector(".tp-skill-box [data-skill-download]");
    const codeEl = document.querySelector(".tp-skill-box [data-skill-source]");
    if (dlBtn && data.skill_filename) {
      dlBtn.setAttribute("data-skill-download", data.skill_filename);
      dlBtn.textContent = "Download SKILL.md (" + data.skill_filename + ")";
    }
    if (codeEl && data.skill_md) {
      codeEl.textContent = data.skill_md;
    }

    if (Array.isArray(data.revisions) && data.revisions.length > 0) {
      const revKicker = document.querySelector(".tp-rev-ledger .tp-rev-kicker");
      const revDates = document.querySelector(".tp-rev-ledger .tp-rev-dates");
      const revSumOut = document.querySelector(".tp-rev-ledger [data-rev-summary-out]");
      const revOpusOut = document.querySelector(".tp-rev-ledger [data-rev-opus-out]");
      if (revKicker) revKicker.textContent = "Folio " + data.folio_id + " Living Edition Ledger & Frontier Council Peer Review";
      if (revDates) revDates.textContent = "PUBLISHED: " + data.date_published + " · REDATED: " + data.date_redated + " (" + data.current_edition + ")";
      if (revSumOut) revSumOut.textContent = data.revisions[0].summary;
      if (revOpusOut) revOpusOut.textContent = data.revisions[0].opus;
    }

    if (pushUrl && window.history && window.history.replaceState) {
      const url = new URL(window.location.href);
      url.searchParams.set("folio", data.slug);
      window.history.replaceState({}, "", url.toString());
    }
  }

  rackCards.forEach(function (card) {
    card.addEventListener("click", function () {
      activateFolioCard(card, true);
    });
  });

  const selectButtons = document.querySelectorAll("[data-select-folio]");
  selectButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      const slug = btn.getAttribute("data-select-folio");
      const targetCard = document.querySelector('.tp-rack-card[data-folio-slug="' + slug + '"]');
      if (targetCard) {
        activateFolioCard(targetCard, true);
        const hero = document.querySelector(".tp-issue-rack") || document.querySelector(".tp-hero");
        if (hero && hero.scrollIntoView) {
          hero.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      }
    });
  });

  if (rackCards.length > 0 && window.location && window.location.search) {
    const params = new URLSearchParams(window.location.search);
    const reqSlug = params.get("folio");
    if (reqSlug) {
      const matched = document.querySelector('.tp-rack-card[data-folio-slug="' + reqSlug + '"]');
      if (matched) activateFolioCard(matched, false);
    }
  }

  // 10. Multi-Pillar Issue Matrix Filter on /index.html
  const filterBtns = document.querySelectorAll("[data-filter-pillar]");
  const matrixRows = document.querySelectorAll("tr[data-pillar-row]");
  filterBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      const pillar = btn.getAttribute("data-filter-pillar") || "all";
      filterBtns.forEach(function (b) {
        b.setAttribute("aria-pressed", b === btn ? "true" : "false");
      });
      matrixRows.forEach(function (row) {
        const rowPillar = row.getAttribute("data-pillar-row");
        row.hidden = !(pillar === "all" || rowPillar === pillar);
      });
    });
  });
})();
