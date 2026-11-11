/**
 * @module featured-spotlight
 * Zero-build, strict-CSP controller for #tp-featured-edition-desk on the Informatico.ai cover.
 * Deterministically selects the active 12-hour cover spotlight (Math.floor(Date.now() / 43200000) % N)
 * and wires Prev / Next / Slot pill controls without .innerHTML or inline handlers.
 */

const HALF_DAY_MS = 12 * 3600 * 1000;

export function computeHalfDaySlot(count, nowMs = Date.now()) {
  if (!Number.isFinite(count) || count <= 0) return 0;
  const bucket = Math.floor(Math.max(0, nowMs) / HALF_DAY_MS);
  return bucket % count;
}

export function initFeaturedSpotlight(scope = document) {
  const desk = scope.querySelector ? scope.querySelector("#tp-featured-edition-desk") : null;
  if (!desk || desk.dataset.spotlightReady === "1") return;
  desk.dataset.spotlightReady = "1";

  const slides = Array.from(desk.querySelectorAll("[data-spotlight-slot]"));
  if (!slides.length) return;

  const slotBtns = Array.from(desk.querySelectorAll("[data-spotlight-pick]"));
  const prevBtn = desk.querySelector("[data-spotlight-step='prev']");
  const nextBtn = desk.querySelector("[data-spotlight-step='next']");
  const liveNode = desk.querySelector("[data-spotlight-live]");
  const counterNode = desk.querySelector("[data-spotlight-counter]");

  let activeIdx = computeHalfDaySlot(slides.length);

  function applySlot(nextIdx, announce = false) {
    const normalized = ((nextIdx % slides.length) + slides.length) % slides.length;
    activeIdx = normalized;

    slides.forEach((slide, idx) => {
      if (idx === normalized) {
        slide.removeAttribute("hidden");
      } else {
        slide.setAttribute("hidden", "");
      }
    });

    slotBtns.forEach((btn) => {
      const target = Number.parseInt(btn.getAttribute("data-spotlight-pick") || "-1", 10);
      btn.setAttribute("aria-pressed", target === normalized ? "true" : "false");
    });

    if (counterNode) {
      const enText = `Slot ${normalized + 1} / ${slides.length} · Rotates every 12h`;
      const esText = `Turno ${normalized + 1} / ${slides.length} · Rota cada 12 h`;
      counterNode.setAttribute("data-en", enText);
      counterNode.setAttribute("data-es", esText);
      const isEs = (document.documentElement.lang || "").toLowerCase().startsWith("es");
      counterNode.textContent = isEs ? esText : enText;
    }

    if (announce && liveNode) {
      const activeSlide = slides[normalized];
      const heading = activeSlide ? activeSlide.querySelector(".tp-spotlight-slide-title") : null;
      const label = heading ? (heading.textContent || "").trim() : `Slot ${normalized + 1}`;
      liveNode.textContent = label;
    }
  }

  applySlot(activeIdx, false);

  slotBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const idx = Number.parseInt(btn.getAttribute("data-spotlight-pick") || "0", 10);
      if (Number.isFinite(idx)) applySlot(idx, true);
    });
  });

  if (prevBtn) {
    prevBtn.addEventListener("click", () => {
      applySlot(activeIdx - 1, true);
    });
  }
  if (nextBtn) {
    nextBtn.addEventListener("click", () => {
      applySlot(activeIdx + 1, true);
    });
  }
}
