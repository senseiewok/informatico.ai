// CC.01 · Cult Classics behaviour: motion pause, parade focus, differential bench, two-clutch gearbox, steering,
// weight drop, bonnet easter egg. DOM attributes and textContent only (the site enforces Trusted Types and forbids
// inline styles), and every effect is optional: with this file blocked the page still reads top to bottom.

const ES = (document.documentElement.lang || "").toLowerCase().startsWith("es");
const L = (en, es) => (ES ? es : en);
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
      if (chip) { chip.classList.add("is-current"); chip.setAttribute("aria-current", "true"); }
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
  const ord = (n) => (ES ? `${n}.ª` : ["", "first", "second", "third", "fourth", "fifth", "sixth"][n]);

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
  const setOpen = (open) => {
    panel.hidden = !open;
    egg.classList.toggle("is-open", open);
    btn.setAttribute("aria-expanded", String(open));
    if (label) label.textContent = open ? btn.dataset.labelClose : btn.dataset.labelOpen;
    if (open && !reduceMotion.matches) panel.scrollIntoView({ block: "nearest", behavior: "smooth" });
  };
  btn.addEventListener("click", () => setOpen(panel.hidden));
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

initPause();
initParade();
initQuarterCar();
initTrack();
initRace();
initDiff();
initDct();
initSteer();
initReveal();
initEgg();
