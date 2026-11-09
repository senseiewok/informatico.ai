/**
 * @module trace-sentence
 * Essay Zero (/about/ and /es-mx/about/) interactive "Trace a sentence" presenter + 65-facet rosette bloom.
 *
 * Zero-build native ES module. CSP-safe: no innerHTML, no eval, no inline handlers, no .style writes.
 * Pattern: a Repository (about-evidence.json) feeds a Presenter that owns one non-modal <dialog>
 * and the sentence buttons; all state flows through attributes and textContent.
 */

const EVIDENCE_URL = new URL("../data/about-evidence.json", import.meta.url);

const LABELS = {
  en: {
    panelTitle: (n, total) => `Sentence ${n} of ${total}`,
    closePanel: "Close evidence panel",
    announce: (n, total, tier, source, date) =>
      `Evidence for sentence ${n} of ${total}. ${tier}. Source: ${source}. Read ${date}.`,
    closed: "Evidence panel closed.",
    statusOk: (n, total, date) =>
      `${n} of ${total} sentences verified against about-evidence.json (audited ${date}).`,
    statusDrift: (bad, total) =>
      `${bad} of ${total} sentences differ from about-evidence.json; they are marked in the text.`,
    statusError:
      "Could not load about-evidence.json; the static table below lists every sentence.",
    sentenceLabel: (n, tier) => `Sentence ${n}, ${tier}. Opens its evidence.`,
    rosetteAnnounce:
      "65-facet geometric rosette bloomed: built with love for the 65 Roses (Cystic Fibrosis) community.",
  },
  es: {
    panelTitle: (n, total) => `Oración ${n} de ${total}`,
    closePanel: "Cerrar el panel de evidencia",
    announce: (n, total, tier, source, date) =>
      `Evidencia de la oración ${n} de ${total}. ${tier}. Fuente: ${source}. Leída el ${date}.`,
    closed: "Panel de evidencia cerrado.",
    statusOk: (n, total, date) =>
      `${n} de ${total} oraciones verificadas contra about-evidence.json (auditado el ${date}).`,
    statusDrift: (bad, total) =>
      `${bad} de ${total} oraciones difieren de about-evidence.json; están marcadas en el texto.`,
    statusError:
      "No se pudo cargar about-evidence.json; la tabla estática abajo enumera cada oración.",
    sentenceLabel: (n, tier) => `Oración ${n}, ${tier}. Abre su evidencia.`,
    rosetteAnnounce:
      "Roseta geométrica de 65 facetas desplegada: construido con cariño para la comunidad de las 65 Rosas (Fibrosis Quística).",
  },
};

function h(tag, attrs = {}, children = []) {
  const el = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (v === null || v === undefined || v === false) continue;
    el.setAttribute(k, String(v));
  }
  for (const child of children) {
    if (child == null) continue;
    el.appendChild(typeof child === "string" ? document.createTextNode(child) : child);
  }
  return el;
}

const EvidenceRepository = {
  async load() {
    const res = await fetch(EVIDENCE_URL, { credentials: "same-origin" });
    if (!res.ok) throw new Error(`about-evidence.json: HTTP ${res.status}`);
    const data = await res.json();
    const required = [
      "id",
      "sentence_en",
      "sentence_es",
      "value",
      "source_path",
      "command",
      "date_read",
      "tier",
      "limitation",
    ];
    if (!Array.isArray(data.sentences)) {
      throw new Error("about-evidence.json: sentences[] missing");
    }
    for (const row of data.sentences) {
      for (const key of required) {
        if (!(key in row) || String(row[key]).length === 0) {
          throw new Error(`about-evidence.json: ${row.id || "?"} lacks ${key}`);
        }
      }
      if (!/^T[0-3]$/.test(row.tier)) {
        throw new Error(`about-evidence.json: ${row.id} has tier ${row.tier}`);
      }
    }
    return data;
  },
};

export function renderSentence(row, lang) {
  const isEs = lang === "es";
  const template = isEs ? row.sentence_es : row.sentence_en;
  const val = isEs && row.value_es ? row.value_es : row.value;
  return template.replaceAll("{value}", val);
}

class TracePresenter {
  #data = null;
  #rows = new Map();
  #order = [];
  #lang = "en";
  #activeId = null;
  #returnFocusTo = null;
  #ac = new AbortController();
  #reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  #keyBuffer = "";

  constructor() {
    this.panel = document.getElementById("tz-panel");
    this.title = document.getElementById("tz-panel-title");
    this.live = document.getElementById("tz-live");
    this.status = document.getElementById("tz-status");
    this.plate = document.querySelector("#plate-0d svg");
    this.rosetteBtn = document.getElementById("tz-rosette-btn");
    this.rosetteWhisper = document.getElementById("tz-rosette-whisper");
    this.fields = {
      sentence: document.getElementById("tz-panel-sentence"),
      tier: document.getElementById("tz-f-tier"),
      source: document.getElementById("tz-f-source"),
      date: document.getElementById("tz-f-date"),
      command: document.getElementById("tz-f-command"),
      limitation: document.getElementById("tz-f-limitation"),
    };
  }

  get labels() {
    return LABELS[this.#lang];
  }

  async init() {
    const { signal } = this.#ac;
    this.#syncLangFromDocument();
    window.addEventListener(
      "tp-lang-change",
      (ev) => {
        this.#lang = ev.detail && ev.detail.isEs ? "es" : "en";
        this.#onLanguageChanged();
      },
      { signal }
    );
    this.#bindPanel(signal);
    this.#bindRosette(signal);
    try {
      this.#data = await EvidenceRepository.load();
    } catch (err) {
      this.#setStatus("error", this.labels.statusError);
      console.error(err);
      return;
    }
    for (const row of this.#data.sentences) {
      this.#rows.set(row.id, row);
      this.#order.push(row.id);
    }
    this.#upgradeSentences(signal);
    this.#checkDrift();
  }

  #syncLangFromDocument() {
    const root = document.documentElement;
    const isEs =
      root.dataset.lang === "es" ||
      (root.lang || "").toLowerCase().startsWith("es");
    this.#lang = isEs ? "es" : "en";
    const close = document.getElementById("tz-panel-close");
    if (close) close.setAttribute("aria-label", this.labels.closePanel);
  }

  #onLanguageChanged() {
    for (const id of this.#order) this.#renderSentenceButton(id);
    if (this.#activeId) this.#fillPanel(this.#activeId);
    const close = document.getElementById("tz-panel-close");
    if (close) close.setAttribute("aria-label", this.labels.closePanel);
    if (this.#data) this.#checkDrift();
  }

  #upgradeSentences(signal) {
    const spans = document.querySelectorAll(".tz-sentence[data-ev]");
    spans.forEach((span) => {
      const id = span.getAttribute("data-ev");
      const row = this.#rows.get(id);
      if (!row) return;
      const btn = h("button", {
        type: "button",
        class: "tz-sentence",
        "data-ev": id,
        "data-static": span.textContent.trim(),
        "aria-expanded": "false",
        "aria-controls": "tz-panel",
        "aria-haspopup": "dialog",
      });
      span.replaceWith(btn);
      btn.addEventListener("click", () => this.open(id, btn), { signal });
      this.#renderSentenceButton(id);
    });
  }

  #renderSentenceButton(id) {
    const btn = document.querySelector(`button.tz-sentence[data-ev="${id}"]`);
    const row = this.#rows.get(id);
    if (!btn || !row) return;
    const n = this.#order.indexOf(id) + 1;
    const tierName = this.#tierName(row.tier);
    const text = renderSentence(row, this.#lang);
    btn.replaceChildren(
      document.createTextNode(text),
      h(
        "span",
        { class: "tz-tier-mark", "data-tier": row.tier, "aria-hidden": "true" },
        [row.tier]
      )
    );
    btn.setAttribute(
      "aria-label",
      `${text} ${this.labels.sentenceLabel(n, tierName)}`
    );
  }

  #checkDrift() {
    const total = this.#order.length;
    let bad = 0;
    for (const id of this.#order) {
      const btn = document.querySelector(`button.tz-sentence[data-ev="${id}"]`);
      if (!btn) continue;
      const row = this.#rows.get(id);
      const staticText = btn.getAttribute("data-static") || "";
      const expectedEn = renderSentence(row, "en");
      const expectedEs = renderSentence(row, "es");
      const drift = staticText !== expectedEn && staticText !== expectedEs;
      if (drift) {
        bad += 1;
        btn.setAttribute("data-drift", "true");
      } else {
        btn.removeAttribute("data-drift");
      }
    }
    if (bad === 0) {
      this.#setStatus(
        "ok",
        this.labels.statusOk(total, total, this.#data.generated)
      );
    } else {
      this.#setStatus("drift", this.labels.statusDrift(bad, total));
    }
  }

  #setStatus(state, text) {
    if (!this.status) return;
    this.status.setAttribute("data-state", state);
    this.status.replaceChildren(document.createTextNode(text));
  }

  #tierName(tier) {
    const t = this.#data && this.#data.tiers && this.#data.tiers[tier];
    return t ? (this.#lang === "es" ? t.es : t.en) : tier;
  }

  #bindPanel(signal) {
    if (!this.panel) return;
    const closeBtn = document.getElementById("tz-panel-close");
    const prevBtn = document.getElementById("tz-prev");
    const nextBtn = document.getElementById("tz-next");
    if (closeBtn) {
      closeBtn.addEventListener("click", () => this.close(), { signal });
    }
    if (prevBtn) {
      prevBtn.addEventListener("click", () => this.step(-1), { signal });
    }
    if (nextBtn) {
      nextBtn.addEventListener("click", () => this.step(1), { signal });
    }
    this.panel.addEventListener(
      "keydown",
      (ev) => {
        if (ev.key === "Escape") {
          ev.preventDefault();
          this.close();
        } else if (ev.altKey && ev.key === "ArrowRight") {
          ev.preventDefault();
          this.step(1);
        } else if (ev.altKey && ev.key === "ArrowLeft") {
          ev.preventDefault();
          this.step(-1);
        }
      },
      { signal }
    );
    this.panel.addEventListener("close", () => this.#afterClose(), { signal });
  }

  #bindRosette(signal) {
    const toggleBloom = () => {
      if (!this.plate) return;
      const bloomed = this.plate.getAttribute("data-rosette-bloom") === "true";
      const nextState = !bloomed;
      this.plate.setAttribute("data-rosette-bloom", nextState ? "true" : "false");
      if (this.rosetteBtn) {
        this.rosetteBtn.setAttribute("aria-pressed", nextState ? "true" : "false");
      }
      if (this.rosetteWhisper) {
        this.rosetteWhisper.hidden = !nextState;
      }
      if (nextState) {
        this.#announce(this.labels.rosetteAnnounce);
      }
    };
    if (this.rosetteBtn) {
      this.rosetteBtn.addEventListener("click", toggleBloom, { signal });
    }
    document.addEventListener(
      "keydown",
      (ev) => {
        const tag = (ev.target && ev.target.tagName) || "";
        if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT") return;
        if (ev.ctrlKey || ev.metaKey || ev.altKey) return;
        if (ev.key === "6" || ev.key === "5") {
          this.#keyBuffer = (this.#keyBuffer + ev.key).slice(-2);
          if (this.#keyBuffer === "65") {
            this.#keyBuffer = "";
            toggleBloom();
          }
        } else {
          this.#keyBuffer = "";
        }
      },
      { signal }
    );
  }

  open(id, invoker) {
    if (!this.#rows.has(id) || !this.panel) return;
    if (invoker) this.#returnFocusTo = invoker;
    this.#activeId = id;
    this.#fillPanel(id);
    if (!this.panel.open) this.panel.show();
    document.querySelectorAll("button.tz-sentence").forEach((b) => {
      b.setAttribute(
        "aria-expanded",
        b.getAttribute("data-ev") === id ? "true" : "false"
      );
    });
    const row = this.#rows.get(id);
    const n = this.#order.indexOf(id) + 1;
    this.#announce(
      this.labels.announce(
        n,
        this.#order.length,
        this.#tierName(row.tier),
        row.source_path,
        row.date_read
      )
    );
    if (this.title) {
      this.title.focus({
        preventScroll: true,
      });
    }
  }

  step(delta) {
    if (!this.#activeId) return;
    const idx = this.#order.indexOf(this.#activeId);
    const next = this.#order[idx + delta];
    if (!next) return;
    const btn = document.querySelector(`button.tz-sentence[data-ev="${next}"]`);
    if (btn) {
      btn.scrollIntoView({
        block: "center",
        behavior: this.#reduceMotion.matches ? "auto" : "smooth",
      });
    }
    this.open(next, btn || this.#returnFocusTo);
  }

  close() {
    if (this.panel && this.panel.open) this.panel.close();
    else this.#afterClose();
  }

  #afterClose() {
    this.#activeId = null;
    document
      .querySelectorAll("button.tz-sentence[aria-expanded='true']")
      .forEach((b) => b.setAttribute("aria-expanded", "false"));
    if (this.plate) this.plate.setAttribute("data-active-tier", "");
    this.#announce(this.labels.closed);
    if (this.#returnFocusTo && document.contains(this.#returnFocusTo)) {
      this.#returnFocusTo.focus();
    }
  }

  #fillPanel(id) {
    const row = this.#rows.get(id);
    const n = this.#order.indexOf(id) + 1;
    const total = this.#order.length;
    if (this.title) this.title.textContent = this.labels.panelTitle(n, total);
    if (this.fields.sentence) {
      this.fields.sentence.textContent = renderSentence(row, this.#lang);
    }
    if (this.fields.tier) {
      this.fields.tier.replaceChildren(
        h("span", { class: "tz-tier-pill", "data-tier": row.tier }, [
          this.#tierName(row.tier),
        ])
      );
    }
    if (this.fields.source) this.fields.source.textContent = row.source_path;
    if (this.fields.date) this.fields.date.textContent = row.date_read;
    if (this.fields.command) this.fields.command.textContent = row.command;
    if (this.fields.limitation) {
      this.fields.limitation.textContent =
        this.#lang === "es" && row.limitation_es
          ? row.limitation_es
          : row.limitation;
    }
    const prevBtn = document.getElementById("tz-prev");
    const nextBtn = document.getElementById("tz-next");
    if (prevBtn) prevBtn.disabled = n <= 1;
    if (nextBtn) nextBtn.disabled = n >= total;
    if (this.plate) this.plate.setAttribute("data-active-tier", row.tier);
  }

  #announce(text) {
    if (!this.live) return;
    this.live.textContent = "";
    queueMicrotask(() => {
      this.live.textContent = text;
    });
  }

  destroy() {
    this.#ac.abort();
  }
}

let activePresenter = null;

export function initTraceSentence(scope = document) {
  const root = scope || document;
  if (!root.querySelector || !root.querySelector("#tz-essay")) return;
  if (activePresenter) {
    activePresenter.destroy();
  }
  activePresenter = new TracePresenter();
  activePresenter.init();
}
