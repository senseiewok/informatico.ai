/**
 * @module timegravity-slope
 * Time & Gravity instruments, hand-written, zero dependencies, zero network calls. One shared state object per
 * instrument drives every panel (cartography habit: one map, many views), so no two readouts can disagree.
 *
 *  - [data-tg-instrument="worldline"] (T.00): a marker slides along a worldline; a picture of the question, not a result.
 *  - [data-tg-instrument="slope"]  (T.01): a body released at rest in ds² = −A(z)c²dt² + dz², A = 1 + 2gz/c²,
 *    integrated with RK4 exactly as tools/timegravity_kernel.py does. Only g_tt varies with height; there is no
 *    force term. Knockout flattens A' to zero (nothing falls); the sign flip is the verifier's planted defect.
 *  - [data-tg-instrument="gps"]    (T.02): a light clock whose tick stretches by γ, and the GPS clock budget from
 *    GM, the orbit radius and c (first order, and the Schwarzschild rate ratio). Knockout: leave the satellite clock
 *    uncorrected and the pseudorange error grows by c × Δt per day; the sign flip corrects it the wrong way.
 *  - [data-tg-instrument="poisson"] (T.03): ∇²Φ = 4πGρ solved on a radial grid (Thomas algorithm) for a uniform
 *    sphere, drawn as a clock-rate map; two bodies of different composition released together. Knockout: remove the
 *    source (M → 0). Planted defect: η = 10⁻³, a composition-dependent fall.
 *  - [data-tg-predict]: predict before reveal (pedagogy): the reader commits to an answer, then sees the verdict.
 *
 * Reduced motion: trajectories are drawn at once instead of animated. Keyboard: native range inputs and buttons.
 * The static SVG in the markup is the fallback; this module only redraws its paths and numbers.
 */
const C = 299792458.0;
const G0 = 9.80665;
const T_PROPER = 1.0;
const N_STEPS = 4000; // enough for 1e-9 relative on screen; the Python verifier uses 20,000
const DAY = 86400.0;
const OMEGA_EARTH = 7.2921150e-5;

const STR = {
  en: {
    falls: "Falls at g: the clock-rate gradient alone produces the acceleration. No force term anywhere.",
    flat: "Knockout: every clock ticks at the same rate, the gradient is zero, and nothing falls.",
    flip: "Planted defect: the slope points the wrong way and the body rises. The verifier rejects this run.",
    scaled: "Gradient scaled: the body falls at the scaled acceleration, still with no force term.",
    nowLabel: "now?",
    gpsOk: "Corrected: the satellite clock is pre-set to run slow by the net amount, so from the ground it keeps time with the ground clocks.",
    gpsFlat: "Knockout: the satellite clock is left uncorrected. Its offset grows every day and the pseudorange error with it; nothing can opt out of the one rate.",
    gpsFlip: "Planted defect: the correction is applied with the wrong sign, so the error is twice the uncorrected one. The verifier rejects this sign.",
    poissonOk: "Both bodies read the same map and fall as one: the geodesic equation has no term for what they are made of.",
    poissonFlat: "Knockout: the source is gone, the map is flat (Φ = 0 everywhere), and nothing falls, as on the previous page.",
    poissonFlip: "Planted defect: η = 10⁻³ makes the fall depend on composition and the bodies separate. No experiment has seen this; the verifier rejects it.",
    predictRight: "Your prediction was right.",
    predictWrong: "Your prediction was off.",
    km: "km",
  },
  es: {
    falls: "Cae a g: el gradiente del ritmo de los relojes produce por sí solo la aceleración. Ninguna fuerza en ningún lado.",
    flat: "Apagado: todos los relojes marchan al mismo ritmo, el gradiente es cero y nada cae.",
    flip: "Defecto plantado: la pendiente apunta al revés y el cuerpo sube. El verificador rechaza esta corrida.",
    scaled: "Gradiente escalado: el cuerpo cae con la aceleración escalada, todavía sin término de fuerza.",
    nowLabel: "¿ahora?",
    gpsOk: "Corregido: el reloj satelital se preajusta para atrasar la cantidad neta, así que desde tierra mantiene el tiempo con los relojes en tierra.",
    gpsFlat: "Apagado: el reloj satelital se deja sin corregir. Su desfase crece cada día y con él el error de pseudodistancia; nada puede quedarse fuera del ritmo único.",
    gpsFlip: "Defecto plantado: la corrección se aplica con el signo equivocado, así que el error es el doble del no corregido. El verificador rechaza este signo.",
    poissonOk: "Ambos cuerpos leen el mismo mapa y caen como uno: la ecuación geodésica no tiene término para lo que están hechos.",
    poissonFlat: "Apagado: la fuente desapareció, el mapa es plano (Φ = 0 en todas partes) y nada cae, como en la página anterior.",
    poissonFlip: "Defecto plantado: η = 10⁻³ hace que la caída dependa de la composición y los cuerpos se separan. Ningún experimento ha visto esto; el verificador lo rechaza.",
    predictRight: "Tu predicción fue correcta.",
    predictWrong: "Tu predicción no acertó.",
    km: "km",
  },
};

function lang() {
  return document.documentElement.lang === "es-MX" ? "es" : "en";
}

function reducedMotion() {
  return !!(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
}

function fmt(x, digits) {
  return Number.isFinite(x) ? x.toFixed(digits) : "—";
}

function readouts(root) {
  const reads = {};
  root.querySelectorAll("[data-tg-read]").forEach((el) => { reads[el.getAttribute("data-tg-read")] = el; });
  return reads;
}

function animate(durationMs, step) {
  if (reducedMotion()) { step(1); return 0; }
  const start = performance.now();
  let raf = 0;
  const tick = (now) => {
    const frac = Math.min(1, (now - start) / durationMs);
    step(frac);
    if (frac < 1) raf = requestAnimationFrame(tick);
  };
  raf = requestAnimationFrame(tick);
  return raf;
}

// ------------------------------------------------------------------------------------------------ T.01 kernel
/** RK4 geodesic from rest; returns {aEff, samples:[[tau, t, z], ...]}. Mirrors timegravity_kernel.integrate. */
export function integrate(gradientScale, flip, T = T_PROPER, n = N_STEPS) {
  const Ap = (2.0 * G0 * gradientScale / (C * C)) * (flip ? -1.0 : 1.0);
  let z = 0.0, t = 0.0, dz = 0.0, dt = 1.0;
  const h = T / n;
  const samples = [];
  const acc = (z_, dz_, dt_) => {
    const A = 1.0 + Ap * z_;
    return [-(Ap / 2.0) * (C * dt_) * (C * dt_), -(Ap / A) * dt_ * dz_];
  };
  const every = Math.max(1, Math.floor(n / 80));
  for (let i = 0; i < n; i++) {
    if (i % every === 0) samples.push([i * h, t, z]);
    const [ddz1, ddt1] = acc(z, dz, dt);
    const z2 = z + 0.5 * h * dz, dz2 = dz + 0.5 * h * ddz1, dt2 = dt + 0.5 * h * ddt1;
    const [ddz2, ddt2] = acc(z2, dz2, dt2);
    const z3 = z + 0.5 * h * dz2, dz3 = dz + 0.5 * h * ddz2, dt3 = dt + 0.5 * h * ddt2;
    const [ddz3, ddt3] = acc(z3, dz3, dt3);
    const z4 = z + h * dz3, dz4 = dz + h * ddz3, dt4 = dt + h * ddt3;
    const [ddz4, ddt4] = acc(z4, dz4, dt4);
    z += h * (dz + 2 * dz2 + 2 * dz3 + dz4) / 6;
    dz += h * (ddz1 + 2 * ddz2 + 2 * ddz3 + ddz4) / 6;
    dt += h * (ddt1 + 2 * ddt2 + 2 * ddt3 + ddt4) / 6;
    t += h * (dt + 2 * dt2 + 2 * dt3 + dt4) / 6;
  }
  samples.push([T, t, z]);
  return { aEff: 2.0 * z / (T * T), slopeAp: Ap, samples };
}

// ------------------------------------------------------------------------------------------------ T.02 kernel
/** First-order GPS terms in µs/day. Mirrors timegravity_kernel.gps_terms. */
export function gpsTerms(a, gm, rGround, sign = 1) {
  const grav = sign * (gm / (C * C)) * (1.0 / rGround - 1.0 / a);
  const vel = -(gm / a) / (2.0 * C * C);
  return { grav: grav * DAY * 1e6, vel: vel * DAY * 1e6, net: (grav + vel) * DAY * 1e6 };
}

/** Double entry: the Schwarzschild rate ratio, µs/day. Mirrors timegravity_kernel.gps_schwarzschild_net. */
export function gpsSchwarzschildNet(a, gm, rGround) {
  const sat = Math.sqrt(1.0 - 3.0 * gm / (a * C * C));
  const ground = Math.sqrt(1.0 - 2.0 * gm / (rGround * C * C) - (OMEGA_EARTH * rGround) ** 2 / (C * C));
  return (sat / ground - 1.0) * DAY * 1e6;
}

export function lorentzGamma(beta) {
  return 1.0 / Math.sqrt(1.0 - beta * beta);
}

// ------------------------------------------------------------------------------------------------ T.03 kernel
/** Poisson on a radial grid for a uniform sphere (Thomas algorithm). Mirrors timegravity_kernel.poisson_radial. */
export function poissonRadial(mass, radius, rMax, n, G) {
  const h = rMax / n;
  const rho = mass / ((4 / 3) * Math.PI * radius ** 3);
  const r = Array.from({ length: n + 1 }, (_, i) => i * h);
  const cellDensity = (ri) => {
    const lo = Math.max(0, ri - 0.5 * h), hi = ri + 0.5 * h;
    const insideHi = Math.min(hi, radius);
    if (insideHi <= lo) return 0;
    return rho * (insideHi ** 3 - lo ** 3) / (hi ** 3 - lo ** 3);
  };
  const A = new Float64Array(n + 1), B = new Float64Array(n + 1), Cc = new Float64Array(n + 1), D = new Float64Array(n + 1);
  for (let i = 1; i < n; i++) {
    const rm = (r[i] - 0.5 * h) ** 2, rp = (r[i] + 0.5 * h) ** 2;
    A[i] = rm / (h * h * r[i] * r[i]);
    Cc[i] = rp / (h * h * r[i] * r[i]);
    B[i] = -(A[i] + Cc[i]);
    D[i] = 4 * Math.PI * G * cellDensity(r[i]);
  }
  B[0] = -3 / (h * h); Cc[0] = 3 / (h * h); D[0] = 4 * Math.PI * G * rho;
  B[n] = 1; A[n] = 0; D[n] = -G * mass / rMax;
  const cp = new Float64Array(n + 1), dp = new Float64Array(n + 1);
  cp[0] = Cc[0] / B[0]; dp[0] = D[0] / B[0];
  for (let i = 1; i <= n; i++) {
    const den = B[i] - A[i] * cp[i - 1];
    cp[i] = i < n ? Cc[i] / den : 0;
    dp[i] = (D[i] - A[i] * dp[i - 1]) / den;
  }
  const phi = new Float64Array(n + 1);
  phi[n] = dp[n];
  for (let i = n - 1; i >= 0; i--) phi[i] = dp[i] - cp[i] * phi[i + 1];
  let worst = 0;
  for (let i = 0; i <= n; i++) {
    if (r[i] > 1.05 * radius) worst = Math.max(worst, Math.abs(phi[i] + G * mass / r[i]) / (G * mass / r[i]));
  }
  return { r, phi, worst, phiCenter: phi[0] };
}

// ------------------------------------------------------------------------------------------------ predict
function initPredict(root) {
  const answer = Number(root.getAttribute("data-tg-answer"));
  const verdict = root.querySelector("[data-tg-verdict]");
  const buttons = root.querySelectorAll("[data-tg-option]");
  let chosen = null;
  const render = () => {
    if (chosen === null || !verdict) return;
    const S = STR[lang()];
    const ok = chosen === answer;
    verdict.hidden = false;
    verdict.setAttribute("data-correct", ok ? "true" : "false");
    verdict.textContent = `${ok ? S.predictRight : S.predictWrong} ${verdict.getAttribute(lang() === "es" ? "data-tg-reveal-es" : "data-tg-reveal-en") || ""}`;
  };
  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      chosen = Number(btn.getAttribute("data-tg-option"));
      buttons.forEach((b) => b.setAttribute("aria-pressed", b === btn ? "true" : "false"));
      render();
    });
  });
  window.addEventListener("tp-lang-change", render);
  root.setAttribute("data-tg-ready", "true");
}

// ------------------------------------------------------------------------------------------------ T.01
function initSlope(root) {
  const svg = root.querySelector("svg.tg-stage");
  const path = root.querySelector(".tg-worldline");
  const body = root.querySelector(".tg-body");
  const gradInput = root.querySelector("[data-tg-grad]");
  const knockoutBtn = root.querySelector("[data-tg-knockout]");
  const flipBtn = root.querySelector("[data-tg-flip]");
  const replayBtn = root.querySelector("[data-tg-replay]");
  const status = root.querySelector("[data-tg-status]");
  const reads = readouts(root);
  if (!svg || !path || !body || !gradInput) return;

  // Plot box from the markup so Python (static plate) and JS agree.
  const x0 = Number(svg.getAttribute("data-x0")), x1 = Number(svg.getAttribute("data-x1"));
  const y0 = Number(svg.getAttribute("data-y0")), y1 = Number(svg.getAttribute("data-y1"));
  const zTop = Number(svg.getAttribute("data-ztop")), zBot = Number(svg.getAttribute("data-zbot"));
  const toX = (t) => x0 + (x1 - x0) * Math.min(1, Math.max(0, t / T_PROPER));
  const toY = (z) => y0 + (y1 - y0) * ((zTop - z) / (zTop - zBot));
  const clampZ = (z) => Math.max(zBot, Math.min(zTop, z));

  const state = { knockout: false, flip: false, raf: 0 };
  const rateCol = root.querySelector(".tg-rate-col");

  function render(doAnimate) {
    const scale = state.knockout ? 0 : Number(gradInput.value);
    const { aEff, slopeAp, samples } = integrate(scale, state.flip);
    path.setAttribute("d", samples.map(([, t, z], i) => `${i ? "L" : "M"} ${toX(t).toFixed(2)} ${toY(clampZ(z)).toFixed(2)}`).join(" "));
    const isFlat = state.knockout || scale === 0;
    const st = isFlat ? "flat" : state.flip ? "flip" : "fall";
    path.setAttribute("data-state", st);
    const S = STR[lang()];
    if (status) {
      status.setAttribute("data-state", st);
      status.textContent = isFlat ? S.flat : state.flip ? S.flip : (Math.abs(scale - 1) < 1e-9 ? S.falls : S.scaled);
    }
    if (rateCol) rateCol.style.opacity = isFlat ? "0.15" : String(0.35 + 0.5 * Math.min(1, scale / 2));
    const relErr = scale > 0 ? Math.abs(aEff + G0 * scale) / (G0 * scale) : 0;
    if (reads.grad) reads.grad.textContent = `${fmt(scale, 2)} ×`;
    if (reads.slope) reads.slope.textContent = `${slopeAp.toExponential(3)} 1/m`;
    if (reads.accel) reads.accel.textContent = `${fmt(aEff, 5)} m/s²`;
    if (reads.err) reads.err.textContent = isFlat ? `|a| = ${Math.abs(aEff).toExponential(1)}` : `${relErr.toExponential(2)}`;
    const errBox = root.querySelector('[data-tg-readout-box="err"]');
    if (errBox) errBox.setAttribute("data-alert", state.flip && !isFlat ? "true" : "false");

    cancelAnimationFrame(state.raf);
    const place = (frac) => {
      const idx = Math.min(samples.length - 1, Math.floor(frac * (samples.length - 1)));
      const [, t, z] = samples[idx];
      body.setAttribute("cx", toX(t).toFixed(2));
      body.setAttribute("cy", toY(clampZ(z)).toFixed(2));
    };
    const length = path.getTotalLength ? path.getTotalLength() : 0;
    if (!doAnimate || reducedMotion()) {
      place(1);
      path.style.strokeDasharray = "";
      path.style.strokeDashoffset = "";
      return;
    }
    state.raf = animate(2200, (frac) => {
      if (length) { path.style.strokeDasharray = `${length}`; path.style.strokeDashoffset = `${length * (1 - frac)}`; }
      place(frac);
    });
  }

  gradInput.addEventListener("input", () => render(false));
  gradInput.addEventListener("change", () => render(true));
  if (knockoutBtn) knockoutBtn.addEventListener("click", () => { state.knockout = !state.knockout; knockoutBtn.setAttribute("aria-pressed", String(state.knockout)); render(true); });
  if (flipBtn) flipBtn.addEventListener("click", () => { state.flip = !state.flip; flipBtn.setAttribute("aria-pressed", String(state.flip)); render(true); });
  if (replayBtn) replayBtn.addEventListener("click", () => render(true));
  window.addEventListener("tp-lang-change", () => render(false));
  root.setAttribute("data-tg-ready", "true");
  render(true);
}

// ------------------------------------------------------------------------------------------------ T.00
function initWorldline(root) {
  const path = root.querySelector(".tg-worldline");
  const marker = root.querySelector(".tg-now-marker");
  const label = root.querySelector(".tg-now-label");
  const slider = root.querySelector("[data-tg-now]");
  if (!path || !marker || !slider || !path.getTotalLength) return;
  const total = path.getTotalLength();
  const place = () => {
    const frac = Number(slider.value) / Number(slider.max || 100);
    const pt = path.getPointAtLength(total * frac);
    marker.setAttribute("cx", pt.x.toFixed(2));
    marker.setAttribute("cy", pt.y.toFixed(2));
    if (label) {
      label.setAttribute("x", (pt.x + 12).toFixed(2));
      label.setAttribute("y", (pt.y - 10).toFixed(2));
      label.textContent = STR[lang()].nowLabel;
    }
  };
  slider.addEventListener("input", place);
  window.addEventListener("tp-lang-change", place);
  root.setAttribute("data-tg-ready", "true");
  place();
}

// ------------------------------------------------------------------------------------------------ T.02
function initGps(root) {
  const gm = Number(root.getAttribute("data-tg-gm"));
  const rGround = Number(root.getAttribute("data-tg-rearth"));
  const betaInput = root.querySelector("[data-tg-beta]");
  const orbitInput = root.querySelector("[data-tg-orbit]");
  const knockoutBtn = root.querySelector("[data-tg-knockout]");
  const flipBtn = root.querySelector("[data-tg-flip]");
  const replayBtn = root.querySelector("[data-tg-replay]");
  const status = root.querySelector("[data-tg-status]");
  const zig = root.querySelector(".tg-zigzag");
  const photon = root.querySelector(".tg-photon");
  const orbit = root.querySelector(".tg-orbit");
  const sat = root.querySelector(".tg-satellite");
  const satLabel = root.querySelector(".tg-sat-label");
  const barGrav = root.querySelector(".tg-bar-grav"), barVel = root.querySelector(".tg-bar-vel"), barNet = root.querySelector(".tg-bar-net"), barErr = root.querySelector(".tg-bar-err");
  const reads = readouts(root);
  if (!betaInput || !orbitInput) return;
  const L = 260, barScale = 3.2, errScalePx = 480 / 25; // error bar: 480 px for 25 km
  const orbitPx = (a) => 72 + 150 * (a - rGround) / (42164000 - rGround);
  const state = { knockout: false, flip: false, raf: 0 };

  function render(doAnimate) {
    const beta = Number(betaInput.value);
    const gamma = lorentzGamma(beta);
    const a = Number(orbitInput.value) * 1000;
    const terms = gpsTerms(a, gm, rGround, 1);
    const counter = gpsSchwarzschildNet(a, gm, rGround);
    const half = beta * gamma * L / 2;
    if (zig) zig.setAttribute("d", `M ${(180 - half).toFixed(1)} 350 L 180 90 L ${(180 + half).toFixed(1)} 350`);
    const rpx = orbitPx(a);
    if (orbit) orbit.setAttribute("r", rpx.toFixed(1));
    if (sat) sat.setAttribute("cx", (560 + rpx).toFixed(1));
    if (satLabel) { satLabel.setAttribute("x", (560 + rpx + 12).toFixed(1)); satLabel.textContent = `a = ${Math.round(a / 1000).toLocaleString()} km`; }
    if (barGrav) barGrav.setAttribute("width", Math.max(0, terms.grav * barScale).toFixed(1));
    if (barVel) barVel.setAttribute("width", Math.max(0, Math.abs(terms.vel) * barScale).toFixed(1));
    if (barNet) barNet.setAttribute("width", Math.max(0, terms.net * barScale).toFixed(1));
    if (reads.gravbar) reads.gravbar.textContent = `+${fmt(terms.grav, 1)} (potential)`;
    if (reads.velbar) reads.velbar.textContent = `${fmt(terms.vel, 1)} (speed)`;
    if (reads.netbar) reads.netbar.textContent = `${terms.net >= 0 ? "+" : ""}${fmt(terms.net, 1)} net`;
    if (reads.gravbar) root.querySelectorAll(".tg-bars text").forEach((tx, i) => { if (i > 0) tx.setAttribute("x", String([terms.grav, Math.abs(terms.vel), terms.net][i - 1] * barScale + 6)); });
    const errKm = state.knockout ? Math.abs(C * terms.net * 1e-6) / 1000 : state.flip ? 2 * Math.abs(C * terms.net * 1e-6) / 1000 : 0;
    const st = state.knockout ? "flat" : state.flip ? "flip" : "fall";
    const S = STR[lang()];
    if (status) { status.setAttribute("data-state", st); status.textContent = state.knockout ? S.gpsFlat : state.flip ? S.gpsFlip : S.gpsOk; }
    if (reads.beta) reads.beta.textContent = fmt(beta, 2);
    if (reads.a) reads.a.textContent = Math.round(a / 1000).toLocaleString();
    if (reads.gamma) reads.gamma.textContent = fmt(gamma, 4);
    if (reads.gammalabel) reads.gammalabel.textContent = `tick × γ = ${fmt(gamma, 3)}`;
    if (reads.terms) reads.terms.textContent = `+${fmt(terms.grav, 2)} · ${fmt(terms.vel, 2)}`;
    if (reads.net) reads.net.textContent = `${terms.net >= 0 ? "+" : ""}${fmt(terms.net, 2)} · ${counter >= 0 ? "+" : ""}${fmt(counter, 2)}`;
    if (reads.poserr) reads.poserr.textContent = errKm > 0 ? `${fmt(errKm, 1)} ${S.km}` : `0 ${S.km} (${lang() === "es" ? "corregido" : "corrected"}; ${fmt(Math.abs(C * terms.net * 1e-6) / 1000, 1)} ${S.km} ${lang() === "es" ? "si no" : "if not"})`;
    const errBox = root.querySelector('[data-tg-readout-box="err"]');
    if (errBox) errBox.setAttribute("data-alert", errKm > 0 ? "true" : "false");
    cancelAnimationFrame(state.raf);
    const errTarget = Math.min(480, errKm * errScalePx);
    const photonAt = (frac) => {
      if (!photon) return;
      // Two legs: up to the top mirror, then down. Base positions follow the zigzag.
      const leg = frac < 0.5 ? frac * 2 : (frac - 0.5) * 2;
      const x = frac < 0.5 ? (180 - half) + half * leg : 180 + half * leg;
      const y = frac < 0.5 ? 350 - 260 * leg : 90 + 260 * leg;
      photon.setAttribute("cx", x.toFixed(1)); photon.setAttribute("cy", y.toFixed(1));
    };
    if (!doAnimate || reducedMotion()) {
      if (barErr) { barErr.setAttribute("width", errTarget.toFixed(1)); }
      if (reads.errbar) reads.errbar.textContent = errKm > 0 ? `${fmt(errKm, 1)} ${S.km}` : `0 ${S.km}`;
      photonAt(1);
      return;
    }
    state.raf = animate(1800 * gamma / lorentzGamma(0.6), (frac) => {
      photonAt(frac);
      if (barErr) barErr.setAttribute("width", (errTarget * frac).toFixed(1));
      if (reads.errbar) reads.errbar.textContent = errKm > 0 ? `${fmt(errKm * frac, 1)} ${S.km}` : `0 ${S.km}`;
    });
  }
  betaInput.addEventListener("input", () => render(false));
  betaInput.addEventListener("change", () => render(true));
  orbitInput.addEventListener("input", () => render(false));
  if (knockoutBtn) knockoutBtn.addEventListener("click", () => { state.knockout = !state.knockout; if (state.knockout) { state.flip = false; if (flipBtn) flipBtn.setAttribute("aria-pressed", "false"); } knockoutBtn.setAttribute("aria-pressed", String(state.knockout)); render(true); });
  if (flipBtn) flipBtn.addEventListener("click", () => { state.flip = !state.flip; if (state.flip) { state.knockout = false; if (knockoutBtn) knockoutBtn.setAttribute("aria-pressed", "false"); } flipBtn.setAttribute("aria-pressed", String(state.flip)); render(true); });
  if (replayBtn) replayBtn.addEventListener("click", () => render(true));
  window.addEventListener("tp-lang-change", () => render(false));
  root.setAttribute("data-tg-ready", "true");
  render(true);
}

// ------------------------------------------------------------------------------------------------ T.03
function initPoisson(root) {
  const gm = Number(root.getAttribute("data-tg-gm"));
  const R = Number(root.getAttribute("data-tg-rearth"));
  const G = Number(root.getAttribute("data-tg-gnewton"));
  const massEarth = gm / G;
  const massInput = root.querySelector("[data-tg-mass]");
  const knockoutBtn = root.querySelector("[data-tg-knockout]");
  const flipBtn = root.querySelector("[data-tg-flip]");
  const replayBtn = root.querySelector("[data-tg-replay]");
  const status = root.querySelector("[data-tg-status]");
  const rings = root.querySelectorAll(".tg-ring");
  const massLabel = root.querySelector(".tg-mass-label");
  const massDisc = root.querySelector(".tg-mass");
  const curve = root.querySelector(".tg-phi-curve");
  const bodyA = root.querySelector(".tg-body-a"), bodyB = root.querySelector(".tg-body-b");
  const reads = readouts(root);
  if (!massInput) return;
  const n = 400, rMax = 4 * R;
  const state = { knockout: false, flip: false, raf: 0 };

  function render(doAnimate) {
    const mFactor = state.knockout ? 0 : Number(massInput.value);
    const mass = mFactor * massEarth;
    const eta = state.flip ? 1e-3 : 0;
    const S = STR[lang()];
    let sol = null;
    if (mass > 0) sol = poissonRadial(mass, R, rMax, n, G);
    const gSurf = mass > 0 ? G * mass / (R * R) : 0;
    const phiRef = mass > 0 ? G * mass / R : 1;
    rings.forEach((ring, k) => {
      const rr = 1.0 + 0.4 * (k + 1);
      const i = Math.min(n, Math.round(rr / 4.0 * n));
      const depth = sol ? Math.abs(sol.phi[i]) / Math.abs(sol.phi[Math.round(n / 4)]) : 0;
      ring.style.opacity = sol ? String(0.15 + 0.6 * depth) : "0.03";
      ring.setAttribute("stroke-width", (3 + 6 * depth).toFixed(1));
    });
    if (massLabel) massLabel.textContent = `M = ${fmt(mFactor, 1)} M⊕`;
    if (massDisc) massDisc.style.opacity = mass > 0 ? "1" : "0.15";
    if (curve) {
      if (sol) {
        const pts = [];
        for (let i = 0; i <= n; i += 10) {
          const x = 30 + 420 * (sol.r[i] / rMax);
          const y = 425 - 40 * (Math.abs(sol.phi[i]) / Math.abs(sol.phiCenter));
          pts.push(`${i ? "L" : "M"} ${x.toFixed(1)} ${y.toFixed(1)}`);
        }
        curve.setAttribute("d", pts.join(" "));
      } else {
        curve.setAttribute("d", "M 30 425 L 450 425");
      }
    }
    const a1 = gSurf * (1 + 0.5 * eta), a2 = gSurf * (1 - 0.5 * eta);
    const T = 1.0;
    const sep = Math.abs(0.5 * (a1 - a2) * T * T);
    const st = state.knockout ? "flat" : state.flip ? "flip" : "fall";
    if (status) { status.setAttribute("data-state", st); status.textContent = state.knockout ? S.poissonFlat : state.flip ? S.poissonFlip : S.poissonOk; }
    if (reads.m) reads.m.textContent = fmt(mFactor, 1);
    if (reads.gsurf) reads.gsurf.textContent = `${fmt(gSurf, 3)} m/s²`;
    if (reads.phi0) reads.phi0.textContent = sol ? fmt(sol.phiCenter / phiRef, 4) : "0 (no source)";
    if (reads.griderr) reads.griderr.textContent = sol ? sol.worst.toExponential(1) : "—";
    if (reads.sep) reads.sep.textContent = `${sep.toExponential(1)} m (η = ${eta ? "1e-3" : "0"})`;
    const errBox = root.querySelector('[data-tg-readout-box="err"]');
    if (errBox) errBox.setAttribute("data-alert", state.flip ? "true" : "false");
    cancelAnimationFrame(state.raf);
    // Drawing: the fall spans y 80 -> 400 for the mean body; the separation is exaggerated ×1e4 and capped.
    const fallPx = mass > 0 ? 320 : 0;
    const sepPx = Math.min(60, sep * 1e4);
    const place = (frac) => {
      const yMean = 80 + fallPx * frac * frac;
      if (bodyA) bodyA.setAttribute("cy", Math.min(400 - 9, yMean + sepPx * frac * frac / 2).toFixed(1));
      if (bodyB) bodyB.setAttribute("cy", Math.min(400 - 13, yMean - sepPx * frac * frac / 2).toFixed(1));
    };
    if (!doAnimate || reducedMotion()) { place(1); return; }
    state.raf = animate(1800, place);
  }
  massInput.addEventListener("input", () => render(false));
  massInput.addEventListener("change", () => render(true));
  if (knockoutBtn) knockoutBtn.addEventListener("click", () => { state.knockout = !state.knockout; knockoutBtn.setAttribute("aria-pressed", String(state.knockout)); render(true); });
  if (flipBtn) flipBtn.addEventListener("click", () => { state.flip = !state.flip; flipBtn.setAttribute("aria-pressed", String(state.flip)); render(true); });
  if (replayBtn) replayBtn.addEventListener("click", () => render(true));
  window.addEventListener("tp-lang-change", () => render(false));
  root.setAttribute("data-tg-ready", "true");
  render(true);
}

// ------------------------------------------------------------------------------------------------ T.07
/** Page–Wootters history state on a d-level clock and a qubit; complex numbers as [re, im]. Mirrors timegravity_kernel_quantum. */
export function pwHistory(d, k, planted) {
  const E = [];
  for (let m = -d / 2; m < d / 2; m++) E.push(planted ? (2 * Math.PI * m * Math.abs(m)) / d : (2 * Math.PI * m) / d);
  const eps = (4 * Math.PI * k) / d;
  const eSys = [eps / 2, -eps / 2];
  const inv = 1 / Math.sqrt(d);
  const psi = Array.from({ length: 2 * d }, () => [0, 0]);
  const cexp = (th) => [Math.cos(th), Math.sin(th)];
  const mul = (a, b) => [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]];
  for (let n = 0; n < d; n++) {
    for (let mi = 0; mi < d; mi++) {
      const cClock = cexp(-E[mi] * n);
      for (let s = 0; s < 2; s++) {
        const comp = cexp(-eSys[s] * n);
        const v = mul(cClock, comp);
        psi[mi * 2 + s][0] += inv * inv * v[0] / Math.SQRT2;
        psi[mi * 2 + s][1] += inv * inv * v[1] / Math.SQRT2;
      }
    }
  }
  let norm = 0;
  psi.forEach((z) => { norm += z[0] * z[0] + z[1] * z[1]; });
  norm = Math.sqrt(norm);
  psi.forEach((z) => { z[0] /= norm; z[1] /= norm; });
  let residual = 0;
  for (let i = 0; i < 2 * d; i++) {
    const h = E[Math.floor(i / 2)] + eSys[i % 2];
    residual += (h * psi[i][0]) ** 2 + (h * psi[i][1]) ** 2;
  }
  residual = Math.sqrt(residual);
  const cond = [];
  let maxDev = 0;
  for (let n = 0; n < d; n++) {
    const amp = [[0, 0], [0, 0]];
    for (let mi = 0; mi < d; mi++) {
      const ph = cexp(E[mi] * n);
      for (let s = 0; s < 2; s++) {
        const v = mul(ph, psi[mi * 2 + s]);
        amp[s][0] += inv * v[0]; amp[s][1] += inv * v[1];
      }
    }
    const w = amp[0][0] ** 2 + amp[0][1] ** 2 + amp[1][0] ** 2 + amp[1][1] ** 2;
    const pr = (amp[0][0] + amp[1][0]) / Math.SQRT2, pi = (amp[0][1] + amp[1][1]) / Math.SQRT2;
    const pPlus = w > 1e-18 ? (pr * pr + pi * pi) / w : NaN;
    const closed = Math.cos((eps * n) / 2) ** 2;
    maxDev = Math.max(maxDev, Math.abs(pPlus - closed));
    cond.push({ n, pPlus, closed, w });
  }
  const energySplit = [];
  for (let mi = 0; mi < d; mi++) {
    const a0 = psi[mi * 2], a1 = psi[mi * 2 + 1];
    const w = a0[0] ** 2 + a0[1] ** 2 + a1[0] ** 2 + a1[1] ** 2;
    const pr = (a0[0] + a1[0]) / Math.SQRT2, pi = (a0[1] + a1[1]) / Math.SQRT2;
    energySplit.push({ m: mi - d / 2, pPlus: w > 1e-18 ? (pr * pr + pi * pi) / w : NaN, w });
  }
  return { eps, residual, cond, maxDev, energySplit };
}

function initPw(root) {
  const d = Number(root.getAttribute("data-tg-d")) || 16;
  const k = Number(root.getAttribute("data-tg-k")) || 1;
  const svg = root.querySelector("svg.tg-stage");
  const nInput = root.querySelector("[data-tg-n]");
  const knockoutBtn = root.querySelector("[data-tg-knockout]");
  const flipBtn = root.querySelector("[data-tg-flip]");
  const status = root.querySelector("[data-tg-status]");
  const marker = root.querySelector(".tg-row-marker");
  const dots = root.querySelectorAll(".tg-pw-dot");
  const tiles = root.querySelectorAll(".tg-tile");
  const curve = root.querySelector(".tg-pw-curve");
  const reads = readouts(root);
  if (!svg || !nInput) return;
  const px0 = Number(svg.getAttribute("data-px0")), px1 = Number(svg.getAttribute("data-px1"));
  const py0 = Number(svg.getAttribute("data-py0")), py1 = Number(svg.getAttribute("data-py1"));
  const ty0 = Number(svg.getAttribute("data-ty0")), th = Number(svg.getAttribute("data-th"));
  const toX = (n) => px0 + (px1 - px0) * n / (d - 1);
  const toY = (p) => py1 - (py1 - py0) * p;
  const state = { knockout: false, flip: false };
  const S0 = {
    en: { ok: "Stationary whole, moving part: conditioning on the clock's time states recovers the Schrödinger curve exactly.",
          flat: "Knockout: read in the energy basis, every conditional state is an energy eigenstate. P(+x) = 1/2 for every reading. Same state, different split, no time.",
          flip: "Planted defect: the clock's spectrum no longer matches the constraint, so Ĥ|Ψ⟩⟩ ≠ 0. The whole is not stationary and the verifier rejects it.",
          yes: "yes: cos² motion", no: "none: flat ½", broken: "not stationary" },
    es: { ok: "Todo estacionario, parte en movimiento: condicionar a los estados de tiempo del reloj recupera la curva de Schrödinger exactamente.",
          flat: "Apagado: leído en la base de energía, cada estado condicional es un autoestado de energía. P(+x) = 1/2 para cada lectura. Mismo estado, otra partición, ningún tiempo.",
          flip: "Defecto plantado: el espectro del reloj ya no coincide con la restricción, así que Ĥ|Ψ⟩⟩ ≠ 0. El todo no es estacionario y el verificador lo rechaza.",
          yes: "sí: movimiento cos²", no: "ninguno: ½ plano", broken: "no estacionario" },
  };
  function render() {
    const L = S0[lang()];
    const res = pwHistory(d, k, state.flip);
    const n = Number(nInput.value);
    const series = state.knockout ? res.energySplit.map((e, i) => ({ n: i, pPlus: Number.isFinite(e.pPlus) ? e.pPlus : 0.5 })) : res.cond;
    dots.forEach((dot, i) => {
      const s = series[i];
      dot.setAttribute("cx", toX(i).toFixed(1));
      dot.setAttribute("cy", toY(s.pPlus).toFixed(1));
    });
    if (curve) curve.style.opacity = state.knockout ? "0.25" : "1";
    tiles.forEach((tile) => {
      const tn = Number(tile.getAttribute("data-n")), col = Number(tile.getAttribute("data-col"));
      const p = state.knockout ? 0.5 : res.cond[tn].pPlus;
      tile.style.opacity = String(0.08 + 0.85 * (col === 0 ? p : 1 - p));
    });
    if (marker) marker.setAttribute("y", (ty0 - 2 + n * th).toFixed(1));
    const st = state.flip ? "flip" : state.knockout ? "flat" : "fall";
    if (status) { status.setAttribute("data-state", st); status.textContent = state.flip ? L.flip : state.knockout ? L.flat : L.ok; }
    if (reads.n) reads.n.textContent = String(n);
    if (reads.residual) reads.residual.textContent = res.residual.toExponential(1);
    if (reads.pn) reads.pn.textContent = fmt(state.knockout ? 0.5 : res.cond[n].pPlus, 4);
    if (reads.dev) reads.dev.textContent = state.knockout ? "—" : res.maxDev.toExponential(1);
    if (reads.split) reads.split.textContent = state.flip ? L.broken : state.knockout ? L.no : L.yes;
    const errBox = root.querySelector('[data-tg-readout-box="err"]');
    if (errBox) errBox.setAttribute("data-alert", state.flip ? "true" : "false");
  }
  nInput.addEventListener("input", render);
  if (knockoutBtn) knockoutBtn.addEventListener("click", () => { state.knockout = !state.knockout; knockoutBtn.setAttribute("aria-pressed", String(state.knockout)); render(); });
  if (flipBtn) flipBtn.addEventListener("click", () => { state.flip = !state.flip; flipBtn.setAttribute("aria-pressed", String(state.flip)); render(); });
  window.addEventListener("tp-lang-change", render);
  root.setAttribute("data-tg-ready", "true");
  render();
}

// ------------------------------------------------------------------------------------------------ T.04
export function zychVisibility(dh, T, omega, g) {
  const dtau = (g * dh * T) / (C * C);
  return { dtau, phase: (omega * dtau) / 2, V: Math.abs(Math.cos((omega * dtau) / 2)) };
}

function initZych(root) {
  const g0 = Number(root.getAttribute("data-tg-g")) || G0;
  const svg = root.querySelector("svg.tg-stage");
  const dhInput = root.querySelector("[data-tg-dh]");
  const TInput = root.querySelector("[data-tg-hold]");
  const wInput = root.querySelector("[data-tg-logw]");
  const knockoutBtn = root.querySelector("[data-tg-knockout]");
  const flipBtn = root.querySelector("[data-tg-flip]");
  const status = root.querySelector("[data-tg-status]");
  const curve = root.querySelector(".tg-zych-curve");
  const markerEl = root.querySelector(".tg-zych-marker");
  const dhLine = root.querySelector(".tg-dh-line");
  const armUp = root.querySelector(".tg-arm-up");
  const handUp = root.querySelector(".tg-hand-up"), handDown = root.querySelector(".tg-hand-down");
  const reads = readouts(root);
  if (!svg || !dhInput || !TInput || !wInput) return;
  const px0 = Number(svg.getAttribute("data-px0")), px1 = Number(svg.getAttribute("data-px1"));
  const py0 = Number(svg.getAttribute("data-py0")), py1 = Number(svg.getAttribute("data-py1"));
  const toX = (dh) => px0 + (px1 - px0) * dh / 10;
  const toY = (v) => py1 - (py1 - py0) * v;
  const state = { knockout: false, flip: false };
  const S0 = {
    en: { ok: "A proposal, not a result: the clock's two readings overlap less as Δh·T grows, and the interference fades by exactly that overlap.",
          flat: "Knockout: no gravity, no proper-time difference, no which-path information. V = 1 for every height.",
          flip: "Planted defect: a clock that never ticks carries no which-path information either, V = 1 everywhere. The verifier rejects a clock that cannot reach zero." },
    es: { ok: "Una propuesta, no un resultado: las dos lecturas del reloj se solapan menos conforme crece Δh·T, y la interferencia se desvanece exactamente por ese solape.",
          flat: "Apagado: sin gravedad, sin diferencia de tiempo propio, sin información de camino. V = 1 para toda altura.",
          flip: "Defecto plantado: un reloj que nunca marcha tampoco lleva información de camino, V = 1 en todas partes. El verificador rechaza un reloj que no puede llegar a cero." },
  };
  function render() {
    const L = S0[lang()];
    const dh = Number(dhInput.value), T = Number(TInput.value), logw = Number(wInput.value);
    const omega = state.flip ? 0 : 2 * Math.PI * 10 ** logw;
    const g = state.knockout ? 0 : g0;
    const pts = [];
    for (let i = 0; i <= 200; i++) {
      const x = i / 20;
      pts.push(`${i ? "L" : "M"} ${toX(x).toFixed(1)} ${toY(zychVisibility(x, T, omega, g).V).toFixed(1)}`);
    }
    if (curve) curve.setAttribute("d", pts.join(" "));
    const cur = zychVisibility(dh, T, omega, g);
    if (markerEl) { markerEl.setAttribute("cx", toX(dh).toFixed(1)); markerEl.setAttribute("cy", toY(cur.V).toFixed(1)); }
    const yUp = 300 - 180 * Math.min(1, dh / 10);
    if (armUp) { armUp.setAttribute("y1", yUp.toFixed(1)); armUp.setAttribute("y2", yUp.toFixed(1)); }
    root.querySelectorAll(".tg-clock-face")[0]?.setAttribute("cy", yUp.toFixed(1));
    if (handUp) { handUp.setAttribute("y1", yUp.toFixed(1)); handUp.setAttribute("y2", (yUp - 18).toFixed(1)); }
    if (dhLine) dhLine.setAttribute("y1", yUp.toFixed(1));
    // exaggerated hands: the upper clock leads by the phase, drawn as an angle
    const ang = Math.min(Math.PI, cur.phase * 2);
    if (handUp) { handUp.setAttribute("x2", (200 + 18 * Math.sin(ang)).toFixed(1)); handUp.setAttribute("y2", (yUp - 18 * Math.cos(ang)).toFixed(1)); }
    if (handDown) { handDown.setAttribute("x2", "200"); handDown.setAttribute("y2", "282"); }
    const omegaSr = 2 * Math.PI * 10 ** logw;
    const zero = omegaSr > 0 && g > 0 ? (Math.PI * C * C) / (g * omegaSr) : Infinity;
    const st = state.flip ? "flip" : state.knockout ? "flat" : "fall";
    if (status) { status.setAttribute("data-state", st); status.textContent = state.flip ? L.flip : state.knockout ? L.flat : L.ok; }
    if (reads.dh) reads.dh.textContent = fmt(dh, 1);
    if (reads.T) reads.T.textContent = fmt(T, 1);
    if (reads.logw) reads.logw.textContent = fmt(logw, 2);
    if (reads.dhlabel) reads.dhlabel.textContent = `Δh = ${fmt(dh, 1)} m`;
    if (reads.dtau) reads.dtau.textContent = `${cur.dtau.toExponential(2)} s`;
    if (reads.phase) reads.phase.textContent = `${fmt(cur.phase, 3)} rad`;
    if (reads.V) reads.V.textContent = fmt(cur.V, 4);
    if (reads.zero) reads.zero.textContent = Number.isFinite(zero) ? `${fmt(zero, 1)} m·s` : "—";
    const errBox = root.querySelector('[data-tg-readout-box="err"]');
    if (errBox) errBox.setAttribute("data-alert", state.flip ? "true" : "false");
  }
  [dhInput, TInput, wInput].forEach((el) => el.addEventListener("input", render));
  if (knockoutBtn) knockoutBtn.addEventListener("click", () => { state.knockout = !state.knockout; knockoutBtn.setAttribute("aria-pressed", String(state.knockout)); render(); });
  if (flipBtn) flipBtn.addEventListener("click", () => { state.flip = !state.flip; flipBtn.setAttribute("aria-pressed", String(state.flip)); render(); });
  window.addEventListener("tp-lang-change", render);
  root.setAttribute("data-tg-ready", "true");
  render();
}

// ------------------------------------------------------------------------------------------------ T.06
const HBAR = 1.054571817e-34;
const G_NEWTON_SI = 6.6743e-11;
export function dpInteraction(m, R, d, G) {
  if (d >= 2 * R) return (G * m * m) / d;
  const lam = d / (2 * R);
  return ((G * m * m) / R) * (6 / 5 - 2 * lam ** 2 + 1.5 * lam ** 3 - 0.2 * lam ** 5);
}
export function dpSelfEnergyDifference(m, R, d, G = G_NEWTON_SI) {
  return 2 * (0.6 * G * m * m / R) - dpInteraction(m, R, d, G);
}

function initDp(root) {
  const svg = root.querySelector("svg.tg-stage");
  const lmInput = root.querySelector("[data-tg-logm]"), lrInput = root.querySelector("[data-tg-logr]"), drInput = root.querySelector("[data-tg-dr]");
  const knockoutBtn = root.querySelector("[data-tg-knockout]"), flipBtn = root.querySelector("[data-tg-flip]");
  const status = root.querySelector("[data-tg-status]");
  const curve = root.querySelector(".tg-dp-curve"), marker = root.querySelector(".tg-dp-marker");
  const excl = root.querySelector(".tg-dp-excluded"), allow = root.querySelector(".tg-dp-allowed");
  const reads = readouts(root);
  if (!svg || !lmInput || !lrInput || !drInput) return;
  const px0 = Number(svg.getAttribute("data-px0")), px1 = Number(svg.getAttribute("data-px1"));
  const py0 = Number(svg.getAttribute("data-py0")), py1 = Number(svg.getAttribute("data-py1"));
  const toX = (lm) => px0 + (px1 - px0) * (lm + 20) / 8;
  const toY = (lt) => py1 - (py1 - py0) * (lt + 6) / 18;
  const state = { knockout: false, flip: false };
  const exclFill = excl ? excl.getAttribute("fill") : "", allowFill = allow ? allow.getAttribute("fill") : "";
  const S0 = {
    en: { ok: "The model's prediction on the left; the data's verdict on the right. Below the line the radiation would have been seen; it was not.",
          flat: "Knockout: no gravity, no E_G, no collapse. The model predicts nothing and the curve leaves the chart.",
          flip: "Planted defect: the bound painted on the wrong side would call the parameter-free value allowed. The verifier rejects this orientation.",
          excluded: "excluded", allowed: "allowed", nothing: "no prediction" },
    es: { ok: "La predicción del modelo a la izquierda; el veredicto de los datos a la derecha. Debajo de la línea la radiación se habría visto; no se vio.",
          flat: "Apagado: sin gravedad, sin E_G, sin colapso. El modelo no predice nada y la curva sale de la gráfica.",
          flip: "Defecto plantado: la cota pintada del lado equivocado llamaría permitido al valor sin parámetros. El verificador rechaza esta orientación.",
          excluded: "excluido", allowed: "permitido", nothing: "sin predicción" },
  };
  function render() {
    const L = S0[lang()];
    const G = state.knockout ? 0 : G_NEWTON_SI;
    const lm = Number(lmInput.value), lr = Number(lrInput.value), dr = Number(drInput.value);
    const R = 10 ** lr;
    const pts = [];
    for (let i = 0; i <= 80; i++) {
      const x = -20 + 8 * i / 80;
      const e = dpSelfEnergyDifference(10 ** x, R, dr * R, G);
      const lt = e > 0 ? Math.max(-6, Math.min(12, Math.log10(HBAR / e))) : 12;
      pts.push(`${i ? "L" : "M"} ${toX(x).toFixed(1)} ${toY(lt).toFixed(1)}`);
    }
    if (curve) curve.setAttribute("d", pts.join(" "));
    const e0 = dpSelfEnergyDifference(10 ** lm, R, dr * R, G);
    const tau = e0 > 0 ? HBAR / e0 : Infinity;
    if (marker) { marker.setAttribute("cx", toX(lm).toFixed(1)); marker.setAttribute("cy", toY(Number.isFinite(tau) ? Math.max(-6, Math.min(12, Math.log10(tau))) : 12).toFixed(1)); }
    if (excl && allow) { excl.setAttribute("fill", state.flip ? allowFill : exclFill); allow.setAttribute("fill", state.flip ? exclFill : allowFill); }
    if (reads.sideleft) reads.sideleft.textContent = state.flip ? L.allowed : L.excluded;
    if (reads.sideright) reads.sideright.textContent = state.flip ? L.excluded : L.allowed;
    if (reads.logm) reads.logm.textContent = fmt(lm, 1);
    if (reads.logr) reads.logr.textContent = fmt(lr, 1);
    if (reads.dr) reads.dr.textContent = fmt(dr, 1);
    if (reads.eg) reads.eg.textContent = e0 > 0 ? `${e0.toExponential(2)} J` : "0 J";
    if (reads.tau) reads.tau.textContent = Number.isFinite(tau) ? `${tau.toPrecision(3)} s` : "∞";
    if (reads.verdict) reads.verdict.textContent = state.knockout ? L.nothing : state.flip ? L.allowed : L.excluded;
    const st = state.flip ? "flip" : state.knockout ? "flat" : "fall";
    if (status) { status.setAttribute("data-state", st); status.textContent = state.flip ? L.flip : state.knockout ? L.flat : L.ok; }
    const errBox = root.querySelector('[data-tg-readout-box="err"]');
    if (errBox) errBox.setAttribute("data-alert", state.flip ? "true" : "false");
  }
  [lmInput, lrInput, drInput].forEach((el) => el.addEventListener("input", render));
  if (knockoutBtn) knockoutBtn.addEventListener("click", () => { state.knockout = !state.knockout; knockoutBtn.setAttribute("aria-pressed", String(state.knockout)); render(); });
  if (flipBtn) flipBtn.addEventListener("click", () => { state.flip = !state.flip; flipBtn.setAttribute("aria-pressed", String(state.flip)); render(); });
  window.addEventListener("tp-lang-change", render);
  root.setAttribute("data-tg-ready", "true");
  render();
}

// ------------------------------------------------------------------------------------------------ T.10
/** Page 1993: S(m,n) = Σ_{k=n+1}^{mn} 1/k − (m−1)/(2n), m ≤ n (nats). */
export function pageAverageEntropy(m, n, correction = true) {
  if (m > n) { const t = m; m = n; n = t; }
  let s = 0;
  for (let k = n + 1; k <= m * n; k++) s += 1 / k;
  return s - (correction ? (m - 1) / (2 * n) : 0);
}

function initPage(root) {
  const svg = root.querySelector("svg.tg-stage");
  const nInput = root.querySelector("[data-tg-nq]");
  const knockoutBtn = root.querySelector("[data-tg-knockout]"), flipBtn = root.querySelector("[data-tg-flip]");
  const status = root.querySelector("[data-tg-status]");
  const curve = root.querySelector(".tg-page-curve"), hawk = root.querySelector(".tg-hawking-line");
  const hawkLabel = root.querySelector(".tg-hawking-label"), pageLabel = root.querySelector(".tg-page-label");
  const dots = root.querySelector(".tg-page-dots");
  const reads = readouts(root);
  if (!svg || !nInput) return;
  const px0 = Number(svg.getAttribute("data-px0")), px1 = Number(svg.getAttribute("data-px1"));
  const py0 = Number(svg.getAttribute("data-py0")), py1 = Number(svg.getAttribute("data-py1"));
  const ymax = Number(svg.getAttribute("data-ymax"));
  const toyN = Number(root.getAttribute("data-tg-toyn")) || 10;
  const toX = (a, N) => px0 + (px1 - px0) * a / N;
  const toY = (s) => py1 - (py1 - py0) * Math.min(ymax, s) / ymax;
  const state = { knockout: false, flip: false };
  const S0 = {
    en: { ok: "Counting, not gravity: a random pure state's smaller part is nearly maximally entangled with the larger, so the radiation's entropy follows the smaller side and comes back down.",
          flat: "Knockout: no unitarity. Every emitted qubit is thermal and the entropy climbs Hawking's line to the end; the information is gone. This is the verifier's planted defect.",
          flip: "Naive count: without Page's −(m−1)/2n correction the curve sits exactly at the maximum ln m, overestimating the entropy most at the halfway point.",
          yes: "yes, at N/2", no: "no: Hawking's line", label: "emitted qubits a, of N = " },
    es: { ok: "Conteo, no gravedad: la parte menor de un estado puro aleatorio está casi máximamente entrelazada con la mayor, así que la entropía de la radiación sigue al lado menor y vuelve a bajar.",
          flat: "Apagado: sin unitariedad. Cada qubit emitido es térmico y la entropía sube por la recta de Hawking hasta el final; la información se fue. Este es el defecto plantado del verificador.",
          flip: "Conteo ingenuo: sin la corrección −(m−1)/2n de Page la curva queda exactamente en el máximo ln m, sobreestimando la entropía sobre todo a la mitad.",
          yes: "sí, en N/2", no: "no: recta de Hawking", label: "qubits emitidos a, de N = " },
  };
  function render() {
    const L = S0[lang()];
    const N = Number(nInput.value);
    const pts = [];
    for (let a = 0; a <= N; a++) {
      let s = 0;
      if (a > 0 && a < N) s = state.knockout ? a * Math.LN2 : pageAverageEntropy(2 ** a, 2 ** (N - a), !state.flip);
      if (a === N && state.knockout) s = N * Math.LN2;
      pts.push(`${a ? "L" : "M"} ${toX(a, N).toFixed(1)} ${toY(s).toFixed(1)}`);
    }
    if (curve) curve.setAttribute("d", pts.join(" "));
    if (hawk) hawk.setAttribute("d", `M ${toX(0, N).toFixed(1)} ${toY(0).toFixed(1)} L ${toX(N, N).toFixed(1)} ${toY(N * Math.LN2).toFixed(1)}`);
    if (hawkLabel) { hawkLabel.setAttribute("x", (toX(N, N) - 4).toFixed(1)); hawkLabel.setAttribute("y", (toY(N * Math.LN2) - 8).toFixed(1)); }
    const half = Math.floor(N / 2);
    const peak = pageAverageEntropy(2 ** half, 2 ** (N - half));
    if (pageLabel) { pageLabel.setAttribute("x", toX(N / 2, N).toFixed(1)); pageLabel.setAttribute("y", (toY(state.knockout ? N * Math.LN2 / 2 : peak) - 14).toFixed(1)); pageLabel.style.opacity = state.knockout ? "0.3" : "1"; }
    if (dots) dots.style.opacity = (N === toyN && !state.knockout && !state.flip) ? "1" : "0.15";
    if (reads.N) reads.N.textContent = String(N);
    if (reads.xlabel) reads.xlabel.textContent = `${L.label}${N}`;
    if (reads.peak) reads.peak.textContent = `${fmt(peak, 3)} nats`;
    if (reads.last) reads.last.textContent = `${fmt(state.knockout ? (N - 1) * Math.LN2 : pageAverageEntropy(2, 2 ** (N - 1), !state.flip), 3)} nats`;
    if (reads.turn) reads.turn.textContent = state.knockout ? L.no : L.yes;
    const st = state.knockout ? "flip" : state.flip ? "flat" : "fall";
    if (status) { status.setAttribute("data-state", st); status.textContent = state.knockout ? L.flat : state.flip ? L.flip : L.ok; }
    const errBox = root.querySelector('[data-tg-readout-box="err"]');
    if (errBox) errBox.setAttribute("data-alert", state.knockout ? "true" : "false");
  }
  nInput.addEventListener("input", render);
  if (knockoutBtn) knockoutBtn.addEventListener("click", () => { state.knockout = !state.knockout; knockoutBtn.setAttribute("aria-pressed", String(state.knockout)); render(); });
  if (flipBtn) flipBtn.addEventListener("click", () => { state.flip = !state.flip; flipBtn.setAttribute("aria-pressed", String(state.flip)); render(); });
  window.addEventListener("tp-lang-change", render);
  root.setAttribute("data-tg-ready", "true");
  render();
}

// ------------------------------------------------------------------------------------------------ T.05
/** Four Newtonian branch phases φ_ij = G m² t / (ħ d_ij); mirrors timegravity_kernel_entangle.branch_phases. */
export function bmvPhases(m, d, dx, t, channel = "quantum", planted = false, G = G_NEWTON_SI) {
  const sep = { LL: d, LR: d + dx, RL: d - dx, RR: d };
  const q = {};
  for (const k of Object.keys(sep)) q[k] = (G * m * m * t) / (HBAR * sep[k]);
  if (channel === "quantum" || (channel === "locc" && planted)) return q;
  if (channel === "locc") {
    const alpha = { L: 0.5 * (q.LL + q.LR), R: 0.5 * (q.RL + q.RR) };
    const beta = { L: 0.5 * (q.LL + q.RL), R: 0.5 * (q.LR + q.RR) };
    const out = {};
    for (const i of "LR") for (const j of "LR") out[i + j] = 0.5 * (alpha[i] + beta[j]);
    return out;
  }
  return null; // disputed: no single prediction
}
export function bmvEntanglementPhase(p) { return p.LR + p.RL - p.LL - p.RR; }
export function bmvConcurrence(dphi) { return Math.abs(Math.sin(0.5 * dphi)); }
/** Jacobi eigenvalues of a real symmetric matrix (small n). */
export function jacobiEigenvalues(a, tol = 1e-12, maxSweeps = 60) {
  const n = a.length;
  const m = a.map((row) => row.slice());
  for (let sweep = 0; sweep < maxSweeps; sweep++) {
    let off = 0;
    for (let i = 0; i < n; i++) for (let j = i + 1; j < n; j++) off += m[i][j] * m[i][j];
    if (off < tol * tol) break;
    for (let p = 0; p < n; p++) for (let q = p + 1; q < n; q++) {
      if (Math.abs(m[p][q]) < 1e-300) continue;
      const theta = (m[q][q] - m[p][p]) / (2 * m[p][q]);
      const tt = Math.sign(theta || 1) / (Math.abs(theta) + Math.sqrt(theta * theta + 1));
      const c = 1 / Math.sqrt(tt * tt + 1), s = tt * c;
      for (let k = 0; k < n; k++) {
        const akp = m[k][p], akq = m[k][q];
        m[k][p] = c * akp - s * akq; m[k][q] = s * akp + c * akq;
      }
      for (let k = 0; k < n; k++) {
        const apk = m[p][k], aqk = m[q][k];
        m[p][k] = c * apk - s * aqk; m[q][k] = s * apk + c * aqk;
      }
    }
  }
  return m.map((row, i) => row[i]);
}
/** Peres negativity of the dephased four-branch state: partial transpose, Hermitian 4×4 → real symmetric 8×8. */
export function bmvNegativity(p, gammaT) {
  const B = ["LL", "LR", "RL", "RR"];
  const eta = Math.exp(-gammaT);
  const re = [], im = [];
  for (let r = 0; r < 4; r++) { re.push([0, 0, 0, 0]); im.push([0, 0, 0, 0]); }
  for (let r = 0; r < 4; r++) for (let c = 0; c < 4; c++) {
    const br = B[r], bc = B[c];
    const damp = 0.25 * (br[0] !== bc[0] ? eta : 1) * (br[1] !== bc[1] ? eta : 1);
    const ph = p[br] - p[bc];
    re[r][c] = damp * Math.cos(ph); im[r][c] = damp * Math.sin(ph);
  }
  // partial transpose on B: (i,j),(k,l) <- (i,l),(k,j)
  const ptRe = [], ptIm = [];
  for (let r = 0; r < 4; r++) { ptRe.push([0, 0, 0, 0]); ptIm.push([0, 0, 0, 0]); }
  for (let i = 0; i < 2; i++) for (let j = 0; j < 2; j++) for (let k = 0; k < 2; k++) for (let l = 0; l < 2; l++) {
    ptRe[2 * i + j][2 * k + l] = re[2 * i + l][2 * k + j];
    ptIm[2 * i + j][2 * k + l] = im[2 * i + l][2 * k + j];
  }
  const big = [];
  for (let r = 0; r < 8; r++) big.push(new Array(8).fill(0));
  for (let r = 0; r < 4; r++) for (let c = 0; c < 4; c++) {
    big[r][c] = ptRe[r][c]; big[r + 4][c + 4] = ptRe[r][c]; big[r][c + 4] = -ptIm[r][c]; big[r + 4][c] = ptIm[r][c];
  }
  const vals = jacobiEigenvalues(big).sort((x, y) => x - y);
  let neg = 0;
  for (let k = 0; k < 4; k++) { const v = 0.5 * (vals[2 * k] + vals[2 * k + 1]); if (v < 0) neg -= v; }
  return neg;
}

function initBmv(root) {
  const svg = root.querySelector("svg.tg-stage");
  const lm = root.querySelector("[data-tg-logm]"), dIn = root.querySelector("[data-tg-d]"), dxIn = root.querySelector("[data-tg-dx]");
  const tIn = root.querySelector("[data-tg-t]"), lgIn = root.querySelector("[data-tg-logg]");
  const chanBtns = Array.from(root.querySelectorAll("[data-tg-channel]")), flipBtn = root.querySelector("[data-tg-flip]");
  const status = root.querySelector("[data-tg-status]");
  const qPath = root.querySelector(".tg-bmv-q"), lLine = root.querySelector(".tg-bmv-l"), band = root.querySelector(".tg-bmv-band"), marker = root.querySelector(".tg-bmv-marker");
  const reads = readouts(root);
  if (!svg || !lm || !dIn || !dxIn || !tIn || !lgIn) return;
  const g = (k) => Number(svg.getAttribute("data-" + k));
  const lx0 = g("lx0"), lx1 = g("lx1"), ya = g("ya"), yb = g("yb"), px0 = g("px0"), px1 = g("px1"), py0 = g("py0"), py1 = g("py1"), tmax = g("tmax");
  const toX = (tt) => px0 + (px1 - px0) * tt / tmax, toY = (e) => py1 - (py1 - py0) * Math.max(0, Math.min(1, e));
  const state = { channel: "quantum", flip: false };
  const S0 = {
    en: { quantum: "Quantum mediator: the four phases as written. Weak is not zero; the curve grows with the hold time and reaches 1 at Δφ = π.",
          locc: "Classical LOCC: each mass feels only the mean field of the other. The force is there, the phases take a product form, and the entanglement is exactly zero.",
          disputed: "Disputed classical non-LOCC: the 2025 literature gives two answers, zero and the quantum value. The band is the interval; this page picks neither edge.",
          flip: "Planted defect: a classical LOCC channel carrying the quantum phases. Local operations and classical communication cannot create entanglement; the verifier rejects this channel.",
          entangled: "entangled", separable: "separable (product state)", unsettled: "not settled: between 0 and the quantum value", defect: "entangled by a classical LOCC channel: rejected" },
    es: { quantum: "Mediador cuántico: las cuatro fases tal cual. Débil no es cero; la curva crece con el tiempo de espera y llega a 1 en Δφ = π.",
          locc: "Clásico LOCC: cada masa siente solo el campo medio de la otra. La fuerza está, las fases toman forma de producto, y el entrelazamiento es exactamente cero.",
          disputed: "Clásico no-LOCC en disputa: la literatura de 2025 da dos respuestas, cero y el valor cuántico. La banda es el intervalo; esta página no elige ningún borde.",
          flip: "Defecto plantado: un canal clásico LOCC que lleva las fases cuánticas. Operaciones locales y comunicación clásica no pueden crear entrelazamiento; el verificador rechaza este canal.",
          entangled: "entrelazado", separable: "separable (estado producto)", unsettled: "sin zanjar: entre 0 y el valor cuántico", defect: "entrelazado por un canal clásico LOCC: rechazado" },
  };
  function render() {
    const L = S0[lang()];
    const m = 10 ** Number(lm.value), dUm = Number(dIn.value);
    let dxUm = Number(dxIn.value);
    if (dxUm > dUm - 10) { dxUm = dUm - 10; dxIn.value = String(dxUm); }
    const d = dUm * 1e-6, dx = dxUm * 1e-6, t = Number(tIn.value), gamma = 10 ** Number(lgIn.value);
    // Left: positions.
    const span = d + dx, sx = (pos) => lx0 + (lx1 - lx0) * (pos + dx / 2) / span;
    const ax = { L: sx(-dx / 2), R: sx(dx / 2) }, bx = { L: sx(d - dx / 2), R: sx(d + dx / 2) };
    const sep = { LL: dUm, LR: dUm + dxUm, RL: dUm - dxUm, RR: dUm };
    root.querySelectorAll("[data-tg-mass]").forEach((el) => {
      const k = el.getAttribute("data-tg-mass");
      el.setAttribute("cx", (k[0] === "A" ? ax[k[1]] : bx[k[1]]).toFixed(1));
    });
    root.querySelectorAll("[data-tg-branch]").forEach((el) => {
      const k = el.getAttribute("data-tg-branch");
      el.setAttribute("x1", ax[k[0]].toFixed(1)); el.setAttribute("x2", bx[k[1]].toFixed(1));
    });
    root.querySelectorAll("[data-tg-sep]").forEach((el) => {
      const k = el.getAttribute("data-tg-sep");
      el.setAttribute("x", ((ax[k[0]] + bx[k[1]]) / 2 + (k === "LR" ? 18 : k === "RL" ? -18 : 0)).toFixed(1));
      el.textContent = `${k} · ${sep[k].toFixed(0)} µm`;
    });
    // Right: curves.
    const pts = [], poly = [];
    for (let i = 0; i <= 120; i++) {
      const tt = tmax * i / 120;
      const e = bmvConcurrence(bmvEntanglementPhase(bmvPhases(m, d, dx, tt, "quantum")));
      pts.push(`${i ? "L" : "M"} ${toX(tt).toFixed(1)} ${toY(e).toFixed(1)}`);
      poly.push(`${toX(tt).toFixed(1)},${toY(e).toFixed(1)}`);
    }
    if (qPath) qPath.setAttribute("d", pts.join(" "));
    if (band) band.setAttribute("points", poly.join(" ") + ` ${px1},${py1} ${px0},${py1}`);
    if (lLine) {
      if (state.flip) lLine.setAttribute("d", pts.join(" "));
      lLine.setAttribute("stroke-dasharray", state.flip ? "2 3" : "7 5");
      lLine.setAttribute("y1", state.flip ? String(toY(bmvConcurrence(bmvEntanglementPhase(bmvPhases(m, d, dx, 0, "quantum"))))) : String(py1 - 1.5));
      lLine.setAttribute("y2", state.flip ? String(toY(bmvConcurrence(bmvEntanglementPhase(bmvPhases(m, d, dx, tmax, "quantum"))))) : String(py1 - 1.5));
    }
    // Readouts for the followed channel.
    const pq = bmvPhases(m, d, dx, t, "quantum");
    const dphiQ = bmvEntanglementPhase(pq);
    const rate = Math.abs(bmvEntanglementPhase(bmvPhases(m, d, dx, 1, "quantum")));
    const tfull = rate > 0 ? Math.PI / rate : Infinity;
    let dphi = dphiQ, ent = 2 * bmvNegativity(pq, gamma * t), verdict = L.entangled, markY = toY(ent);
    if (state.channel === "locc") {
      const pl = bmvPhases(m, d, dx, t, "locc", state.flip);
      dphi = bmvEntanglementPhase(pl); ent = 2 * bmvNegativity(pl, gamma * t);
      verdict = state.flip ? L.defect : L.separable; markY = toY(ent);
    } else if (state.channel === "disputed") {
      verdict = L.unsettled; markY = toY(0.5 * ent);
    }
    if (ent < 1e-9) ent = 0;
    if (state.channel === "quantum" && ent === 0) verdict = L.separable;
    if (marker) { marker.setAttribute("cx", toX(t).toFixed(1)); marker.setAttribute("cy", markY.toFixed(1)); }
    if (reads.logm) reads.logm.textContent = fmt(Number(lm.value), 1);
    if (reads.d) reads.d.textContent = dUm.toFixed(0);
    if (reads.dx) reads.dx.textContent = dxUm.toFixed(0);
    if (reads.t) reads.t.textContent = fmt(t, 1);
    if (reads.logg) reads.logg.textContent = fmt(Number(lgIn.value), 1);
    if (reads.dphi) reads.dphi.textContent = state.channel === "disputed" ? `0 … ${dphiQ.toFixed(3)} rad` : `${dphi.toFixed(3)} rad`;
    if (reads.ent) reads.ent.textContent = state.channel === "disputed" ? `0 … ${(2 * bmvNegativity(pq, gamma * t)).toFixed(3)}` : ent.toFixed(3);
    if (reads.tfull) reads.tfull.textContent = Number.isFinite(tfull) ? `${tfull.toFixed(1)} s` : "∞";
    if (reads.verdict) reads.verdict.textContent = verdict;
    const st = state.flip && state.channel === "locc" ? "flip" : state.channel;
    if (status) { status.setAttribute("data-state", st); status.textContent = st === "flip" ? L.flip : L[state.channel]; }
    const errBox = root.querySelector('[data-tg-readout-box="err"]');
    if (errBox) errBox.setAttribute("data-alert", st === "flip" ? "true" : "false");
  }
  [lm, dIn, dxIn, tIn, lgIn].forEach((el) => el.addEventListener("input", render));
  chanBtns.forEach((btn) => btn.addEventListener("click", () => {
    state.channel = btn.getAttribute("data-tg-channel");
    chanBtns.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
    render();
  }));
  if (flipBtn) flipBtn.addEventListener("click", () => {
    state.flip = !state.flip; flipBtn.setAttribute("aria-pressed", String(state.flip));
    if (state.flip) { state.channel = "locc"; chanBtns.forEach((b) => b.setAttribute("aria-pressed", String(b.getAttribute("data-tg-channel") === "locc"))); }
    render();
  });
  window.addEventListener("tp-lang-change", render);
  root.setAttribute("data-tg-ready", "true");
  render();
}

export function initTimeGravity(scope = document) {
  const once = (sel, fn) => scope.querySelectorAll(sel).forEach((el) => { if (!el.hasAttribute("data-tg-ready")) fn(el); });
  once("[data-tg-predict]", initPredict);
  once('[data-tg-instrument="slope"]', initSlope);
  once('[data-tg-instrument="worldline"]', initWorldline);
  once('[data-tg-instrument="gps"]', initGps);
  once('[data-tg-instrument="poisson"]', initPoisson);
  once('[data-tg-instrument="pw"]', initPw);
  once('[data-tg-instrument="zych"]', initZych);
  once('[data-tg-instrument="dp"]', initDp);
  once('[data-tg-instrument="bmv"]', initBmv);
  once('[data-tg-instrument="page"]', initPage);
}

initTimeGravity(document);
