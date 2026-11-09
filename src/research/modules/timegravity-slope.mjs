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

export function initTimeGravity(scope = document) {
  const once = (sel, fn) => scope.querySelectorAll(sel).forEach((el) => { if (!el.hasAttribute("data-tg-ready")) fn(el); });
  once("[data-tg-predict]", initPredict);
  once('[data-tg-instrument="slope"]', initSlope);
  once('[data-tg-instrument="worldline"]', initWorldline);
  once('[data-tg-instrument="gps"]', initGps);
  once('[data-tg-instrument="poisson"]', initPoisson);
}

initTimeGravity(document);
