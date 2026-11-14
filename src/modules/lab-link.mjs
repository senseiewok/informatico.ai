/**
 * @module lab-link
 * Optional masthead link to a copy of this site running on the reader's own machine.
 *
 * Off for every visitor by default. `?lab=<port>` remembers a loopback port for this browser tab
 * only (session storage, so a link someone else crafted cannot outlive the tab) and adds one "Lab"
 * link to the masthead; `?lab=off` forgets it. The port number is the only input:
 * scheme, host and path are fixed in this file, so the link can only ever point at the reader's
 * own loopback address, never at another site. Nothing is fetched and nothing is sent.
 */
const STORAGE_KEY = "informatico.lab.port.v1";
const PARAM = "lab";
const NAV_KEY = "lab";

/** A port is four or five digits between 1024 and 65535. Anything else is rejected. */
export function parseLabPort(value) {
  if (typeof value !== "string" || !/^[0-9]{4,5}$/.test(value)) {
    return null;
  }
  const port = Number(value);
  return port >= 1024 && port <= 65535 ? port : null;
}

/** The only address this module can ever produce. */
export function labHref(port) {
  return `http://127.0.0.1:${port}/`;
}

function readStored(storage) {
  try {
    return storage ? storage.getItem(STORAGE_KEY) : null;
  } catch {
    return null;
  }
}

function writeStored(storage, value) {
  try {
    if (!storage) {
      return;
    }
    if (value === null) {
      storage.removeItem(STORAGE_KEY);
    } else {
      storage.setItem(STORAGE_KEY, String(value));
    }
  } catch {
    /* private mode or blocked storage: the link simply lasts for this page only */
  }
}

/**
 * Decide the port from the query string and the remembered value.
 * Returns a valid port, or null when the link should not be shown.
 */
export function resolveLabPort(search, storage) {
  const params = new URLSearchParams(search || "");
  if (params.has(PARAM)) {
    const raw = params.get(PARAM);
    if (raw === "off") {
      writeStored(storage, null);
      return null;
    }
    const fromQuery = parseLabPort(raw);
    if (fromQuery !== null) {
      writeStored(storage, fromQuery);
      return fromQuery;
    }
  }
  return parseLabPort(readStored(storage));
}

function safeStorage() {
  try {
    return window.sessionStorage;
  } catch {
    return null; /* some browsers throw on the property itself when storage is blocked */
  }
}

/**
 * Never throws: this runs before the rest of the page boots, so any failure here must leave
 * the page exactly as it was.
 */
export function initLabLink(doc = document, loc = window.location, storage = safeStorage()) {
  try {
    const port = resolveLabPort(loc.search, storage);
    if (port === null) {
      return null;
    }
    const nav = doc.querySelector(".tp-masthead .tp-nav");
    if (!nav || nav.querySelector(`[data-tp-nav="${NAV_KEY}"]`)) {
      return null;
    }
    const isEs = (doc.documentElement.getAttribute("lang") || "").toLowerCase().startsWith("es");
    const link = doc.createElement("a");
    link.className = "tp-nav-link";
    link.setAttribute("data-tp-nav", NAV_KEY);
    link.setAttribute("data-en", "Lab");
    link.setAttribute("data-es", "Laboratorio");
    link.setAttribute("rel", "noopener noreferrer");
    link.setAttribute("href", labHref(port));
    link.textContent = isEs ? "Laboratorio" : "Lab";
    nav.append(link);
    return link;
  } catch {
    return null;
  }
}
