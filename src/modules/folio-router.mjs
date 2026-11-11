/**
 * @module folio-router
 * Site navigation for Informatico.ai: the Contents dialog (every essay and bounty folio, one click from any page)
 * with live search. Every essay lives at its own URL; links are plain links, nothing is swapped in place.
 */
export function initFolioRouter() {
  const dialog = document.getElementById("tp-contents");
  if (!dialog || dialog.dataset.bound === "true") return;
  dialog.dataset.bound = "true";

  const openers = document.querySelectorAll("[data-open-contents]");
  const search = document.getElementById("tp-contents-search");
  const empty = document.getElementById("tp-contents-empty");
  const items = dialog.querySelectorAll("li[data-contents-item], li[data-contents-bounty-item]");
  const pillarItems = dialog.querySelectorAll("li[data-contents-item]");
  const cols = dialog.querySelectorAll(".tp-contents-col");
  const bountySections = dialog.querySelectorAll(".tp-contents-bounties");
  let lastOpener = null;

  function setExpanded(value) {
    openers.forEach((btn) => btn.setAttribute("aria-expanded", value ? "true" : "false"));
  }

  function applySearch() {
    const q = (search && search.value ? search.value : "").trim().toLowerCase();
    let shown = 0;
    items.forEach((li) => {
      const haystack = (li.getAttribute("data-search") || "") + " " + (li.textContent || "").toLowerCase();
      const match = !q || haystack.includes(q);
      li.hidden = !match;
      if (match) shown += 1;
    });
    cols.forEach((col) => {
      col.hidden = !col.querySelector("li[data-contents-item]:not([hidden])");
    });
    bountySections.forEach((sec) => {
      sec.hidden = !sec.querySelector("li[data-contents-bounty-item]:not([hidden])");
    });
    if (empty) empty.hidden = shown > 0;
  }

  openers.forEach((btn) => {
    btn.addEventListener("click", () => {
      if (typeof dialog.showModal !== "function") return;
      lastOpener = btn;
      dialog.showModal();
      setExpanded(true);
      if (search && window.matchMedia && window.matchMedia("(min-width: 601px)").matches) {
        search.focus();
      }
    });
  });

  dialog.addEventListener("close", () => {
    setExpanded(false);
    if (search && search.value) {
      search.value = "";
      applySearch();
    }
    if (lastOpener) lastOpener.focus();
  });

  dialog.querySelectorAll("[data-close-contents]").forEach((btn) => {
    btn.addEventListener("click", () => dialog.close());
  });

  // A click on the backdrop (the dialog box itself, outside its inner panel) closes it.
  dialog.addEventListener("click", (ev) => {
    if (ev.target === dialog) dialog.close();
  });

  if (search) search.addEventListener("input", applySearch);

  function syncSearchLabels(isEs) {
    if (!search) return;
    const total = pillarItems.length;
    search.setAttribute(
      "placeholder",
      isEs
        ? "Buscar en " + total + " ensayos, 6 retos, 6 herramientas y 3 síntesis"
        : "Search " + total + " essays, 6 bounties, 6 tools & 3 syntheses"
    );
    search.setAttribute(
      "aria-label",
      isEs ? "Buscar ensayos, retos y herramientas" : "Search essays, bounties and tools"
    );
  }

  window.addEventListener("tp-lang-change", (ev) => {
    syncSearchLabels(Boolean(ev && ev.detail && ev.detail.isEs));
  });
  syncSearchLabels(document.documentElement.lang === "es-MX");
}
