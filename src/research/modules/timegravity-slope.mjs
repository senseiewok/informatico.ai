/**
 * @module timegravity-slope
 * Time & Gravity instruments, hand-written, zero dependencies, zero network calls.
 *
 *  - [data-tg-instrument="slope"]  (T.01): a body released at rest in ds² = −A(z)c²dt² + dz², A = 1 + 2gz/c²,
 *    integrated with RK4 exactly as tools/timegravity_kernel.py does. Only g_tt varies with height; there is no
 *    force term. Knockout flattens A' to zero (nothing falls); the sign flip is the verifier's planted defect.
 *  - [data-tg-instrument="worldline"] (T.00): a marker slides along a worldline; a picture of the question, not a result.
 *
 * Reduced motion: trajectories are drawn at once instead of animated. Keyboard: native range inputs and buttons.
 * The static SVG in the markup is the fallback; this module only redraws its paths.
 */
const C = 299792458.0;
const G0 = 9.80665;
const T_PROPER = 1.0;
const N_STEPS = 4000; // enough for 1e-9 relative on screen; the Python verifier uses 20,000

const STR = {
  en: {
    falls: "Falls at g: the clock-rate gradient alone produces the acceleration. No force term anywhere.",
    flat: "Knockout: every clock ticks at the same rate, the gradient is zero, and nothing falls.",
    flip: "Planted defect: the slope points the wrong way and the body rises. The verifier rejects this run.",
    scaled: "Gradient scaled: the body falls at the scaled acceleration, still with no force term.",
    nowLabel: "now?",
  },
  es: {
    falls: "Cae a g: el gradiente del ritmo de los relojes produce por sí solo la aceleración. Ninguna fuerza en ningún lado.",
    flat: "Apagado: todos los relojes marchan al mismo ritmo, el gradiente es cero y nada cae.",
    flip: "Defecto plantado: la pendiente apunta al revés y el cuerpo sube. El verificador rechaza esta corrida.",
    scaled: "Gradiente escalado: el cuerpo cae con la aceleración escalada, todavía sin término de fuerza.",
    nowLabel: "¿ahora?",
  },
};

function lang() {
  return document.documentElement.lang === "es-MX" ? "es" : "en";
}

function reducedMotion() {
  return !!(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
}

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

function fmt(x, digits) {
  return Number.isFinite(x) ? x.toFixed(digits) : "—";
}

function initSlope(root) {
  const svg = root.querySelector("svg.tg-stage");
  const path = root.querySelector(".tg-worldline");
  const body = root.querySelector(".tg-body");
  const gradInput = root.querySelector("[data-tg-grad]");
  const knockoutBtn = root.querySelector("[data-tg-knockout]");
  const flipBtn = root.querySelector("[data-tg-flip]");
  const replayBtn = root.querySelector("[data-tg-replay]");
  const status = root.querySelector("[data-tg-status]");
  const reads = {};
  root.querySelectorAll("[data-tg-read]").forEach((el) => { reads[el.getAttribute("data-tg-read")] = el; });
  if (!svg || !path || !body || !gradInput) return;

  // Plot box from the markup so Python (static plate) and JS agree.
  const x0 = Number(svg.getAttribute("data-x0")), x1 = Number(svg.getAttribute("data-x1"));
  const y0 = Number(svg.getAttribute("data-y0")), y1 = Number(svg.getAttribute("data-y1"));
  const zTop = Number(svg.getAttribute("data-ztop")), zBot = Number(svg.getAttribute("data-zbot"));
  const toX = (t) => x0 + (x1 - x0) * (t / T_PROPER);
  const toY = (z) => y0 + (y1 - y0) * ((zTop - z) / (zTop - zBot));

  let raf = 0;
  let knockout = false;
  let flip = false;

  const rateCol = root.querySelector(".tg-rate-col");

  function render(animate) {
    const scale = knockout ? 0 : Number(gradInput.value);
    const { aEff, slopeAp, samples } = integrate(scale, flip);
    const d = samples.map(([, t, z], i) => `${i ? "L" : "M"} ${toX(t).toFixed(2)} ${toY(Math.max(zBot, Math.min(zTop, z))).toFixed(2)}`).join(" ");
    path.setAttribute("d", d);
    const state = knockout ? "flat" : flip ? "flip" : "fall";
    path.setAttribute("data-state", state);
    if (status) {
      status.setAttribute("data-state", state);
      const S = STR[lang()];
      status.textContent = knockout ? S.flat : flip ? S.flip : (Math.abs(scale - 1) < 1e-9 ? S.falls : S.scaled);
    }
    if (rateCol) rateCol.style.opacity = knockout ? "0.15" : String(0.35 + 0.5 * Math.min(1, scale / 2));
    const relErr = Math.abs(aEff + G0 * scale) / G0;
    if (reads.grad) reads.grad.textContent = `${fmt(scale, 2)} ×`;
    if (reads.slope) reads.slope.textContent = `${slopeAp.toExponential(3)} 1/m`;
    if (reads.accel) reads.accel.textContent = `${fmt(aEff, 5)} m/s²`;
    if (reads.err) reads.err.textContent = knockout ? `|a| = ${Math.abs(aEff).toExponential(1)}` : `${relErr.toExponential(2)}`;
    const errBox = root.querySelector('[data-tg-readout-box="err"]');
    if (errBox) errBox.setAttribute("data-alert", flip && !knockout ? "true" : "false");

    cancelAnimationFrame(raf);
    const last = samples[samples.length - 1];
    const place = (frac) => {
      const idx = Math.min(samples.length - 1, Math.floor(frac * (samples.length - 1)));
      const [, t, z] = samples[idx];
      body.setAttribute("cx", toX(t).toFixed(2));
      body.setAttribute("cy", toY(Math.max(zBot, Math.min(zTop, z))).toFixed(2));
    };
    if (!animate || reducedMotion()) {
      body.setAttribute("cx", toX(last[1]).toFixed(2));
      body.setAttribute("cy", toY(Math.max(zBot, Math.min(zTop, last[2]))).toFixed(2));
      path.style.strokeDasharray = "";
      path.style.strokeDashoffset = "";
      return;
    }
    const length = path.getTotalLength ? path.getTotalLength() : 0;
    const start = performance.now();
    const dur = 2200;
    const step = (now) => {
      const frac = Math.min(1, (now - start) / dur);
      if (length) {
        path.style.strokeDasharray = `${length}`;
        path.style.strokeDashoffset = `${length * (1 - frac)}`;
      }
      place(frac);
      if (frac < 1) raf = requestAnimationFrame(step);
    };
    raf = requestAnimationFrame(step);
  }

  gradInput.addEventListener("input", () => render(false));
  gradInput.addEventListener("change", () => render(true));
  if (knockoutBtn) {
    knockoutBtn.addEventListener("click", () => {
      knockout = !knockout;
      knockoutBtn.setAttribute("aria-pressed", knockout ? "true" : "false");
      render(true);
    });
  }
  if (flipBtn) {
    flipBtn.addEventListener("click", () => {
      flip = !flip;
      flipBtn.setAttribute("aria-pressed", flip ? "true" : "false");
      render(true);
    });
  }
  if (replayBtn) replayBtn.addEventListener("click", () => render(true));
  window.addEventListener("tp-lang-change", () => render(false));
  root.setAttribute("data-tg-ready", "true");
  render(true);
}

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

export function initTimeGravity(scope = document) {
  scope.querySelectorAll('[data-tg-instrument="slope"]').forEach((el) => { if (!el.hasAttribute("data-tg-ready")) initSlope(el); });
  scope.querySelectorAll('[data-tg-instrument="worldline"]').forEach((el) => { if (!el.hasAttribute("data-tg-ready")) initWorldline(el); });
}

initTimeGravity(document);
