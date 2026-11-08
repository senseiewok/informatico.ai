/**
 * @module main
 * Native ES6 Module entry point for Informatico.ai (/research/).
 * Coordinates theme plates, bilingual Web Component audio player, standalone HTML Folio loading,
 * interactive solvers, per-Folio bilingual crosswords, and SKILL.md companions.
 */
import { initThemePlate } from "./theme-plate.mjs";
import { initPlateSolvers } from "./solvers.mjs";
import { initCompanionAndLedger } from "./companion-ledger.mjs";
import { initFolioRouter } from "./folio-router.mjs";
import { initPlateWebGL } from "./webgl-observatory.mjs";
import { initArticleAudio } from "./article-audio.mjs";
import { initFolioPuzzles } from "./folio-puzzle.mjs";
import { initPhysicsDiscoveryCrucible } from "./physics-discovery-crucible.mjs";

function bootMagazine(scope = document) {
  initThemePlate();
  initArticleAudio(scope);
  initPlateSolvers(scope);
  initCompanionAndLedger(scope);
  initPlateWebGL(scope);
  initFolioPuzzles(scope);
  initPhysicsDiscoveryCrucible(scope);
}

bootMagazine(document);
initFolioRouter((newArticleRoot) => {
  bootMagazine(newArticleRoot);
});
