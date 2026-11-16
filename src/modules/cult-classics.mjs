// CC.01 · Cult Classics behaviour: motion pause, parade focus, differential bench, two-clutch gearbox, steering,
// weight drop, bonnet easter egg, coupled 2D cornering <-> 3D WebGL2 hardware atelier, GLB/DXF CAD export,
// dual-scale 1:20 <-> 1:5 axle loupe, Sankey torque ribbon, 6-axis polar radar, 5-era relay & gallery lightbox.
// DOM attributes and textContent only (strict CSP & Trusted Types safe).
import { encodeCustomGlbBuffer } from "./glb-viewer.mjs";

const isEs = () => (document.documentElement.lang || "").toLowerCase().startsWith("es");
const L = (en, es) => (isEs() ? es : en);
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

function store(key, value) {
  try {
    if (value === undefined) return window.localStorage.getItem(key);
    window.localStorage.setItem(key, value);
  } catch (_e) { /* private mode or blocked storage: the default is fine */ }
  return null;
}

// ---------------------------------------------------------------- motion pause (WCAG 2.2.2)
function initPause() {
  const btn = document.querySelector("[data-cc-pause]");
  if (!btn) return;
  const root = document.documentElement;
  const apply = (paused) => {
    root.classList.toggle("cc-paused", paused);
    btn.setAttribute("aria-pressed", String(paused));
    btn.textContent = paused ? btn.dataset.labelResume : btn.dataset.labelPause;
  };
  apply(store("cc-motion") === "paused");
  btn.addEventListener("click", () => {
    const paused = !root.classList.contains("cc-paused");
    apply(paused);
    store("cc-motion", paused ? "paused" : "running");
  });
  document.addEventListener("visibilitychange", () => {
    if (store("cc-motion") !== "paused") root.classList.toggle("cc-paused", document.hidden);
  });
}

// ---------------------------------------------------------------- parade: the current card's car comes forward
function initParade() {
  const lanes = new Map();
  document.querySelectorAll(".cc-parade .cc-car").forEach((svg) => lanes.set(svg.dataset.gen, svg.parentElement));
  const cards = document.querySelectorAll(".cc-card[data-gen]");
  if (!lanes.size || !cards.length || !("IntersectionObserver" in window)) return;
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      lanes.forEach((lane) => lane.classList.remove("is-current"));
      const lane = lanes.get(e.target.dataset.gen);
      if (lane) lane.classList.add("is-current");
    });
  }, { rootMargin: "-40% 0px -50% 0px" });
  cards.forEach((c) => io.observe(c));
  // Generation rail: mark the chip of the card in view.
  const chips = new Map();
  document.querySelectorAll(".cc-gen-chip").forEach((c) => chips.set(c.dataset.gen, c));
  if (!chips.size) return;
  const railIo = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      chips.forEach((c) => { c.classList.remove("is-current"); c.removeAttribute("aria-current"); });
      const chip = chips.get(e.target.dataset.gen);
      if (chip) { chip.classList.add("is-current"); chip.setAttribute("aria-current", "step"); }
    });
  }, { rootMargin: "-40% 0px -50% 0px" });
  cards.forEach((c) => railIo.observe(c));
}

// ---------------------------------------------------------------- parallax racetrack (decorative, scroll-linked)
function initTrack() {
  const layers = [...document.querySelectorAll(".cc-track .cc-layer")];
  if (!layers.length) return;
  let queued = false;
  const paint = () => {
    queued = false;
    if (reduceMotion.matches || document.documentElement.classList.contains("cc-paused")) return;
    const y = window.scrollY;
    layers.forEach((g) => {
      const depth = Number(g.dataset.depth) || 0;
      g.setAttribute("transform", `translate(0 ${(-((y * depth) % 1000)).toFixed(1)})`);
    });
  };
  window.addEventListener("scroll", () => {
    if (!queued) { queued = true; window.requestAnimationFrame(paint); }
  }, { passive: true });
  paint();
}

// ---------------------------------------------------------------- ghost race: constant average speed per lap time
function initRace() {
  const race = document.querySelector("[data-cc-race]");
  if (!race) return;
  const path = race.querySelector("#cc-loop-path");
  const ghosts = [...race.querySelectorAll(".cc-ghost")];
  const btn = race.querySelector("[data-cc-race-start]");
  const readout = race.querySelector(".cc-readout");
  if (!path || !ghosts.length || typeof path.getTotalLength !== "function") return;
  const total = path.getTotalLength();
  const fastest = Number(race.dataset.fastest);
  const COMPRESS = 100; // 100 real seconds per animated second
  const place = (g, frac) => {
    const p = path.getPointAtLength(total * Math.min(frac, 1));
    const c = g.querySelector("circle");
    const tx = g.querySelector("text");
    c.setAttribute("cx", p.x.toFixed(1));
    c.setAttribute("cy", p.y.toFixed(1));
    tx.setAttribute("x", p.x.toFixed(1));
    tx.setAttribute("y", (p.y + 3.5).toFixed(1));
  };
  // Snapshot when the fastest car crosses the line: every other car is short of it by its gap.
  const snapshot = () => ghosts.forEach((g) => place(g, fastest / Number(g.dataset.secs)));
  const fmt = (s) => {
    const m = Math.floor(s / 60);
    const r = (s - m * 60).toFixed(s % 1 ? 2 : 0).padStart(s % 1 ? 5 : 2, "0");
    return `${m}:${r}`;
  };
  const slowest = Math.max(...ghosts.map((g) => Number(g.dataset.secs)));
  let raf = 0;
  const run = () => {
    window.cancelAnimationFrame(raf);
    if (reduceMotion.matches) {
      snapshot();
      readout.textContent = L(
        `Snapshot as the quickest car crosses the line at ${fmt(fastest)}; the others are short of it by their gap.`,
        `Instantánea cuando el auto más rápido cruza la meta en ${fmt(fastest)}; los demás quedan atrás por su diferencia.`);
      btn.textContent = btn.dataset.labelAgain;
      return;
    }
    const t0 = performance.now();
    readout.textContent = L("Green flag.", "Bandera verde.");
    const tick = (now) => {
      const simSecs = ((now - t0) / 1000) * COMPRESS;
      ghosts.forEach((g) => place(g, simSecs / Number(g.dataset.secs)));
      if (simSecs < slowest) {
        raf = window.requestAnimationFrame(tick);
      } else {
        readout.textContent = L(
          `All eight home. First: ${fmt(fastest)}. Last: ${fmt(slowest)}. Gap: ${Math.round(slowest - fastest)} s.`,
          `Los ocho en la meta. Primero: ${fmt(fastest)}. Último: ${fmt(slowest)}. Diferencia: ${Math.round(slowest - fastest)} s.`);
        btn.textContent = btn.dataset.labelAgain;
      }
    };
    raf = window.requestAnimationFrame(tick);
  };
  btn.addEventListener("click", run);
}

// ---------------------------------------------------------------- differential bench (schematic, illustrative)
function initDiff() {
  const bench = document.querySelector("[data-cc-diff]");
  if (!bench) return;
  const range = bench.querySelector("#cc-throttle");
  const readout = bench.querySelector(".cc-readout");
  const tIn = bench.querySelector(".cc-torque-in");
  const tOut = bench.querySelector(".cc-torque-out");
  const slip = bench.querySelectorAll(".cc-slip path");
  const caliper = bench.querySelector(".cc-caliper");
  const plates = bench.querySelectorAll(".cc-plate-disc");
  // Same model as tools/folios/classics/cc01_mechanics.py (inputs come from the page; MODEL values except the lock).
  const d = bench.dataset;
  const P = { r: +d.r, mu: +d.mu, nin: +d.nin, nout: +d.nout, brake: +d.brake, lock: +d.lock, demand: +d.demand };
  const gIn = P.mu * P.nin * P.r;
  const gOut = P.mu * P.nout * P.r;
  const split = (T, mode) => {
    const half = T / 2;
    let rin, rout, brake = 0;
    if (mode === "open") {
      rin = rout = Math.min(half, gIn);
    } else if (mode === "xds") {
      const side = Math.min(half, gIn + P.brake, gOut);
      brake = Math.max(0, side - gIn);
      rin = side - brake;
      rout = side;
    } else {
      rin = Math.min(half, gIn);
      const transfer = Math.min(Math.max(0, T - 2 * rin), P.lock, gOut - rin);
      rout = rin + Math.max(0, transfer);
    }
    return { rin, rout, brake, road: rin + rout, spinning: half > gIn + 1e-9 };
  };
  const nm = (x) => `${Math.round(x).toLocaleString("en-US")} Nm`;
  const SCALE = 80 / (P.demand / 2); // arrow pixels per newton-metre

  const update = () => {
    const mode = (bench.querySelector("input[name=cc-diff-mode]:checked") || {}).value || "open";
    const th = Number(range.value) / 100;
    const T = th * P.demand;
    const s = split(T, mode);
    const unused = Math.max(0, T - s.road - s.brake);
    const spin = T > 0 ? Math.min(1, unused / (T / 2)) : 0;
    tIn.setAttribute("x2", String(150 - 10 - s.rin * SCALE));
    tOut.setAttribute("x2", String(210 + 10 + s.rout * SCALE));
    slip.forEach((p, i) => p.setAttribute("opacity", String(Math.min(1, spin * (i ? 0.9 : 1.4)))));
    caliper.setAttribute("opacity", String(s.brake > 0 ? 0.35 + 0.65 * (s.brake / P.brake) : 0));
    const squeeze = mode === "lock" ? th : 0;
    plates.forEach((p) => {
      const i = Number(p.dataset.i);
      p.setAttribute("transform", `translate(${(-(i - 2) * 2.2 * squeeze).toFixed(2)} 0)`);
    });

    let msg;
    if (T === 0) {
      msg = L("Throttle closed: both wheels grip.", "Acelerador cerrado: las dos ruedas agarran.");
    } else {
      msg = L(`Demand ${nm(T)} · inside ${nm(s.rin)} · outside ${nm(s.rout)}` + (s.brake ? ` · brake ${nm(s.brake)}` : "") +
              ` · to the road ${nm(s.road)}` + (s.spinning ? " · inside wheel at its grip limit." : "."),
              `Pedido ${nm(T)} · interior ${nm(s.rin)} · exterior ${nm(s.rout)}` + (s.brake ? ` · freno ${nm(s.brake)}` : "") +
              ` · al camino ${nm(s.road)}` + (s.spinning ? " · rueda interior en su límite de agarre." : "."));
    }
    readout.textContent = msg;
    range.setAttribute("aria-valuetext", `${Math.round(th * 100)}%`); // the live readout says the rest
  };
  range.addEventListener("input", update);
  bench.querySelectorAll("input[name=cc-diff-mode]").forEach((r) => r.addEventListener("change", update));
  document.addEventListener("tp-lang-change", update);
  update();
}

// ---------------------------------------------------------------- dual-clutch gearbox
function initDct() {
  const bench = document.querySelector("[data-cc-dct]");
  if (!bench) return;
  const btn = bench.querySelector("[data-cc-shift]");
  const readout = bench.querySelector(".cc-readout");
  const gears = bench.querySelectorAll(".cc-gear");
  const odd = { shaft: bench.querySelector(".cc-shaft-odd"), clutch: bench.querySelector(".cc-clutch-odd") };
  const even = { shaft: bench.querySelector(".cc-shaft-even"), clutch: bench.querySelector(".cc-clutch-even") };
  let gear = 1;
  const ord = (n) => (isEs() ? `${n}.ª` : ["", "first", "second", "third", "fourth", "fifth", "sixth"][n]);

  const render = () => {
    const live = gear % 2 ? odd : even;
    const idle = gear % 2 ? even : odd;
    live.shaft.classList.add("is-live");
    idle.shaft.classList.remove("is-live");
    live.clutch.classList.remove("is-open");
    idle.clutch.classList.add("is-open");
    gears.forEach((g) => {
      const n = Number(g.dataset.gear);
      g.classList.toggle("is-live", n === gear);
      g.classList.toggle("is-next", n === gear + 1);
    });
    const clutchNo = gear % 2 ? 1 : 2;
    if (gear < 6) {
      readout.textContent = L(
        `${ord(gear)[0].toUpperCase()}${ord(gear).slice(1)} gear on clutch ${clutchNo}. ${ord(gear + 1)[0].toUpperCase()}${ord(gear + 1).slice(1)} is already selected on the other shaft; the shift is one clutch opening as the other closes.`,
        `${ord(gear)} velocidad en el embrague ${clutchNo}. La ${ord(gear + 1)} ya está seleccionada en la otra flecha; el cambio es un embrague que abre mientras el otro cierra.`
      );
      btn.textContent = L("Shift up", "Subir velocidad");
    } else {
      readout.textContent = L("Sixth gear on clutch 2. Nothing left to pre-select.",
                              "6.ª velocidad en el embrague 2. Ya no queda nada que preseleccionar.");
      btn.textContent = L("Back to first", "Volver a primera");
    }
  };
  btn.addEventListener("click", () => {
    gear = gear >= 6 ? 1 : gear + 1;
    render();
  });
  document.addEventListener("tp-lang-change", render);
  render();
}

// ---------------------------------------------------------------- steering: progressive vs standard rack
function initSteer() {
  const range = document.getElementById("cc-steer-range");
  if (!range) return;
  const prog = document.querySelector(".cc-steer-prog");
  const std = document.querySelector(".cc-steer-std");
  const update = () => {
    const f = Number(range.value) / 100;
    const a = Math.round(f * 380);
    const b = Math.round(f * 500);
    prog.setAttribute("transform", `rotate(${-a} 80 60)`);
    std.setAttribute("transform", `rotate(${-b} 240 60)`);
    range.setAttribute("aria-valuetext", f === 0 ? L("Centred", "Centrado")
      : L(`${Math.round(f * 100)}%: GTI ${a}°, lesser Golf ${b}°`, `${Math.round(f * 100)} %: GTI ${a}°, Golf menos potente ${b}°`));
  };
  range.addEventListener("input", update);
  document.addEventListener("tp-lang-change", update);
  update();
}

// ---------------------------------------------------------------- weights drop when seen (static if reduced motion)
function initReveal() {
  const els = document.querySelectorAll("[data-cc-reveal]");
  if (!els.length) return;
  if (reduceMotion.matches || !("IntersectionObserver" in window)) {
    els.forEach((el) => el.classList.add("is-visible"));
    return;
  }
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add("is-visible");
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.4 });
  els.forEach((el) => io.observe(el));
}

// ---------------------------------------------------------------- the bonnet
function initEgg() {
  const btn = document.querySelector(".cc-egg-btn");
  const panel = document.getElementById("cc-egg-panel");
  if (!btn || !panel) return;
  const egg = btn.closest(".cc-egg");
  const label = btn.querySelector(".cc-egg-label");
  const initialEs = isEs();
  const labelFor = (open) => {
    if (isEs() === initialEs) return open ? btn.dataset.labelClose : btn.dataset.labelOpen;
    return open ? L("Close the bonnet", "Cerrar el cofre") : L("Lift the bonnet", "Levantar el cofre");
  };
  const setOpen = (open) => {
    panel.hidden = !open;
    egg.classList.toggle("is-open", open);
    btn.setAttribute("aria-expanded", String(open));
    if (label) label.textContent = labelFor(open);
    if (open && !reduceMotion.matches) panel.scrollIntoView({ block: "nearest", behavior: "smooth" });
  };
  btn.addEventListener("click", () => setOpen(panel.hidden));
  document.addEventListener("tp-lang-change", () => {
    if (label) label.textContent = labelFor(!panel.hidden);
  });
  document.addEventListener("keydown", (e) => {
    // Leave Escape to an open dialog (e.g. Contents) and to focus elsewhere on the page.
    if (e.defaultPrevented || document.querySelector("dialog[open]")) return;
    if (!btn.closest(".cc-egg").contains(document.activeElement)) return;
    if (e.key === "Escape" && !panel.hidden) {
      setOpen(false);
      btn.focus();
    }
  });
}

// ---------------------------------------------------------------- quarter car: two natural frequencies
function initQuarterCar() {
  const box = document.querySelector("[data-cc-qc]");
  if (!box) return;
  const range = box.querySelector("#cc-qc-range");
  const ms = +box.dataset.ms, ks = +box.dataset.ks, kt = +box.dataset.kt;
  const muOut = box.querySelector(".cc-qc-mu");
  const bodyOut = box.querySelector(".cc-qc-body-hz");
  const hopOut = box.querySelector(".cc-qc-hop-hz");
  const wheel = box.querySelector(".cc-qc-wheel");
  const hz = (mu) => {
    const a = ms * mu, b = -(ms * (ks + kt) + mu * ks), c = ks * kt;
    const disc = Math.sqrt(b * b - 4 * a * c);
    return [Math.sqrt((-b - disc) / (2 * a)) / (2 * Math.PI), Math.sqrt((-b + disc) / (2 * a)) / (2 * Math.PI)];
  };
  const update = () => {
    const mu = Number(range.value);
    const [fb, fh] = hz(mu);
    muOut.textContent = `${mu} kg`;
    bodyOut.textContent = `${fb.toFixed(2)} Hz`;
    hopOut.textContent = `${fh.toFixed(1)} Hz`;
    wheel.setAttribute("height", String(24 + (mu - 30) * 0.8));
    range.setAttribute("aria-valuetext", `${mu} kg`);
  };
  range.addEventListener("input", update);
  update();
}

// ---------------------------------------------------------------- jump-bar scroll spy
function initJumpSpy() {
  const pills = [...document.querySelectorAll('.tp-essay-jump-pill[href^="#"]')];
  if (!pills.length || !("IntersectionObserver" in window)) return;
  const targets = pills
    .map((p) => ({ pill: p, el: document.getElementById(p.getAttribute("href").slice(1)) }))
    .filter((t) => t.el);
  if (!targets.length) return;
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const id = entry.target.id;
      pills.forEach((p) => p.classList.toggle("is-active", p.getAttribute("href") === `#${id}`));
    });
  }, { rootMargin: "-20% 0px -65% 0px" });
  targets.forEach((t) => io.observe(t.el));
}

// ---------------------------------------------------------------- 5-era engineering relay
function initGenerationsRelay() {
  const root = document.querySelector("[data-cc-relay]");
  if (!root) return;
  const btns = [...root.querySelectorAll("[data-cc-gen-btn]")];
  const segs = [...root.querySelectorAll("[data-cc-seg]")];
  const cards = [...root.querySelectorAll("[data-cc-relay-card]")];
  const activate = (idx) => {
    btns.forEach((b) => b.setAttribute("aria-pressed", String(Number(b.dataset.ccGenBtn) === idx)));
    segs.forEach((s) => s.classList.toggle("is-active", Number(s.dataset.ccSeg) === idx));
    cards.forEach((c) => { c.hidden = Number(c.dataset.ccRelayCard) !== idx; });
  };
  btns.forEach((b) => b.addEventListener("click", () => activate(Number(b.dataset.ccGenBtn))));
  segs.forEach((s) => s.addEventListener("click", () => activate(Number(s.dataset.ccSeg))));
}

// ---------------------------------------------------------------- dual-scale 1:20 <-> 1:5 axle loupe
function initAxleLoupe() {
  const root = document.querySelector("[data-cc-loupe]");
  if (!root) return;
  const btns = [...root.querySelectorAll("[data-cc-node]")];
  const dots = [...root.querySelectorAll("[data-cc-node-dot]")];
  const views = [...root.querySelectorAll("[data-cc-loupe-view]")];
  const cards = [...root.querySelectorAll("[data-cc-node-card]")];
  const select = (idx) => {
    btns.forEach((b) => b.setAttribute("aria-pressed", String(Number(b.dataset.ccNode) === idx)));
    dots.forEach((d) => d.classList.toggle("is-active", Number(d.dataset.ccNodeDot) === idx));
    views.forEach((v) => {
      const match = Number(v.dataset.ccLoupeView) === idx;
      v.classList.toggle("is-active", match);
      if (match) v.removeAttribute("hidden"); else v.setAttribute("hidden", "");
    });
    cards.forEach((c) => { c.hidden = Number(c.dataset.ccNodeCard) !== idx; });
  };
  btns.forEach((b) => b.addEventListener("click", () => select(Number(b.dataset.ccNode))));
  dots.forEach((d) => d.addEventListener("click", () => select(Number(d.dataset.ccNodeDot))));
}

// ---------------------------------------------------------------- alluvial torque Sankey ribbon
function initSankeyRibbon() {
  const root = document.querySelector("[data-cc-sankey]");
  if (!root) return;
  const btns = [...root.querySelectorAll("[data-cc-flow]")];
  const modes = [...root.querySelectorAll("[data-cc-sankey-mode]")];
  const readout = root.querySelector("[data-cc-sankey-readout]");
  let current = "lock";
  const paintReadout = () => {
    if (!readout) return;
    const key = `${current}${isEs() ? "Es" : "En"}`;
    if (readout.dataset[key]) readout.textContent = readout.dataset[key];
  };
  const select = (kind) => {
    current = kind;
    btns.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.ccFlow === kind)));
    modes.forEach((m) => {
      const match = m.dataset.ccSankeyMode === kind;
      m.classList.toggle("is-active", match);
      if (match) m.removeAttribute("hidden"); else m.setAttribute("hidden", "");
    });
    paintReadout();
  };
  btns.forEach((b) => b.addEventListener("click", () => select(b.dataset.ccFlow)));
  document.addEventListener("tp-lang-change", paintReadout);
}

// ---------------------------------------------------------------- 6-axis polar envelope radar
function initPolarRadar() {
  const root = document.querySelector("[data-cc-radar]");
  if (!root) return;
  const btns = [...root.querySelectorAll("[data-cc-radar-era]")];
  const poly = root.querySelector(".cc-radar-poly");
  const readout = root.querySelector("[data-cc-radar-readout]");
  if (!poly || !btns.length) return;
  const cx = 240, cy = 160, rMax = 94;
  const angles = Array.from({ length: 6 }, (_, i) => -Math.PI / 2 + i * (Math.PI / 3));
  let activeBtn = btns.find((b) => b.getAttribute("aria-pressed") === "true") || btns[btns.length - 1];
  const apply = (btn) => {
    activeBtn = btn;
    btns.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
    const scores = (btn.dataset.scores || "").split(",").map(Number);
    if (scores.length === 6) {
      const pts = scores.map((s, i) => `${(cx + rMax * (s / 100) * Math.cos(angles[i])).toFixed(1)},${(cy + rMax * (s / 100) * Math.sin(angles[i])).toFixed(1)}`).join(" ");
      poly.setAttribute("points", pts);
    }
    if (readout) readout.textContent = isEs() ? (btn.dataset.noteEs || "") : (btn.dataset.noteEn || "");
  };
  btns.forEach((b) => b.addEventListener("click", () => apply(b)));
  document.addEventListener("tp-lang-change", () => apply(activeBtn));
}

// ---------------------------------------------------------------- 6-station literature lineage explorer
function initLineageExplorer() {
  const root = document.querySelector("[data-cc-lineage]");
  if (!root) return;
  const btns = [...root.querySelectorAll("[data-cc-lineage-btn]")];
  const nodes = [...root.querySelectorAll("[data-cc-lineage-node]")];
  const cards = [...root.querySelectorAll("[data-cc-lineage-card]")];
  const select = (idx) => {
    btns.forEach((b) => b.setAttribute("aria-pressed", String(Number(b.dataset.ccLineageBtn) === idx)));
    nodes.forEach((n) => n.classList.toggle("is-active", Number(n.dataset.ccLineageNode) === idx));
    cards.forEach((c) => { c.hidden = Number(c.dataset.ccLineageCard) !== idx; });
  };
  btns.forEach((b) => b.addEventListener("click", () => select(Number(b.dataset.ccLineageBtn))));
  nodes.forEach((n) => n.addEventListener("click", () => select(Number(n.dataset.ccLineageNode))));
}

// ---------------------------------------------------------------- procedural 3D hardware mesh + WebGL2 + GLB/DXF export
function orientOutwardTriangles(pos, idx, nrm, vStart, vEnd, iStart, iEnd) {
  let cx = 0, cy = 0, cz = 0;
  const count = Math.max(1, vEnd - vStart);
  for (let v = vStart; v < vEnd; v += 1) {
    cx += pos[v * 3]; cy += pos[v * 3 + 1]; cz += pos[v * 3 + 2];
  }
  cx /= count; cy /= count; cz /= count;
  let vol6 = 0;
  for (let t = iStart; t < iEnd; t += 3) {
    const ia = idx[t] * 3, ib = idx[t + 1] * 3, ic = idx[t + 2] * 3;
    const ax = pos[ia] - cx, ay = pos[ia + 1] - cy, az = pos[ia + 2] - cz;
    const bx = pos[ib] - cx, by = pos[ib + 1] - cy, bz = pos[ib + 2] - cz;
    const dx = pos[ic] - cx, dy = pos[ic + 1] - cy, dz = pos[ic + 2] - cz;
    vol6 += ax * (by * dz - bz * dy) + ay * (bz * dx - bx * dz) + az * (bx * dy - by * dx);
  }
  if (vol6 < 0) {
    for (let t = iStart; t < iEnd; t += 3) {
      const tmp = idx[t + 1]; idx[t + 1] = idx[t + 2]; idx[t + 2] = tmp;
    }
    for (let v = vStart; v < vEnd; v += 1) {
      nrm[v * 3] = -nrm[v * 3]; nrm[v * 3 + 1] = -nrm[v * 3 + 1]; nrm[v * 3 + 2] = -nrm[v * 3 + 2];
    }
  }
}

export function buildHardwareMesh(kind = "vaq", params = {}) {
  const ay = Number(params.ay ?? 0.7);
  const strat = params.strat || "lock";
  const lockFrac = Number(params.lockFrac ?? 0.65);
  const pos = [], nrm = [], col = [], idx = [], lines = [];

  const pushV = (x, y, z, nx, ny, nz, c) => {
    const vi = pos.length / 3;
    pos.push(x, y, z);
    nrm.push(nx, ny, nz);
    col.push(c[0], c[1], c[2]);
    return vi;
  };
  const pushBox = (cx, cy, cz, sx, sy, sz, c, tiltZ = 0) => {
    const vStart = pos.length / 3, iStart = idx.length;
    const hx = sx * 0.5, hy = sy * 0.5, hz = sz * 0.5;
    const cs = Math.cos(tiltZ), sn = Math.sin(tiltZ);
    const xf = (lx, ly, lz) => [cx + lx * cs - ly * sn, cy + lx * sn + ly * cs, cz + lz];
    const nf = (nx, ny, nz) => [nx * cs - ny * sn, nx * sn + ny * cs, nz];
    const faces = [
      [[hx, -hy, -hz], [hx, hy, -hz], [hx, hy, hz], [hx, -hy, hz], [1, 0, 0]],
      [[-hx, -hy, hz], [-hx, hy, hz], [-hx, hy, -hz], [-hx, -hy, -hz], [-1, 0, 0]],
      [[-hx, hy, -hz], [-hx, hy, hz], [hx, hy, hz], [hx, hy, -hz], [0, 1, 0]],
      [[-hx, -hy, hz], [-hx, -hy, -hz], [hx, -hy, -hz], [hx, -hy, hz], [0, -1, 0]],
      [[-hx, -hy, hz], [hx, -hy, hz], [hx, hy, hz], [-hx, hy, hz], [0, 0, 1]],
      [[hx, -hy, -hz], [-hx, -hy, -hz], [-hx, hy, -hz], [hx, hy, -hz], [0, 0, -1]],
    ];
    for (const [p0, p1, p2, p3, n] of faces) {
      const [nx, ny, nz] = nf(n[0], n[1], n[2]);
      const v0 = pushV(...xf(...p0), nx, ny, nz, c);
      const v1 = pushV(...xf(...p1), nx, ny, nz, c);
      const v2 = pushV(...xf(...p2), nx, ny, nz, c);
      const v3 = pushV(...xf(...p3), nx, ny, nz, c);
      idx.push(v0, v1, v2, v0, v2, v3);
    }
    orientOutwardTriangles(pos, idx, nrm, vStart, pos.length / 3, iStart, idx.length);
  };
  const pushCyl = (ax, ay0, az, bx, by0, bz, radius, segs, c) => {
    const vStart = pos.length / 3, iStart = idx.length;
    const dx = bx - ax, dy = by0 - ay0, dz = bz - az;
    const len = Math.hypot(dx, dy, dz) || 1;
    const ux = dx / len, uy = dy / len, uz = dz / len;
    const ref = Math.abs(ux) < 0.8 ? [1, 0, 0] : [0, 1, 0];
    let rx = uy * ref[2] - uz * ref[1], ry = uz * ref[0] - ux * ref[2], rz = ux * ref[1] - uy * ref[0];
    const rl = Math.hypot(rx, ry, rz) || 1;
    rx /= rl; ry /= rl; rz /= rl;
    const tx = uy * rz - uz * ry, ty = uz * rx - ux * rz, tz = ux * ry - uy * rx;
    const ringA = [], ringB = [];
    for (let i = 0; i < segs; i += 1) {
      const th = (i / segs) * Math.PI * 2;
      const ct = Math.cos(th), st = Math.sin(th);
      const nx = ct * rx + st * tx, ny = ct * ry + st * ty, nz = ct * rz + st * tz;
      ringA.push(pushV(ax + radius * nx, ay0 + radius * ny, az + radius * nz, nx, ny, nz, c));
      ringB.push(pushV(bx + radius * nx, by0 + radius * ny, bz + radius * nz, nx, ny, nz, c));
    }
    const ca = pushV(ax, ay0, az, -ux, -uy, -uz, c);
    const cb = pushV(bx, by0, bz, ux, uy, uz, c);
    for (let i = 0; i < segs; i += 1) {
      const ni = (i + 1) % segs;
      idx.push(ringA[i], ringA[ni], ringB[ni], ringA[i], ringB[ni], ringB[i]);
      idx.push(ca, ringA[ni], ringA[i], cb, ringB[i], ringB[ni]);
    }
    orientOutwardTriangles(pos, idx, nrm, vStart, pos.length / 3, iStart, idx.length);
  };
  const pushLine = (x1, y1, z1, x2, y2, z2) => lines.push(x1, y1, z1, x2, y2, z2);

  const cSteel = [0.58, 0.62, 0.68];
  const cAlloy = [0.76, 0.78, 0.80];
  const cBlue = [0.16, 0.34, 0.56];
  const cRed = [0.72, 0.21, 0.14];
  const cBrass = [0.76, 0.58, 0.24];

  if (kind === "strut") {
    const roll = ay * 0.14;
    pushCyl(-0.22, -0.58, 0, 0.14, 0.68, 0, 0.085, 18, cBlue);
    pushCyl(0.14, 0.58, 0, 0.14, 0.74, 0, 0.20, 20, cSteel);
    for (let t = 0; t < 6; t += 1) {
      const y = -0.14 + t * 0.12;
      const cx = -0.02 + t * 0.026;
      pushCyl(cx - 0.14, y, 0, cx + 0.14, y + 0.04, 0.02, 0.032, 10, cBrass);
    }
    pushBox(-0.18, -0.54, 0, 0.62, 0.09, 0.36, cAlloy, -0.06);
    pushCyl(-0.56, -0.44, 0, -0.44, -0.44, 0, 0.38, 28, cSteel);
    pushBox(-0.52, -0.22, 0.24, 0.14, 0.24, 0.20, cRed, roll);
    pushLine(-0.22, -0.62, 0, 0.16, 0.76, 0);
    pushLine(-0.58, -0.78, 0, -0.58, 0.05, 0);
  } else if (kind === "dct") {
    pushCyl(-0.92, 0.10, 0, 0.92, 0.10, 0, 0.065, 18, cRed);
    pushCyl(-0.62, 0.10, 0, 0.42, 0.10, 0, 0.115, 20, cBlue);
    pushCyl(-0.88, 0.10, 0, -0.64, 0.10, 0, 0.28, 24, cSteel);
    const ratios = [0.28, 0.24, 0.20, 0.17, 0.14, 0.12];
    ratios.forEach((rad, i) => {
      const gx = -0.34 + i * 0.18;
      pushCyl(gx - 0.03, 0.10, 0, gx + 0.03, 0.10, 0, rad, 20, i % 2 === 0 ? cRed : cBlue);
      pushCyl(gx - 0.03, -0.34, 0.14, gx + 0.03, -0.34, 0.14, 0.36 - rad, 20, cAlloy);
    });
    pushCyl(-0.46, -0.34, 0.14, 0.86, -0.34, 0.14, 0.075, 18, cSteel);
    pushCyl(0.68, -0.34, -0.48, 0.68, -0.34, 0.48, 0.22, 24, cBrass);
    pushLine(-1.02, 0.10, 0, 1.02, 0.10, 0);
    pushLine(-0.56, -0.34, 0.14, 0.96, -0.34, 0.14);
  } else if (kind === "rear") {
    const hop = 0.08 + ay * 0.14;
    pushBox(0, 0.48, 0, 0.88, 0.24, 0.56, cAlloy, ay * 0.08);
    pushBox(0, -0.38, 0, 0.48, 0.18, 0.42, cBlue, -ay * 0.05);
    pushCyl(-0.56, -0.38, 0, -0.42, -0.38, 0, 0.34, 24, cSteel);
    pushCyl(0.42, -0.38, 0, 0.56, -0.38, 0, 0.34, 24, cSteel);
    for (let c = 0; c < 5; c += 1) {
      const y = -0.18 + c * 0.11;
      pushCyl(-0.24, y, 0.12, -0.08, y + 0.03, 0.12, 0.03, 10, cRed);
      pushCyl(0.08, y, -0.12, 0.24, y + 0.03, -0.12, 0.03, 10, cRed);
    }
    pushBox(0, -0.38, 0.28, 1.04, 0.07, 0.08, cBrass, 0);
    pushLine(-0.72, -0.74, 0, 0.72, -0.74, 0);
    pushLine(0, -0.38, 0, 0, 0.48 + hop, 0);
  } else {
    pushCyl(-0.98, 0, 0, 0.98, 0, 0, 0.075, 18, cSteel);
    pushCyl(-0.28, 0, 0, 0.22, 0, 0, 0.26, 24, cBlue);
    pushCyl(-0.34, 0, 0, -0.26, 0, 0, 0.36, 26, cAlloy);
    const squeeze = strat === "lock" ? (1 - lockFrac * 0.22) : 1;
    for (let p = 0; p < 5; p += 1) {
      const px = 0.28 + p * 0.055 * squeeze;
      pushCyl(px, 0, 0, px + 0.028, 0, 0, 0.21, 20, p % 2 === 0 ? cRed : cBrass);
    }
    pushBox(0.42, -0.26, 0.18, 0.28, 0.18, 0.22, cSteel, 0);
    pushCyl(-0.96, 0, 0, -0.84, 0, 0, 0.32, 24, cSteel);
    pushCyl(0.84, 0, 0, 0.96, 0, 0, 0.32, 24, strat === "lock" ? cRed : cBlue);
    pushLine(-1.12, 0, 0, 1.12, 0, 0);
    pushLine(-0.90, 0.42, 0, 0.90, 0.42 + ay * 0.24, 0);
  }

  return {
    kind,
    vertexCount: pos.length / 3,
    triangleCount: idx.length / 3,
    positions: new Float32Array(pos),
    normals: new Float32Array(nrm),
    colors: new Float32Array(col),
    indices: new Uint32Array(idx),
    rulingLines: new Float32Array(lines),
  };
}

function buildDxfString(mesh, label) {
  const out = [
    "0", "SECTION", "2", "HEADER",
    "9", "$ACADVER", "1", "AC1015",
    "9", "$INSUNITS", "70", "6",
    "0", "ENDSEC", "0", "SECTION", "2", "ENTITIES",
  ];
  const p = mesh.positions, idx = mesh.indices;
  for (let i = 0; i < idx.length; i += 3) {
    const a = idx[i] * 3, b = idx[i + 1] * 3, c = idx[i + 2] * 3;
    out.push(
      "0", "3DFACE", "8", `CC01_${label.toUpperCase()}`,
      "10", p[a].toFixed(4), "20", p[a + 1].toFixed(4), "30", p[a + 2].toFixed(4),
      "11", p[b].toFixed(4), "21", p[b + 1].toFixed(4), "31", p[b + 2].toFixed(4),
      "12", p[c].toFixed(4), "22", p[c + 1].toFixed(4), "32", p[c + 2].toFixed(4),
      "13", p[c].toFixed(4), "23", p[c + 1].toFixed(4), "33", p[c + 2].toFixed(4)
    );
  }
  const rl = mesh.rulingLines;
  for (let i = 0; i + 5 < rl.length; i += 6) {
    out.push(
      "0", "LINE", "8", "CC01_KINEMATICS",
      "10", rl[i].toFixed(4), "20", rl[i + 1].toFixed(4), "30", rl[i + 2].toFixed(4),
      "11", rl[i + 3].toFixed(4), "21", rl[i + 4].toFixed(4), "31", rl[i + 5].toFixed(4)
    );
  }
  out.push("0", "ENDSEC", "0", "EOF", "");
  return out.join("\n");
}

function triggerDownload(blob, filename) {
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
  window.setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function makeMvpMatrix(aspect, yaw, pitch, dist) {
  const f = 1 / Math.tan((42 * Math.PI) / 360), n = 0.1, far = 25;
  const p = [f / aspect, 0, 0, 0, 0, f, 0, 0, 0, 0, (far + n) / (n - far), -1, 0, 0, (2 * far * n) / (n - far), 0];
  const cy = Math.cos(yaw), sy = Math.sin(yaw), cp = Math.cos(pitch), sp = Math.sin(pitch);
  const mv = [
    cy, sy * sp, sy * cp, 0,
    0, cp, -sp, 0,
    -sy, cy * sp, cy * cp, 0,
    0, 0, -dist, 1,
  ];
  const out = new Float32Array(16);
  for (let r = 0; r < 4; r += 1) {
    for (let c = 0; c < 4; c += 1) {
      out[c * 4 + r] = p[r] * mv[c * 4] + p[4 + r] * mv[c * 4 + 1] + p[8 + r] * mv[c * 4 + 2] + p[12 + r] * mv[c * 4 + 3];
    }
  }
  return out;
}

function compileProgram(gl, vsSrc, fsSrc) {
  const make = (type, src) => {
    const sh = gl.createShader(type);
    gl.shaderSource(sh, src);
    gl.compileShader(sh);
    if (!gl.getShaderParameter(sh, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(sh) || "shader error");
    return sh;
  };
  const prog = gl.createProgram();
  gl.attachShader(prog, make(gl.VERTEX_SHADER, vsSrc));
  gl.attachShader(prog, make(gl.FRAGMENT_SHADER, fsSrc));
  gl.linkProgram(prog);
  if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(prog) || "link error");
  return prog;
}

function initCoupledAtelier() {
  const root = document.querySelector("[data-cc-atelier]");
  if (!root) return;
  const ayRange = root.querySelector("#cc-ay-range");
  const ayVal = root.querySelector("#cc-ay-val");
  const demRange = root.querySelector("#cc-demand-range");
  const demVal = root.querySelector("#cc-demand-val");
  const stratBtns = [...root.querySelectorAll("[data-cc-strat]")];
  const hwBtns = [...root.querySelectorAll("[data-cc-hardware]")];
  const cornerReadout = root.querySelector("[data-cc-corner-readout]");
  const rollLine = root.querySelector(".cc-chassis-roll");
  const gripIn = root.querySelector(".cc-grip-in");
  const gripOut = root.querySelector(".cc-grip-out");
  const vecIn = root.querySelector(".cc-vec-in");
  const vecOut = root.querySelector(".cc-vec-out");
  const canvas = root.querySelector("#cc-webgl-canvas");
  const wireChk = root.querySelector("#cc-show-wire");
  const exportBtns = [...root.querySelectorAll("[data-cc-export]")];
  const cadReadout = root.querySelector("[data-cc-cad-readout]");
  if (!ayRange || !demRange || !canvas) return;

  const P = {
    r: +root.dataset.r, mu: +root.dataset.mu, brake: +root.dataset.brake, lock: +root.dataset.lock,
    n0: +root.dataset.n0, tref: +root.dataset.tref, ayref: +root.dataset.ayref, track: +root.dataset.track,
  };
  let strat = "lock";
  let kind = "vaq";
  let yaw = 0.52, pitch = 0.34, dist = 2.65;
  let lastYawKnm = 0.56;
  let currentMesh = buildHardwareMesh(kind, { ay: +ayRange.value, strat });

  let gl = null;
  let progMesh = null, progLine = null;
  let bufPos = null, bufNrm = null, bufCol = null, bufIdx = null, bufWire = null;
  let ctx2d = null;
  let visible = true;

  const VS_MESH = `#version 300 es
  in vec3 aPos; in vec3 aNrm; in vec3 aCol;
  uniform mat4 uMvp;
  out vec3 vNrm; out vec3 vCol;
  void main() { vNrm = aNrm; vCol = aCol; gl_Position = uMvp * vec4(aPos, 1.0); }`;
  const FS_MESH = `#version 300 es
  precision mediump float;
  in vec3 vNrm; in vec3 vCol;
  out vec4 outCol;
  void main() {
    vec3 l = normalize(vec3(0.45, 0.78, 0.52));
    float d = 0.32 + 0.68 * max(dot(normalize(vNrm), l), 0.0);
    outCol = vec4(vCol * d, 1.0);
  }`;
  const VS_LINE = `#version 300 es
  in vec3 aPos;
  uniform mat4 uMvp;
  void main() { gl_Position = uMvp * vec4(aPos, 1.0); }`;
  const FS_LINE = `#version 300 es
  precision mediump float;
  out vec4 outCol;
  void main() { outCol = vec4(0.69, 0.19, 0.12, 1.0); }`;

  const uploadMesh = () => {
    if (!gl || !bufPos) return;
    gl.bindBuffer(gl.ARRAY_BUFFER, bufPos); gl.bufferData(gl.ARRAY_BUFFER, currentMesh.positions, gl.STATIC_DRAW);
    gl.bindBuffer(gl.ARRAY_BUFFER, bufNrm); gl.bufferData(gl.ARRAY_BUFFER, currentMesh.normals, gl.STATIC_DRAW);
    gl.bindBuffer(gl.ARRAY_BUFFER, bufCol); gl.bufferData(gl.ARRAY_BUFFER, currentMesh.colors, gl.STATIC_DRAW);
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, bufIdx); gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, currentMesh.indices, gl.STATIC_DRAW);
    gl.bindBuffer(gl.ARRAY_BUFFER, bufWire); gl.bufferData(gl.ARRAY_BUFFER, currentMesh.rulingLines, gl.STATIC_DRAW);
  };

  const initGl = () => {
    try {
      gl = canvas.getContext("webgl2", { antialias: true, alpha: true });
      if (gl) {
        progMesh = compileProgram(gl, VS_MESH, FS_MESH);
        progLine = compileProgram(gl, VS_LINE, FS_LINE);
        bufPos = gl.createBuffer(); bufNrm = gl.createBuffer(); bufCol = gl.createBuffer();
        bufIdx = gl.createBuffer(); bufWire = gl.createBuffer();
        gl.enable(gl.DEPTH_TEST);
        uploadMesh();
        return;
      }
    } catch (_e) { gl = null; }
    ctx2d = canvas.getContext("2d");
  };
  initGl();

  const drawScene = () => {
    if (!visible) return;
    const w = canvas.width || 640, h = canvas.height || 480;
    const mvp = makeMvpMatrix(w / Math.max(1, h), yaw, pitch, dist);
    if (gl && !gl.isContextLost()) {
      gl.viewport(0, 0, w, h);
      gl.clearColor(0, 0, 0, 0);
      gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
      gl.useProgram(progMesh);
      gl.uniformMatrix4fv(gl.getUniformLocation(progMesh, "uMvp"), false, mvp);
      const aP = gl.getAttribLocation(progMesh, "aPos"), aN = gl.getAttribLocation(progMesh, "aNrm"), aC = gl.getAttribLocation(progMesh, "aCol");
      gl.bindBuffer(gl.ARRAY_BUFFER, bufPos); gl.enableVertexAttribArray(aP); gl.vertexAttribPointer(aP, 3, gl.FLOAT, false, 0, 0);
      gl.bindBuffer(gl.ARRAY_BUFFER, bufNrm); gl.enableVertexAttribArray(aN); gl.vertexAttribPointer(aN, 3, gl.FLOAT, false, 0, 0);
      gl.bindBuffer(gl.ARRAY_BUFFER, bufCol); gl.enableVertexAttribArray(aC); gl.vertexAttribPointer(aC, 3, gl.FLOAT, false, 0, 0);
      gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, bufIdx);
      gl.drawElements(gl.TRIANGLES, currentMesh.indices.length, gl.UNSIGNED_INT, 0);
      if (wireChk && wireChk.checked && currentMesh.rulingLines.length) {
        gl.useProgram(progLine);
        gl.uniformMatrix4fv(gl.getUniformLocation(progLine, "uMvp"), false, mvp);
        const lP = gl.getAttribLocation(progLine, "aPos");
        gl.bindBuffer(gl.ARRAY_BUFFER, bufWire); gl.enableVertexAttribArray(lP); gl.vertexAttribPointer(lP, 3, gl.FLOAT, false, 0, 0);
        gl.drawArrays(gl.LINES, 0, currentMesh.rulingLines.length / 3);
      }
    } else if (ctx2d) {
      ctx2d.clearRect(0, 0, w, h);
      ctx2d.strokeStyle = "#1f4e78";
      ctx2d.lineWidth = 1.5;
      const proj = (x, y, z) => {
        const vx = mvp[0] * x + mvp[4] * y + mvp[8] * z + mvp[12];
        const vy = mvp[1] * x + mvp[5] * y + mvp[9] * z + mvp[13];
        const vw = Math.max(0.2, mvp[3] * x + mvp[7] * y + mvp[11] * z + mvp[15]);
        return [(vx / vw * 0.5 + 0.5) * w, (0.5 - vy / vw * 0.5) * h];
      };
      ctx2d.beginPath();
      const idx = currentMesh.indices, p = currentMesh.positions;
      for (let i = 0; i < idx.length; i += 6) {
        const a = idx[i] * 3, b = idx[i + 1] * 3;
        const [ax, ay1] = proj(p[a], p[a + 1], p[a + 2]), [bx, by1] = proj(p[b], p[b + 1], p[b + 2]);
        ctx2d.moveTo(ax, ay1); ctx2d.lineTo(bx, by1);
      }
      ctx2d.stroke();
    }
  };

  const paintCadReadout = () => {
    if (!cadReadout) return;
    cadReadout.textContent = L(
      `3D ${kind.toUpperCase()} assembly · ${currentMesh.vertexCount} vertices / ${currentMesh.triangleCount} triangles · Yaw M_z = ${lastYawKnm.toFixed(2)} kN·m`,
      `Ensamble 3D ${kind.toUpperCase()} · ${currentMesh.vertexCount} vértices / ${currentMesh.triangleCount} triángulos · Guiñada M_z = ${lastYawKnm.toFixed(2)} kN·m`
    );
  };

  const updateCoupled = () => {
    const ay = +ayRange.value;
    const tReq = +demRange.value;
    if (ayVal) ayVal.textContent = `${ay.toFixed(2)} g`;
    if (demVal) demVal.textContent = `${tReq.toLocaleString("en-US")} Nm`;
    ayRange.setAttribute("aria-valuetext", `${ay.toFixed(2)} g`);
    demRange.setAttribute("aria-valuetext", `${tReq.toLocaleString("en-US")} Nm`);

    const transfer = ay * (P.tref / P.ayref);
    const nIn = Math.max(400, P.n0 - transfer);
    const nOut = P.n0 + transfer;
    const gIn = P.mu * nIn * P.r;
    const gOut = P.mu * nOut * P.r;
    const half = tReq / 2;
    let rin, rout;
    if (strat === "open") {
      rin = rout = Math.min(half, gIn);
    } else if (strat === "xds") {
      const side = Math.min(half, gIn + P.brake, gOut);
      const brk = Math.max(0, side - gIn);
      rin = side - brk; rout = side;
    } else {
      rin = Math.min(half, gIn);
      const tr = Math.min(Math.max(0, tReq - 2 * rin), P.lock, gOut - rin);
      rout = rin + Math.max(0, tr);
    }
    lastYawKnm = (((rout - rin) / P.r) * (P.track / 2)) / 1000;
    const road = rin + rout;

    if (rollLine) {
      const dy = Math.round(ay * 18);
      rollLine.setAttribute("y1", String(92 - dy));
      rollLine.setAttribute("y2", String(92 + dy));
    }
    if (gripIn) gripIn.setAttribute("r", String(Math.max(14, Math.min(70, 54 * Math.sqrt(nIn / P.n0))).toFixed(1)));
    if (gripOut) gripOut.setAttribute("r", String(Math.max(14, Math.min(82, 54 * Math.sqrt(nOut / P.n0))).toFixed(1)));
    if (vecIn) vecIn.setAttribute("y2", (184 - Math.min(88, (rin / 2000) * 84)).toFixed(1));
    if (vecOut) vecOut.setAttribute("y2", (184 - Math.min(98, (rout / 2000) * 84)).toFixed(1));
    if (cornerReadout) {
      cornerReadout.textContent = L(
        `MODEL N_in = ${Math.round(nIn)} N · N_out = ${Math.round(nOut)} N · T_road = ${Math.round(road)} Nm · M_z = ${lastYawKnm.toFixed(2)} kN·m`,
        `MODELO N_in = ${Math.round(nIn)} N · N_out = ${Math.round(nOut)} N · T_road = ${Math.round(road)} Nm · M_z = ${lastYawKnm.toFixed(2)} kN·m`
      );
    }
    currentMesh = buildHardwareMesh(kind, { ay, strat, lockFrac: Math.min(1, tReq / 3000) });
    uploadMesh();
    drawScene();
    paintCadReadout();
  };

  ayRange.addEventListener("input", updateCoupled);
  demRange.addEventListener("input", updateCoupled);
  stratBtns.forEach((b) => b.addEventListener("click", () => {
    strat = b.dataset.ccStrat;
    stratBtns.forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    updateCoupled();
  }));
  hwBtns.forEach((b) => b.addEventListener("click", () => {
    kind = b.dataset.ccHardware;
    hwBtns.forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    updateCoupled();
  }));
  if (wireChk) wireChk.addEventListener("change", drawScene);

  exportBtns.forEach((b) => b.addEventListener("click", () => {
    const fmt = b.dataset.ccExport;
    const ay = +ayRange.value, tReq = +demRange.value;
    if (fmt === "glb") {
      const buf = encodeCustomGlbBuffer(currentMesh, [1, 1, 1], `cc01_${kind}`, ay, tReq);
      triggerDownload(new Blob([buf], { type: "model/gltf-binary" }), `golf-gti-cc01-${kind}.glb`);
    } else if (fmt === "dxf") {
      const dxf = buildDxfString(currentMesh, kind);
      triggerDownload(new Blob([dxf], { type: "application/dxf" }), `golf-gti-cc01-${kind}.dxf`);
    }
  }));

  let dragging = false, px = 0, py = 0;
  canvas.addEventListener("pointerdown", (e) => {
    dragging = true; px = e.clientX; py = e.clientY;
    canvas.setPointerCapture?.(e.pointerId);
  });
  canvas.addEventListener("pointermove", (e) => {
    if (!dragging) return;
    yaw += (e.clientX - px) * 0.01;
    pitch = Math.max(-1.2, Math.min(1.2, pitch + (e.clientY - py) * 0.01));
    px = e.clientX; py = e.clientY;
    drawScene();
  });
  const endDrag = () => { dragging = false; };
  canvas.addEventListener("pointerup", endDrag);
  canvas.addEventListener("pointercancel", endDrag);
  canvas.addEventListener("wheel", (e) => {
    e.preventDefault();
    dist = Math.max(1.4, Math.min(5.2, dist + Math.sign(e.deltaY) * 0.2));
    drawScene();
  }, { passive: false });
  canvas.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") { yaw -= 0.14; e.preventDefault(); }
    else if (e.key === "ArrowRight") { yaw += 0.14; e.preventDefault(); }
    else if (e.key === "ArrowUp") { pitch = Math.max(-1.2, pitch - 0.12); e.preventDefault(); }
    else if (e.key === "ArrowDown") { pitch = Math.min(1.2, pitch + 0.12); e.preventDefault(); }
    else if (e.key === "+" || e.key === "=") { dist = Math.max(1.4, dist - 0.2); e.preventDefault(); }
    else if (e.key === "-") { dist = Math.min(5.2, dist + 0.2); e.preventDefault(); }
    else if (e.key === "r" || e.key === "R") { yaw = 0.52; pitch = 0.34; dist = 2.65; e.preventDefault(); }
    else return;
    drawScene();
  });

  if ("ResizeObserver" in window) {
    new ResizeObserver((entries) => {
      const box = entries[0]?.contentRect;
      if (!box || box.width < 10) return;
      const dpr = Math.min(2, window.devicePixelRatio || 1);
      canvas.width = Math.round(box.width * dpr);
      canvas.height = Math.round(box.height * dpr);
      drawScene();
    }).observe(canvas.parentElement);
  }
  if ("IntersectionObserver" in window) {
    new IntersectionObserver((entries) => {
      visible = entries[0].isIntersecting;
      if (visible) drawScene();
    }).observe(root);
  }
  canvas.addEventListener("webglcontextlost", (e) => { e.preventDefault(); });
  canvas.addEventListener("webglcontextrestored", () => { initGl(); uploadMesh(); drawScene(); });
  document.addEventListener("tp-lang-change", () => { updateCoupled(); });
  updateCoupled();
}

// ---------------------------------------------------------------- consolidated 14-item visual archive & zero-jump lightbox
function initVisualGalleryAndLightbox() {
  const gallery = document.querySelector("[data-cc-gallery]");
  const dlg = document.getElementById("cc-lightbox");
  if (!gallery || !dlg) return;

  const filterBtns = [...gallery.querySelectorAll("[data-cc-filter]")];
  const cards = [...gallery.querySelectorAll(".cc-gallery-grid .cc-media-card")];
  const lbImg = document.getElementById("cc-lightbox-img");
  const lbBadge = document.getElementById("cc-lb-badge");
  const lbCap = document.getElementById("cc-lb-cap");
  const btnPrev = dlg.querySelector("[data-cc-lb-prev]");
  const btnNext = dlg.querySelector("[data-cc-lb-next]");
  const btnClose = dlg.querySelector("[data-cc-lb-close]");

  const items = cards.map((card) => {
    const id = card.dataset.ccMediaId;
    const btn = card.querySelector("[data-cc-open-media]");
    const img = card.querySelector("img");
    return { id, card, btn, img };
  });

  let activeFilter = "all";
  let currentId = items[0]?.id || "";
  let opener = null;

  const visibleItems = () => items.filter((it) => !it.card.hidden);
  const paintSlide = (item) => {
    if (!item || !item.img || !item.btn) return;
    currentId = item.id;
    const d = item.btn.dataset;
    const es = isEs();
    lbImg.src = item.img.getAttribute("src") || "";
    lbImg.alt = es ? (d.altEs || item.img.alt) : (d.altEn || item.img.alt);
    lbImg.width = Number(item.img.getAttribute("width")) || 1280;
    lbImg.height = Number(item.img.getAttribute("height")) || 720;
    if (lbBadge) lbBadge.textContent = es ? (d.badgeEs || "") : (d.badgeEn || "");
    if (lbCap) lbCap.textContent = es ? (d.capEs || "") : (d.capEn || "");
  };

  const openById = (id, trigger) => {
    const found = items.find((it) => it.id === id) || items[0];
    if (!found) return;
    opener = trigger || document.activeElement;
    paintSlide(found);
    if (typeof dlg.showModal === "function" && !dlg.open) dlg.showModal();
    else dlg.setAttribute("open", "");
  };
  const stepSlide = (delta) => {
    const pool = visibleItems();
    const list = pool.length && pool.some((it) => it.id === currentId) ? pool : items;
    const idx = Math.max(0, list.findIndex((it) => it.id === currentId));
    const next = list[(idx + delta + list.length) % list.length];
    paintSlide(next);
  };
  const closeDlg = () => {
    if (typeof dlg.close === "function" && dlg.open) dlg.close();
    else dlg.removeAttribute("open");
  };

  filterBtns.forEach((b) => b.addEventListener("click", () => {
    activeFilter = b.dataset.ccFilter;
    filterBtns.forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    cards.forEach((c) => {
      c.hidden = activeFilter !== "all" && c.dataset.ccMediaKind !== activeFilter;
    });
  }));

  document.querySelectorAll("[data-cc-open-media]").forEach((el) => {
    el.addEventListener("click", () => openById(el.dataset.ccOpenMedia, el));
  });
  document.querySelectorAll("[data-cc-open-media-frame]").forEach((el) => {
    el.addEventListener("click", () => openById(el.dataset.ccOpenMediaFrame, el));
  });

  btnPrev?.addEventListener("click", () => stepSlide(-1));
  btnNext?.addEventListener("click", () => stepSlide(1));
  btnClose?.addEventListener("click", closeDlg);
  dlg.addEventListener("click", (e) => { if (e.target === dlg) closeDlg(); });
  dlg.addEventListener("close", () => {
    if (opener && typeof opener.focus === "function") opener.focus();
  });
  dlg.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") { e.preventDefault(); stepSlide(-1); }
    else if (e.key === "ArrowRight") { e.preventDefault(); stepSlide(1); }
  });
  document.addEventListener("tp-lang-change", () => {
    if (dlg.open) {
      const it = items.find((x) => x.id === currentId);
      if (it) paintSlide(it);
    }
  });
}

initPause();
initParade();
initJumpSpy();
initGenerationsRelay();
initAxleLoupe();
initCoupledAtelier();
initSankeyRibbon();
initPolarRadar();
initLineageExplorer();
initQuarterCar();
initTrack();
initRace();
initDiff();
initDct();
initSteer();
initReveal();
initEgg();
initVisualGalleryAndLightbox();
