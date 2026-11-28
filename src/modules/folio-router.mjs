/**
 * @module folio-router
 * Site navigation for Informatico.ai: the Contents dialog (the seven sections, then every essay and bounty folio,
 * one click from any page) with live search. Every essay lives at its own URL; links are plain links, nothing is
 * swapped in place.
 *
 * While the dialog is open the page behind it does not scroll (html.tp-contents-open in informatico.css) and
 * closing puts the page back where it was. The dialog's heading takes the opening focus (autofocus in the HTML),
 * so a phone does not raise its keyboard and resize the view; the search field is focused only where there is a
 * keyboard and a fine pointer.
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
  const sectionList = dialog.querySelector(".tp-contents-sections");
  const root = document.documentElement;
  let lastOpener = null;
  let pageAt = null;

  function lockPage() {
    pageAt = { left: window.scrollX, top: window.scrollY };
    // A scrollbar that takes up width (not an overlay one) leaves a gap when it goes: keep its gutter.
    root.classList.toggle("tp-contents-gutter", window.innerWidth > root.clientWidth);
    root.classList.add("tp-contents-open");
  }

  function unlockPage() {
    root.classList.remove("tp-contents-open", "tp-contents-gutter");
    if (pageAt) window.scrollTo({ left: pageAt.left, top: pageAt.top, behavior: "instant" });
    pageAt = null;
  }

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
    // The section list is navigation, not a search result: it steps aside while a search is typed.
    if (sectionList) sectionList.hidden = q !== "";
  }

  openers.forEach((btn) => {
    btn.addEventListener("click", () => {
      if (typeof dialog.showModal !== "function" || dialog.open) return;
      lastOpener = btn;
      lockPage();
      dialog.showModal();
      dialog.scrollTop = 0;
      setExpanded(true);
      // A touch screen would answer a focused text field with its keyboard, which resizes the view.
      const typing = "(min-width: 601px) and (hover: hover) and (pointer: fine)";
      if (search && window.matchMedia && window.matchMedia(typing).matches) {
        search.focus({ preventScroll: true });
      }
    });
  });

  dialog.addEventListener("close", () => {
    setExpanded(false);
    if (search && search.value) {
      search.value = "";
      applySearch();
    }
    if (lastOpener) lastOpener.focus({ preventScroll: true });
    unlockPage();
  });

  dialog.querySelectorAll("[data-close-contents]").forEach((btn) => {
    btn.addEventListener("click", () => dialog.close());
  });

  dialog.addEventListener("click", (ev) => {
    // A plain tap on a link closes the dialog, so the page is unlocked before it leaves (and is not found
    // still open when the reader comes back).
    const link = ev.target instanceof Element ? ev.target.closest("a[href]") : null;
    if (link) {
      const plain = ev.button === 0 && !ev.metaKey && !ev.ctrlKey && !ev.shiftKey && !ev.altKey;
      if (plain && !ev.defaultPrevented) dialog.close();
      return;
    }
    // A click on the backdrop (reported on the dialog itself, at a point outside its box) closes it.
    if (ev.target !== dialog) return;
    const box = dialog.getBoundingClientRect();
    const inside =
      ev.clientX >= box.left && ev.clientX <= box.right && ev.clientY >= box.top && ev.clientY <= box.bottom;
    if (!inside) dialog.close();
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

  // Names that are not visible text (the masthead list, the Close button) follow the language too.
  function syncAriaLabels(isEs) {
    document.querySelectorAll("[data-aria-en][data-aria-es]").forEach((el) => {
      el.setAttribute("aria-label", el.getAttribute(isEs ? "data-aria-es" : "data-aria-en"));
    });
  }

  window.addEventListener("tp-lang-change", (ev) => {
    const isEs = Boolean(ev && ev.detail && ev.detail.isEs);
    syncSearchLabels(isEs);
    syncAriaLabels(isEs);
  });
  syncSearchLabels(document.documentElement.lang === "es-MX");
  syncAriaLabels(document.documentElement.lang === "es-MX");
}
