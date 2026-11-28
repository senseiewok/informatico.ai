/**
 * @module card-images
 * An essay card whose picture fails to load becomes a text card on purpose (class tp-rack-card-noimg, styled in
 * informatico.css) instead of showing an empty grey box. Strict CSP: a class is toggled, nothing else.
 */

const CARD_SELECTOR = ".tp-rack-card";
const IMG_SELECTOR = ".tp-rack-card .tp-rack-thumb";
const NOIMG_CLASS = "tp-rack-card-noimg";

function markCard(img) {
  const card = img.closest ? img.closest(CARD_SELECTOR) : null;
  if (card) card.classList.add(NOIMG_CLASS);
}

export function initCardImages(scope = document) {
  if (!scope.querySelectorAll) return;
  scope.querySelectorAll(IMG_SELECTOR).forEach((img) => {
    if (img.dataset.cardImageWatched === "1") return;
    img.dataset.cardImageWatched = "1";
    // Already failed before this module ran: complete, but with no picture in it.
    if (img.complete && img.naturalWidth === 0 && img.getAttribute("src")) {
      markCard(img);
      return;
    }
    img.addEventListener("error", () => markCard(img), { once: true });
  });
}
