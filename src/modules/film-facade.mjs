/**
 * @module film-facade
 * Click-to-play film player for the cover.
 *
 * The page ships a poster and a hidden play button, and no frame. Until the reader presses play nothing
 * is requested from YouTube: no frame, no script, no thumbnail and no preconnect. On the press this module
 * builds one frame for the privacy-enhanced player host and puts it where the button was. From then on
 * YouTube serves the player and applies its own storage and network behavior; this module has no say in that.
 *
 * The video ID is the only input. Scheme, host, path and query are fixed in this file, and the ID is
 * checked against a strict pattern again at click time, so the frame can only ever point at one host.
 * The page's policy (script-src 'self', style-src-attr 'none', Trusted Types with no policy) is kept:
 * elements are made with createElement and setAttribute only, and size comes from a class, never from
 * an inline style.
 */
const EMBED_ORIGIN = "https://www.youtube-nocookie.com";
const EMBED_QUERY = "autoplay=1&rel=0&playsinline=1";
const ID_PATTERN = /^[A-Za-z0-9_-]{11}$/;
const READY_ATTR = "data-film-ready";

/** A YouTube video ID is exactly 11 characters of A-Z a-z 0-9 _ -. Anything else is rejected. */
export function isFilmId(value) {
  return typeof value === "string" && ID_PATTERN.test(value);
}

/** The only address this module can ever produce, or null for a bad ID. */
export function filmEmbedSrc(id) {
  return isFilmId(id) ? `${EMBED_ORIGIN}/embed/${id}?${EMBED_QUERY}` : null;
}

/** Build the player frame. Returns null, and builds nothing, for a bad ID. */
export function createFilmFrame(doc, id, title) {
  const src = filmEmbedSrc(id);
  if (src === null) {
    return null;
  }
  const frame = doc.createElement("iframe");
  frame.setAttribute("class", "tp-film-frame");
  frame.setAttribute("src", src);
  frame.setAttribute("title", title);
  frame.setAttribute("allow", "autoplay; fullscreen");
  frame.setAttribute("referrerpolicy", "strict-origin-when-cross-origin");
  frame.setAttribute("width", "640");
  frame.setAttribute("height", "360");
  frame.setAttribute("tabindex", "0");
  return frame;
}

function frameTitle(facade, isEs) {
  const title = facade.getAttribute(isEs ? "data-title-es" : "data-title-en");
  return title || (isEs ? "Reproductor de video de YouTube" : "YouTube video player");
}

function playFilm(facade, button) {
  const doc = facade.ownerDocument;
  const isEs = (doc.documentElement.getAttribute("lang") || "").toLowerCase().startsWith("es");
  const frame = createFilmFrame(doc, facade.getAttribute("data-yt"), frameTitle(facade, isEs));
  if (frame === null) {
    return null;
  }
  button.replaceWith(frame);
  frame.focus();
  return frame;
}

/**
 * Show the play button on every facade in scope and wire its click. Safe to call again on the same
 * scope. A facade with a bad ID keeps its button hidden, so the plain link beside it stays the only way
 * to the film. Never throws: a failure here must leave the page as it was.
 */
export function initFilmFacade(scope = document) {
  let wired = 0;
  try {
    scope.querySelectorAll(`.tp-film-facade[data-yt]:not([${READY_ATTR}])`).forEach((facade) => {
      const button = facade.querySelector("button.tp-film-play");
      if (!button || !isFilmId(facade.getAttribute("data-yt"))) {
        return;
      }
      facade.setAttribute(READY_ATTR, "");
      button.addEventListener("click", () => playFilm(facade, button), { once: true });
      button.removeAttribute("hidden");
      const figure = facade.closest(".tp-cover-film");
      const privacy = figure ? figure.querySelector(".tp-film-privacy") : null;
      if (privacy) {
        privacy.removeAttribute("hidden");
      }
      wired += 1;
    });
  } catch {
    /* leave the page as it was: the plain link still opens the film */
  }
  return wired;
}
