/**
 * @module featured-spotlight
 * Zero-build, strict-CSP controller for "This week's essay" (#tp-featured-edition-desk) on the Informatico.ai cover.
 * Picks the week's essay from the slides already in the page (weeks start Monday 00:00 UTC), shows the
 * next three of the same rotation under "Read next", and points the hero's "Start reading" at the week's essay.
 * No .innerHTML and no inline handlers; without scripts the page keeps its first essay and first three titles.
 */

const WEEK_MS = 7 * 24 * 3600 * 1000;
// The Unix epoch was a Thursday; shifting by three days makes each week start on Monday 00:00 UTC.
const MONDAY_SHIFT_MS = 3 * 24 * 3600 * 1000;
const COMING_NEXT_COUNT = 3;
// A link this module copies must be a plain relative page path, such as "architecture/a11/" or "../math/m11/".
const RELATIVE_PAGE_RE = /^(?:\.\.?\/)*[a-z0-9-]+(?:\/[a-z0-9-]+)*\/$/;

export function computeWeekSlot(count, nowMs = Date.now()) {
  if (!Number.isFinite(count) || count <= 0) return 0;
  const bucket = Math.floor((Math.max(0, nowMs) + MONDAY_SHIFT_MS) / WEEK_MS);
  return bucket % count;
}

/** The slots listed under "Coming next" for an active slot: the next ones in the rotation, in reading order. */
export function comingNextSlots(active, count, howMany = COMING_NEXT_COUNT) {
  const out = [];
  if (!Number.isFinite(count) || count <= 1) return out;
  for (let step = 1; step <= Math.min(howMany, count - 1); step += 1) {
    out.push((active + step) % count);
  }
  return out;
}

export function initFeaturedSpotlight(scope = document, nowMs = Date.now()) {
  const desk = scope.querySelector ? scope.querySelector("#tp-featured-edition-desk") : null;
  if (!desk || desk.dataset.spotlightReady === "1") return;
  desk.dataset.spotlightReady = "1";

  const slides = Array.from(desk.querySelectorAll("[data-spotlight-slot]"));
  if (!slides.length) return;

  const active = computeWeekSlot(slides.length, nowMs);
  slides.forEach((slide, idx) => {
    if (idx === active) {
      slide.removeAttribute("hidden");
    } else {
      slide.setAttribute("hidden", "");
    }
  });

  const comingItems = Array.from(desk.querySelectorAll("[data-coming-slot]"));
  if (comingItems.length) {
    const bySlot = new Map();
    comingItems.forEach((item) => {
      bySlot.set(Number.parseInt(item.getAttribute("data-coming-slot") || "-1", 10), item);
      item.setAttribute("hidden", "");
    });
    const list = comingItems[0].parentNode;
    comingNextSlots(active, slides.length).forEach((slot) => {
      const item = bySlot.get(slot);
      if (!item) return;
      item.removeAttribute("hidden");
      list.appendChild(item); // keeps the three in reading order when the rotation wraps round
    });
  }

  const start = scope.querySelector("[data-spotlight-start]");
  const link = slides[active].querySelector(".tp-spotlight-slide-title a");
  const href = link ? link.getAttribute("href") || "" : "";
  if (start && RELATIVE_PAGE_RE.test(href)) {
    start.setAttribute("href", href);
  }
}
