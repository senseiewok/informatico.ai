#!/usr/bin/env python3
"""Magazine CSS bundle and update_informatico_css() generator for Informatico.ai."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
REVAMP_CSS = r"""
/* Informatico.ai navigation & declutter revamp (2026-11): one slim header, Contents dialog, pager, quiet metadata. */
@layer revamp {
  .tp-masthead.tp-masthead-slim {
    padding: 0;
    margin: 0;
    border-bottom: 1px solid var(--tp-rule-strong);
    backdrop-filter: saturate(1.2) blur(6px);
  }

  .tp-masthead-slim .tp-masthead-inner {
    flex-wrap: nowrap;
    height: 3.5rem;
    min-height: 0;
    padding-block: 0;
    gap: 1.25rem;
  }

  .tp-masthead-slim .tp-se-logo {
    width: 2rem;
    height: 2rem;
  }

  .tp-masthead-slim .tp-brand-title {
    font-size: 1rem;
    letter-spacing: 0.04em;
  }

  .tp-masthead-slim .tp-nav {
    flex: 1 1 auto;
    flex-wrap: nowrap;
    justify-content: center;
    gap: 0.25rem;
    overflow: visible;
    width: auto;
  }

  .tp-masthead-slim .tp-nav-link {
    font-family: var(--tp-font-ui, system-ui, sans-serif);
    font-size: 0.92rem;
    letter-spacing: 0;
    text-transform: none;
    padding: 0.5rem 0.75rem;
    border: 0;
    border-radius: 999px;
    background: none;
    color: var(--tp-graphite);
    min-height: 2.5rem;
    display: inline-flex;
    align-items: center;
  }

  .tp-masthead-slim .tp-nav-link:hover {
    color: var(--tp-ink);
    background-color: var(--tp-stone-deep);
  }

  .tp-masthead-slim .tp-nav-link[aria-current="page"] {
    color: var(--tp-ink);
    background-color: var(--tp-stone-deep);
    font-weight: 600;
  }

  .tp-masthead-tools {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    flex-shrink: 0;
  }

  .tp-tool-btn {
    font-family: var(--tp-font-ui, system-ui, sans-serif);
    font-size: 0.88rem;
    min-height: 2.5rem;
    min-width: 2.75rem;
    padding: 0.4rem 0.8rem;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.45rem;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 999px;
    background-color: var(--tp-vellum);
    color: var(--tp-ink);
    cursor: pointer;
  }

  .tp-tool-btn:hover {
    border-color: var(--tp-ink);
  }

  .tp-contents-btn {
    background-color: var(--tp-ink);
    color: var(--tp-vellum);
    border-color: var(--tp-ink);
  }

  .tp-contents-btn:hover {
    opacity: 0.9;
  }

  .tp-contents-icon {
    width: 0.95rem;
    height: 0.7rem;
    border-block: 2px solid currentColor;
    position: relative;
  }

  .tp-contents-icon::after {
    content: "";
    position: absolute;
    left: 0;
    right: 0;
    top: 50%;
    border-top: 2px solid currentColor;
    transform: translateY(-50%);
  }

  @media (max-width: 860px) {
    .tp-masthead-slim .tp-nav {
      display: none;
    }

    .tp-masthead-slim .tp-masthead-inner {
      justify-content: space-between;
    }
  }

  @media (max-width: 420px) {
    .tp-contents-btn [data-en] {
      position: absolute;
      width: 1px;
      height: 1px;
      overflow: hidden;
      clip-path: inset(50%);
      white-space: nowrap;
    }

    .tp-masthead-slim .tp-brand-title {
      font-size: 0.92rem;
    }
  }

  /* Contents dialog */
  .tp-contents {
    width: min(1180px, calc(100vw - 2rem));
    max-height: min(86vh, 920px);
    padding: 0;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 14px;
    background-color: var(--tp-vellum);
    color: var(--tp-ink);
    box-shadow: 0 24px 64px color-mix(in srgb, var(--tp-ink) 28%, transparent);
  }

  .tp-contents::backdrop {
    background-color: color-mix(in srgb, var(--tp-ink) 55%, transparent);
  }

  .tp-contents-inner {
    padding: 1.25rem clamp(1rem, 2.5vw, 2rem) 1.75rem;
  }

  .tp-contents-head {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    position: sticky;
    top: 0;
    padding-block: 0.25rem 1rem;
    background-color: var(--tp-vellum);
    z-index: 1;
  }

  .tp-contents-head h2 {
    margin: 0;
    font-family: var(--font-display, Georgia, serif);
    font-size: 1.5rem;
  }

  .tp-contents-search {
    flex: 1 1 auto;
    min-height: 2.6rem;
    padding: 0.5rem 0.9rem;
    font: inherit;
    font-size: 1rem;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 999px;
    background-color: var(--tp-stone);
    color: var(--tp-ink);
  }

  .tp-contents-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 1.5rem;
  }

  .tp-contents-col h3 {
    margin: 0 0 0.6rem;
    font-size: 1rem;
  }

  .tp-contents-col h3 a {
    color: var(--tp-ink);
    text-decoration: none;
    border-bottom: 2px solid var(--tp-minium);
  }

  .tp-contents-col ol {
    list-style: none;
    margin: 0;
    padding: 0;
    display: grid;
    gap: 0.1rem;
  }

  .tp-contents-col li a {
    display: grid;
    grid-template-columns: 3.1rem minmax(0, 1fr);
    gap: 0.4rem;
    padding: 0.45rem 0.4rem;
    border-radius: 8px;
    color: var(--tp-ink);
    text-decoration: none;
    font-size: 0.92rem;
    line-height: 1.3;
  }

  .tp-contents-col li a:hover,
  .tp-contents-col li a:focus-visible {
    background-color: var(--tp-stone-deep);
  }

  .tp-contents-col li a[aria-current="page"] {
    background-color: var(--tp-stone-deep);
    font-weight: 600;
  }

  .tp-contents-id {
    font-family: var(--tp-font-mono, monospace);
    font-size: 0.78rem;
    color: var(--tp-slate);
    padding-top: 0.1rem;
  }

  .tp-contents-title {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .tp-contents-empty {
    color: var(--tp-graphite);
  }

  @media (max-width: 980px) {
    .tp-contents-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 600px) {
    .tp-contents {
      width: 100vw;
      max-width: 100vw;
      height: 100dvh;
      max-height: 100dvh;
      margin: 0;
      border-radius: 0;
    }

    .tp-contents-grid {
      grid-template-columns: 1fr;
    }

    .tp-contents-head {
      flex-wrap: wrap;
    }

    .tp-contents-search {
      order: 3;
      flex-basis: 100%;
    }

    .tp-contents-close {
      margin-left: auto;
    }
  }

  /* Breadcrumb: one quiet line */
  .tp-breadcrumb-bar {
    position: static;
    background: none;
    border: 0;
    padding: 1rem 0 0;
  }

  .tp-breadcrumb-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    list-style: none;
    margin: 0;
    padding: 0;
    font-size: 0.86rem;
    color: var(--tp-slate);
  }

  .tp-breadcrumb-list .tp-crumb-item + .tp-crumb-item::before {
    content: "›";
    margin-right: 0.35rem;
    color: var(--tp-slate);
  }

  .tp-breadcrumb-list .tp-crumb-link {
    color: var(--tp-graphite);
    text-decoration: none;
  }

  .tp-breadcrumb-list .tp-crumb-link:hover {
    text-decoration: underline;
  }

  /* Calmer type: kickers are small but not shouted */
  .tp-body .tp-kicker {
    font-family: var(--tp-font-ui, system-ui, sans-serif);
    font-size: 0.82rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }

  /* Cover — Swiss Above-the-Fold 6-Track & Bounty Architecture */
  .tp-cover-hero {
    display: grid;
    grid-template-columns: minmax(0, 1.18fr) minmax(0, 0.82fr);
    gap: 1.15rem clamp(1.25rem, 2.8vw, 2.5rem);
    align-items: center;
    padding: clamp(0.95rem, 1.8vw, 1.35rem) 0 clamp(0.95rem, 1.8vw, 1.25rem);
    border-bottom: 1px solid var(--tp-rule-strong);
  }

  .tp-cover-hero .tp-h1 {
    font-size: clamp(1.72rem, 2.55vw, 2.45rem);
    line-height: 1.1;
    margin: 0.2rem 0 0.45rem;
    max-width: 24ch;
  }

  .tp-cover-hero .tp-standfirst {
    font-size: clamp(0.94rem, 1.1vw, 1.05rem);
    line-height: 1.44;
    margin: 0;
    max-width: 56ch;
  }

  .tp-cover-figure {
    margin: 0;
  }

  .tp-cover-figure img {
    display: block;
    width: 100%;
    max-height: 205px;
    height: auto;
    aspect-ratio: 16 / 9;
    object-fit: cover;
    border-radius: 10px;
    background-color: var(--tp-stone-deep);
  }

  .tp-cover-figure figcaption {
    margin-top: 0.35rem;
    font-size: 0.76rem;
    line-height: 1.32;
    color: var(--tp-slate);
  }

  .tp-cover-ctas {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 0.85rem;
  }

  .tp-cta {
    display: inline-flex;
    align-items: center;
    min-height: 2.45rem;
    padding: 0.42rem 0.95rem;
    border-radius: 999px;
    border: 1px solid var(--tp-ink);
    background-color: transparent;
    color: var(--tp-ink);
    font: inherit;
    font-size: 0.88rem;
    font-weight: 600;
    text-decoration: none;
    cursor: pointer;
  }

  .tp-cta-primary {
    background-color: var(--tp-ink);
    color: var(--tp-vellum);
  }

  .tp-cta-bounty {
    border-color: var(--tp-prussian);
    background-color: var(--tp-prussian-soft);
    color: var(--tp-prussian);
  }

  .tp-cta-bounty:hover {
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
  }

  /* Above-the-Fold 6-Track & Skills Navigator Strip */
  .tp-cover-track-strip {
    grid-column: 1 / -1;
    display: grid;
    grid-template-columns: repeat(6, minmax(0, 1fr));
    gap: 0.55rem;
    padding-top: 0.65rem;
    border-top: 1px solid var(--tp-rule);
  }

  .tp-track-chip {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 0.18rem;
    padding: 0.52rem 0.68rem;
    border-radius: 8px;
    border: 1px solid var(--tp-rule-strong);
    background-color: var(--tp-vellum);
    color: var(--tp-ink);
    text-decoration: none;
    min-width: 0;
    transition: border-color 0.15s ease, transform 0.15s ease;
  }

  .tp-track-chip:hover {
    border-color: var(--tp-prussian);
  }

  .tp-track-chip-bounty {
    border-color: var(--tp-verdigris);
    background-color: color-mix(in srgb, var(--tp-verdigris) 8%, var(--tp-vellum));
  }

  .tp-track-chip-kicker {
    font-family: var(--font-mono, monospace);
    font-size: 0.66rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: var(--tp-prussian);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .tp-track-chip-bounty .tp-track-chip-kicker {
    color: var(--tp-verdigris);
  }

  .tp-track-chip-toolchain {
    background: linear-gradient(135deg, var(--tp-vellum) 0%, var(--tp-prussian-soft) 100%);
    border-color: var(--tp-minium);
  }

  .tp-track-chip-toolchain .tp-track-chip-kicker {
    color: var(--tp-minium);
  }

  .tp-toolchain-boundary-banner {
    margin: 1rem 0 1.35rem;
    padding: 0.85rem 1.1rem;
    border: 1.5px solid var(--tp-minium);
    border-left-width: 5px;
    border-radius: 8px;
    background-color: var(--tp-stone);
    color: var(--tp-ink);
    font-size: 0.88rem;
    line-height: 1.5;
  }

  .tp-toolchain-boundary-banner strong {
    font-family: var(--font-mono, monospace);
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--tp-minium);
    display: block;
    margin-bottom: 0.25rem;
  }

  .tp-glb-viewer {
    margin: 1.25rem 0;
    padding: 1rem;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 10px;
    background-color: var(--tp-stone);
  }

  .tp-glb-toolbar {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 0.6rem;
    margin-bottom: 0.65rem;
  }

  .tp-glb-status {
    font-family: var(--font-mono, monospace);
    font-size: 0.76rem;
    font-weight: 600;
    color: var(--tp-prussian);
  }

  .tp-glb-canvas {
    width: 100%;
    height: 320px;
    display: block;
    border-radius: 8px;
    border: 1px solid var(--tp-rule);
    background-color: var(--tp-vellum);
    cursor: grab;
    touch-action: none;
  }

  .tp-glb-canvas:active {
    cursor: grabbing;
  }

  .tp-toolchain-files-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 0.75rem;
    margin: 1rem 0;
  }

  .tp-toolchain-file-card {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
    padding: 0.75rem 0.9rem;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 8px;
    background-color: var(--tp-vellum);
    text-decoration: none;
    color: var(--tp-ink);
    transition: border-color 0.15s ease;
  }

  .tp-toolchain-file-card:hover {
    border-color: var(--tp-prussian);
  }

  .tp-toolchain-file-fmt {
    font-family: var(--font-mono, monospace);
    font-size: 0.7rem;
    font-weight: 700;
    color: var(--tp-verdigris);
  }

  .tp-toolchain-file-name {
    font-family: var(--font-mono, monospace);
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--tp-prussian);
  }

  .tp-toolchain-file-meta {
    font-family: var(--font-mono, monospace);
    font-size: 0.68rem;
    color: var(--tp-graphite);
    overflow-wrap: anywhere;
  }

  .tp-small-studio-box {
    margin: 1.15rem 0;
    padding: 1rem 1.2rem;
    border: 1px solid var(--tp-verdigris);
    border-left-width: 4px;
    border-radius: 8px;
    background-color: var(--tp-vellum);
  }

  .tp-small-studio-kicker {
    font-family: var(--font-mono, monospace);
    font-size: 0.73rem;
    font-weight: 700;
    color: var(--tp-verdigris);
    text-transform: uppercase;
    letter-spacing: 0.04em;
    display: block;
    margin-bottom: 0.3rem;
  }

  .tp-track-chip-title {
    font-family: var(--font-display, Georgia, serif);
    font-size: 0.88rem;
    font-weight: 700;
    line-height: 1.2;
    color: var(--tp-ink);
  }

  .tp-track-chip-meta {
    font-family: var(--tp-font-ui, system-ui, sans-serif);
    font-size: 0.72rem;
    color: var(--tp-graphite);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .tp-cover-pillar {
    padding: clamp(1.1rem, 2vw, 1.65rem) 0;
    border-bottom: 1px solid var(--tp-rule);
  }

  .tp-cover-pillar-head {
    display: grid;
    grid-template-columns: minmax(0, 1fr) auto;
    column-gap: 1.5rem;
    align-items: end;
    margin-bottom: 0.8rem;
  }

  .tp-cover-pillar-head .tp-kicker,
  .tp-cover-pillar-head .tp-h2,
  .tp-cover-hook {
    grid-column: 1;
  }

  .tp-cover-pillar-head .tp-h2 {
    margin: 0 0 0.25rem;
    font-size: clamp(1.38rem, 2.1vw, 1.85rem);
  }

  .tp-cover-pillar-head .tp-h2 a {
    color: inherit;
    text-decoration: none;
  }

  .tp-cover-hook {
    margin: 0;
    max-width: 72ch;
    color: var(--tp-graphite);
    font-size: 0.96rem;
    line-height: 1.42;
  }

  .tp-cover-more {
    grid-column: 2;
    grid-row: 1 / span 3;
    align-self: end;
    white-space: nowrap;
    color: var(--tp-ink);
    font-weight: 600;
    text-decoration: none;
    border-bottom: 2px solid var(--tp-minium);
  }

  .tp-cover-row {
    display: grid;
    grid-auto-flow: column;
    grid-auto-columns: minmax(250px, 1fr);
    gap: 1rem;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    padding-bottom: 0.75rem;
    scrollbar-width: thin;
  }

  .tp-cover-row > .tp-rack-card {
    scroll-snap-align: start;
  }

  @media (min-width: 1280px) {
    .tp-cover-row {
      grid-auto-flow: row;
      grid-template-columns: repeat(5, minmax(0, 1fr));
      overflow: visible;
    }
  }

  @media (max-width: 1120px) {
    .tp-cover-track-strip {
      grid-template-columns: repeat(3, minmax(0, 1fr));
    }
  }

  @media (max-width: 860px) {
    .tp-cover-hero {
      grid-template-columns: 1fr;
      gap: 0.85rem;
      padding: 0.85rem 0 1rem;
    }

    .tp-cover-copy {
      order: 1;
    }

    .tp-cover-track-strip {
      order: 2;
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .tp-cover-figure {
      order: 3;
    }

    .tp-cover-figure img {
      max-height: 175px;
    }

    .tp-cover-pillar-head {
      grid-template-columns: 1fr;
    }

    .tp-cover-more {
      grid-column: 1;
      grid-row: auto;
      justify-self: start;
      margin-top: 0.5rem;
    }

    .tp-cover-row {
      grid-auto-columns: 78%;
    }
  }

  /* Cards: image, id + time, title, two-line deck */
  .tp-body .tp-rack-card {
    padding: 0;
    gap: 0;
    border-radius: 12px;
    overflow: hidden;
    justify-content: flex-start;
    background-color: var(--tp-vellum);
    border: 1px solid var(--tp-rule);
  }

  .tp-body .tp-rack-card:hover {
    border-color: var(--tp-ink);
  }

  .tp-body .tp-rack-thumb-wrap {
    display: block;
    width: 100%;
    aspect-ratio: 16 / 9;
    background-color: var(--tp-stone-deep);
    overflow: hidden;
  }

  .tp-body .tp-rack-thumb {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .tp-body .tp-rack-top {
    display: flex;
    justify-content: space-between;
    width: 100%;
    padding: 0.8rem 0.95rem 0;
    font-size: 0.8rem;
    color: var(--tp-slate);
  }

  .tp-body .tp-rack-id {
    font-family: var(--tp-font-mono, monospace);
    color: var(--tp-minium);
  }

  .tp-body .tp-rack-badge {
    border: 0;
    padding: 0;
    background: none;
    font-family: var(--tp-font-ui, system-ui, sans-serif);
    font-size: 0.8rem;
    text-transform: none;
    letter-spacing: 0;
  }

  .tp-body .tp-rack-title {
    padding: 0.35rem 0.95rem 0;
    font-family: var(--font-display, Georgia, serif);
    font-size: 1.06rem;
    line-height: 1.25;
  }

  .tp-rack-dek {
    padding: 0.4rem 0.95rem 1rem;
    font-size: 0.88rem;
    line-height: 1.4;
    color: var(--tp-graphite);
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  /* Pillar hub */
  .tp-pillar-hero {
    padding: clamp(1.25rem, 4vw, 3rem) 0 clamp(1.5rem, 3vw, 2.25rem);
  }

  .tp-pillar-hero .tp-standfirst {
    max-width: 62ch;
    font-size: clamp(1.06rem, 1.4vw, 1.25rem);
  }

  .tp-page-hub .tp-issue-rack {
    border: 0;
    padding: 0 0 2rem;
    background: none;
  }

  .tp-page-hub .tp-rack-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 1.1rem;
  }

  /* Folio: hero, lead image, one act bar */
  .tp-page-folio .tp-hero {
    padding-top: clamp(1rem, 3vw, 2rem);
    border-bottom: 0;
  }

  .tp-page-folio .tp-why-matters-lead {
    max-width: 68ch;
  }

  .tp-editorial-figure[data-lead-figure] {
    margin: 1.5rem 0 0;
  }

  .tp-editorial-figure[data-lead-figure] .tp-editorial-img {
    width: 100%;
    height: auto;
    border-radius: 12px;
    background-color: var(--tp-stone-deep);
  }

  .tp-body .tp-act-jump-bar {
    position: sticky;
    top: calc(3.5rem + 1px);
    z-index: 30;
    flex-wrap: nowrap;
    overflow-x: auto;
    scrollbar-width: none;
    margin: 1.25rem 0 0;
    padding: 0.5rem 0;
    border-top: 1px solid var(--tp-rule);
    border-bottom: 1px solid var(--tp-rule);
    background-color: var(--tp-stone);
  }

  .tp-body .tp-act-jump-bar::-webkit-scrollbar {
    display: none;
  }

  .tp-body .tp-act-pill {
    flex-shrink: 0;
    min-height: 2.25rem;
    font-family: var(--tp-font-ui, system-ui, sans-serif);
    font-size: 0.86rem;
    letter-spacing: 0;
    text-transform: none;
    border-radius: 999px;
  }

  .tp-page-folio [id^="act"] {
    scroll-margin-top: 7.5rem;
  }

  .tp-chronology th[scope="row"],
  .tp-chronology thead th:first-child {
    min-width: 4.5rem;
    white-space: nowrap;
  }

  .tp-sources-list .tp-scite-badge-link {
    display: none;
  }

  @media (max-width: 860px) {
    .tp-body .tp-act-jump-bar {
      mask-image: linear-gradient(to right, var(--tp-ink) 85%, transparent);
      padding-right: 2rem;
    }
  }

  .tp-body tp-article-audio .tp-audio-chapters {
    display: none;
  }

  html:not([lang="es-MX"]) .tp-es-dossier {
    display: none;
  }

  /* Builders' disclosure at the end */
  .tp-method-disclosure {
    margin: 2rem 0 0;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 12px;
    background-color: var(--tp-vellum);
  }

  .tp-method-summary {
    cursor: pointer;
    padding: 1rem 1.25rem;
    font-weight: 600;
    min-height: 2.75rem;
  }

  .tp-method-body {
    padding: 0 1.25rem 1.25rem;
    display: grid;
    gap: 1.25rem;
  }

  /* Pager */
  .tp-pager {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
    margin: 2.5rem 0 0.75rem;
  }

  .tp-pager-link {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
    padding: 1.1rem 1.25rem;
    min-height: 5.5rem;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 12px;
    background-color: var(--tp-vellum);
    color: var(--tp-ink);
    text-decoration: none;
  }

  .tp-pager-link:hover {
    border-color: var(--tp-ink);
  }

  .tp-pager-next {
    text-align: right;
  }

  .tp-pager-empty {
    visibility: hidden;
  }

  .tp-pager-dir {
    font-size: 0.82rem;
    color: var(--tp-slate);
  }

  .tp-pager-link strong {
    font-family: var(--font-display, Georgia, serif);
    font-size: 1.08rem;
    line-height: 1.3;
  }

  .tp-pager-all {
    margin: 0 0 2rem;
  }

  .tp-pager-all a {
    color: var(--tp-ink);
    font-weight: 600;
  }

  @media (max-width: 640px) {
    .tp-pager {
      grid-template-columns: 1fr;
    }

    .tp-pager-next {
      text-align: left;
    }

    .tp-pager-empty {
      display: none;
    }
  }

  /* One footer */
  .tp-site-footer {
    display: grid;
    gap: 0.5rem;
    padding: 2rem 0 1rem;
    margin-top: 1rem;
    border-top: 1px solid var(--tp-rule-strong);
    font-family: var(--tp-font-ui, system-ui, sans-serif);
    font-size: 0.9rem;
    color: var(--tp-graphite);
  }

  .tp-site-footer p {
    margin: 0;
  }

  .tp-site-footer a {
    color: var(--tp-ink);
  }

  /* ---- Layer 5 Art of the Possible SVG Generative Overlays ---- */
  .tp-svg-art-possible-layer {
    pointer-events: none;
  }
  .tp-svg-precision-loupe,
  .tp-svg-phase-attractor-group,
  .tp-svg-quantum-wef-bridge {
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.22s ease, visibility 0.22s ease;
  }
  .tp-plate.is-svg-loupe-active .tp-svg-precision-loupe,
  .tp-plate.is-svg-attractor-active .tp-svg-phase-attractor-group,
  .tp-plate.is-svg-quantum-wef-active .tp-svg-quantum-wef-bridge {
    opacity: 1;
    visibility: visible;
  }
  .tp-svg-proof-dag-edge {
    stroke-dasharray: 6 4;
  }
  .tp-plate.is-svg-knockout-active .tp-svg-art-possible-layer {
    opacity: 1;
  }
  @media (prefers-reduced-motion: no-preference) {
    .tp-svg-proof-dag-edge,
    .tp-svg-phase-attractor {
      animation: tpSvgDashFlow 12s linear infinite;
    }
  }

  /* ---- Open-Bounty & Prize Crucible Special Feature + Standalone Bounty Folios ---- */
  .tp-bounty-crucible {
    margin: 2.75rem 0;
    padding: 1.75rem;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 10px;
    background-color: var(--tp-vellum);
    scroll-margin-top: 5rem;
    box-sizing: border-box;
    max-width: 100%;
    overflow: hidden;
  }
  .tp-bounty-header {
    max-width: 78ch;
    margin-bottom: 1.25rem;
  }
  .tp-bounty-svg-wrap {
    margin: 1rem 0 1.25rem;
    overflow-x: auto;
    max-width: 100%;
  }
  .tp-bounty-crucible-svg {
    width: 100%;
    height: auto;
    display: block;
  }
  .tp-bounty-filter-bar {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 0 0 1.25rem;
    padding: 0.65rem 0.85rem;
    border: 1px solid var(--tp-rule);
    border-radius: 8px;
    background-color: var(--tp-stone);
  }
  .tp-bounty-filter-btn {
    appearance: none;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 999px;
    background-color: var(--tp-vellum);
    color: var(--tp-ink);
    font-family: var(--font-mono, monospace);
    font-size: 0.75rem;
    font-weight: 600;
    padding: 0.36rem 0.8rem;
    cursor: pointer;
    transition: background-color 0.16s ease, color 0.16s ease, border-color 0.16s ease;
  }
  .tp-bounty-filter-btn:hover {
    border-color: var(--tp-prussian);
  }
  .tp-bounty-filter-btn[aria-pressed="true"] {
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
    border-color: var(--tp-prussian);
  }
  .tp-bounty-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1.25rem;
    width: 100%;
  }
  @media (max-width: 1180px) {
    .tp-bounty-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }
  @media (max-width: 720px) {
    .tp-bounty-grid {
      grid-template-columns: minmax(0, 1fr);
      gap: 1rem;
    }
  }
  .tp-bounty-card {
    padding: 1.2rem;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 10px;
    background-color: var(--tp-stone);
    color: var(--tp-ink);
    display: flex;
    flex-direction: column;
    gap: 0.68rem;
    min-width: 0;
    max-width: 100%;
    box-sizing: border-box;
    scroll-margin-top: 5rem;
  }
  .tp-bounty-card[hidden] {
    display: none;
  }
  .tp-bounty-card-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 0.45rem;
    flex-wrap: wrap;
    min-width: 0;
  }
  .tp-bounty-badge {
    font-family: var(--font-mono, monospace);
    font-size: 0.7rem;
    font-weight: 700;
    padding: 0.2rem 0.52rem;
    border-radius: 4px;
    background-color: var(--tp-prussian-soft);
    color: var(--tp-prussian);
    overflow-wrap: anywhere;
  }
  .tp-bounty-pillar {
    font-family: var(--font-mono, monospace);
    font-size: 0.71rem;
    color: var(--tp-verdigris);
    font-weight: 600;
  }
  .tp-bounty-title {
    font-size: 1.05rem;
    line-height: 1.3;
    margin: 0;
    color: var(--tp-ink);
  }
  .tp-bounty-title a {
    color: inherit;
    text-decoration: none;
  }
  .tp-bounty-title a:hover {
    text-decoration: underline;
  }
  .tp-bounty-spec-strip {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 0.4rem;
    padding: 0.42rem 0.6rem;
    border-radius: 6px;
    background-color: var(--tp-vellum);
    border: 1px solid var(--tp-rule);
    min-width: 0;
  }
  .tp-bounty-eq {
    font-family: var(--font-mono, monospace);
    font-size: 0.72rem;
    color: var(--tp-prussian);
    font-weight: 600;
    overflow-wrap: anywhere;
    word-break: break-word;
    min-width: 0;
  }
  .tp-bounty-pass-pill {
    font-family: var(--font-mono, monospace);
    font-size: 0.68rem;
    font-weight: 700;
    color: var(--tp-verdigris);
    white-space: nowrap;
  }
  .tp-bounty-body {
    font-size: 0.9rem;
    line-height: 1.54;
    margin: 0;
    flex-grow: 1;
    color: var(--tp-ink-soft);
    overflow-wrap: break-word;
  }
  .tp-bounty-card-actions {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    padding-top: 0.6rem;
    border-top: 1px solid var(--tp-rule);
    min-width: 0;
  }
  .tp-bounty-story-cta {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.5rem 0.85rem;
    border-radius: 7px;
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
    font-family: var(--tp-font-ui, system-ui, sans-serif);
    font-size: 0.84rem;
    font-weight: 600;
    text-decoration: none;
    text-align: center;
    transition: opacity 0.15s ease;
  }
  .tp-bounty-story-cta:hover {
    opacity: 0.92;
  }
  .tp-bounty-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    min-width: 0;
  }
  .tp-bounty-folio-pill,
  .tp-bounty-ext-pill {
    display: inline-flex;
    align-items: center;
    padding: 0.22rem 0.52rem;
    border-radius: 5px;
    font-family: var(--font-mono, monospace);
    font-size: 0.71rem;
    font-weight: 600;
    text-decoration: none;
    line-height: 1.28;
    max-width: 100%;
    overflow-wrap: anywhere;
  }
  .tp-bounty-folio-pill {
    background-color: var(--tp-prussian-soft);
    color: var(--tp-prussian);
    border: 1px solid var(--tp-rule-strong);
  }
  .tp-bounty-folio-pill:hover {
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
  }
  .tp-bounty-ext-pill {
    background-color: var(--tp-vellum);
    color: var(--tp-verdigris);
    border: 1px solid var(--tp-rule);
  }
  .tp-bounty-ext-pill:hover {
    border-color: var(--tp-verdigris);
  }
  .tp-bounty-links {
    font-size: 0.8rem;
    line-height: 1.48;
    margin: 0;
    padding-top: 0.45rem;
    border-top: 1px dashed var(--tp-rule);
    overflow-wrap: anywhere;
  }
  .tp-bounty-grounding-note {
    margin-top: 1.35rem;
    padding: 1rem 1.2rem;
    border-left: 3px solid var(--tp-prussian);
    border-radius: 0 8px 8px 0;
    background-color: var(--tp-stone);
    color: var(--tp-ink-soft);
    font-size: 0.85rem;
    line-height: 1.56;
  }
  .tp-bounty-grounding-note p {
    margin: 0;
    max-width: none;
  }
  .tp-bounty-grounding-links {
    margin-top: 0.5rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.76rem;
    overflow-wrap: anywhere;
  }
  /* Contents Dialog Bounties Band */
  .tp-contents-bounties {
    margin-top: 1.25rem;
    padding-top: 1rem;
    border-top: 1px solid var(--tp-rule-strong);
  }
  .tp-contents-bounties h3 {
    margin: 0 0 0.6rem;
    font-size: 1rem;
  }
  .tp-contents-bounties h3 a {
    color: var(--tp-ink);
    text-decoration: none;
    border-bottom: 2px solid var(--tp-verdigris);
  }
  .tp-contents-bounties-list {
    list-style: none;
    margin: 0;
    padding: 0;
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.4rem;
  }
  .tp-contents-bounties-list li a {
    display: grid;
    grid-template-columns: 3.1rem minmax(0, 1fr);
    gap: 0.4rem;
    padding: 0.45rem 0.5rem;
    border-radius: 8px;
    border: 1px solid var(--tp-rule);
    background-color: var(--tp-stone);
    color: var(--tp-ink);
    text-decoration: none;
    font-size: 0.88rem;
    line-height: 1.3;
  }
  .tp-contents-bounties-list li a:hover {
    border-color: var(--tp-prussian);
  }
  @media (max-width: 860px) {
    .tp-contents-bounties-list {
      grid-template-columns: 1fr;
    }
  }
  /* Dedicated Bounty Folio Truth Boundary & Proof Dossier */
  .tp-truth-boundary-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.25rem;
    margin: 1.25rem 0 1.75rem;
  }
  @media (max-width: 780px) {
    .tp-truth-boundary-grid {
      grid-template-columns: 1fr;
    }
  }
  .tp-truth-card {
    padding: 1.25rem 1.35rem;
    border-radius: 10px;
    border: 1px solid var(--tp-rule-strong);
    background-color: var(--tp-vellum);
  }
  .tp-truth-card-certified {
    border-top: 4px solid var(--tp-verdigris);
  }
  .tp-truth-card-horizon {
    border-top: 4px solid var(--tp-prussian);
  }
  .tp-truth-card h3 {
    margin-top: 0.25rem;
    font-size: 1.05rem;
  }
  .tp-truth-card ul {
    margin: 0.65rem 0 0;
    padding-left: 1.2rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    font-size: 0.9rem;
    line-height: 1.5;
  }
  .tp-bounty-proof-dossier {
    margin: 1.5rem 0;
    padding: 1.35rem;
    border: 1px solid var(--tp-rule-strong);
    border-left: 4px solid var(--tp-verdigris);
    border-radius: 0 10px 10px 0;
    background-color: var(--tp-vellum);
  }
  @media (max-width: 640px) {
    .tp-bounty-crucible {
      padding: 1rem 0.85rem;
      margin: 2rem 0;
    }
    .tp-bounty-card {
      padding: 1rem;
    }
    input[type="range"] {
      min-height: 32px;
    }
  }
  @media (prefers-reduced-motion: no-preference) {
    .tp-bounty-ribbon {
      animation: tpSvgDashFlow 14s linear infinite;
    }
    .tp-bounty-ribbon-alt {
      animation: tpSvgDashFlow 18s linear infinite reverse;
    }
  }

  /* ---- Feature 1 & 2: Symbolic Physics Discovery Lab & Open-Source Stack Radar ---- */
  .tp-symbolic-physics-lab,
  .tp-oss-physics-radar {
    margin: 3.5rem 0;
    padding: 2rem;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 10px;
    background-color: var(--tp-vellum);
    scroll-margin-top: 5rem;
  }
  .tp-spl-controls,
  .tp-oss-controls {
    display: flex;
    flex-wrap: wrap;
    gap: 1.25rem;
    align-items: flex-end;
    margin: 1.25rem 0;
    padding: 1.1rem 1.25rem;
    border: 1px solid var(--tp-rule);
    border-radius: 8px;
    background-color: var(--tp-stone);
  }
  .tp-spl-field {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
    min-width: 190px;
    flex: 1 1 200px;
  }
  .tp-spl-label {
    font-family: var(--font-mono, monospace);
    font-size: 0.76rem;
    font-weight: 600;
    color: var(--tp-ink);
  }
  .tp-spl-select {
    font-family: var(--tp-font-ui, system-ui, sans-serif);
    font-size: 0.88rem;
    padding: 0.45rem 0.65rem;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 6px;
    background-color: var(--tp-vellum);
    color: var(--tp-ink);
  }
  .tp-spl-Readout-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
    margin: 1.25rem 0;
  }
  .tp-spl-metric-card {
    padding: 1rem 1.15rem;
    border: 1px solid var(--tp-rule);
    border-radius: 8px;
    background-color: var(--tp-stone);
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
  }
  .tp-spl-metric-label {
    font-family: var(--font-mono, monospace);
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--tp-ink-soft);
  }
  .tp-spl-metric-val {
    font-family: var(--font-mono, monospace);
    font-size: 1rem;
    font-weight: 700;
    color: var(--tp-prussian);
  }
  .tp-oss-grounding-strip {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
    margin: 0.9rem 0 1rem;
    padding: 0.65rem 0.9rem;
    border: 1px solid var(--tp-rule);
    border-radius: 8px;
    background-color: var(--tp-stone);
  }
  .tp-oss-grounding-pill {
    font-family: var(--font-mono, monospace);
    font-size: 0.73rem;
    font-weight: 600;
    color: var(--tp-verdigris);
    padding: 0.2rem 0.55rem;
    border: 1px solid var(--tp-rule);
    border-radius: 999px;
    background-color: var(--tp-vellum);
  }
  .tp-oss-filter-bar {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.5rem;
    margin: 1rem 0 1.25rem;
  }
  .tp-oss-search-input {
    font-family: var(--font-mono, monospace);
    font-size: 0.76rem;
    padding: 0.4rem 0.75rem;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 999px;
    background-color: var(--tp-stone);
    color: var(--tp-ink);
    min-width: 210px;
    flex: 1 1 210px;
  }
  .tp-oss-scite-meta {
    font-family: var(--font-mono, monospace);
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--tp-verdigris);
    margin: 0.35rem 0;
  }
  .tp-oss-filter-btn {
    font-family: var(--font-mono, monospace);
    font-size: 0.76rem;
    padding: 0.4rem 0.85rem;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 999px;
    background-color: var(--tp-stone);
    color: var(--tp-ink);
    cursor: pointer;
  }
  .tp-oss-filter-btn[aria-pressed="true"] {
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
    border-color: var(--tp-prussian);
  }
  .tp-oss-card.is-hidden {
    display: none;
  }
  /* ---- Multi-Chapter Proof & Derivation Monograph Spine ---- */
  .tp-proof-spine {
    display: flex;
    flex-direction: column;
    gap: 1.75rem;
    margin: 2rem 0 2.5rem;
  }
  .tp-proof-chapter,
  .tp-worked-verification-chapter,
  .tp-transfer-chapter {
    padding: 1.5rem 1.65rem;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 10px;
    background-color: var(--tp-vellum);
  }
  .tp-proof-chapter h3,
  .tp-worked-verification-chapter h3,
  .tp-transfer-chapter h3 {
    margin-top: 0;
  }
  .tp-theorem-box {
    margin: 1rem 0 1.25rem;
    padding: 1.1rem 1.35rem;
    border-left: 4px solid var(--tp-prussian);
    border-radius: 0 8px 8px 0;
    background-color: var(--tp-stone);
  }
  .tp-theorem-eq {
    font-size: 1.02rem;
    font-weight: 700;
    margin: 0.35rem 0;
    color: var(--tp-prussian);
  }
  .tp-theorem-meta {
    font-size: 0.84rem;
    color: var(--tp-ink-soft);
    margin: 0;
  }
  .tp-proof-stage-block {
    margin: 1rem 0;
    padding: 1rem 1.25rem;
    border-left: 3px solid var(--tp-verdigris);
    border-radius: 0 8px 8px 0;
    background-color: var(--tp-stone);
  }
  .tp-proof-stage-block h4 {
    margin: 0 0 0.45rem;
    font-size: 0.96rem;
    color: var(--tp-ink);
  }
  .tp-invariant-list {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin: 1rem 0;
    padding-left: 1.35rem;
  }
  .tp-invariant-list li span {
    display: block;
    font-size: 0.83rem;
    color: var(--tp-ink-soft);
    margin-top: 0.2rem;
  }
  .tp-counterfactual-proof {
    padding: 1.1rem 1.35rem;
    border-left: 4px solid var(--tp-minium);
    border-radius: 0 8px 8px 0;
    background-color: var(--tp-stone);
  }
  .tp-worked-verification-chapter,
  .tp-transfer-chapter {
    margin: 2rem 0;
  }

  /* ---- 5-Pace Human Distillation Ladder & Inline Visual Intuition Bridge ---- */
  .tp-plain-bridge-box,
  .tp-analogy-box {
    margin: 1.4rem 0 1.65rem;
    padding: 1.25rem 1.45rem;
    border: 1px solid var(--tp-rule-strong);
    border-left: 4px solid var(--tp-verdigris);
    border-radius: 0 10px 10px 0;
    background-color: var(--tp-vellum);
    box-sizing: border-box;
  }
  .tp-analogy-box {
    border-left-color: var(--tp-prussian);
  }
  .tp-plain-bridge-kicker {
    display: inline-block;
    margin-bottom: 0.45rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--tp-verdigris);
  }
  .tp-analogy-box .tp-plain-bridge-kicker {
    color: var(--tp-prussian);
  }
  .tp-plain-bridge-box p,
  .tp-analogy-box p {
    margin: 0.45rem 0 0;
    font-size: 1.01rem;
    line-height: 1.68;
  }
  .tp-distill-figure {
    margin: 1.5rem 0 1.85rem;
    padding: 1.15rem 1.25rem;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 10px;
    background-color: var(--tp-vellum);
    box-sizing: border-box;
    max-width: 100%;
    overflow: hidden;
  }
  .tp-distill-svg {
    display: block;
    width: 100%;
    height: auto;
  }
  .tp-distill-caption {
    margin-top: 0.65rem;
    font-size: 0.84rem;
    line-height: 1.48;
    color: var(--tp-graphite);
  }

  /* ---- 30-Second Studio Quick-Start Action Bar (Tech & Tools) ---- */
  .tp-studio-quickstart {
    margin: 1.4rem 0 2rem;
    padding: 1.25rem 1.45rem;
    border: 2px solid var(--tp-prussian);
    border-radius: 12px;
    background: linear-gradient(180deg, var(--tp-vellum) 0%, var(--tp-stone) 100%);
    box-shadow: 0 4px 18px rgba(13, 27, 42, 0.06);
  }
  .tp-studio-quickstart-head {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 0.75rem;
    margin-bottom: 1rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid var(--tp-rule-strong);
  }
  .tp-studio-quickstart-badge {
    font-family: var(--font-mono, monospace);
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--tp-vellum);
    background-color: var(--tp-prussian);
    padding: 0.28rem 0.65rem;
    border-radius: 4px;
  }
  .tp-studio-quickstart-sub {
    font-size: 0.9rem;
    color: var(--tp-ink-soft);
  }
  .tp-studio-steps-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
  }
  .tp-studio-step-card {
    padding: 0.95rem 1.1rem;
    border: 1px solid var(--tp-rule-strong);
    border-radius: 8px;
    background-color: var(--tp-vellum);
  }
  .tp-studio-step-num {
    display: inline-block;
    font-family: var(--font-mono, monospace);
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--tp-verdigris);
    margin-bottom: 0.35rem;
  }
  .tp-studio-step-title {
    margin: 0 0 0.45rem;
    font-size: 0.98rem;
    font-weight: 700;
    color: var(--tp-ink);
  }
  .tp-studio-step-card p {
    margin: 0 0 0.65rem;
    font-size: 0.87rem;
    line-height: 1.5;
    color: var(--tp-ink-soft);
  }
  .tp-studio-pill-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
  }
  .tp-studio-dl-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    padding: 0.34rem 0.68rem;
    border: 1px solid var(--tp-prussian);
    border-radius: 6px;
    font-family: var(--font-mono, monospace);
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--tp-prussian);
    background-color: var(--tp-stone);
    text-decoration: none;
    transition: background-color 0.15s ease, color 0.15s ease;
  }
  .tp-studio-dl-pill:hover {
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
  }
  .tp-studio-dl-pill--primary {
    background-color: var(--tp-verdigris);
    border-color: var(--tp-verdigris);
    color: var(--tp-vellum);
  }
}
"""


def update_informatico_css() -> None:
    css_path = ROOT / "src" / "research" / "informatico.css"
    css = css_path.read_text(encoding="utf-8")
    marker = "/* 5-Act Long-Form Editorial Magazine & Informatico.ai Styles */"
    if marker in css:
        css = css.split(marker)[0].rstrip() + "\n}\n"

    addition = f"""  {marker}
  .tp-rack-grid {{
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }}

  @media (max-width: 980px) {{
    .tp-rack-grid {{
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }}
  }}

  @media (max-width: 640px) {{
    .tp-rack-grid {{
      grid-template-columns: 1fr;
    }}
  }}

  .tp-reading-meta {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 0.85rem;
  }}

  .tp-meta-pill {{
    font-family: var(--font-mono, monospace);
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 0.22rem 0.55rem;
    background-color: var(--tp-vellum);
    border: 1px solid var(--tp-rule-strong);
    color: var(--tp-graphite);
  }}

  .tp-meta-pill-verified {{
    border-color: var(--tp-verdigris);
    color: var(--tp-verdigris);
    background-color: var(--tp-verdigris-soft);
  }}

  .tp-dropcap::first-letter {{
    float: left;
    font-family: var(--font-display, Georgia, serif);
    font-size: 3.35rem;
    line-height: 0.84;
    padding-right: 0.55rem;
    padding-top: 0.12rem;
    color: var(--tp-minium);
    font-weight: 700;
  }}

  .tp-pullquote {{
    margin: 1.4rem 0;
    padding: 1rem 1.25rem;
    background-color: var(--tp-vellum);
    border-left: 4px solid var(--tp-minium);
    border-top: 1px solid var(--tp-rule);
    border-bottom: 1px solid var(--tp-rule);
    font-family: var(--font-display, Georgia, serif);
    font-size: 1.12rem;
    font-style: italic;
    line-height: 1.45;
    color: var(--tp-ink);
  }}

  .tp-pullquote p {{
    margin: 0;
  }}

  .tp-analogy-box {{
    margin: 1rem 0 1.35rem;
    padding: 0.9rem 1.1rem;
    background-color: var(--tp-vellum);
    border: 1px solid var(--tp-rule-strong);
    border-left: 3px solid var(--tp-prussian);
    font-size: 0.92rem;
    color: var(--tp-ink);
  }}

  .tp-walkthrough-box {{
    margin: 0.85rem 0 1.15rem;
    padding: 0.95rem 1.15rem;
    background-color: var(--tp-vellum);
    border: 1px solid var(--tp-rule-strong);
    border-top: 3px solid var(--tp-verdigris);
  }}

  .tp-walkthrough-box h3 {{
    margin: 0 0 0.45rem 0;
    font-size: 0.95rem;
    font-family: var(--font-mono, monospace);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--tp-verdigris);
  }}

  .tp-walkthrough-box ol {{
    margin: 0;
    padding-left: 1.2rem;
    font-size: 0.88rem;
    line-height: 1.5;
  }}

  .tp-walkthrough-box li {{
    margin-bottom: 0.35rem;
  }}

  .tp-cf-bridge-box {{
    margin: 1.15rem 0 1.4rem;
    padding: 1.05rem 1.2rem;
    background-color: var(--tp-vellum);
    border: 1.5px solid var(--tp-verdigris);
    border-left: 5px solid var(--tp-verdigris);
  }}

  .tp-cf-bridge-box h3 {{
    margin: 0 0 0.45rem 0;
    font-family: var(--font-mono, monospace);
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--tp-verdigris);
  }}

  .tp-cf-bridge-box p {{
    margin: 0;
    font-size: 0.93rem;
  }}

  .tp-discovery-news-box {{
    margin: 1.15rem 0;
    padding: 1.05rem 1.2rem;
    background-color: var(--tp-vellum);
    border: 1px solid var(--tp-rule-strong);
    border-left: 5px solid var(--tp-prussian);
  }}

  .tp-discovery-news-box h3 {{
    margin: 0.25rem 0 0.45rem 0;
    font-size: 1.02rem;
    color: var(--tp-ink);
  }}

  .tp-discovery-news-box p {{
    margin: 0;
    font-size: 0.92rem;
    line-height: 1.55;
  }}

  .tp-cite-link {{
    color: var(--tp-prussian);
    text-decoration: underline;
    text-underline-offset: 2px;
    font-weight: 600;
  }}

  .tp-scite-badge-link {{
    display: inline-block;
    font-family: var(--font-mono, monospace);
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--tp-verdigris);
    text-decoration: none;
    padding: 0.08rem 0.38rem;
    border: 1px solid var(--tp-verdigris);
    background-color: var(--tp-verdigris-soft);
  }}

  .tp-scite-strip {{
    margin: 1rem 0 1.35rem;
    padding: 1rem 1.15rem;
    background-color: var(--tp-vellum);
    border: 1px solid var(--tp-rule-strong);
    border-left: 4px solid var(--tp-prussian);
    font-size: 0.88rem;
  }}

  .tp-scite-strip h3 {{
    margin: 0 0 0.45rem 0;
    font-family: var(--font-mono, monospace);
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--tp-prussian);
  }}

  .tp-discovery-steps {{
    margin: 0.6rem 0 0;
    padding-left: 1.2rem;
    font-size: 0.85rem;
    line-height: 1.48;
  }}

  .tp-discovery-steps li {{
    margin-bottom: 0.3rem;
  }}

  .tp-sources-list {{
    font-size: 0.84rem;
    line-height: 1.5;
    color: var(--tp-graphite);
    padding-left: 1.25rem;
  }}

  .tp-sources-list li {{
    margin-bottom: 0.4rem;
  }}

  .tp-sponsor-slot {{
    min-height: 176px;
    padding: 1rem;
    background-color: var(--tp-vellum);
    border: 1px dashed var(--tp-rule-strong);
    border-top: 3px solid var(--tp-ochre);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  .tp-sponsor-kicker {{
    display: inline-block;
    font-family: var(--font-mono, monospace);
    font-size: 0.64rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--tp-sienna);
    margin-bottom: 0.35rem;
  }}

  .tp-rail code,
  .tp-spec-plate code,
  .tp-sponsor-slot code,
  .tp-scite-strip code {{
    overflow-wrap: anywhere;
    word-break: break-word;
  }}

  .tp-editorial-figure {{
    margin: 0 0 1.6rem 0;
    background-color: var(--tp-vellum);
    border: 1px solid var(--tp-rule-strong);
    border-top: 3px solid var(--tp-prussian);
    overflow: hidden;
  }}

  .tp-editorial-badge-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.5rem;
    padding: 0.45rem 0.85rem;
    background-color: var(--tp-stone);
    border-bottom: 1px solid var(--tp-rule);
    font-family: var(--font-mono, monospace);
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--tp-graphite);
  }}

  .tp-editorial-img {{
    display: block;
    width: 100%;
    height: auto;
    aspect-ratio: 16 / 9;
    object-fit: cover;
    background-color: var(--tp-stone);
  }}

  .tp-editorial-caption {{
    padding: 0.75rem 1rem;
    font-size: 0.84rem;
    line-height: 1.5;
    color: var(--tp-ink);
    border-top: 1px solid var(--tp-rule);
  }}

  .tp-drawn-note {{
    display: block;
    margin-top: 0.35rem;
    font-size: 0.78rem;
    color: var(--tp-graphite);
  }}

  .tp-dispatch-plate-wrap {{
    margin: -0.25rem 0 0.85rem 0;
    border: 1px solid var(--tp-rule-strong);
    overflow: hidden;
    background-color: var(--tp-stone);
  }}

  .tp-dispatch-thumb {{
    display: block;
    width: 100%;
    height: auto;
    aspect-ratio: 16 / 9;
    object-fit: cover;
  }}

  .tp-utopia-showcase {{
    margin: 1.5rem 0 2.2rem 0;
    padding: 1.5rem;
    background-color: var(--tp-vellum);
    border: 1.5px solid var(--tp-rule-strong);
    border-top: 4px solid var(--tp-prussian);
  }}

  .tp-utopia-diptych {{
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.25rem;
    margin: 1.25rem 0;
  }}

  @media (max-width: 920px) {{
    .tp-utopia-diptych {{
      grid-template-columns: 1fr;
    }}
  }}


  .tp-human-potential-box {{
    margin: 1.15rem 0;
    padding: 1rem 1.2rem;
    background-color: var(--tp-verdigris-soft);
    border: 1px solid var(--tp-verdigris);
    border-left: 5px solid var(--tp-verdigris);
    font-size: 0.92rem;
    line-height: 1.55;
    color: var(--tp-ink);
  }}

  .tp-human-potential-box p {{
    margin: 0.25rem 0 0 0;
  }}

  .tp-sweep-btn[aria-pressed="true"] {{
    background-color: var(--tp-verdigris);
    border-color: var(--tp-verdigris);
    color: var(--tp-vellum);
  }}

  .tp-lens-bar {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    align-items: center;
  }}

  .tp-lens-btn {{
    font-family: var(--font-mono, monospace);
    font-size: 0.68rem;
    font-weight: 600;
    padding: 0.28rem 0.58rem;
    background-color: var(--tp-stone);
    color: var(--tp-ink);
    border: 1px solid var(--tp-rule-strong);
    cursor: pointer;
    transition: background-color 150ms ease, color 150ms ease, transform 150ms ease;
  }}

  .tp-lens-btn[aria-pressed="true"] {{
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
    border-color: var(--tp-prussian);
  }}

  .tp-lens-btn-util {{
    border-style: dashed;
  }}

  .tp-svg-wrap,
  .tp-webgl-wrap {{
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    height: 100%;
    background-color: var(--tp-vellum);
  }}

  .tp-svg-wrap .tp-plate-head,
  .tp-webgl-wrap .tp-plate-head {{
    min-height: 44px;
    margin-bottom: 0.45rem;
    padding-bottom: 0.42rem;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 0.45rem;
  }}

  .tp-plate-live-badge {{
    display: inline-flex;
    align-items: center;
    height: 24px;
    padding: 0 0.5rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.67rem;
    font-weight: 700;
    color: var(--tp-prussian);
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule-strong);
    white-space: nowrap;
  }}

  .tp-svg-wrap .tp-svg-stage,
  .tp-webgl-wrap .tp-webgl-canvas,
  .tp-webgl-wrap .tp-lens-svg {{
    width: 100%;
    height: 265px;
    margin-top: 0;
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule-strong);
    box-sizing: border-box;
  }}

  .tp-lens-svg:not([hidden]),
  .tp-webgl-canvas:not([hidden]) {{
    display: block;
  }}

  .tp-lens-svg[hidden],
  .tp-webgl-canvas[hidden] {{
    display: none;
  }}

  .tp-stage-axis-hud {{
    margin-top: 0.42rem;
    padding: 0.34rem 0.62rem;
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule);
    font-family: var(--font-mono, monospace);
    font-size: 0.68rem;
    line-height: 1.35;
    color: var(--tp-graphite);
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 0.4rem;
  }}

  .tp-svg-beacon {{
    transition: transform 320ms cubic-bezier(0.22, 1, 0.36, 1);
  }}

  .tp-svg-stage path,
  .tp-svg-stage polygon,
  .tp-svg-stage circle,
  .tp-svg-stage rect {{
    transition: d 180ms ease, points 180ms ease, r 180ms ease, cx 180ms ease, cy 180ms ease, x 180ms ease, fill 180ms ease;
  }}

  @media (prefers-reduced-motion: no-preference) {{
    @keyframes tpSvgDashFlow {{
      to {{
        stroke-dashoffset: -24;
      }}
    }}

    @keyframes tpBeaconPulse {{
      0%, 100% {{
        r: 12px;
        stroke-opacity: 0.85;
      }}
      50% {{
        r: 17px;
        stroke-opacity: 0.35;
      }}
    }}

    .tp-svg-flow-line {{
      animation: tpSvgDashFlow var(--tp-flow-duration, 1.8s) linear infinite;
    }}

    .tp-svg-beacon-ring {{
      animation: tpBeaconPulse 2.2s ease-in-out infinite;
    }}

    @keyframes tpWavefrontExpand {{
      0% {{
        r: 6px;
        stroke-opacity: 0.78;
        fill-opacity: 0.18;
      }}
      100% {{
        r: 34px;
        stroke-opacity: 0;
        fill-opacity: 0;
      }}
    }}

    .tp-wave-ring {{
      animation: tpWavefrontExpand 2.6s cubic-bezier(0.16, 1, 0.3, 1) infinite;
    }}

    .tp-wave-ring-2 {{
      animation-delay: 0.86s;
    }}

    .tp-wave-ring-3 {{
      animation-delay: 1.72s;
    }}
  }}

  /* Widescreen Full-Viewport Editorial Grid, Split-Stage Workbench & Motion Plate Controls */
  @media (min-width: 1520px) {{
    .tp-rack-grid {{
      grid-template-columns: repeat(4, minmax(0, 1fr));
    }}
  }}

  @media (min-width: 1360px) {{
    .tp-folio-layout {{
      grid-template-columns: minmax(0, 2.35fr) minmax(300px, 0.78fr);
      gap: 2.5rem;
    }}

    .tp-dispatch-list {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 1.35rem;
    }}
  }}

  .tp-plate-head-actions {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.55rem;
  }}

  .tp-plate-split-workbench {{
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.15rem;
    align-items: stretch;
  }}

  @media (min-width: 1220px) {{
    .tp-plate-split-workbench[data-layout-mode="split"] {{
      grid-template-columns: minmax(0, 1.06fr) minmax(0, 0.94fr);
    }}
  }}

  .tp-plate-col-svg,
  .tp-plate-col-webgl {{
    min-width: 0;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }}

  .tp-plate-col-webgl .tp-webgl-wrap {{
    margin-top: 0;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  .tp-layout-toggle-btn[aria-pressed="true"] {{
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
    border-color: var(--tp-prussian);
  }}

  .tp-media-mode-bar {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.35rem;
  }}

  .tp-media-mode-btn {{
    font-family: var(--font-mono, monospace);
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    padding: 0.2rem 0.52rem;
    background-color: var(--tp-vellum);
    color: var(--tp-ink);
    border: 1px solid var(--tp-rule-strong);
    cursor: pointer;
    transition: background-color 140ms ease, color 140ms ease, border-color 140ms ease;
  }}

  .tp-media-mode-btn[aria-pressed="true"] {{
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
    border-color: var(--tp-prussian);
  }}

  .tp-editorial-media-stage {{
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    background-color: var(--tp-stone);
    overflow: hidden;
  }}

  .tp-editorial-svg-overlay {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 2;
  }}

  .tp-svg-particle {{
    transition: r 150ms ease, fill-opacity 150ms ease;
  }}

  .tp-vector-arrow line,
  .tp-vector-arrow polygon {{
    transition: transform 160ms ease, stroke 160ms ease, fill 160ms ease;
  }}

  .tp-volumes-grid {{
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.25rem;
    margin: 1.25rem 0 2rem 0;
  }}

  @media (max-width: 1100px) {{
    .tp-volumes-grid {{
      grid-template-columns: 1fr;
    }}
  }}

  .tp-volume-card {{
    background-color: var(--tp-vellum);
    border: 1.5px solid var(--tp-rule-strong);
    border-top: 4px solid var(--tp-prussian);
    padding: 1.25rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 1rem;
  }}

  .tp-volume-card h3 {{
    margin: 0.35rem 0 0.55rem 0;
    font-size: 1.08rem;
    line-height: 1.35;
    color: var(--tp-ink);
  }}

  .tp-volume-card p {{
    margin: 0 0 0.75rem 0;
    font-size: 0.88rem;
    line-height: 1.52;
    color: var(--tp-graphite);
  }}

  .tp-volume-folios {{
    font-family: var(--font-mono, monospace);
    font-size: 0.78rem;
    padding: 0.5rem 0.65rem;
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule);
    margin-bottom: 0.35rem;
  }}

  .tp-volume-card[data-volume-active="true"] {{
    border-color: var(--tp-verdigris);
    border-top-width: 4px;
    border-top-color: var(--tp-verdigris);
    background-color: var(--tp-verdigris-soft);
  }}

  .tp-volume-pillar-grid {{
    display: flex;
    flex-direction: column;
    gap: 0.32rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.74rem;
    padding: 0.55rem 0.68rem;
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule);
    margin-bottom: 0.45rem;
  }}

  .tp-vol-pillar-row {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.35rem;
    line-height: 1.4;
  }}

  .tp-vol-p-tag {{
    display: inline-block;
    min-width: 3.1rem;
    text-align: center;
    font-size: 0.64rem;
    font-weight: 700;
    padding: 0.08rem 0.32rem;
    background-color: var(--tp-vellum);
    border: 1px solid var(--tp-rule-strong);
    color: var(--tp-prussian);
  }}

  .tp-volume-card-actions {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    align-items: center;
  }}

  .tp-volume-nav-bar {{
    background-color: var(--tp-vellum);
    border-bottom: 1px solid var(--tp-rule-strong);
    padding: 0.42rem clamp(1.1rem, 2.4vw, 2.75rem);
    position: relative;
    z-index: 35;
  }}

  .tp-volume-nav-inner {{
    max-width: clamp(1440px, 95vw, 1880px);
    margin: 0 auto;
  }}

  .tp-volume-nav-top {{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    min-height: 30px;
    gap: 0.65rem;
  }}

  .tp-breadcrumb-list {{
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.38rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.73rem;
    line-height: 1;
  }}

  .tp-crumb-item {{
    display: inline-flex;
    align-items: center;
    min-height: 28px;
    line-height: 1;
  }}

  .tp-crumb-link {{
    display: inline-flex;
    align-items: center;
    height: 28px;
    line-height: 1;
    color: var(--tp-graphite);
    text-decoration: none;
    font-weight: 600;
    padding: 0 0.42rem;
    border-radius: 2px;
    box-sizing: border-box;
  }}

  .tp-crumb-link:hover {{
    color: var(--tp-ink);
    background-color: var(--tp-mortar);
    text-decoration: underline;
  }}

  .tp-crumb-sep {{
    display: inline-flex;
    align-items: center;
    height: 28px;
    line-height: 1;
    color: var(--tp-slate);
    opacity: 0.65;
    user-select: none;
  }}

  .tp-crumb-current {{
    color: var(--tp-ink);
    display: inline-flex;
    flex-wrap: wrap;
    align-items: center;
    min-height: 28px;
    line-height: 1;
    gap: 0.35rem;
  }}

  .tp-crumb-title {{
    color: var(--tp-graphite);
    font-weight: 500;
  }}

  .tp-vol-hub-link,
  .tp-crumb-vol-tag {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 28px;
    line-height: 1;
    font-family: var(--font-mono, monospace);
    font-size: 0.67rem;
    font-weight: 700;
    color: var(--tp-verdigris);
    background-color: var(--tp-verdigris-soft);
    border: 1px solid var(--tp-verdigris);
    padding: 0 0.52rem;
    text-decoration: none;
    box-sizing: border-box;
    white-space: nowrap;
  }}

  .tp-vol-hub-link:hover {{
    background-color: var(--tp-verdigris);
    color: var(--tp-vellum);
  }}

  .tp-volume-nav-left,
  .tp-volume-nav-right {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.42rem;
  }}

  .tp-crumb-drawer {{
    position: relative;
    display: inline-flex;
    align-items: center;
  }}

  .tp-crumb-drawer-toggle {{
    list-style: none;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 28px;
    line-height: 1;
    font-family: var(--font-mono, monospace);
    font-size: 0.68rem;
    font-weight: 700;
    padding: 0 0.68rem;
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
    border: 1px solid var(--tp-prussian);
    cursor: pointer;
    user-select: none;
    box-sizing: border-box;
    white-space: nowrap;
  }}

  .tp-crumb-drawer-toggle::-webkit-details-marker {{
    display: none;
  }}

  .tp-crumb-drawer[open] .tp-crumb-drawer-toggle {{
    background-color: var(--tp-verdigris);
    color: var(--tp-vellum);
    border-color: var(--tp-verdigris);
  }}

  .tp-crumb-drawer-panel {{
    position: absolute;
    right: 0;
    top: calc(100% + 0.45rem);
    width: min(1220px, 95vw);
    max-height: 82vh;
    overflow-y: auto;
    background-color: var(--tp-vellum);
    border: 1.5px solid var(--tp-ink);
    box-shadow: var(--tp-shadow-flyout);
    padding: 1rem 1.15rem;
    z-index: 60;
    display: flex;
    flex-direction: column;
    gap: 0.85rem;
  }}

  .tp-crumb-drawer-section {{
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }}

  .tp-crumb-drawer-section + .tp-crumb-drawer-section {{
    padding-top: 0.72rem;
    border-top: 1px solid var(--tp-rule-strong);
  }}

  .tp-crumb-drawer-header {{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 0.5rem;
  }}

  .tp-topic-mega-grid {{
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 0.65rem;
  }}

  @media (max-width: 1120px) {{
    .tp-topic-mega-grid {{
      grid-template-columns: repeat(3, minmax(0, 1fr));
    }}
  }}

  @media (max-width: 720px) {{
    .tp-topic-mega-grid {{
      grid-template-columns: 1fr;
    }}
  }}

  .tp-topic-col {{
    display: flex;
    flex-direction: column;
    gap: 0.32rem;
    padding: 0.55rem;
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule);
    border-top: 3px solid var(--tp-prussian);
  }}

  .tp-topic-col[data-active-topic="true"] {{
    border-top-color: var(--tp-verdigris);
    background-color: var(--tp-verdigris-soft);
  }}

  .tp-topic-col-head {{
    display: flex;
    flex-direction: column;
    gap: 0.1rem;
    text-decoration: none;
    color: var(--tp-ink);
    padding-bottom: 0.35rem;
    border-bottom: 1px solid var(--tp-rule);
    font-family: var(--font-mono, monospace);
    font-size: 0.71rem;
  }}

  .tp-topic-roman {{
    font-size: 0.61rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--tp-graphite);
  }}

  .tp-topic-article-list {{
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
  }}

  .tp-topic-article-link {{
    display: flex;
    flex-direction: column;
    gap: 0.08rem;
    padding: 0.28rem 0.42rem;
    background-color: var(--tp-vellum);
    border: 1px solid var(--tp-rule);
    text-decoration: none;
    color: var(--tp-ink);
    font-size: 0.71rem;
    line-height: 1.25;
  }}

  .tp-topic-article-link:hover {{
    border-color: var(--tp-prussian);
    background-color: var(--tp-mortar);
  }}

  .tp-topic-article-link[data-active-folio="true"] {{
    background-color: var(--tp-verdigris);
    border-color: var(--tp-verdigris);
    color: var(--tp-vellum);
  }}

  .tp-topic-article-top {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: var(--font-mono, monospace);
    font-size: 0.65rem;
  }}

  .tp-topic-vol-chip {{
    font-style: normal;
    font-size: 0.59rem;
    opacity: 0.8;
  }}

  .tp-topic-article-title {{
    font-size: 0.69rem;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }}

  .tp-archive-disclosure {{
    margin: 1.75rem 0;
    border: 1px solid var(--tp-rule-strong);
    background-color: var(--tp-vellum);
  }}

  .tp-archive-summary {{
    list-style: none;
    cursor: pointer;
    padding: 0.75rem 1rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--tp-ink);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .tp-archive-summary::-webkit-details-marker {{
    display: none;
  }}

  .tp-archive-disclosure[open] .tp-archive-summary {{
    border-bottom: 1px solid var(--tp-rule);
  }}

  .tp-archive-disclosure .tp-dispatch-stream {{
    padding: 1rem;
    margin: 0;
  }}

  .tp-vol-active-badge {{
    font-family: var(--font-mono, monospace);
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    padding: 0.22rem 0.55rem;
    background-color: var(--tp-verdigris-soft);
    border: 1px solid var(--tp-verdigris);
    color: var(--tp-verdigris);
  }}

  .tp-vol-tab-group,
  .tp-pillar-vol-filter,
  .tp-vol-stepper-links {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.32rem;
  }}

  .tp-vol-filter-kicker,
  .tp-vol-step-pos,
  .tp-vol-sibling-label {{
    font-family: var(--font-mono, monospace);
    font-size: 0.68rem;
    font-weight: 600;
    color: var(--tp-graphite);
  }}

  .tp-vol-nav-pill,
  .tp-vol-filter-btn,
  .tp-vol-step-link {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 28px;
    line-height: 1;
    font-family: var(--font-mono, monospace);
    font-size: 0.68rem;
    font-weight: 600;
    padding: 0 0.55rem;
    background-color: var(--tp-stone);
    color: var(--tp-ink);
    border: 1px solid var(--tp-rule-strong);
    text-decoration: none;
    cursor: pointer;
    box-sizing: border-box;
    white-space: nowrap;
  }}

  .tp-vol-step-link:hover,
  .tp-vol-nav-pill:hover {{
    background-color: var(--tp-mortar);
  }}

  .tp-vol-nav-pill[aria-pressed="true"],
  .tp-vol-filter-btn[aria-pressed="true"] {{
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
    border-color: var(--tp-prussian);
  }}

  .tp-volume-sibling-bar {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.45rem;
    padding-top: 0.42rem;
    border-top: 1px dashed var(--tp-rule);
  }}
  .tp-volume-sibling-bar[hidden] {{
    display: none;
  }}

  .tp-vol-sibling-list {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.32rem;
  }}

  .tp-vol-sibling-pill {{
    font-family: var(--font-mono, monospace);
    font-size: 0.67rem;
    padding: 0.18rem 0.48rem;
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule);
    color: var(--tp-ink);
    text-decoration: none;
  }}

  .tp-vol-sibling-pill[data-active-folio="true"] {{
    background-color: var(--tp-verdigris);
    border-color: var(--tp-verdigris);
    color: var(--tp-vellum);
    font-weight: 700;
  }}

  .tp-es-dossier {{
    margin: 1.15rem 0 1.4rem 0;
    border: 1.5px solid var(--tp-prussian);
    background-color: var(--tp-vellum);
  }}
  .tp-es-summary {{
    list-style: none;
    cursor: pointer;
    padding: 0.68rem 1rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.76rem;
    color: var(--tp-prussian);
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 0.5rem;
    background-color: var(--tp-stone);
  }}
  .tp-es-summary::-webkit-details-marker {{
    display: none;
  }}
  .tp-es-badge {{
    font-size: 0.68rem;
    font-weight: 700;
    padding: 0.14rem 0.48rem;
    border: 1px solid var(--tp-prussian);
    background-color: var(--tp-vellum);
    color: var(--tp-prussian);
  }}
  .tp-es-body {{
    padding: 0.9rem 1.1rem;
    border-top: 1px solid var(--tp-rule);
    font-size: 0.92rem;
    line-height: 1.58;
    color: var(--tp-ink);
  }}
  .tp-es-body p {{
    margin: 0 0 0.65rem 0;
  }}
  .tp-es-body p:last-child {{
    margin-bottom: 0;
  }}
  .tp-matrix-status-bar {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 0.65rem;
    margin-top: 0.55rem;
    padding: 0.42rem 0.75rem;
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule);
    font-family: var(--font-mono, monospace);
    font-size: 0.74rem;
    color: var(--tp-prussian);
  }}

  /* ---- Informatico.ai Bauhaus 2x2 Matrix [Io / ai] Square Seal & SVG Animation ---- */
  .tp-logo-draw {{
    stroke-dasharray: none;
    stroke-dashoffset: 0;
  }}

  .tp-logo-datum {{
    fill: var(--tp-minium);
    stroke: none;
    transform-box: fill-box;
    transform-origin: center;
    transition: transform 0.25s ease;
  }}

  @keyframes tpLogoDraw {{
    0% {{
      stroke-dasharray: 1;
      stroke-dashoffset: 1;
    }}
    99% {{
      stroke-dasharray: 1;
      stroke-dashoffset: 0;
    }}
    100% {{
      stroke-dasharray: none;
      stroke-dashoffset: 0;
    }}
  }}

  @keyframes tpDatumBreathe {{
    0%, 100% {{
      opacity: 0.86;
      transform: scale(1);
    }}
    50% {{
      opacity: 1;
      transform: scale(1.22);
    }}
  }}

  @media (prefers-reduced-motion: no-preference) {{
    .tp-logo-q1 {{
      stroke-dasharray: 1;
      stroke-dashoffset: 1;
      animation: tpLogoDraw 0.45s cubic-bezier(0.22, 1, 0.36, 1) 0s forwards;
    }}

    .tp-logo-q2 {{
      stroke-dasharray: 1;
      stroke-dashoffset: 1;
      animation: tpLogoDraw 0.45s cubic-bezier(0.22, 1, 0.36, 1) 0.14s forwards;
    }}

    .tp-logo-q3 {{
      stroke-dasharray: 1;
      stroke-dashoffset: 1;
      animation: tpLogoDraw 0.45s cubic-bezier(0.22, 1, 0.36, 1) 0.28s forwards;
    }}

    .tp-logo-q4 {{
      stroke-dasharray: 1;
      stroke-dashoffset: 1;
      animation: tpLogoDraw 0.45s cubic-bezier(0.22, 1, 0.36, 1) 0.42s forwards;
    }}

    .tp-logo-datum {{
      animation: tpDatumBreathe 4s ease-in-out 0.75s infinite;
    }}

    .tp-brand:hover .tp-logo-datum,
    .tp-brand:focus-visible .tp-logo-datum {{
      transform: rotate(45deg) scale(1.25);
    }}
  }}

  /* ---- Editorial Art Director & Mobile Magazine Choreography (Quanta / El Croquis / Kinfolk) ---- */
  .tp-standfirst {{
    font-family: var(--font-display, Georgia, "Times New Roman", serif);
    font-size: clamp(1.1rem, 1.38vw, 1.28rem);
    line-height: 1.56;
    color: var(--tp-ink);
    max-width: 68ch;
  }}

  .tp-prose p {{
    font-size: 1.05rem;
    line-height: 1.74;
    color: var(--tp-ink);
  }}

  .tp-why-matters-lead {{
    margin: 1.05rem 0 1.15rem 0;
    padding: 0.95rem 1.2rem;
    background-color: var(--tp-vellum);
    border: 1px solid var(--tp-rule-strong);
    border-left: 4px solid var(--tp-minium);
    max-width: 68ch;
  }}

  .tp-why-kicker {{
    display: block;
    font-family: var(--font-mono, monospace);
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--tp-minium);
    margin-bottom: 0.32rem;
  }}

  .tp-why-matters-lead p {{
    margin: 0;
    font-family: var(--font-display, Georgia, "Times New Roman", serif);
    font-size: 1.02rem;
    line-height: 1.54;
    color: var(--tp-ink);
  }}

  .tp-act-jump-bar {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.42rem;
    margin-top: 0.95rem;
    padding-top: 0.75rem;
    border-top: 1px solid var(--tp-rule);
  }}

  .tp-act-pill {{
    display: inline-flex;
    align-items: center;
    padding: 0.3rem 0.68rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.03em;
    color: var(--tp-ink);
    background-color: var(--tp-vellum);
    border: 1px solid var(--tp-rule-strong);
    text-decoration: none;
    white-space: nowrap;
    transition: background-color 140ms ease, color 140ms ease, border-color 140ms ease;
  }}

  .tp-act-pill:hover {{
    background-color: var(--tp-mortar);
    border-color: var(--tp-prussian);
  }}

  .tp-act-pill-highlight {{
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
    border-color: var(--tp-prussian);
  }}

  .tp-act-pill-highlight:hover {{
    background-color: var(--tp-verdigris);
    border-color: var(--tp-verdigris);
    color: var(--tp-vellum);
  }}

  .tp-dossier-strip {{
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.85rem;
    margin: 0.85rem 0 1.35rem 0;
    align-items: start;
  }}

  @media (max-width: 960px) {{
    .tp-dossier-strip {{
      grid-template-columns: 1fr;
      gap: 0.55rem;
    }}
  }}

  .tp-dossier-strip .tp-es-dossier,
  .tp-colophon-disclosure {{
    margin: 0;
    border: 1px solid var(--tp-rule-strong);
    background-color: var(--tp-vellum);
  }}

  .tp-colophon-summary {{
    list-style: none;
    cursor: pointer;
    padding: 0.62rem 0.95rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.73rem;
    color: var(--tp-graphite);
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 0.5rem;
    background-color: var(--tp-stone);
  }}

  .tp-colophon-summary::-webkit-details-marker {{
    display: none;
  }}

  .tp-colophon-disclosure[open] .tp-colophon-summary {{
    border-bottom: 1px solid var(--tp-rule);
  }}

  .tp-colophon-disclosure .tp-colophon-grid {{
    margin: 0;
    border: none;
  }}

  .tp-plate-provenance-details {{
    margin-top: 0.45rem;
    border-top: 1px dashed var(--tp-rule);
    padding-top: 0.38rem;
  }}

  .tp-plate-provenance-summary {{
    list-style: none;
    cursor: pointer;
    font-family: var(--font-mono, monospace);
    font-size: 0.68rem;
    font-weight: 600;
    color: var(--tp-graphite);
    user-select: none;
  }}

  .tp-plate-provenance-summary::-webkit-details-marker {{
    display: none;
  }}

  .tp-skill-source-details {{
    margin-top: 0.85rem;
    border: 1px solid var(--tp-rule-strong);
    background-color: var(--tp-stone);
  }}

  .tp-skill-source-summary {{
    list-style: none;
    cursor: pointer;
    padding: 0.55rem 0.85rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--tp-prussian);
  }}

  .tp-skill-source-summary::-webkit-details-marker {{
    display: none;
  }}

  .tp-rack-thumb-wrap {{
    margin: -0.25rem -0.25rem 0.55rem -0.25rem;
    overflow: hidden;
    border-bottom: 1px solid var(--tp-rule);
    background-color: var(--tp-stone);
  }}

  .tp-rack-thumb {{
    display: block;
    width: 100%;
    height: auto;
    aspect-ratio: 16 / 9;
    object-fit: cover;
    transition: transform 240ms ease;
  }}

  .tp-rack-card:hover .tp-rack-thumb {{
    transform: scale(1.03);
  }}

  .tp-pillars-showcase {{
    margin: 1.35rem 0 2.1rem 0;
  }}

  .tp-issue-card-cover {{
    display: block;
    margin: -1.15rem -1.15rem 0.95rem -1.15rem;
    overflow: hidden;
    border-bottom: 1px solid var(--tp-rule-strong);
    background-color: var(--tp-stone);
  }}

  .tp-issue-card-img {{
    display: block;
    width: 100%;
    height: auto;
    aspect-ratio: 16 / 9;
    object-fit: cover;
    transition: transform 280ms ease;
  }}

  .tp-issue-card:hover .tp-issue-card-img {{
    transform: scale(1.03);
  }}

  .tp-pillar-curiosity-hook {{
    padding: 0.68rem 0.85rem;
    margin: 0.55rem 0 0.75rem 0;
    background-color: var(--tp-stone);
    border-left: 3px solid var(--tp-minium);
    font-family: var(--font-display, Georgia, "Times New Roman", serif);
    font-size: 0.94rem;
    line-height: 1.48;
    color: var(--tp-ink);
  }}

  .tp-issue-card-folios {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.32rem;
    margin: 0.75rem 0 0.35rem 0;
  }}

  .tp-folio-chip {{
    display: inline-flex;
    align-items: center;
    padding: 0.2rem 0.48rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.66rem;
    font-weight: 600;
    color: var(--tp-prussian);
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule-strong);
    text-decoration: none;
    transition: background-color 140ms ease, color 140ms ease;
  }}

  .tp-folio-chip:hover {{
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
    border-color: var(--tp-prussian);
  }}

  .tp-matrix-search-row {{
    margin: 0.65rem 0 0.75rem 0;
  }}

  .tp-matrix-search-input {{
    width: 100%;
    max-width: 680px;
    padding: 0.58rem 0.85rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.8rem;
    color: var(--tp-ink);
    background-color: var(--tp-vellum);
    border: 1.5px solid var(--tp-rule-strong);
    box-sizing: border-box;
  }}

  .tp-matrix-search-input:focus {{
    outline: 2px solid var(--tp-prussian);
    border-color: var(--tp-prussian);
  }}

  /* Mobile Editorial Pacing & De-Cluttering (@media max-width: 720px) */
  @media (max-width: 720px) {{
    .tp-masthead {{
      padding: 0.55rem 0.9rem;
    }}

    .tp-masthead-inner {{
      gap: 0.45rem;
    }}

    .tp-brand-sub {{
      font-size: 0.62rem;
    }}

    .tp-cat-badge {{
      display: none;
    }}

    .tp-nav {{
      width: 100%;
      flex-wrap: nowrap;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
      padding-bottom: 0.15rem;
      gap: 0.35rem;
    }}

    .tp-nav::-webkit-scrollbar {{
      display: none;
    }}

    .tp-nav-link,
    .tp-plate-btn {{
      flex: 0 0 auto;
      font-size: 0.7rem;
      padding: 0.28rem 0.55rem;
    }}

    .tp-volume-nav-bar {{
      padding: 0.35rem 0.9rem;
    }}

    .tp-crumb-title,
    .tp-vol-step-pos {{
      display: none;
    }}

    .tp-shell {{
      padding: 1rem 0.95rem 2.5rem;
    }}

    .tp-hero {{
      padding: 1.1rem 1rem;
    }}

    .tp-meta-pill-secondary {{
      display: none;
    }}

    .tp-meta-pill {{
      font-size: 0.62rem;
      padding: 0.18rem 0.45rem;
    }}

    .tp-h1 {{
      font-size: clamp(1.58rem, 6.4vw, 2.05rem);
      line-height: 1.16;
      letter-spacing: -0.015em;
    }}

    .tp-standfirst {{
      font-size: 1.06rem;
      line-height: 1.54;
    }}

    .tp-why-matters-lead {{
      padding: 0.8rem 0.95rem;
      margin: 0.85rem 0;
    }}

    .tp-why-matters-lead p {{
      font-size: 0.96rem;
    }}

    .tp-act-jump-bar {{
      flex-wrap: nowrap;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
      padding-bottom: 0.2rem;
    }}

    .tp-act-jump-bar::-webkit-scrollbar {{
      display: none;
    }}

    .tp-editorial-figure {{
      margin-left: 0;
      margin-right: 0;
    }}

    .tp-prose p {{
      font-size: 1.02rem;
      line-height: 1.72;
    }}

    .tp-pullquote {{
      font-size: 1.05rem;
      padding: 0.85rem 1rem;
    }}
  }}

  /* ---- Frontier Magazine Council: Literary Serif Prose, De-Boxed Byline, <tp-article-audio> Web Component & Zero-Overflow Contract ---- */
  .tp-h1,
  .tp-h2,
  .tp-standfirst,
  .tp-prose p,
  .tp-prose li,
  .tp-why-matters-lead p,
  .tp-pullquote,
  .tp-dropcap::first-letter {{
    font-family: var(--tp-font-editorial, Georgia, "Times New Roman", serif);
  }}

  .tp-prose p,
  .tp-prose li {{
    font-size: clamp(1.04rem, 1.08vw, 1.13rem);
    line-height: 1.76;
    letter-spacing: 0.002em;
    color: var(--tp-ink);
  }}

  .tp-prose > h2 {{
    padding-top: 1.35rem;
    margin-top: 2.1rem;
    border-top: 1px solid var(--tp-rule-strong);
  }}

  .tp-prose > h2:first-of-type {{
    margin-top: 0.5rem;
  }}

  .tp-reading-meta {{
    align-items: center;
    gap: 0.35rem 0.75rem;
    padding-bottom: 0.55rem;
    margin-bottom: 0.75rem;
    border-bottom: 1px solid var(--tp-rule);
  }}

  .tp-meta-pill {{
    background: transparent;
    border: none;
    padding: 0;
    font-size: 0.68rem;
    color: var(--tp-graphite);
  }}

  .tp-meta-pill + .tp-meta-pill::before {{
    content: "·";
    margin-right: 0.65rem;
    color: var(--tp-slate);
  }}

  .tp-meta-pill-verified {{
    color: var(--tp-verdigris);
    font-weight: 700;
  }}

  /* Native Bilingual Article Audio Web Component (<tp-article-audio>) */
  tp-article-audio.tp-article-audio {{
    display: flex;
    flex-direction: column;
    gap: 0.52rem;
    margin-top: 0.95rem;
    padding: 0.72rem 0.95rem;
    background-color: var(--tp-vellum);
    border: 1px solid var(--tp-rule-strong);
    border-left: 4px solid var(--tp-prussian);
    box-sizing: border-box;
    max-width: 100%;
  }}

  .tp-audio-top-row {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 0.65rem;
  }}

  .tp-audio-controls-left {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.4rem;
  }}

  .tp-audio-play-btn {{
    display: inline-flex;
    align-items: center;
    gap: 0.42rem;
    min-height: 36px;
    padding: 0.32rem 0.82rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: var(--tp-vellum);
    background-color: var(--tp-prussian);
    border: 1px solid var(--tp-prussian);
    cursor: pointer;
    touch-action: manipulation;
    -webkit-tap-highlight-color: transparent;
    box-sizing: border-box;
  }}

  .tp-audio-play-btn[aria-pressed="true"] {{
    background-color: var(--tp-verdigris);
    border-color: var(--tp-verdigris);
  }}

  .tp-audio-util-btn {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 36px;
    min-width: 36px;
    padding: 0.28rem 0.58rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.7rem;
    font-weight: 700;
    color: var(--tp-ink);
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule-strong);
    cursor: pointer;
    touch-action: manipulation;
    -webkit-tap-highlight-color: transparent;
    box-sizing: border-box;
  }}

  .tp-audio-voice-select {{
    max-width: 240px;
    text-overflow: ellipsis;
  }}

  .tp-audio-status-group {{
    display: flex;
    flex: 1 1 220px;
    flex-direction: column;
    gap: 0.25rem;
    min-width: 0;
  }}

  .tp-audio-status-text {{
    font-family: var(--font-mono, monospace);
    font-size: 0.68rem;
    color: var(--tp-graphite);
    overflow-wrap: anywhere;
  }}

  .tp-audio-progress {{
    width: 100%;
    height: 8px;
    cursor: pointer;
    touch-action: manipulation;
    accent-color: var(--tp-verdigris);
  }}

  @media (max-width: 720px) {{
    .tp-audio-play-btn,
    .tp-audio-util-btn {{
      min-height: 42px;
    }}
  }}

  .tp-audio-chapters {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.35rem;
    padding-top: 0.42rem;
    border-top: 1px dashed var(--tp-rule);
  }}

  .tp-audio-chapter-btn {{
    display: inline-flex;
    align-items: center;
    min-height: 32px;
    padding: 0.2rem 0.55rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.66rem;
    font-weight: 600;
    color: var(--tp-ink);
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule);
    cursor: pointer;
    box-sizing: border-box;
  }}

  .tp-audio-chapter-btn[aria-pressed="true"] {{
    background-color: var(--tp-prussian-soft);
    border-color: var(--tp-prussian);
    color: var(--tp-prussian);
    font-weight: 700;
  }}

  /* Strict Viewport Containment & Zero Horizontal Overflow Contract */
  .tp-volume-nav-inner {{
    position: relative;
  }}

  .tp-crumb-drawer {{
    position: static;
  }}

  .tp-crumb-drawer-panel {{
    position: absolute;
    left: 0;
    right: 0;
    top: calc(100% + 0.35rem);
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
  }}

  .tp-shell,
  #tp-folio-mount,
  #tp-active-folio-mount,
  .tp-folio-layout,
  .tp-folio-layout > *,
  .tp-prose,
  .tp-rail,
  .tp-dossier-strip,
  .tp-dossier-strip > *,
  details.tp-colophon-disclosure,
  details.tp-es-dossier,
  .tp-colophon-summary,
  .tp-es-summary,
  .tp-colophon-grid,
  .tp-colophon-cell,
  .tp-es-body,
  .tp-plate,
  .tp-plate-split-workbench,
  .tp-plate-split-workbench > *,
  .tp-svg-wrap,
  .tp-webgl-wrap,
  .tp-editorial-figure,
  .tp-editorial-badge-bar,
  .tp-editorial-caption,
  .tp-puzzle-atelier,
  .tp-cw-workbench,
  .tp-cw-clues-columns,
  .tp-skill-box {{
    min-width: 0;
    max-width: 100%;
    box-sizing: border-box;
  }}

  /* ---- Subtle Futuristic SVG Telemetry HUD & Interactive Bilingual Crossword Atelier ---- */
  .tp-futuristic-hud-strip {{
    width: 100%;
    margin-bottom: 0.65rem;
    padding: 0.18rem 0.45rem;
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule);
    border-left: 3px solid var(--tp-verdigris);
    box-sizing: border-box;
    overflow: hidden;
  }}

  .tp-futuristic-cadence-svg {{
    display: block;
    width: 100%;
    height: 26px;
  }}

  .tp-act-pill-puzzle {{
    border-color: var(--tp-verdigris);
    color: var(--tp-verdigris);
    font-weight: 700;
  }}

  .tp-puzzle-atelier {{
    margin: 2.25rem 0;
    padding: 1.45rem 1.55rem;
    scroll-margin-top: 6.2rem;
    background-color: var(--tp-vellum);
    border: 1.5px solid var(--tp-rule-strong);
    border-top: 4px solid var(--tp-prussian);
    display: flex;
    flex-direction: column;
    gap: 1.05rem;
  }}

  .tp-puzzle-atelier.is-puzzle-solved {{
    border-top-color: var(--tp-verdigris);
    box-shadow: inset 0 0 0 1px var(--tp-verdigris);
  }}

  .tp-puzzle-header {{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: flex-start;
    gap: 1rem;
    padding-bottom: 0.9rem;
    border-bottom: 1px solid var(--tp-rule-strong);
  }}

  .tp-puzzle-header-left {{
    display: flex;
    align-items: flex-start;
    gap: 0.95rem;
    flex: 1 1 460px;
    min-width: 0;
  }}

  .tp-puzzle-seal-wrap {{
    flex: 0 0 48px;
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule-strong);
  }}

  .tp-puzzle-title-stack {{
    display: flex;
    flex-direction: column;
    gap: 0.28rem;
    min-width: 0;
  }}

  .tp-puzzle-sub {{
    margin: 0;
    font-size: 0.92rem;
    line-height: 1.5;
    color: var(--tp-graphite);
  }}

  .tp-puzzle-header-right {{
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 0.45rem;
    flex: 0 1 320px;
  }}

  .tp-cw-edition-badge {{
    display: inline-flex;
    align-items: center;
    padding: 0.22rem 0.58rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.66rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    color: var(--tp-prussian);
    background-color: var(--tp-prussian-soft);
    border: 1px solid var(--tp-prussian);
  }}

  .tp-passport-bar {{
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
    padding: 0.45rem 0.68rem;
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule-strong);
    width: 100%;
    box-sizing: border-box;
  }}

  .tp-passport-count {{
    font-family: var(--font-mono, monospace);
    font-size: 0.67rem;
    font-weight: 700;
    color: var(--tp-ink);
  }}

  .tp-passport-progress,
  .tp-cw-word-progress {{
    width: 100%;
    height: 6px;
    accent-color: var(--tp-verdigris);
  }}

  .tp-cw-active-bar {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 0.65rem;
    padding: 0.58rem 0.85rem;
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule-strong);
    border-left: 4px solid var(--tp-prussian);
  }}

  .tp-cw-active-clue-dir {{
    font-family: var(--font-mono, monospace);
    font-size: 0.72rem;
    font-weight: 700;
    padding: 0.16rem 0.48rem;
    color: var(--tp-vellum);
    background-color: var(--tp-prussian);
    letter-spacing: 0.04em;
  }}

  .tp-cw-active-clue-text {{
    flex: 1 1 320px;
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--tp-ink);
  }}

  .tp-cw-active-bar .tp-cw-word-progress {{
    flex: 0 0 130px;
    width: 130px;
  }}

  .tp-cw-workbench {{
    display: grid;
    grid-template-columns: minmax(310px, 430px) minmax(0, 1fr);
    gap: 1.45rem;
    align-items: start;
  }}

  .tp-crossword-stage-wrap {{
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }}

  .tp-crossword-grid {{
    display: grid;
    grid-template-rows: repeat(10, minmax(0, 1fr));
    width: 100%;
    max-width: 420px;
    aspect-ratio: 1 / 1;
    background-color: var(--tp-mortar);
    border: 2px solid var(--tp-rule-strong);
    gap: 1px;
    box-sizing: border-box;
    user-select: none;
  }}

  .tp-cw-row {{
    display: grid;
    grid-template-columns: repeat(10, minmax(0, 1fr));
    gap: 1px;
  }}

  .tp-cw-cell {{
    position: relative;
    width: 100%;
    height: 100%;
    min-height: 28px;
    padding: 0;
    margin: 0;
    border: none;
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
    font-family: var(--font-mono, monospace);
  }}

  .tp-cw-cell.is-block {{
    background-color: var(--tp-mortar);
    background-image: repeating-linear-gradient(
      -45deg,
      transparent,
      transparent 4px,
      var(--tp-rule) 4px,
      var(--tp-rule) 5px
    );
  }}

  .tp-cw-cell.is-letter {{
    background-color: var(--tp-vellum);
    color: var(--tp-ink);
    cursor: pointer;
    transition: background-color 120ms ease, color 120ms ease;
  }}

  .tp-cw-cell.is-letter.is-word-highlight {{
    background-color: var(--tp-prussian-soft);
    color: var(--tp-ink);
  }}

  html[data-theme="blueprint"] .tp-cw-cell.is-letter.is-word-highlight,
  html[data-theme="dark"] .tp-cw-cell.is-letter.is-word-highlight,
  html[data-plate-theme="dark"] .tp-cw-cell.is-letter.is-word-highlight {{
    background-color: var(--tp-prussian-soft);
    color: var(--tp-ink);
  }}

  .tp-cw-cell.is-letter.is-active-cell {{
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
  }}

  .tp-cw-cell.is-letter.is-active-cell .tp-cw-num {{
    color: var(--tp-vellum);
  }}

  .tp-cw-cell.is-letter.is-correct {{
    box-shadow: inset 0 0 0 2px var(--tp-verdigris);
  }}

  .tp-cw-cell.is-letter.is-wrong {{
    box-shadow: inset 0 0 0 2px var(--tp-minium);
    color: var(--tp-minium);
  }}

  .tp-cw-num {{
    position: absolute;
    top: 2px;
    left: 3px;
    font-size: 0.56rem;
    font-weight: 700;
    line-height: 1;
    color: var(--tp-graphite);
    pointer-events: none;
  }}

  .tp-cw-char {{
    font-size: 1.02rem;
    font-weight: 800;
    line-height: 1;
    letter-spacing: 0.02em;
    margin-top: 4px;
    pointer-events: none;
  }}

  .tp-cw-toolbar {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.38rem;
  }}

  .tp-cw-btn {{
    font-family: var(--font-mono, monospace);
    font-size: 0.68rem;
    font-weight: 700;
    padding: 0.36rem 0.62rem;
    min-height: 34px;
    color: var(--tp-ink);
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule-strong);
    cursor: pointer;
    touch-action: manipulation;
    -webkit-tap-highlight-color: transparent;
    box-sizing: border-box;
  }}

  .tp-cw-btn:hover {{
    border-color: var(--tp-prussian);
    background-color: var(--tp-mortar);
  }}

  .tp-cw-btn-primary {{
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
    border-color: var(--tp-prussian);
  }}

  .tp-cw-btn-primary:hover {{
    background-color: var(--tp-verdigris);
    border-color: var(--tp-verdigris);
    color: var(--tp-vellum);
  }}

  .tp-cw-clues-columns {{
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.15rem;
  }}

  .tp-cw-clue-col {{
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule-strong);
    padding: 0.85rem 0.95rem;
    display: flex;
    flex-direction: column;
    gap: 0.55rem;
  }}

  .tp-cw-clue-heading {{
    margin: 0;
    padding-bottom: 0.38rem;
    border-bottom: 1.5px solid var(--tp-prussian);
    font-family: var(--font-mono, monospace);
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--tp-ink);
  }}

  .tp-cw-clues-list {{
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
  }}

  .tp-cw-clue-item {{
    margin: 0;
  }}

  .tp-cw-clue-btn {{
    width: 100%;
    text-align: left;
    padding: 0.42rem 0.55rem;
    background-color: var(--tp-vellum);
    border: 1px solid var(--tp-rule);
    border-left: 3px solid transparent;
    color: var(--tp-ink);
    font-size: 0.84rem;
    line-height: 1.42;
    cursor: pointer;
    display: flex;
    flex-wrap: wrap;
    gap: 0.28rem;
    align-items: baseline;
    box-sizing: border-box;
  }}

  .tp-cw-clue-item.is-active-clue .tp-cw-clue-btn {{
    border-color: var(--tp-prussian);
    border-left-color: var(--tp-prussian);
    background-color: var(--tp-prussian-soft);
    font-weight: 600;
  }}

  .tp-cw-clue-item.is-clue-complete .tp-cw-clue-btn {{
    border-left-color: var(--tp-verdigris);
    color: var(--tp-graphite);
  }}

  .tp-cw-clue-item.is-clue-complete .tp-cw-clue-num {{
    color: var(--tp-verdigris);
  }}

  .tp-cw-clue-num {{
    font-family: var(--font-mono, monospace);
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--tp-prussian);
    min-width: 1.35rem;
  }}

  .tp-cw-clue-meta {{
    font-family: var(--font-mono, monospace);
    font-size: 0.68rem;
    color: var(--tp-graphite);
  }}

  .tp-cw-status-readout {{
    margin: 0;
    padding: 0.45rem 0.72rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.73rem;
    color: var(--tp-graphite);
    background-color: var(--tp-stone);
    border: 1px solid var(--tp-rule);
  }}

  .tp-cw-status-readout.is-status-ok {{
    color: var(--tp-verdigris);
    border-color: var(--tp-verdigris);
    background-color: var(--tp-verdigris-soft);
    font-weight: 700;
  }}

  .tp-cw-status-readout.is-status-warn {{
    color: var(--tp-minium);
    border-color: var(--tp-minium);
    font-weight: 700;
  }}

  .tp-rack-card-meta {{
    display: inline-flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.32rem;
  }}

  .tp-rack-solved-seal {{
    display: inline-flex;
    align-items: center;
    padding: 0.08rem 0.38rem;
    font-family: var(--font-mono, monospace);
    font-size: 0.62rem;
    font-weight: 700;
    color: var(--tp-verdigris);
    background-color: var(--tp-verdigris-soft);
    border: 1px solid var(--tp-verdigris);
    margin-left: 0.25rem;
  }}

  @media (prefers-reduced-motion: no-preference) {{
    @keyframes tpFuturisticWaveFlow {{
      to {{
        stroke-dashoffset: -52;
      }}
    }}

    @keyframes tpReticleOrbit {{
      to {{
        transform: rotate(360deg);
      }}
    }}

    @keyframes tpScanBeamGlide {{
      0%, 100% {{
        transform: translateX(0);
        stroke-opacity: 0.12;
      }}
      50% {{
        transform: translateX(220px);
        stroke-opacity: 0.34;
      }}
    }}

    @keyframes tpPuzzleSealPulse {{
      0%, 100% {{
        transform: scale(1);
      }}
      50% {{
        transform: scale(1.16);
      }}
    }}

    .tp-futuristic-wave-primary {{
      animation: tpFuturisticWaveFlow 3.4s linear infinite;
    }}

    .tp-futuristic-wave-secondary {{
      animation: tpFuturisticWaveFlow 5.2s linear infinite reverse;
    }}

    .tp-futuristic-reticle,
    .tp-svg-orbit-reticle,
    .tp-seal-outer-ring {{
      transform-box: fill-box;
      transform-origin: center;
      animation: tpReticleOrbit 14s linear infinite;
    }}

    .tp-futuristic-reticle-right,
    .tp-seal-inner-ring {{
      transform-box: fill-box;
      transform-origin: center;
      animation: tpReticleOrbit 10s linear infinite reverse;
    }}

    .tp-svg-scan-beam {{
      animation: tpScanBeamGlide 7.5s ease-in-out infinite;
    }}

    .tp-puzzle-atelier.is-puzzle-solved .tp-seal-core-node {{
      transform-box: fill-box;
      transform-origin: center;
      animation: tpPuzzleSealPulse 1.8s ease-in-out infinite;
    }}
  }}

  .tp-shell {{
    overflow-x: clip;
  }}

  .tp-plate-live-badge {{
    display: inline-flex;
    flex-wrap: wrap;
    align-items: center;
    min-height: 24px;
    height: auto;
    max-width: 100%;
    padding: 0.2rem 0.5rem;
    white-space: normal;
    overflow-wrap: anywhere;
    word-break: break-word;
    box-sizing: border-box;
  }}

  .tp-shell code,
  .tp-prose code,
  .tp-es-body code,
  .tp-colophon-val,
  .tp-kicker,
  .tp-scite-badge-link,
  .tp-cite-link,
  .tp-colophon-summary span,
  .tp-colophon-summary strong,
  .tp-es-summary span,
  .tp-es-summary strong {{
    overflow-wrap: anywhere;
    word-break: break-word;
  }}

  .tp-table-wrap {{
    width: 100%;
    max-width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    box-sizing: border-box;
  }}

  @media (max-width: 900px) {{
    .tp-masthead {{
      padding: 0.45rem 0.9rem;
    }}

    .tp-masthead-inner {{
      padding: 0;
      gap: 0.4rem;
    }}

    .tp-cat-badge {{
      display: none;
    }}

    .tp-nav {{
      width: 100%;
      flex-wrap: nowrap;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
      gap: 0.35rem;
    }}

    .tp-nav::-webkit-scrollbar {{
      display: none;
    }}

    .tp-crumb-title,
    .tp-vol-step-pos {{
      display: none;
    }}

    .tp-folio-layout,
    .tp-dossier-strip,
    .tp-colophon-grid,
    .tp-plate-split-workbench,
    .tp-dispatch-grid,
    .tp-volumes-grid,
    .tp-issue-cards,
    .tp-cw-workbench,
    .tp-cw-clues-columns {{
      grid-template-columns: minmax(0, 1fr);
    }}
  }}
}}

@layer overrides {{
  .tp-body strong,
  .tp-body b,
  .tp-body em,
  .tp-body i {{
    color: inherit;
  }}

  .tp-body td {{
    color: var(--tp-graphite);
  }}

  .tp-body th {{
    color: var(--tp-ink);
  }}

  .tp-body a {{
    color: var(--tp-prussian);
  }}

  .tp-body .tp-brand,
  .tp-body .tp-rack-card,
  .tp-body .tp-topic-article-link,
  .tp-body .tp-act-pill,
  .tp-body .tp-crumb-link {{
    color: var(--tp-ink);
  }}

  .tp-body .tp-topic-article-link[data-active-folio="true"],
  .tp-body .tp-vol-sibling-pill[data-active-folio="true"],
  .tp-body .tp-crumb-drawer-toggle,
  .tp-body .tp-act-pill-highlight,
  .tp-body .tp-audio-play-btn,
  .tp-body .tp-cw-btn-primary,
  .tp-body .tp-cw-cell.is-letter.is-active-cell,
  .tp-body .tp-cw-active-clue-dir,
  .tp-body .tp-skill-btn:not(.tp-skill-btn-secondary) {{
    color: var(--tp-vellum);
  }}

  .tp-body .tp-skill-btn.tp-skill-btn-secondary {{
    color: var(--tp-ink);
    background-color: var(--tp-stone);
  }}

  .tp-body .tp-cw-cell.is-letter {{
    background-color: var(--tp-vellum);
    color: var(--tp-ink);
  }}

  .tp-body .tp-cw-cell.is-letter.is-word-highlight {{
    background-color: var(--tp-prussian-soft);
    color: var(--tp-ink);
  }}

  html[data-theme="blueprint"] .tp-body .tp-cw-cell.is-letter.is-word-highlight,
  html[data-theme="dark"] .tp-body .tp-cw-cell.is-letter.is-word-highlight,
  html[data-plate-theme="dark"] .tp-body .tp-cw-cell.is-letter.is-word-highlight {{
    background-color: var(--tp-prussian-soft);
    color: var(--tp-ink);
  }}

  .tp-body .tp-cw-cell.is-letter.is-active-cell {{
    background-color: var(--tp-prussian);
    color: var(--tp-vellum);
  }}

  .tp-body .skip-link {{
    background-color: var(--tp-ink);
    color: var(--tp-vellum);
  }}

  .tp-body code {{
    color: var(--tp-code-fg, var(--tp-prussian));
    background-color: var(--tp-mortar);
    padding: 0.1rem 0.34rem;
    border-radius: 3px;
  }}

  .tp-body .tp-human-potential-box {{
    background-color: var(--tp-vellum);
  }}

  .tp-body .skip-link:focus,
  .tp-body .skip-link:focus-visible {{
    position: fixed;
    top: 0.65rem;
    left: 0.65rem;
    z-index: 9999;
    padding: 0.55rem 1rem;
    background-color: var(--tp-ink);
    color: var(--tp-vellum);
    font-family: var(--tp-font-mono);
    font-size: 0.82rem;
    font-weight: 700;
    text-decoration: none;
    outline: 3px solid var(--tp-minium);
    outline-offset: 2px;
  }}

  .tp-body a:focus-visible,
  .tp-body button:focus-visible,
  .tp-body input:focus-visible,
  .tp-body select:focus-visible,
  .tp-body summary:focus-visible,
  .tp-body [tabindex="0"]:focus-visible,
  .tp-body .tp-scrub:focus-visible,
  .tp-body .tp-webgl-canvas:focus-visible {{
    outline: 3px solid var(--tp-minium);
    outline-offset: 2px;
    box-shadow: 0 0 0 2px var(--tp-vellum);
  }}
}}
"""
    css = css.rstrip()
    if css.endswith("}"):
        css = css[:-1].rstrip() + "\n\n" + addition
    css = css.rstrip() + "\n" + REVAMP_CSS
    css_path.write_text(css, encoding="utf-8")
