/**
 * @module main
 * Native ES6 Module entry point for Informatico.ai (/).
 * Coordinates theme plates, bilingual Web Component audio player, standalone HTML Folio loading,
 * interactive solvers, per-Folio bilingual crosswords, SKILL.md companions, and Essay Zero trace-sentence.
 */
import { initThemePlate } from "./theme-plate.mjs";
import { initPlateSolvers } from "./solvers.mjs";
import { initCompanionAndLedger } from "./companion-ledger.mjs";
import { initFolioRouter } from "./folio-router.mjs";
import { initPlateWebGL } from "./webgl-observatory.mjs";
import { initArticleAudio } from "./article-audio.mjs";
import { initFolioPuzzles } from "./folio-puzzle.mjs";
import { initPhysicsDiscoveryCrucible } from "./physics-discovery-crucible.mjs";
import { initGlbViewers } from "./glb-viewer.mjs";
import { initTraceSentence } from "./trace-sentence.mjs";
import { initFeaturedSpotlight } from "./featured-spotlight.mjs";

function bootMagazine(scope = document) {
  initThemePlate();
  initFeaturedSpotlight(scope);
  initArticleAudio(scope);
  initPlateSolvers(scope);
  initCompanionAndLedger(scope);
  initPlateWebGL(scope);
  initFolioPuzzles(scope);
  initPhysicsDiscoveryCrucible(scope);
  initGlbViewers(scope);
  initTraceSentence(scope);
}

bootMagazine(document);
initFolioRouter((newArticleRoot) => {
  bootMagazine(newArticleRoot);
});
