// Native Bilingual Article Audio Player Web Component (<tp-article-audio>).
// Zero-build Custom Element (Custom Elements v1) providing a Quanta / Works in Progress /
// Economist-style editorial audio bar for every 5-Act monograph in Informatico.ai.
// Primary engine: Pre-rendered 24 kHz Neural AI (.mp3) decoded via CSP-safe Web Audio API
// (fetch + AudioContext.decodeAudioData under connect-src 'self'; media-src 'none').
// Secondary engine: Upgraded Web Speech API (window.speechSynthesis) with async voiceschanged
// discovery, Neural/Natural/Google voice ranking (penalizing legacy SAPI5 voices), and a
// Scientific & Mathematical Prosody Normalizer in English (en-US) and Mexican Spanish (es-MX).

const SPEEDS = [1.15, 1.35, 1.5, 1.0, 0.85];

const AUDIO_TRACK_PATH_RE = /^((?:\.\.\/){1,5}|\/)audio\/([a-zA-Z0-9_-]+)\.(mp3|ogg|wav|m4a)$/i;
const SAFE_AUDIO_PREFIXES = ["/", "../", "../../", "../../../", "../../../../", "../../../../../"];
const SAFE_AUDIO_EXTS = { mp3: ".mp3", ogg: ".ogg", wav: ".wav", m4a: ".m4a" };

export function sanitizeAudioTrackPath(raw) {
  if (typeof raw !== "string" || !raw) return "";
  const match = AUDIO_TRACK_PATH_RE.exec(raw.trim());
  if (!match) return "";
  const prefix = SAFE_AUDIO_PREFIXES.find((p) => p === match[1]);
  const ext = SAFE_AUDIO_EXTS[match[3].toLowerCase()];
  if (!prefix || !ext) return "";
  const safeStem = encodeURIComponent(match[2]);
  const safeRel = "audio/" + safeStem + ext;
  return prefix + safeRel;
}

const ACT_DEFS = [
  { id: "act-i", selector: '[id^="act1-heading"]', labelEn: "Act I · Story", labelEs: "Acto I · Historia", esIndex: 0 },
  { id: "act-ii", selector: '[id^="act2-heading"]', labelEn: "Act II · Intuition", labelEs: "Acto II · Intuición", esIndex: 0 },
  { id: "act-iii", selector: '[id^="act3-heading"]', labelEn: "Act III · Workbench", labelEs: "Acto III · Laboratorio", esIndex: 1 },
  { id: "act-iv", selector: '[id^="act4-heading"]', labelEn: "Act IV · Discovery", labelEs: "Acto IV · Descubrimiento", esIndex: 1 },
  { id: "act-v", selector: '[id^="act5-heading"]', labelEn: "Act V · Summary", labelEs: "Acto V · Síntesis", esIndex: 2 },
];

const DEFAULT_CHAPTER_OFFSETS = [0.0, 0.21, 0.43, 0.65, 0.84];

const SUBSCRIPT_DIGITS = {
  "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4",
  "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9",
  "₊": "+", "₋": "-", "₌": "=", "₍": "(", "₎": ")",
  "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4",
  "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9",
  "⁺": "+", "⁻": "-",
};

const GREEK_EN = [
  ["ΔΔG", " delta delta G "],
  ["ΔG‡", " delta G double-dagger "],
  ["ΔG", " delta G "],
  ["ΔE", " delta E "],
  ["ΔS", " delta S "],
  ["ΔH", " delta H "],
  ["ΔP", " delta P "],
  ["∇²", " Laplacian "],
  ["∇", " gradient "],
  ["∂", " partial "],
  ["∑", " sum over "],
  ["∏", " product over "],
  ["∫", " integral of "],
  ["∞", " infinity "],
  ["≈", " approximately equals "],
  ["≠", " is not equal to "],
  ["≥", " is greater than or equal to "],
  ["≤", " is less than or equal to "],
  ["∝", " is proportional to "],
  ["→", " yields "],
  ["↔", " is in equilibrium with "],
  ["⇌", " is in reversible equilibrium with "],
  ["±", " plus or minus "],
  ["×", " times "],
  ["μm", " micrometers "],
  ["μM", " micromolar "],
  ["μs", " microseconds "],
  ["Δ", " delta "],
  ["α", " alpha "],
  ["β", " beta "],
  ["γ", " gamma "],
  ["δ", " delta "],
  ["ε", " epsilon "],
  ["ζ", " zeta "],
  ["η", " eta "],
  ["θ", " theta "],
  ["κ", " kappa "],
  ["λ", " lambda "],
  ["μ", " mu "],
  ["ν", " nu "],
  ["ξ", " xi "],
  ["π", " pi "],
  ["ρ", " rho "],
  ["σ", " sigma "],
  ["τ", " tau "],
  ["φ", " phi "],
  ["χ", " chi "],
  ["ψ", " psi "],
  ["ω", " omega "],
  ["Ω", " omega "],
  ["Φ", " phi "],
  ["Ψ", " psi "],
  ["Λ", " lambda "],
];

const GREEK_ES = [
  ["ΔΔG", " delta delta G "],
  ["ΔG‡", " delta G de activación "],
  ["ΔG", " delta G "],
  ["ΔE", " delta E "],
  ["ΔS", " delta S "],
  ["ΔH", " delta H "],
  ["ΔP", " delta P "],
  ["∇²", " laplaciano "],
  ["∇", " gradiente "],
  ["∂", " derivada parcial "],
  ["∑", " suma sobre "],
  ["∏", " producto sobre "],
  ["∫", " integral de "],
  ["∞", " infinito "],
  ["≈", " aproximadamente igual a "],
  ["≠", " distinto de "],
  ["≥", " mayor o igual a "],
  ["≤", " menor o igual a "],
  ["∝", " proporcional a "],
  ["→", " hacia "],
  ["↔", " en equilibrio con "],
  ["⇌", " en equilibrio reversible con "],
  ["±", " más menos "],
  ["×", " por "],
  ["μm", " micrómetros "],
  ["μM", " micromolar "],
  ["μs", " microsegundos "],
  ["Δ", " delta "],
  ["α", " alfa "],
  ["β", " beta "],
  ["γ", " gamma "],
  ["δ", " delta "],
  ["ε", " épsilon "],
  ["ζ", " zeta "],
  ["η", " eta "],
  ["θ", " theta "],
  ["κ", " kappa "],
  ["λ", " lambda "],
  ["μ", " mu "],
  ["ν", " nu "],
  ["ξ", " xi "],
  ["π", " pi "],
  ["ρ", " ro "],
  ["σ", " sigma "],
  ["τ", " tau "],
  ["φ", " fi "],
  ["χ", " ji "],
  ["ψ", " psi "],
  ["ω", " omega "],
  ["Ω", " omega "],
  ["Φ", " fi "],
  ["Ψ", " psi "],
  ["Λ", " lambda "],
];

export function normalizeScientificSpeech(raw, lang = "en") {
  let s = String(raw || "")
    .replace(/\[Scite\s*↗?\]/g, "")
    .replace(/https?:\/\/\S+/g, "")
    .replace(/\b([CEAPMLDGTRBX])\.0(\d)\b/g, "$1 $2")
    .replace(/\b([CEAPMLDGTRBX])\.(\d{2})\b/g, "$1 $2");

  const isEs = String(lang || "en").toLowerCase().startsWith("es");
  if (isEs) {
    s = s
      .replace(/\bppFEV[₁1]\b/g, "porcentaje predicho de F E V uno")
      .replace(/\bFEV[₁1]\b/g, "F E V uno")
      .replace(/\bk_B\s*T\b/g, "k B T")
      .replace(/\bmRNA\b/g, "A R N mensajero")
      .replace(/\btRNA\b/g, "A R N de transferencia")
      .replace(/\bsgRNA\b/g, "A R N guía")
      .replace(/\bCFTR\b/g, "C F T R")
      .replace(/\bF508del\b/g, "F quinientos ocho del")
      .replace(/\bInformatico\.ai\b/gi, "Informático punto A I")
      .replace(/\bsenseiewok\.ai\b/gi, "Sensei Ewok punto A I");
  } else {
    s = s
      .replace(/\bppFEV[₁1]\b/g, "percent predicted F E V 1")
      .replace(/\bFEV[₁1]\b/g, "F E V 1")
      .replace(/\bk_B\s*T\b/g, "k B T")
      .replace(/\bmRNA\b/g, "messenger R N A")
      .replace(/\btRNA\b/g, "transfer R N A")
      .replace(/\bsgRNA\b/g, "single guide R N A")
      .replace(/\bCFTR\b/g, "C F T R")
      .replace(/\bF508del\b/g, "F 508 del")
      .replace(/\bInformatico\.ai\b/gi, "Informatico dot A I")
      .replace(/\bsenseiewok\.ai\b/gi, "Sensei Ewok dot A I");
  }

  const pairs = isEs ? GREEK_ES : GREEK_EN;
  for (let i = 0; i < pairs.length; i += 1) {
    const [sym, spoken] = pairs[i];
    if (s.includes(sym)) {
      s = s.split(sym).join(spoken);
    }
  }

  s = s.replace(/[₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻]/g, (ch) => SUBSCRIPT_DIGITS[ch] || ch);
  s = s
    .replace(/_([a-zA-Z0-9]+)/g, " $1")
    .replace(/−/g, isEs ? " menos " : " minus ")
    .replace(/[·—]/g, ", ")
    .replace(/–/g, isEs ? " a " : " to ")
    .replace(/\|/g, isEs ? ", dado " : ", given ")
    .replace(/[{}[\]]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
  return s;
}

function getActiveLang() {
  const root = document.documentElement;
  if (root.dataset.lang === "es" || (root.getAttribute("lang") || "").toLowerCase().startsWith("es")) {
    return "es";
  }
  return "en";
}

function cleanNarrationText(raw, lang = "en") {
  return normalizeScientificSpeech(raw, lang);
}

function isMobileTouchDevice() {
  if (typeof navigator === "undefined") return false;
  const ua = navigator.userAgent || "";
  return /(android|iphone|ipad|ipod|mobile)/i.test(ua) || (/Macintosh/i.test(ua) && Number(navigator.maxTouchPoints) > 1);
}

export function scoreBrowserVoice(v, langCode) {
  if (!v || !v.lang) return -999;
  const vLang = v.lang.toLowerCase().replace("_", "-");
  const targetPrefix = langCode === "es" ? "es" : "en";
  if (!vLang.startsWith(targetPrefix)) return -999;

  let score = 0;
  const preferredLocale = langCode === "es" ? "es-mx" : "en-us";
  if (vLang === preferredLocale) score += 35;
  else if (langCode === "es" && (vLang === "es-us" || vLang === "es-419" || vLang === "es-es")) score += 22;
  else if (langCode === "en" && (vLang === "en-gb" || vLang === "en-au" || vLang === "en-ca")) score += 20;
  else score += 10;

  const name = String(v.name || "");
  if (/multilingual|natural|neural|online/i.test(name)) score += 110;
  else if (/andrew|ava|brian|emma|jenny|aria|guy|dalia|jorge|elena|paulina|samantha|daniel|siri|premium|enhanced/i.test(name)) score += 85;
  else if (/google/i.test(name)) score += 75;
  else if (v.localService === false) score += 55;
  if (/ava|emma|jenny|aria|dalia|elena|paulina|samantha|monica|female|woman/i.test(name)) score += 40;

  if (isMobileTouchDevice() && v.localService !== false) {
    score += 40;
  }

  // Strongly penalize legacy 1990s SAPI5 / desktop robotic voices so they only run if zero neural/cloud voices exist
  if (/david|zira|mark|sabina|helena|hazel|hedda|hortense|espeak|festival|desktop/i.test(name)) {
    score -= 80;
  }
  return score;
}

export function splitIntoSpeechChunks(text, maxLen = 200) {
  const clean = String(text || "").replace(/\s+/g, " ").trim();
  if (!clean) return [];
  const sentences = clean.split(/(?<=[.!?。])\s+/);
  const chunks = [];
  let buf = "";
  for (let i = 0; i < sentences.length; i += 1) {
    const s = sentences[i].trim();
    if (!s) continue;
    if (s.length <= maxLen) {
      if (!buf) {
        buf = s;
      } else if (buf.length + 1 + s.length <= maxLen) {
        buf += ` ${s}`;
      } else {
        chunks.push(buf);
        buf = s;
      }
    } else {
      if (buf) {
        chunks.push(buf);
        buf = "";
      }
      const words = s.split(/\s+/);
      let piece = "";
      for (let j = 0; j < words.length; j += 1) {
        const w = words[j];
        if (!piece) piece = w;
        else if (piece.length + 1 + w.length <= maxLen) piece += ` ${w}`;
        else {
          chunks.push(piece);
          piece = w;
        }
      }
      if (piece) chunks.push(piece);
    }
  }
  if (buf) chunks.push(buf);
  return chunks;
}

const SAGRADA_ACT_DEFS = [
  { id: "sf-story", selector: "#relay", labelEn: "I · Story & Relay", labelEs: "I · Historia y Relevo" },
  { id: "sf-part1", selector: "#part-1", labelEn: "II · 1882–1926", labelEs: "II · 1882–1926" },
  { id: "sf-part3", selector: "#part-3", labelEn: "III · 1936–2026+", labelEs: "III · 1936–2026+" },
  { id: "sf-arch", selector: "#architects-study", labelEn: "IV · Architects", labelEs: "IV · Arquitectos" },
  { id: "sf-lab", selector: "#part-6", labelEn: "V · Lab & Closing", labelEs: "V · Laboratorio" },
];

const GTI_ACT_DEFS = [
  { id: "cc-relay", selector: "#relay", labelEn: "I · 5 Eras", labelEs: "I · 5 Eras" },
  { id: "cc-moves", selector: "#part-1", labelEn: "II · Mk1–Mk5", labelEs: "II · Mk1–Mk5" },
  { id: "cc-grip", selector: "#part-4", labelEn: "III · Grip & 3D", labelEs: "III · Agarre y 3D" },
  { id: "cc-study", selector: "#engineers-study", labelEn: "IV · Engineers", labelEs: "IV · Ingeniería" },
  { id: "cc-lab", selector: "#part-6", labelEn: "V · Physics Lab", labelEs: "V · Laboratorio" },
];

export function resolveSectionDefs(host) {
  const articleScope = (host && (host.closest("#tp-active-folio-mount") || host.closest("main"))) || document;
  if (articleScope.querySelector(".sf-feature")) {
    return SAGRADA_ACT_DEFS;
  }
  if (articleScope.querySelector(".cc-feature")) {
    return GTI_ACT_DEFS;
  }
  return ACT_DEFS;
}

function localizedText(el, lang) {
  if (!el) return "";
  const attr = lang === "es" ? el.getAttribute("data-es") : el.getAttribute("data-en");
  return attr && attr.trim() ? attr.trim() : el.textContent || "";
}

export function getRankedVoices(langCode) {
  if (typeof window === "undefined" || !("speechSynthesis" in window)) return [];
  const voices = window.speechSynthesis.getVoices() || [];
  return voices
    .map((voice) => ({ voice, score: scoreBrowserVoice(voice, langCode) }))
    .filter((item) => item.score > -500)
    .sort((a, b) => b.score - a.score)
    .map((item) => item.voice);
}

export function pickBestVoice(langCode, preferredURI = "") {
  const ranked = getRankedVoices(langCode);
  if (!ranked.length) return null;
  if (preferredURI) {
    const match = ranked.find((v) => v.voiceURI === preferredURI || v.name === preferredURI);
    if (match) return match;
  }
  return ranked[0];
}

function extractCustomFolioChapters(articleScope, hero, defs, selectors, briefSel, citeCls, lang) {
  const pickMany = (selector) =>
    Array.from(articleScope.querySelectorAll(selector))
      .map((el) => cleanNarrationText(localizedText(el, lang), lang))
      .filter(Boolean);
  const titleTxt = cleanNarrationText(localizedText(hero.querySelector(".tp-h1"), lang), lang);
  const dekTxt = cleanNarrationText(localizedText(hero.querySelector(".tp-standfirst"), lang), lang);
  const briefTxt = cleanNarrationText(localizedText(hero.querySelector(briefSel), lang), lang);
  const openingTxt = pickMany(selectors[0]).join(" ");
  const texts = [
    cleanNarrationText(`${titleTxt}. ${dekTxt} ${briefTxt} ${openingTxt}`, lang),
    cleanNarrationText(pickMany(selectors[1]).join(" ") || openingTxt, lang),
    cleanNarrationText(pickMany(selectors[2]).join(" ") || briefTxt, lang),
    cleanNarrationText(pickMany(selectors[3]).join(" ") || briefTxt, lang),
    cleanNarrationText(pickMany(selectors[4]).join(" ") || `${titleTxt}. ${briefTxt}`, lang),
  ];
  void citeCls;
  return defs.map((act, idx) => ({
    index: idx,
    act,
    text: texts[idx] || cleanNarrationText(`${titleTxt}. ${dekTxt}`, lang),
  }));
}

export function collectChaptersFromScope(host) {
  const articleScope = host.closest("#tp-active-folio-mount") || host.closest("main") || document;
  const hero = host.closest(".tp-hero") || articleScope.querySelector(".tp-hero") || articleScope;
  const lang = getActiveLang();

  if (articleScope.querySelector(".sf-feature")) {
    return extractCustomFolioChapters(
      articleScope,
      hero,
      SAGRADA_ACT_DEFS,
      [
        ".sf-opening p:not(.sf-cite)",
        "#part-1 .sf-part-opener p:not(.sf-cite), #part-1 .sf-card-body, #part-2 .sf-part-opener p:not(.sf-cite), #part-2 .sf-card-body",
        "#part-3 .sf-part-opener p:not(.sf-cite), #part-3 .sf-card-body, #part-4 .sf-part-opener p:not(.sf-cite), #part-4 .sf-card-body",
        "#atelier > .sf-lede, #architects-study > .sf-lede, #architects-study .sf-lineage-card p:not(.sf-cite)",
        "#part-6 > .sf-lede, .sf-closing p:not(.sf-cite)",
      ],
      ".sf-brief",
      "sf-cite",
      lang
    );
  }

  if (articleScope.querySelector(".cc-feature")) {
    return extractCustomFolioChapters(
      articleScope,
      hero,
      GTI_ACT_DEFS,
      [
        ".cc-opening p:not(.cc-cite), #relay .cc-lede",
        "#part-1 .cc-part-opener p:not(.cc-cite), #part-1 .cc-card-body, #part-2 .cc-part-opener p:not(.cc-cite), #part-2 .cc-card-body, #part-3 .cc-part-opener p:not(.cc-cite), #part-3 .cc-card-body",
        "#part-4 .cc-part-opener p:not(.cc-cite), #part-4 .cc-card-body, #part-5 .cc-part-opener p:not(.cc-cite), #part-5 .cc-card-body, #atelier > .cc-lede",
        "#engineers-study > .cc-lede, #engineers-study .cc-lineage-card p:not(.cc-cite), #ghost-race > .cc-lede",
        "#part-6 > .cc-lede, .cc-closing p:not(.cc-cite)",
      ],
      ".cc-brief",
      "cc-cite",
      lang
    );
  }

  const h1 = hero.querySelector(".tp-h1");
  const standfirst = hero.querySelector(".tp-standfirst");
  const whyP = hero.querySelector(".tp-why-matters-lead p");
  const esParas = Array.from(articleScope.querySelectorAll("details.tp-es-dossier .tp-es-body p"));

  if (lang === "es") {
    const titleEs = (h1 && (h1.getAttribute("data-es") || h1.textContent)) || "Monográfico Informático punto A I";
    const subEs = (standfirst && (standfirst.getAttribute("data-es") || standfirst.textContent)) || "";
    const whyEs = (whyP && (whyP.getAttribute("data-es") || whyP.textContent)) || "";
    const p0 = cleanNarrationText(esParas[0] ? esParas[0].textContent : "", "es");
    const p1 = cleanNarrationText(esParas[1] ? esParas[1].textContent : "", "es");
    const p2 = cleanNarrationText(esParas[2] ? esParas[2].textContent : "", "es");

    return [
      {
        index: 0,
        act: ACT_DEFS[0],
        text: cleanNarrationText(`${titleEs}. ${subEs} ${whyEs} ${p0}`, "es"),
      },
      {
        index: 1,
        act: ACT_DEFS[1],
        text: cleanNarrationText(p0 || `${titleEs}. ${subEs}`, "es"),
      },
      {
        index: 2,
        act: ACT_DEFS[2],
        text: cleanNarrationText(p1 || subEs, "es"),
      },
      {
        index: 3,
        act: ACT_DEFS[3],
        text: cleanNarrationText(p1 || whyEs, "es"),
      },
      {
        index: 4,
        act: ACT_DEFS[4],
        text: cleanNarrationText(p2 || `${titleEs}. Edición bilingüe verificada.`, "es"),
      },
    ];
  }

  // English 5-Act extraction from live article DOM
  const titleEn = cleanNarrationText((h1 && (h1.getAttribute("data-en") || h1.textContent)) || "", "en");
  const subEn = cleanNarrationText((standfirst && (standfirst.getAttribute("data-en") || standfirst.textContent)) || "", "en");
  const whyEn = cleanNarrationText((whyP && (whyP.getAttribute("data-en") || whyP.textContent)) || "", "en");

  const prose = articleScope.querySelector(".tp-prose");
  if (!prose) {
    return ACT_DEFS.map((act, idx) => ({
      index: idx,
      act,
      text: cleanNarrationText(`${titleEn}. ${subEn} ${whyEn}`, "en"),
    }));
  }

  const buckets = [[], [], [], [], []];
  let currentBucket = 0;
  Array.from(prose.children).forEach((child) => {
    const id = child.getAttribute("id") || "";
    if (id.startsWith("act1-heading") || id === "act-i-story") currentBucket = 0;
    else if (id.startsWith("act2-heading") || id === "act-ii-intuition") currentBucket = 1;
    else if (id.startsWith("act3-heading") || id === "act-iii-interactive") currentBucket = 2;
    else if (id.startsWith("act4-heading") || id === "act-iv-discovery") currentBucket = 3;
    else if (id.startsWith("act5-heading") || id === "act-v-sources") currentBucket = 4;

    if (
      child.tagName === "H2" ||
      child.tagName === "P" ||
      child.tagName === "BLOCKQUOTE" ||
      child.classList.contains("tp-analogy-box") ||
      child.classList.contains("tp-walkthrough-box") ||
      child.classList.contains("tp-human-potential-box") ||
      child.classList.contains("tp-cf-bridge-box") ||
      child.classList.contains("tp-discovery-news-box")
    ) {
      buckets[currentBucket].push(cleanNarrationText(child.textContent, "en"));
    }
  });

  buckets[0].unshift(cleanNarrationText(`${titleEn}. ${subEn} ${whyEn}`, "en"));

  return ACT_DEFS.map((act, idx) => ({
    index: idx,
    act,
    text: cleanNarrationText(buckets[idx].join(" "), "en") || cleanNarrationText(`${titleEn}. ${subEn}`, "en"),
  }));
}

// Shared decoded AudioBuffer cache across page lifetime
const AUDIO_BUFFER_CACHE = new Map();

function formatTimeSec(sec) {
  const s = Math.max(0, Math.floor(sec || 0));
  const m = Math.floor(s / 60);
  const r = s % 60;
  return `${m}:${r < 10 ? "0" : ""}${r}`;
}

export class TpArticleAudioElement extends HTMLElement {
  static get observedAttributes() {
    return [
      "data-folio",
      "data-reading-time",
      "data-audio-src",
      "data-audio-src-es",
      "data-audio-chapters",
      "data-audio-chapters-es",
    ];
  }

  constructor() {
    super();
    this._playing = false;
    this._paused = false;
    this._loading = false;
    this._loadToken = 0;
    this._speechToken = 0;
    this._speechTimer = 0;
    this._usingMediaEl = false;
    this._unlocked = false;
    this._chapterIndex = 0;
    this._speedIndex = 0;
    this._utterance = null;
    this._audioEl = null;
    this._audioCtx = null;
    this._bufferSource = null;
    this._audioBuffer = null;
    this._bufferStartCtxTime = 0;
    this._bufferOffsetSec = 0;
    this._rafId = 0;
    this._chapters = [];
    this._built = false;
    this._onLangChange = () => this._handleLanguageSwitch();
    this._onVoicesChanged = () => {
      if (this._built) this._syncLabels();
    };
  }

  connectedCallback() {
    if (!this._built) {
      this._buildDOM();
      this._built = true;
    }
    if (typeof window !== "undefined" && "speechSynthesis" in window) {
      try {
        window.speechSynthesis.getVoices();
        if (typeof window.speechSynthesis.addEventListener === "function") {
          window.speechSynthesis.addEventListener("voiceschanged", this._onVoicesChanged);
        }
      } catch (_e) {
        /* ignore speechSynthesis discovery errors */
      }
    }
    this._syncLabels();
    window.addEventListener("tp-lang-change", this._onLangChange);
  }

  disconnectedCallback() {
    this.stop();
    window.removeEventListener("tp-lang-change", this._onLangChange);
    if (typeof window !== "undefined" && "speechSynthesis" in window && typeof window.speechSynthesis.removeEventListener === "function") {
      try {
        window.speechSynthesis.removeEventListener("voiceschanged", this._onVoicesChanged);
      } catch (_e) {
        /* ignore */
      }
    }
  }

  attributeChangedCallback() {
    if (this._built) {
      this.stop();
      this._syncLabels();
    }
  }

  _getNeuralSrc(lang) {
    const raw = this.getAttribute(lang === "es" ? "data-audio-src-es" : "data-audio-src") || "";
    if (!raw) return "";
    let candidate = raw;
    if (
      typeof window !== "undefined" &&
      window.location &&
      window.location.pathname.includes("/es-mx/") &&
      raw.startsWith("../../audio/")
    ) {
      candidate = `../${raw}`;
    }
    return sanitizeAudioTrackPath(candidate);
  }

  _unlockAudioContextSync() {
    if (typeof window === "undefined") return null;
    if (typeof navigator !== "undefined" && navigator.audioSession) {
      try {
        if (navigator.audioSession.type !== "playback") {
          navigator.audioSession.type = "playback";
        }
      } catch (_e) {
        /* ignore if audioSession is read-only */
      }
    }
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (typeof AudioCtx !== "function") return null;
    if (!this._audioCtx) {
      try {
        this._audioCtx = new AudioCtx();
      } catch (_e) {
        return null;
      }
    }
    const ctx = this._audioCtx;
    if (ctx.state === "suspended" || ctx.state === "interrupted") {
      try {
        const p = ctx.resume();
        if (p && typeof p.catch === "function") p.catch(() => {});
      } catch (_e) {
        /* ignore */
      }
    }
    if (!this._unlocked) {
      try {
        const silentBuf = ctx.createBuffer(1, 1, 22050);
        const unlockSource = ctx.createBufferSource();
        unlockSource.buffer = silentBuf;
        unlockSource.connect(ctx.destination);
        unlockSource.start(0);
        this._unlocked = true;
      } catch (_e) {
        /* ignore */
      }
    }
    return ctx;
  }

  _decodeAudioBuffer(ctx, arrayBuf) {
    const copy = arrayBuf.slice(0);
    return new Promise((resolve, reject) => {
      let settled = false;
      const onResolve = (buf) => {
        if (!settled) {
          settled = true;
          resolve(buf);
        }
      };
      const onReject = (err) => {
        if (!settled) {
          settled = true;
          reject(err);
        }
      };
      try {
        const maybePromise = ctx.decodeAudioData(copy, onResolve, onReject);
        if (maybePromise && typeof maybePromise.then === "function") {
          maybePromise.then(onResolve, onReject);
        }
      } catch (err) {
        onReject(err);
      }
    });
  }

  _getChapterRatios(lang) {
    const raw = this.getAttribute(lang === "es" ? "data-audio-chapters-es" : "data-audio-chapters") || "";
    if (raw) {
      const parts = raw
        .split(",")
        .map((x) => parseFloat(x.trim()))
        .filter((n) => Number.isFinite(n) && n >= 0 && n <= 1);
      if (parts.length === ACT_DEFS.length) return parts;
    }
    return DEFAULT_CHAPTER_OFFSETS;
  }

  _buildDOM() {
    while (this.firstChild) {
      this.removeChild(this.firstChild);
    }
    this.classList.add("tp-article-audio");
    this.setAttribute("role", "region");
    this.setAttribute("aria-label", "Article Audio Narrator / Reproductor de Audio Neural del Monográfico");

    const topRow = document.createElement("div");
    topRow.className = "tp-audio-top-row";

    const leftGroup = document.createElement("div");
    leftGroup.className = "tp-audio-controls-left";

    // Play / Pause primary button
    const playBtn = document.createElement("button");
    playBtn.type = "button";
    playBtn.className = "tp-audio-play-btn";
    playBtn.setAttribute("data-audio-action", "toggle");
    playBtn.setAttribute("aria-pressed", "false");

    const playIcon = document.createElement("span");
    playIcon.className = "tp-audio-icon";
    playIcon.setAttribute("aria-hidden", "true");
    playIcon.textContent = "▶";

    const playLabel = document.createElement("span");
    playLabel.className = "tp-audio-play-label";
    playLabel.setAttribute("data-audio-play-label", "");

    playBtn.appendChild(playIcon);
    playBtn.appendChild(playLabel);
    playBtn.addEventListener("click", () => this.togglePlay());

    // Stop button
    const stopBtn = document.createElement("button");
    stopBtn.type = "button";
    stopBtn.className = "tp-audio-util-btn";
    stopBtn.setAttribute("data-audio-action", "stop");
    stopBtn.setAttribute("title", "Stop narration / Detener narración");
    stopBtn.setAttribute("aria-label", "Stop narration");
    stopBtn.textContent = "■";
    stopBtn.addEventListener("click", () => this.stop());

    // Speed cycle button
    const speedBtn = document.createElement("button");
    speedBtn.type = "button";
    speedBtn.className = "tp-audio-util-btn tp-audio-speed-btn";
    speedBtn.setAttribute("data-audio-action", "speed");
    speedBtn.setAttribute("title", "Playback speed / Velocidad de narración");
    speedBtn.textContent = "1.15×";
    speedBtn.addEventListener("click", () => this.cycleSpeed());

    leftGroup.appendChild(playBtn);
    leftGroup.appendChild(stopBtn);
    leftGroup.appendChild(speedBtn);

    // Status & progress group
    const statusGroup = document.createElement("div");
    statusGroup.className = "tp-audio-status-group";

    const statusText = document.createElement("span");
    statusText.className = "tp-audio-status-text";
    statusText.setAttribute("data-audio-status", "");
    statusText.setAttribute("aria-live", "polite");

    const progress = document.createElement("progress");
    progress.className = "tp-audio-progress";
    progress.setAttribute("max", "100");
    progress.setAttribute("value", "0");
    progress.setAttribute("aria-label", "Article narration progress");
    progress.addEventListener("click", (e) => {
      const rect = progress.getBoundingClientRect();
      if (!rect.width) return;
      const frac = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
      if (this._usingMediaEl && this._audioEl && Number.isFinite(this._audioEl.duration) && this._audioEl.duration > 0) {
        const seekSec = frac * this._audioEl.duration;
        this._audioEl.currentTime = seekSec;
        progress.setAttribute("value", String(Math.round(frac * 100)));
        this._syncLabels(seekSec);
        return;
      }
      if (!this._audioBuffer || !this._audioBuffer.duration) return;
      const seekSec = frac * this._audioBuffer.duration;
      if (this._playing && !this._paused) {
        this._unlockAudioContextSync();
        this._startBufferPlayback(seekSec);
      } else {
        this._bufferOffsetSec = seekSec;
        progress.setAttribute("value", String(Math.round(frac * 100)));
        this._syncLabels(seekSec);
      }
    });

    statusGroup.appendChild(statusText);
    statusGroup.appendChild(progress);

    topRow.appendChild(leftGroup);
    topRow.appendChild(statusGroup);

    // 5-Act Chapter Stepper Row
    const defs = resolveSectionDefs(this);
    const chapterRow = document.createElement("div");
    chapterRow.className = "tp-audio-chapters";
    chapterRow.setAttribute("role", "group");
    chapterRow.setAttribute("aria-label", "Jump audio narration by Act");

    this._chapterBtns = defs.map((act, idx) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "tp-audio-chapter-btn";
      btn.setAttribute("data-audio-chapter", String(idx));
      btn.setAttribute("aria-pressed", idx === 0 ? "true" : "false");
      btn.textContent = act.labelEn;
      btn.addEventListener("click", () => this.jumpToChapter(idx));
      chapterRow.appendChild(btn);
      return btn;
    });

    const audioEl = document.createElement("audio");
    audioEl.preload = "none";
    audioEl.hidden = true;
    audioEl.setAttribute("playsinline", "");

    this.appendChild(topRow);
    this.appendChild(chapterRow);
    this.appendChild(audioEl);

    this._playBtn = playBtn;
    this._playIcon = playIcon;
    this._playLabel = playLabel;
    this._speedBtn = speedBtn;
    this._statusText = statusText;
    this._progressEl = progress;
    this._audioEl = audioEl;
  }

  _syncLabels(currentSec = this._bufferOffsetSec) {
    if (!this._built) return;
    const lang = getActiveLang();
    const folioCode = (this.getAttribute("data-folio") || "FOLIO").toUpperCase();
    const readingTime = this.getAttribute("data-reading-time") || "14 MIN";
    const speed = SPEEDS[this._speedIndex];
    this._speedBtn.textContent = `${speed}×`;

    const defs = resolveSectionDefs(this);
    const activeAct = defs[this._chapterIndex] || defs[0];
    const actTitle = lang === "es" ? activeAct.labelEs : activeAct.labelEn;
    const usingNeuralTrack = Boolean(this._getNeuralSrc(lang));
    const engineTag = usingNeuralTrack
      ? lang === "es"
        ? "IA Neural 24 kHz"
        : "Neural AI 24 kHz"
      : lang === "es"
        ? "Voz Natural"
        : "Natural Voice";

    const mediaDur = this._usingMediaEl && this._audioEl && Number.isFinite(this._audioEl.duration) ? this._audioEl.duration : 0;
    const mediaPos = this._usingMediaEl && this._audioEl ? this._audioEl.currentTime || 0 : currentSec;
    const totalSec = mediaDur > 0 ? mediaDur : (this._audioBuffer ? this._audioBuffer.duration : 0);
    const timeStr = totalSec > 0 ? ` · ${formatTimeSec(mediaDur > 0 ? mediaPos : currentSec)} / ${formatTimeSec(totalSec)}` : "";

    if (this._loading) {
      this._playIcon.textContent = "⏳";
      this._playBtn.setAttribute("aria-pressed", "true");
      this._playLabel.textContent = lang === "es" ? "Cargando..." : "Loading...";
      this._statusText.textContent =
        lang === "es"
          ? `Cargando pista de voz IA neural (24 kHz) · ${folioCode}...`
          : `Loading 24 kHz Neural AI voice track · ${folioCode}...`;
    } else if (this._playing && !this._paused) {
      this._playIcon.textContent = "⏸";
      this._playBtn.setAttribute("aria-pressed", "true");
      this._playLabel.textContent = lang === "es" ? "Pausar Audio" : "Pause Audio";
      this._statusText.textContent =
        lang === "es"
          ? `Narrando ${folioCode} (${engineTag} · ES-MX) · ${actTitle}${timeStr}`
          : `Narrating ${folioCode} (${engineTag} · EN-US) · ${actTitle}${timeStr}`;
    } else if (this._paused) {
      this._playIcon.textContent = "▶";
      this._playBtn.setAttribute("aria-pressed", "false");
      this._playLabel.textContent = lang === "es" ? "Reanudar Audio" : "Resume Audio";
      this._statusText.textContent =
        lang === "es"
          ? `En pausa · ${folioCode} · ${actTitle}${timeStr}`
          : `Paused · ${folioCode} · ${actTitle}${timeStr}`;
    } else {
      this._playIcon.textContent = "▶";
      this._playBtn.setAttribute("aria-pressed", "false");
      this._playLabel.textContent =
        lang === "es"
          ? `Escuchar Monográfico (${readingTime.replace("READ", "AUDIO")})`
          : `Listen to Monograph (${readingTime.replace("READ", "AUDIO")})`;
      this._statusText.textContent =
        lang === "es"
          ? `Audio Bilingüe · ES-MX / EN · 5 Secciones (${actTitle})`
          : `Bilingual Audio · EN / ES-MX · 5 Sections (${actTitle})`;
    }

    if (this._chapterBtns) {
      this._chapterBtns.forEach((btn, idx) => {
        const def = defs[idx] || ACT_DEFS[idx];
        btn.textContent = lang === "es" ? def.labelEs : def.labelEn;
        btn.setAttribute("aria-pressed", idx === this._chapterIndex ? "true" : "false");
      });
    }
  }

  _handleLanguageSwitch() {
    const wasPlaying = this._playing && !this._paused;
    this.stop();
    this._audioBuffer = null;
    this._syncLabels();
    if (wasPlaying) {
      this.playChapter(this._chapterIndex);
    }
  }

  togglePlay() {
    if (this._loading) {
      this.stop();
      return;
    }
    if (this._playing && !this._paused) {
      this.pause();
    } else if (this._paused) {
      this.resume();
    } else {
      this.playChapter(this._chapterIndex);
    }
  }

  _stopBufferSource() {
    if (this._rafId) {
      cancelAnimationFrame(this._rafId);
      this._rafId = 0;
    }
    if (this._bufferSource) {
      this._bufferSource.onended = null;
      try {
        this._bufferSource.stop();
      } catch (_e) {
        /* ignore */
      }
      try {
        this._bufferSource.disconnect();
      } catch (_e) {
        /* ignore */
      }
      this._bufferSource = null;
    }
  }

  pause() {
    if (this._loading) {
      this.stop();
      return;
    }
    if (this._usingMediaEl && this._audioEl && this._playing && !this._paused) {
      this._audioEl.pause();
      this._paused = true;
      this._syncLabels(this._audioEl.currentTime || 0);
      return;
    }
    if (this._bufferSource && this._audioCtx && this._playing && !this._paused) {
      const speed = SPEEDS[this._speedIndex];
      const elapsed = (this._audioCtx.currentTime - this._bufferStartCtxTime) * speed;
      this._bufferOffsetSec = Math.min(
        this._audioBuffer ? this._audioBuffer.duration : 0,
        this._bufferOffsetSec + Math.max(0, elapsed)
      );
      this._stopBufferSource();
      this._paused = true;
      this._syncLabels(this._bufferOffsetSec);
      return;
    }
    if (typeof window !== "undefined" && "speechSynthesis" in window && (window.speechSynthesis.speaking || this._playing)) {
      window.speechSynthesis.pause();
      this._paused = true;
      this._syncLabels();
    }
  }

  resume() {
    const lang = getActiveLang();
    if (this._paused && this._usingMediaEl && this._audioEl && this._getNeuralSrc(lang)) {
      this._paused = false;
      this._playing = true;
      const p = this._audioEl.play();
      if (p && typeof p.catch === "function") p.catch(() => {});
      this._syncLabels(this._audioEl.currentTime || 0);
      return;
    }
    if (this._paused && this._audioBuffer && this._getNeuralSrc(lang)) {
      this._unlockAudioContextSync();
      this._paused = false;
      this._playing = true;
      this._startBufferPlayback(this._bufferOffsetSec);
      this._syncLabels(this._bufferOffsetSec);
      return;
    }
    if (typeof window !== "undefined" && "speechSynthesis" in window && this._paused) {
      window.speechSynthesis.resume();
      this._paused = false;
      this._playing = true;
      this._syncLabels();
      return;
    }
    this.playChapter(this._chapterIndex);
  }

  stop() {
    this._loadToken += 1;
    this._speechToken += 1;
    if (this._speechTimer) {
      clearTimeout(this._speechTimer);
      this._speechTimer = 0;
    }
    this._loading = false;
    this._usingMediaEl = false;
    this._stopBufferSource();
    this._bufferOffsetSec = 0;
    if (this._audioEl) {
      this._audioEl.ontimeupdate = null;
      this._audioEl.onended = null;
      this._audioEl.onerror = null;
      this._audioEl.pause();
      try {
        this._audioEl.currentTime = 0;
      } catch (_e) {
        /* ignore before metadata load */
      }
    }
    if (typeof window !== "undefined" && "speechSynthesis" in window) {
      window.speechSynthesis.cancel();
    }
    this._playing = false;
    this._paused = false;
    this._utterance = null;
    if (this._progressEl) {
      this._progressEl.setAttribute("value", "0");
    }
    this._syncLabels(0);
  }

  cycleSpeed() {
    const oldSpeed = SPEEDS[this._speedIndex];
    this._speedIndex = (this._speedIndex + 1) % SPEEDS.length;
    const newSpeed = SPEEDS[this._speedIndex];
    if (this._usingMediaEl && this._audioEl && this._playing) {
      this._audioEl.playbackRate = newSpeed;
      this._syncLabels(this._audioEl.currentTime || 0);
      return;
    }
    if (this._bufferSource && this._audioCtx && this._playing && !this._paused) {
      const elapsed = (this._audioCtx.currentTime - this._bufferStartCtxTime) * oldSpeed;
      this._bufferOffsetSec = Math.min(
        this._audioBuffer ? this._audioBuffer.duration : 0,
        this._bufferOffsetSec + Math.max(0, elapsed)
      );
      this._bufferStartCtxTime = this._audioCtx.currentTime;
      this._bufferSource.playbackRate.value = newSpeed;
      this._syncLabels(this._bufferOffsetSec);
      return;
    }
    this._syncLabels(this._bufferOffsetSec);
    if (this._playing && !this._paused && !this._loading) {
      this.playChapter(this._chapterIndex);
    }
  }

  jumpToChapter(index) {
    const defs = resolveSectionDefs(this);
    const clamped = Math.max(0, Math.min(defs.length - 1, index));
    this._chapterIndex = clamped;
    const actDef = defs[clamped];
    const articleScope = this.closest("#tp-active-folio-mount") || document;
    const targetHeading = articleScope.querySelector(actDef.selector);
    if (targetHeading && typeof targetHeading.scrollIntoView === "function") {
      targetHeading.scrollIntoView({ behavior: "smooth", block: "start" });
    }
    this.playChapter(clamped);
  }

  _startBufferPlayback(offsetSec) {
    if (!this._audioBuffer || !this._audioCtx) return;
    this._stopBufferSource();
    if (this._audioCtx.state === "suspended" || this._audioCtx.state === "interrupted") {
      try {
        const p = this._audioCtx.resume();
        if (p && typeof p.catch === "function") p.catch(() => {});
      } catch (_e) {
        /* ignore */
      }
    }
    const speed = SPEEDS[this._speedIndex];
    const lang = getActiveLang();
    const ratios = this._getChapterRatios(lang);
    const duration = Math.max(0.1, this._audioBuffer.duration);
    const safeOffset = Math.max(0, Math.min(duration - 0.05, offsetSec));

    const source = this._audioCtx.createBufferSource();
    source.buffer = this._audioBuffer;
    source.playbackRate.value = speed;
    source.connect(this._audioCtx.destination);

    this._bufferOffsetSec = safeOffset;
    this._bufferStartCtxTime = this._audioCtx.currentTime;
    this._bufferSource = source;
    this._loading = false;
    this._playing = true;
    this._paused = false;

    const tick = () => {
      if (!this._playing || this._paused || !this._bufferSource) return;
      const curSpeed = SPEEDS[this._speedIndex];
      const posSec = Math.min(
        duration,
        this._bufferOffsetSec + (this._audioCtx.currentTime - this._bufferStartCtxTime) * curSpeed
      );
      const frac = Math.max(0, Math.min(1, posSec / duration));
      if (this._progressEl) {
        this._progressEl.setAttribute("value", String(Math.round(frac * 100)));
      }
      let activeIdx = 0;
      for (let i = ratios.length - 1; i >= 0; i -= 1) {
        if (frac >= ratios[i] - 0.01) {
          activeIdx = i;
          break;
        }
      }
      if (activeIdx !== this._chapterIndex) {
        this._chapterIndex = activeIdx;
      }
      this._syncLabels(posSec);
      if (posSec < duration) {
        this._rafId = requestAnimationFrame(tick);
      }
    };

    source.onended = () => {
      if (!this._playing || this._paused) return;
      this._stopBufferSource();
      this._playing = false;
      this._paused = false;
      this._bufferOffsetSec = 0;
      if (this._progressEl) {
        this._progressEl.setAttribute("value", "100");
      }
      this._syncLabels(0);
    };

    source.start(0, safeOffset);
    this._rafId = requestAnimationFrame(tick);
    this._syncLabels(safeOffset);
  }

  async _playNeuralAudioTrack(src, chapterIndex, lang, token) {
    const ctx = this._audioCtx;
    if (!ctx || typeof window.fetch !== "function") {
      return false;
    }
    try {
      let audioBuffer = AUDIO_BUFFER_CACHE.get(src);
      if (!audioBuffer) {
        const resp = await window.fetch(src);
        if (!resp.ok) return false;
        if (token !== this._loadToken || !this._playing) return false;
        const arrayBuf = await resp.arrayBuffer();
        if (token !== this._loadToken || !this._playing) return false;
        audioBuffer = await this._decodeAudioBuffer(ctx, arrayBuf);
        AUDIO_BUFFER_CACHE.set(src, audioBuffer);
      }
      if (token !== this._loadToken || !this._playing) return false;
      this._audioBuffer = audioBuffer;
      const ratios = this._getChapterRatios(lang);
      const startRatio = ratios[chapterIndex] || 0;
      const offsetSec = startRatio * audioBuffer.duration;
      this._startBufferPlayback(offsetSec);
      return true;
    } catch (_err) {
      return false;
    }
  }

  _playMediaElementTrack(src, chapterIndex, lang, token) {
    const el = this._audioEl;
    const safeSrc = sanitizeAudioTrackPath(src);
    if (!el || !safeSrc || typeof el.play !== "function") return false;
    const speed = SPEEDS[this._speedIndex];
    const ratios = this._getChapterRatios(lang);
    const startRatio = ratios[chapterIndex] || 0;

    this._usingMediaEl = true;
    if (el.getAttribute("src") !== safeSrc) {
      el.setAttribute("src", safeSrc);
    }
    el.playbackRate = speed;

    const applyInitialSeek = () => {
      if (token !== this._loadToken || !this._usingMediaEl) return;
      if (startRatio > 0 && Number.isFinite(el.duration) && el.duration > 0) {
        try {
          el.currentTime = startRatio * el.duration;
        } catch (_e) {
          /* ignore */
        }
      }
    };
    if (el.readyState >= 1) applyInitialSeek();
    else el.addEventListener("loadedmetadata", applyInitialSeek, { once: true });

    el.ontimeupdate = () => {
      if (token !== this._loadToken || !this._playing || this._paused || !this._usingMediaEl) return;
      const dur = Number.isFinite(el.duration) && el.duration > 0 ? el.duration : 0;
      const pos = el.currentTime || 0;
      if (dur > 0) {
        const frac = Math.max(0, Math.min(1, pos / dur));
        if (this._progressEl) this._progressEl.setAttribute("value", String(Math.round(frac * 100)));
        let activeIdx = 0;
        for (let i = ratios.length - 1; i >= 0; i -= 1) {
          if (frac >= ratios[i] - 0.01) {
            activeIdx = i;
            break;
          }
        }
        if (activeIdx !== this._chapterIndex) this._chapterIndex = activeIdx;
      }
      this._syncLabels(pos);
    };

    el.onended = () => {
      if (token !== this._loadToken || !this._playing) return;
      this._playing = false;
      this._paused = false;
      if (this._progressEl) this._progressEl.setAttribute("value", "100");
      this._syncLabels(0);
    };

    el.onerror = () => {
      if (token !== this._loadToken || !this._usingMediaEl) return;
      this._usingMediaEl = false;
      const ctx = this._unlockAudioContextSync();
      if (ctx) {
        this._playNeuralAudioTrack(safeSrc, chapterIndex, lang, token).then((ok) => {
          if (token === this._loadToken && !ok && this._playing) {
            this._playWebSpeechChapter(chapterIndex, lang, SPEEDS[this._speedIndex]);
          }
        });
      } else {
        this._playWebSpeechChapter(chapterIndex, lang, SPEEDS[this._speedIndex]);
      }
    };

    this._loading = false;
    this._playing = true;
    this._paused = false;
    this._syncLabels(0);
    try {
      const p = el.play();
      if (p && typeof p.catch === "function") {
        p.catch(() => {
          if (token === this._loadToken && this._playing) {
            el.onerror();
          }
        });
      }
      return true;
    } catch (_err) {
      this._usingMediaEl = false;
      return false;
    }
  }

  playChapter(index) {
    const defs = resolveSectionDefs(this);
    const clamped = Math.max(0, Math.min(defs.length - 1, index));
    this._chapterIndex = clamped;
    const lang = getActiveLang();
    const speed = SPEEDS[this._speedIndex];
    const isMobileTouch = isMobileTouchDevice();

    this._speechToken += 1;
    if (this._speechTimer) {
      clearTimeout(this._speechTimer);
      this._speechTimer = 0;
    }
    this._stopBufferSource();
    if (this._audioEl) {
      this._audioEl.pause();
    }

    const basePct = Math.round((clamped / defs.length) * 100);
    if (this._progressEl) {
      this._progressEl.setAttribute("value", String(basePct));
    }

    // 1. Primary Engine: Pre-rendered Neural AI .mp3 track
    const customSrc = this._getNeuralSrc(lang);
    if (customSrc) {
      if (typeof window !== "undefined" && "speechSynthesis" in window) {
        window.speechSynthesis.cancel();
      }
      const token = (this._loadToken += 1);
      // On mobile browsers (especially iOS Safari where hardware mute silences Web Audio), prefer native <audio> synchronously inside tap gesture
      if (isMobileTouch && this._playMediaElementTrack(customSrc, clamped, lang, token)) {
        return;
      }
      const ctx = this._unlockAudioContextSync();
      if (ctx) {
        const cached = AUDIO_BUFFER_CACHE.get(customSrc);
        this._usingMediaEl = false;
        this._loading = !cached;
        this._playing = true;
        this._paused = false;
        this._syncLabels(this._bufferOffsetSec);
        this._playNeuralAudioTrack(customSrc, clamped, lang, token).then((ok) => {
          if (token !== this._loadToken) return;
          this._loading = false;
          if (!ok && this._playing) {
            this._playWebSpeechChapter(clamped, lang, speed);
          }
        });
        return;
      }
    }

    // 2. Fallback Web Speech API Synthesis (EN-US / ES-MX) with sentence-chunked queue & Prosody Normalizer
    this._usingMediaEl = false;
    this._playWebSpeechChapter(clamped, lang, speed);
  }

  _playWebSpeechChapter(clamped, lang, speed, forceNoVoice = false) {
    this._chapters = collectChaptersFromScope(this);
    const defs = resolveSectionDefs(this);
    const chapter = this._chapters[clamped] || this._chapters[0];
    const chunks = splitIntoSpeechChunks(chapter ? chapter.text : "", 200);

    if (
      typeof window === "undefined" ||
      !("speechSynthesis" in window) ||
      typeof SpeechSynthesisUtterance === "undefined" ||
      chunks.length === 0
    ) {
      this._playing = true;
      this._paused = false;
      this._syncLabels();
      return;
    }

    const synth = window.speechSynthesis;
    const token = (this._speechToken += 1);
    if (this._speechTimer) {
      clearTimeout(this._speechTimer);
      this._speechTimer = 0;
    }

    if (synth.paused) {
      try {
        synth.resume();
      } catch (_e) {
        /* ignore */
      }
    }
    const wasBusy = Boolean(synth.speaking || synth.pending);
    if (wasBusy) {
      synth.cancel();
    }

    const bestVoice = forceNoVoice ? null : pickBestVoice(lang);
    this._playing = true;
    this._paused = false;
    this._syncLabels();

    const speakChunk = (chunkIdx, retriedDefault) => {
      if (token !== this._speechToken || !this._playing) return;
      if (chunkIdx >= chunks.length) {
        if (clamped + 1 < defs.length) {
          this._chapterIndex = clamped + 1;
          this._playWebSpeechChapter(clamped + 1, lang, SPEEDS[this._speedIndex], retriedDefault);
        } else {
          this._playing = false;
          this._paused = false;
          if (this._progressEl) this._progressEl.setAttribute("value", "100");
          this._syncLabels();
        }
        return;
      }

      const utter = new SpeechSynthesisUtterance(chunks[chunkIdx]);
      utter.rate = SPEEDS[this._speedIndex] || speed;
      utter.pitch = 1.0;
      if (bestVoice && !retriedDefault) {
        utter.voice = bestVoice;
        utter.lang = bestVoice.lang ? bestVoice.lang.replace("_", "-") : (lang === "es" ? "es-MX" : "en-US");
      } else {
        utter.lang = lang === "es" ? "es-MX" : "en-US";
      }

      utter.onend = () => {
        if (token !== this._speechToken || !this._playing) return;
        const frac = (chunkIdx + 1) / chunks.length;
        const totalPct = Math.min(100, Math.round(((clamped + frac) / defs.length) * 100));
        if (this._progressEl) this._progressEl.setAttribute("value", String(totalPct));
        speakChunk(chunkIdx + 1, retriedDefault);
      };

      utter.onerror = (ev) => {
        if (token !== this._speechToken) return;
        const errCode = ev && ev.error ? String(ev.error).toLowerCase() : "";
        if (errCode === "canceled" || errCode === "interrupted") return;
        if (!retriedDefault && bestVoice) {
          speakChunk(chunkIdx, true);
          return;
        }
        this._playing = false;
        this._paused = false;
        this._syncLabels();
      };

      this._utterance = utter;
      synth.speak(utter);
    };

    if (wasBusy) {
      this._speechTimer = setTimeout(() => {
        this._speechTimer = 0;
        speakChunk(0, forceNoVoice);
      }, 45);
    } else {
      speakChunk(0, forceNoVoice);
    }
  }
}

export function initArticleAudio(scope = document) {
  if (typeof window !== "undefined" && "customElements" in window && !customElements.get("tp-article-audio")) {
    customElements.define("tp-article-audio", TpArticleAudioElement);
  }
  const players = scope.querySelectorAll("tp-article-audio");
  players.forEach((p) => {
    if (typeof p._syncLabels === "function") {
      p._syncLabels();
    }
  });
}
