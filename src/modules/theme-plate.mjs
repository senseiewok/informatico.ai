/**
 * @module theme-plate
 * Limestone Paper <-> Prussian Cyanotype Blueprint toggle & EN / ES-MX atomic bilingual controller for Informatico.ai.
 */

const NAV_LABELS = {
  en: {
    index: "Index",
    engineering: "Engineering",
    architecture: "Architecture",
    physics: "Physics",
    math: "Mathematics",
    about: "About",
    sub: "Engineering · Architecture · Physics · Mathematics",
    whyKicker: "Why it matters",
    actPills: ["I · Story", "II · Intuition", "III · Lab", "IV · Discovery", "V · Sources", "VI · Puzzle"],
    walkthroughHeading: "Three experiments to try",
    chronHeading: "Historical Turning Points & Chronology",
    sourcesHeading: "Primary Literature & Standards Citations",
    searchPlaceholder:
      "Search 32 monographs by topic, everyday question, equation, or DOI (e.g. Formula 1, Barragán, earthquake, bridge, Lean 4)...",
    plateLimestone: "Dark",
    plateBlueprint: "Light",
    copySkill: "Copy SKILL.md",
    copyTelemetry: "Copy Live Telemetry JSON",
  },
  es: {
    index: "Índice",
    engineering: "Ingeniería",
    architecture: "Arquitectura",
    physics: "Física",
    math: "Matemáticas",
    about: "Acerca de",
    sub: "Ingeniería · Arquitectura · Física · Matemáticas",
    whyKicker: "Por qué importa",
    actPills: ["I · Historia", "II · Intuición", "III · Laboratorio", "IV · Descubrimiento", "V · Fuentes", "VI · Crucigrama"],
    walkthroughHeading: "Tres experimentos para probar",
    chronHeading: "Hitos Históricos y Cronología Científica",
    sourcesHeading: "Literatura Primaria y Normas Técnicas",
    searchPlaceholder:
      "Buscar en los 32 monográficos por tema, pregunta cotidiana, ecuación o DOI (ej. Fórmula 1, Barragán, sismo, puente, Lean 4)...",
    plateLimestone: "Oscuro",
    plateBlueprint: "Claro",
    copySkill: "Copiar SKILL.md",
    copyTelemetry: "Copiar Telemetría JSON",
  },
};

function themeLabel(isDark, isEs) {
  if (isDark) return isEs ? "Cambiar a tema claro" : "Switch to light theme";
  return isEs ? "Cambiar a tema oscuro" : "Switch to dark theme";
}

export function applyMagazineLanguage(isEs, scope = document) {
  const root = document.documentElement;
  root.lang = isEs ? "es-MX" : "en";
  root.dataset.lang = isEs ? "es" : "en";

  const langBtn = document.getElementById("tp-lang-toggle");
  if (langBtn) {
    langBtn.setAttribute("aria-pressed", isEs ? "true" : "false");
    langBtn.textContent = isEs ? "EN" : "ES";
    langBtn.setAttribute("aria-label", isEs ? "Read in English" : "Leer en español");
    langBtn.setAttribute("title", isEs ? "English" : "Español");
  }

  const dict = isEs ? NAV_LABELS.es : NAV_LABELS.en;
  document.querySelectorAll("[data-tp-nav]").forEach((el) => {
    const key = el.getAttribute("data-tp-nav");
    if (key && dict[key]) {
      el.textContent = dict[key];
    }
  });

  const subEl = document.querySelector(".tp-brand-sub");
  if (subEl) {
    subEl.textContent = dict.sub;
  }

  const plateBtn = document.getElementById("tp-blueprint-toggle");
  if (plateBtn) {
    const isBlueprint = root.getAttribute("data-theme") === "blueprint";
    plateBtn.textContent = isBlueprint ? dict.plateBlueprint : dict.plateLimestone;
    plateBtn.setAttribute("aria-label", themeLabel(isBlueprint, isEs));
  }

  const rootScope = scope || document;

  rootScope.querySelectorAll("[data-en][data-es]").forEach((el) => {
    const targetText = isEs ? el.getAttribute("data-es") : el.getAttribute("data-en");
    if (targetText) {
      el.textContent = targetText;
    }
  });

  rootScope.querySelectorAll(".tp-why-kicker").forEach((el) => {
    el.textContent = dict.whyKicker;
  });

  rootScope.querySelectorAll(".tp-act-jump-bar").forEach((bar) => {
    const pills = bar.querySelectorAll(".tp-act-pill");
    pills.forEach((pill, idx) => {
      if (dict.actPills[idx]) {
        pill.textContent = dict.actPills[idx];
      }
    });
  });

  rootScope.querySelectorAll(".tp-walkthrough-box h3").forEach((el) => {
    el.textContent = dict.walkthroughHeading;
  });

  rootScope.querySelectorAll(".tp-plate-provenance-summary").forEach((el) => {
    el.textContent = isEs
      ? "Sobre esta ilustración"
      : "About this illustration";
  });

  const lensLabels = isEs
    ? ["1 · Superficie 3D", "2 · Retrato de Fase", "3 · Listón de Conservación", "4 · Radar Polar de 6 Ejes"]
    : ["1 · 3D Surface", "2 · Phase Portrait", "3 · Conservation Ribbon", "4 · 6-Axis Polar Radar"];
  rootScope.querySelectorAll(".tp-lens-btn[data-lens-mode]").forEach((btn) => {
    const idx = parseInt(btn.getAttribute("data-lens-mode") || "-1", 10);
    if (idx >= 0 && idx < lensLabels.length) {
      btn.textContent = lensLabels[idx];
    }
  });

  rootScope.querySelectorAll("button[data-skill-download]").forEach((el) => {
    const fn = el.getAttribute("data-skill-download") || "SKILL.md";
    el.textContent = (isEs ? "Descargar SKILL.md (" : "Download SKILL.md (") + fn + ")";
  });

  rootScope.querySelectorAll("button[data-py-download]").forEach((el) => {
    const fn = el.getAttribute("data-py-download") || "verify.py";
    el.textContent = (isEs ? "Descargar Verificador Python (" : "Download Python Tool (") + fn + ")";
  });

  rootScope.querySelectorAll("button[data-skill-copy]").forEach((el) => {
    el.textContent = dict.copySkill;
  });

  rootScope.querySelectorAll("button[data-telemetry-copy]").forEach((el) => {
    el.textContent = dict.copyTelemetry;
  });

  rootScope.querySelectorAll("[data-pillar-volume-filter='all']").forEach((el) => {
    el.textContent = isEs ? "Todos (8)" : "All (8)";
  });

  const resetBtn = document.getElementById("tp-matrix-reset-btn");
  if (resetBtn) {
    resetBtn.textContent = isEs ? "Restablecer Filtros ×" : "Reset Volume & Pillar Filters ×";
  }

  const searchInput = document.getElementById("tp-matrix-search");
  if (searchInput) {
    searchInput.setAttribute("placeholder", dict.searchPlaceholder);
  }

  const ogLocale = document.querySelector('meta[property="og:locale"]');
  const ogLocaleAlt = document.querySelector('meta[property="og:locale:alternate"]');
  if (ogLocale) ogLocale.setAttribute("content", isEs ? "es_MX" : "en_US");
  if (ogLocaleAlt) ogLocaleAlt.setAttribute("content", isEs ? "en_US" : "es_MX");

  const dossiers = rootScope.querySelectorAll("details.tp-es-dossier");
  dossiers.forEach((d) => {
    if (isEs) {
      d.open = true;
    }
  });

  if (typeof window !== "undefined" && typeof window.CustomEvent === "function") {
    window.dispatchEvent(new CustomEvent("tp-lang-change", { detail: { isEs } }));
  }
}

export function initThemePlate(scope = document) {
  const plateBtn = document.getElementById("tp-blueprint-toggle");
  if (plateBtn && plateBtn.dataset.bound !== "true") {
    plateBtn.dataset.bound = "true";
    plateBtn.addEventListener("click", () => {
      const root = document.documentElement;
      const isEs = root.lang === "es-MX";
      const dict = isEs ? NAV_LABELS.es : NAV_LABELS.en;
      const isBlueprint = root.getAttribute("data-theme") === "blueprint";
      if (isBlueprint) {
        root.removeAttribute("data-theme");
        root.setAttribute("data-plate-theme", "paper");
        plateBtn.setAttribute("aria-pressed", "false");
        plateBtn.textContent = dict.plateLimestone;
        plateBtn.setAttribute("aria-label", themeLabel(false, isEs));
      } else {
        root.setAttribute("data-theme", "blueprint");
        root.setAttribute("data-plate-theme", "dark");
        plateBtn.setAttribute("aria-pressed", "true");
        plateBtn.textContent = dict.plateBlueprint;
        plateBtn.setAttribute("aria-label", themeLabel(true, isEs));
      }
    });
  }

  if (typeof window !== "undefined" && document.body && document.body.dataset.scrollProgressBound !== "true") {
    document.body.dataset.scrollProgressBound = "true";
    const updateScrollProgress = () => {
      const docEl = document.documentElement;
      const scrollTop = window.scrollY || docEl.scrollTop || 0;
      const maxScroll = Math.max(1, docEl.scrollHeight - docEl.clientHeight);
      const pct = Math.min(100, Math.max(0, (scrollTop / maxScroll) * 100)).toFixed(1) + "%";
      docEl.style.setProperty("--tp-scroll-pct", pct);
    };
    window.addEventListener("scroll", updateScrollProgress, { passive: true });
    updateScrollProgress();
  }

  if (typeof window !== "undefined" && "IntersectionObserver" in window) {
    const rootScope = scope || document;
    const actHeadings = rootScope.querySelectorAll("h2[id^='act']");
    const actPills = rootScope.querySelectorAll(".tp-act-jump-bar .tp-act-pill");
    if (actHeadings.length > 0 && actPills.length > 0) {
      const obs = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting && entry.target.id) {
              const targetHref = "#" + entry.target.id;
              actPills.forEach((p) => {
                p.classList.toggle("is-active", p.getAttribute("href") === targetHref);
              });
            }
          });
        },
        { rootMargin: "-15% 0px -70% 0px", threshold: 0 }
      );
      actHeadings.forEach((h) => obs.observe(h));
    }
  }

  const params = new URLSearchParams(window.location.search);
  const langParam = (params.get("lang") || "").toLowerCase();
  const initialEs = langParam === "es" || langParam === "es-mx" || document.documentElement.lang === "es-MX";
  applyMagazineLanguage(initialEs, scope);

  const langBtn = document.getElementById("tp-lang-toggle");
  if (langBtn && langBtn.dataset.bound !== "true") {
    langBtn.dataset.bound = "true";
    langBtn.addEventListener("click", () => {
      const nextEs = document.documentElement.lang !== "es-MX";
      // Each language has its own address on informatico.ai (Spanish under /es-mx/): go to the one the page names.
      // Anywhere else (a local preview, another host) the alternate is on another origin, so switch in place.
      const alt = document.querySelector('link[rel="alternate"][hreflang="' + (nextEs ? "es-MX" : "en") + '"]');
      if (alt && alt.href) {
        const target = new URL(alt.href, window.location.href);
        if (target.origin === window.location.origin && target.pathname !== window.location.pathname) {
          target.hash = window.location.hash;
          window.location.assign(target.toString());
          return;
        }
      }
      const url = new URL(window.location.href);
      if (nextEs) {
        url.searchParams.set("lang", "es");
      } else {
        url.searchParams.delete("lang");
      }
      window.history.replaceState({}, "", url.toString());
      applyMagazineLanguage(nextEs, document);
      if (nextEs) {
        const firstDossier = document.querySelector("details.tp-es-dossier");
        if (firstDossier) {
          firstDossier.open = true;
        }
      }
    });
  }
}
