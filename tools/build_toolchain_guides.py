#!/usr/bin/env python3
"""Build standalone bilingual (/toolchain/<slug>/ and /es-mx/toolchain/<slug>/) guide pages.

Covers the two methodology & formal-verification companions under Tech & Tools:
  - /toolchain/proof-observatory/  (Lean 4 Proof Observatory & Formal Math)
  - /toolchain/ai-loop/            (The AI Loop: Local Models & Deterministic Verifiers)

Kept separate from TOOLCHAIN_FOLIOS (X.01..X.07 3D CAD generators) so CAD-specific
byte-manifest suites remain focused on neutral 3D/2D geometry while sharing the exact
Informatico.ai masthead, contents dialog, footer, strict CSP, and Spanish twin pipeline.
"""
from __future__ import annotations

from pathlib import Path
import sys

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import build_longform_folios as B  # noqa: E402

GUIDE_DATE_PUBLISHED = "2026-11-22"
GUIDE_DATE_MODIFIED = "2026-11-22"

GUIDE_SLUGS = ("proof-observatory", "ai-loop")

GUIDE_SEO: dict[str, tuple[str, str, str, str]] = {
    "proof-observatory": (
        "Lean 4 Proof Observatory & Formal Math",
        "How Lean 4 kernel checking works and how to audit public repositories on Fermat's Last Theorem, zeta zeros, 3SUM-APSP, and k-CNF counting.",
        "Observatorio de Pruebas en Lean 4",
        "Cómo funciona el núcleo de Lean 4 y cómo auditar repositorios públicos sobre Fermat, ceros de zeta, algoritmos 3SUM-APSP y conteo k-CNF.",
    ),
    "ai-loop": (
        "The AI Loop · Local Models & Verifiers",
        "Architecture for pairing open-weight local models on Ollama with frontier orchestration, tool-free diff review, and planted-defect Python verifiers.",
        "El Ciclo de IA · Modelos Locales y Verificación",
        "Arquitectura para combinar modelos locales en Ollama con orquestación de frontera, revisión ciega de cambios y verificadores en Python con defectos.",
    ),
}

GUIDE_CARDS: dict[str, dict[str, str]] = {
    "proof-observatory": {
        "code": "METHODOLOGY · LEAN 4",
        "plate": "m12",
        "reading_en": "12 min read",
        "reading_es": "12 min de lectura",
        "title_en": "Lean 4 Proof Observatory · Kernel Architecture & Auditing Public Formalizations",
        "title_es": "Observatorio de Pruebas en Lean 4 · Arquitectura del Núcleo y Auditoría de Repositorios",
        "dek_en": "How Lean 4's small trusted kernel checks proofs, what four public Lean 4 projects state in their READMEs, and three commands to audit them yourself.",
        "dek_es": "Cómo el núcleo pequeño de Lean 4 revisa demostraciones, qué declaran cuatro proyectos públicos en Lean 4 en sus README y tres comandos para auditarlos tú mismo.",
    },
    "ai-loop": {
        "code": "ARCHITECTURE · AI LOOP",
        "plate": "x01",
        "reading_en": "11 min read",
        "reading_es": "11 min de lectura",
        "title_en": "The AI Loop · Open-Weight Local Workers, Blind Diff Review & Deterministic Verifiers",
        "title_es": "El Ciclo de IA · Modelos Locales Abiertos, Revisión Ciega de Cambios y Verificadores Deterministas",
        "dek_en": "Why reliable engineering separates scoping, local Ollama generation, deterministic Python verifiers, and tool-free cross-lineage diff review instead of trusting single-model prose.",
        "dek_es": "Por qué la ingeniería confiable separa planeación, generación local en Ollama, verificadores deterministas en Python y revisión ciega entre linajes en vez de confiar en un solo modelo.",
    },
}


def bi(tag: str, en: str, es: str, cls: str = "", extra_attrs: str = "") -> str:
    """Render an element whose text is plain (no child markup) with data-en and data-es."""
    cls_attr = f' class="{cls}"' if cls else ""
    extra = f" {extra_attrs.strip()}" if extra_attrs.strip() else ""
    return f'<{tag}{cls_attr}{extra} data-en="{B.esc(en)}" data-es="{B.esc(es)}">{B.esc(en)}</{tag}>'


def sp(en: str, es: str) -> str:
    """Inline plain-text bilingual span safe inside mixed paragraphs containing <code> or <a>."""
    return bi("span", en, es)


def _svg_bi_text(x: int | float, y: int | float, en: str, es: str, attrs: str) -> str:
    """Render an SVG <text> node with data-en and data-es so to_spanish_static swaps it cleanly."""
    return f'<text x="{x}" y="{y}" {attrs} data-en="{B.esc(en)}" data-es="{B.esc(es)}">{B.esc(en)}</text>'


def _render_proof_svg() -> str:
    """Zero-inline-style bilingual SVG schematic of the 4-stage Lean 4 formalization & kernel-audit pipeline."""
    return f"""        <figure class="tp-editorial-figure" role="group" aria-labelledby="proof-fig-cap">
          <svg class="tp-svg-stage" viewBox="0 0 920 250" role="img" aria-labelledby="proof-dag-title proof-dag-desc">
            {bi("title", "Lean 4 Formalization Pipeline from Theorem Statement to Independent Kernel Replay", "Tubería de Formalización en Lean 4 desde el Enunciado hasta la Reproducción en el Núcleo", extra_attrs='id="proof-dag-title"')}
            {bi("desc", "Four sequential stages: 1. Explicit .lean theorem signature, 2. Dependency blueprint DAG, 3. Automated and human tactic search, and 4. Small trusted kernel replay checking sorryAx and axioms.", "Cuatro etapas secuenciales: 1. Firma explícita del teorema .lean, 2. Grafo DAG de lemas, 3. Búsqueda de tácticas humana o asistida, y 4. Reproducción en el núcleo revisando sorryAx y axiomas.", extra_attrs='id="proof-dag-desc"')}
            <rect x="12" y="14" width="896" height="222" rx="8" fill="#f5f1e8" stroke="#b9afa0" stroke-width="1.5"/>
            <rect x="32" y="48" width="190" height="142" rx="6" fill="#ffffff" stroke="#1f3a52" stroke-width="1.8"/>
            {_svg_bi_text(127, 74, "STAGE 01 · STATEMENT", "ETAPA 01 · ENUNCIADO", 'text-anchor="middle" font-family="monospace" font-size="11" font-weight="700" fill="#1f3a52"')}
            {_svg_bi_text(127, 100, "Top-Level .lean Spec", "Firma Principal .lean", 'text-anchor="middle" font-family="serif" font-size="14" font-weight="700" fill="#16191d"')}
            {_svg_bi_text(127, 124, "Human-audited definitions", "Definiciones auditadas", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#3c434a"')}
            {_svg_bi_text(127, 142, "Explicit hypotheses & types", "Hipótesis y tipos explícitos", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#3c434a"')}
            {_svg_bi_text(127, 168, "Inspect premises first", "Revisar premisas primero", 'text-anchor="middle" font-family="monospace" font-size="10.5" fill="#7a2e1d"')}

            <line x1="222" y1="119" x2="252" y2="119" stroke="#1f3a52" stroke-width="2"/>
            <polygon points="252,119 244,114 244,124" fill="#1f3a52"/>

            <rect x="256" y="48" width="190" height="142" rx="6" fill="#ffffff" stroke="#1f3a52" stroke-width="1.8"/>
            {_svg_bi_text(351, 74, "STAGE 02 · BLUEPRINT", "ETAPA 02 · GRAFO DAG", 'text-anchor="middle" font-family="monospace" font-size="11" font-weight="700" fill="#1f3a52"')}
            {_svg_bi_text(351, 100, "Lemma DAG Decomposition", "Descomposición en Lemas", 'text-anchor="middle" font-family="serif" font-size="14" font-weight="700" fill="#16191d"')}
            {_svg_bi_text(351, 124, "Isolates subgoals & interfaces", "Aísla submetas e interfaces", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#3c434a"')}
            {_svg_bi_text(351, 142, "Parallelizes proof obligations", "Paraleliza obligaciones", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#3c434a"')}
            <text x="351" y="168" text-anchor="middle" font-family="monospace" font-size="10.5" fill="#7a2e1d">Mathlib4 + local lemmas</text>

            <line x1="446" y1="119" x2="476" y2="119" stroke="#1f3a52" stroke-width="2"/>
            <polygon points="476,119 468,114 468,124" fill="#1f3a52"/>

            <rect x="480" y="48" width="190" height="142" rx="6" fill="#ffffff" stroke="#8a6421" stroke-width="1.8"/>
            {_svg_bi_text(575, 74, "STAGE 03 · SEARCH", "ETAPA 03 · BÚSQUEDA", 'text-anchor="middle" font-family="monospace" font-size="11" font-weight="700" fill="#8a6421"')}
            {_svg_bi_text(575, 100, "Tactic & Witness Synthesis", "Síntesis de Tácticas", 'text-anchor="middle" font-family="serif" font-size="14" font-weight="700" fill="#16191d"')}
            {_svg_bi_text(575, 124, "Untrusted AI or human tactics", "Tácticas humanas o de IA", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#3c434a"')}
            {_svg_bi_text(575, 142, "Elaborator rejects type drift", "Rechaza desvíos de tipos", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#3c434a"')}
            <text x="575" y="168" text-anchor="middle" font-family="monospace" font-size="10.5" fill="#8a6421">simp · ring · linarith · exact</text>

            <line x1="670" y1="119" x2="700" y2="119" stroke="#1d5c3f" stroke-width="2.2"/>
            <polygon points="700,119 692,114 692,124" fill="#1d5c3f"/>

            <rect x="704" y="48" width="184" height="142" rx="6" fill="#eef6f1" stroke="#1d5c3f" stroke-width="2.2"/>
            {_svg_bi_text(796, 74, "STAGE 04 · KERNEL GATE", "ETAPA 04 · NÚCLEO", 'text-anchor="middle" font-family="monospace" font-size="11" font-weight="700" fill="#1d5c3f"')}
            {_svg_bi_text(796, 100, "Independent Kernel Replay", "Reproducción del Núcleo", 'text-anchor="middle" font-family="serif" font-size="14" font-weight="700" fill="#16191d"')}
            {_svg_bi_text(796, 124, "Check #print axioms", "Revisar #print axioms", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#1d5c3f"')}
            {_svg_bi_text(796, 142, "Refuse any sorryAx", "Rechazar todo sorryAx", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#1d5c3f"')}
            <text x="796" y="168" text-anchor="middle" font-family="monospace" font-size="10.5" fill="#1d5c3f">lake build + lean4checker</text>

            {_svg_bi_text(460, 218, "Creative search may hallucinate in Stage 03; verification requires both Stage 04 kernel replay and human Stage 01 statement audit.", "La búsqueda en la Etapa 03 puede alucinar; verificar exige tanto reproducir la Etapa 04 como auditar el enunciado en la Etapa 01.", 'text-anchor="middle" font-family="monospace" font-size="10.8" fill="#3c434a"')}
          </svg>
          {bi("figcaption", "Four-stage Lean 4 pipeline: untrusted tactic search stays separate from a small, independently replayable type-checking kernel.", "Tubería de cuatro etapas en Lean 4: la búsqueda no confiable de tácticas queda separada de un núcleo pequeño y reproducible de revisión de tipos.", "tp-editorial-caption", 'id="proof-fig-cap"')}
        </figure>"""


def _render_ai_loop_svg() -> str:
    """Zero-inline-style bilingual SVG schematic of the Orchestrator -> Local Worker -> Verifier -> Blind Diff Challenger loop."""
    return f"""        <figure class="tp-editorial-figure" role="group" aria-labelledby="ai-loop-fig-cap">
          <svg class="tp-svg-stage" viewBox="0 0 920 265" role="img" aria-labelledby="ai-loop-title ai-loop-desc">
            {bi("title", "Local-First AI Loop with Deterministic Verifiers and Blind Cross-Lineage Diff Review", "Ciclo de IA Local con Verificadores Deterministas y Revisión Ciega entre Linajes", extra_attrs='id="ai-loop-title"')}
            {bi("desc", "Closed verification loop connecting Scoping Orchestrator, Local Open-Weight Worker on Ollama, Deterministic Python Verifier, and Tool-Free Cross-Lineage Diff Challenger.", "Ciclo cerrado de verificación que conecta Orquestador, Modelo Local en Ollama, Verificador Determinista en Python y Revisor Ciego de Otro Linaje.", extra_attrs='id="ai-loop-desc"')}
            <rect x="12" y="14" width="896" height="237" rx="8" fill="#f5f1e8" stroke="#b9afa0" stroke-width="1.5"/>

            <rect x="30" y="42" width="192" height="132" rx="6" fill="#ffffff" stroke="#1f3a52" stroke-width="1.8"/>
            {_svg_bi_text(126, 68, "ROLE 01 · ORCHESTRATOR", "ROL 01 · ORQUESTADOR", 'text-anchor="middle" font-family="monospace" font-size="11" font-weight="700" fill="#1f3a52"')}
            {_svg_bi_text(126, 93, "Bounded Task Packet", "Paquete de Tarea Acotado", 'text-anchor="middle" font-family="serif" font-size="14" font-weight="700" fill="#16191d"')}
            {_svg_bi_text(126, 116, "Explicit file scope & spec", "Alcance y archivos exactos", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#3c434a"')}
            {_svg_bi_text(126, 134, "Done criteria written first", "Criterio escrito antes", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#3c434a"')}
            {_svg_bi_text(126, 156, "1 repo · isolated worktree", "1 repo · árbol aislado", 'text-anchor="middle" font-family="monospace" font-size="10.5" fill="#1f3a52"')}

            <line x1="222" y1="108" x2="252" y2="108" stroke="#1f3a52" stroke-width="2"/>
            <polygon points="252,108 244,103 244,113" fill="#1f3a52"/>

            <rect x="256" y="42" width="192" height="132" rx="6" fill="#ffffff" stroke="#8a6421" stroke-width="1.8"/>
            {_svg_bi_text(352, 68, "ROLE 02 · LOCAL WORKER", "ROL 02 · MODELO LOCAL", 'text-anchor="middle" font-family="monospace" font-size="11" font-weight="700" fill="#8a6421"')}
            {_svg_bi_text(352, 93, "Open-Weight Ollama GPU", "GPU Local con Ollama", 'text-anchor="middle" font-family="serif" font-size="14" font-weight="700" fill="#16191d"')}
            {_svg_bi_text(352, 116, "Drafts bounded code or JSON", "Borradores de código o JSON", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#3c434a"')}
            {_svg_bi_text(352, 134, "Zero cloud data egress", "Cero salida de datos", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#3c434a"')}
            <text x="352" y="156" text-anchor="middle" font-family="monospace" font-size="10.5" fill="#8a6421">Qwen · Gemma · Nemotron</text>

            <line x1="448" y1="108" x2="478" y2="108" stroke="#1f3a52" stroke-width="2"/>
            <polygon points="478,108 470,103 470,113" fill="#1f3a52"/>

            <rect x="482" y="42" width="192" height="132" rx="6" fill="#eef6f1" stroke="#1d5c3f" stroke-width="2.2"/>
            {_svg_bi_text(578, 68, "ROLE 03 · VERIFIER GATE", "ROL 03 · VERIFICADOR", 'text-anchor="middle" font-family="monospace" font-size="11" font-weight="700" fill="#1d5c3f"')}
            {_svg_bi_text(578, 93, "Deterministic Stdlib Check", "Prueba Determinista Stdlib", 'text-anchor="middle" font-family="serif" font-size="14" font-weight="700" fill="#16191d"')}
            {_svg_bi_text(578, 116, "Exact math, CSP & mesh laws", "Matemática, CSP y mallas", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#1d5c3f"')}
            {_svg_bi_text(578, 134, "Must reject planted defect", "Rechaza defecto plantado", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#1d5c3f"')}
            <text x="578" y="156" text-anchor="middle" font-family="monospace" font-size="10.5" fill="#1d5c3f">verify_*.py --planted-defect</text>

            <line x1="674" y1="108" x2="704" y2="108" stroke="#1d5c3f" stroke-width="2"/>
            <polygon points="704,108 696,103 696,113" fill="#1d5c3f"/>

            <rect x="708" y="42" width="182" height="132" rx="6" fill="#ffffff" stroke="#7a2e1d" stroke-width="1.8"/>
            {_svg_bi_text(799, 68, "ROLE 04 · CHALLENGER", "ROL 04 · REVISOR CIEGO", 'text-anchor="middle" font-family="monospace" font-size="11" font-weight="700" fill="#7a2e1d"')}
            {_svg_bi_text(799, 93, "Blind Cross-Lineage Diff", "Diff entre Otro Linaje", 'text-anchor="middle" font-family="serif" font-size="14" font-weight="700" fill="#16191d"')}
            {_svg_bi_text(799, 116, "Reads git diff with 0 tools", "Lee git diff sin herramientas", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#3c434a"')}
            {_svg_bi_text(799, 134, "Caged in <untrusted_data>", "Aislado en <untrusted_data>", 'text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#3c434a"')}
            {_svg_bi_text(799, 156, "Human maintainer merges", "Persona mantenedora fusiona", 'text-anchor="middle" font-family="monospace" font-size="10.5" fill="#7a2e1d"')}

            <path d="M 578 174 L 578 210 L 352 210 L 352 178" fill="none" stroke="#9e2a2b" stroke-width="1.8" stroke-dasharray="5,4"/>
            <polygon points="352,174 347,182 357,182" fill="#9e2a2b"/>
            {_svg_bi_text(465, 228, "NON-ZERO EXIT OR DEFECT FOUND · Return exact traceback (max 2 bounded repair rounds)", "SALIDA NO CERO O DEFECTO HALLADO · Devuelve rastreo exacto (máximo 2 rondas acotadas)", 'text-anchor="middle" font-family="monospace" font-size="10.8" fill="#9e2a2b"')}
          </svg>
          {bi("figcaption", "Architecture of the AI Loop: models draft and challenge diffs across distinct training lineages, while deterministic Python verifiers hold hard veto power.", "Arquitectura del Ciclo de IA: los modelos redactan y cuestionan cambios entre distintos linajes de entrenamiento, mientras que los verificadores deterministas en Python conservan el veto duro.", "tp-editorial-caption", 'id="ai-loop-fig-cap"')}
        </figure>"""


def render_proof_observatory_body(lang: str = "en") -> str:
    """Main content for /toolchain/proof-observatory/ with full EN + ES-MX parity and honest README attribution."""
    es = lang == "es"
    lbl_qs = "Audita formalizaciones en Lean 4 en tres pasos" if es else "Audit Lean 4 formalizations in three steps"
    lbl_jump = "Secciones del Observatorio de Pruebas en Lean 4" if es else "Sections of the Lean 4 Proof Observatory"
    lbl_plain = "En palabras sencillas" if es else "In plain words"
    lbl_table = "Repositorios públicos en Lean 4 tal como los describen sus propios README" if es else "Public Lean 4 repositories as described by their own READMEs"

    return f"""    <div class="tp-studio-quickstart" role="region" aria-label="{B.esc(lbl_qs)}">
      <div class="tp-studio-quickstart-head">
        {bi("span", "⚡ 3-STEP KERNEL AUDIT · HOW TO CHECK A FORMAL PROOF YOURSELF", "⚡ AUDITORÍA DEL NÚCLEO EN 3 PASOS · CÓMO VERIFICAR UNA PRUEBA FORMAL", "tp-studio-quickstart-badge")}
        {bi("span", "Built for mathematicians, computer scientists, engineers, and curious readers.", "Diseñado para matemáticos, científicos de la computación, ingenieros y lectores curiosos.", "tp-studio-quickstart-sub")}
      </div>
      <div class="tp-studio-steps-grid">
        <div class="tp-studio-step-card">
          {bi("span", "Step 1 · Read the Top-Level Theorem", "Paso 1 · Lee el Teorema Principal", "tp-studio-step-num")}
          {bi("h2", "Audit Definitions Before Claims", "Audita Primero las Definiciones", "tp-studio-step-title")}
          <p>{sp("Open the public ", "Abre los archivos ")}<code>.lean</code>{sp(" files on GitHub. Check whether the formal signature states the intended theorem without vacuous premises or altered definitions.", " públicos en GitHub. Comprueba si la firma formal expresa el teorema previsto sin premisas vacías ni definiciones alteradas.")}</p>
        </div>
        <div class="tp-studio-step-card">
          {bi("span", "Step 2 · Run the Trusted Kernel Locally", "Paso 2 · Ejecuta Localmente el Núcleo", "tp-studio-step-num")}
          {bi("h2", "Replay & Inspect #print axioms", "Reproduce e Inspecciona #print axioms", "tp-studio-step-title")}
          <p>{sp("Do not take a summary on trust. Run ", "No aceptes un resumen a ciegas. Ejecuta ")}<code>lake build</code>{sp(", ", ", ")}<code>#print axioms</code>{sp(", and ", " y ")}<code>lean4checker --fresh</code>{sp(" locally to check for any ", " en tu equipo para buscar cualquier ")}<code>sorryAx</code>{sp(" or custom axiom.", " o axioma propio.")}</p>
        </div>
        <div class="tp-studio-step-card">
          {bi("span", "Step 3 · Explore Companion Folios", "Paso 3 · Explora los Folios Compañeros", "tp-studio-step-num")}
          {bi("h2", "Connect Proof to Computation", "Conecta Prueba y Cómputo", "tp-studio-step-title")}
          <p>{sp("Read the companion mathematical analyses in ", "Lee los análisis matemáticos compañeros en el ")}<a href="../../math/m01/">Folio M.01</a>{sp(", ", ", ")}<a href="../../math/m02/">Folio M.02</a>{sp(", ", ", ")}<a href="../../math/m06/">Folio M.06</a>{sp(", ", ", ")}<a href="../../math/m12/">Folio M.12</a>{sp(", and ", " y ")}<a href="../ai-loop/">{sp("The AI Loop", "El Ciclo de IA")}</a>.</p>
        </div>
      </div>
    </div>

    <nav class="tp-essay-jump-bar" aria-label="{B.esc(lbl_jump)}">
      <a class="tp-essay-jump-pill" href="#proof-act1" data-en="I · Trusted Kernel" data-es="I · Núcleo Confiable">I · Trusted Kernel</a>
      <a class="tp-essay-jump-pill" href="#proof-act2" data-en="II · Public Repositories" data-es="II · Repositorios Públicos">II · Public Repositories</a>
      <a class="tp-essay-jump-pill" href="#proof-act3" data-en="III · 3 Human Audit Checks" data-es="III · 3 Revisiones Humanas">III · 3 Human Audit Checks</a>
      <a class="tp-essay-jump-pill" href="#proof-act4" data-en="IV · Primary Sources" data-es="IV · Fuentes Primarias">IV · Primary Sources</a>
    </nav>

    <section class="tp-folio-layout" aria-labelledby="proof-act1">
      <div class="tp-prose">
        {bi("h2", "Act I — Why a Small Trusted Kernel Separates Search from Checking", "Acto I — Por Qué un Núcleo Pequeño Separa la Búsqueda de la Revisión", extra_attrs='id="proof-act1"')}
        <p class="tp-dropcap">{sp("Proof search may be large, heuristic, or untrusted, yet every finished proof must compile to a term checked by a small kernel. Lean 4 (", "La búsqueda de demostraciones puede ser enorme, heurística o poco confiable, pero toda prueba terminada debe compilarse a un término revisado por un núcleo pequeño. Lean 4 (")}<code>de Moura &amp; Ullrich, CADE-28, 2021</code>{sp(") builds that separation directly into its type checker.", ") integra esa separación directamente en su verificador de tipos.")}</p>
        <div class="tp-plain-bridge-box" role="note" aria-label="{B.esc(lbl_plain)}">
          {bi("span", "In Plain Words · What Lean 4 Checks—and What Humans Still Must Check", "En Palabras Sencillas · Qué Verifica Lean 4 y Qué Deben Auditar las Personas", "tp-plain-bridge-kicker")}
          {bi("p", "Think of a long proof like aircraft wiring. A person or an AI model can propose thousands of connections rapidly, while Lean 4's kernel tests continuity and rejects missing cases. Two tasks remain human: build the repository yourself instead of quoting a headline, and read the top-level statement to check that it asks the intended question.", "Piensa en una demostración larga como el cableado de un avión. Una persona o un modelo de IA puede proponer miles de conexiones con rapidez, mientras el núcleo de Lean 4 revisa la continuidad y rechaza casos omitidos. Dos tareas siguen siendo humanas: compilar el repositorio en tu equipo en vez de repetir titulares, y leer el enunciado principal para comprobar que plantea la pregunta prevista.")}
        </div>
        <p>{sp("Shared libraries such as mathlib (", "Bibliotecas compartidas como mathlib (")}<code>The mathlib Community, 2020</code>{sp(") break large proofs into dependency graphs of reusable lemmas. Public Lean 4 blueprints—including the Imperial College London Fermat project (", ") dividen demostraciones extensas en grafos de lemas reutilizables. Proyectos públicos en Lean 4 —como el blueprint de Fermat en Imperial College London (")}<code>Buzzard, Taylor, et al.</code>{sp(") and the Freiman–Ruzsa project in ", ") y el proyecto de Freiman–Ruzsa del ")}<a href="../../math/m04/">Folio M.04</a>{sp("—use that modular layout.", "— usan esta estructura modular.")}</p>

{_render_proof_svg()}

        {bi("h2", "Act II — Public Lean 4 Repositories & What Their READMEs State", "Acto II — Repositorios Públicos en Lean 4 y Qué Declaran sus README", extra_attrs='id="proof-act2"')}
        <p>{sp("Across Folios ", "En los Folios ")}<a href="../../math/m01/">M.01</a>, <a href="../../math/m02/">M.02</a>, <a href="../../math/m06/">M.06</a>, {sp("and ", "y ")}<a href="../../math/m12/">M.12</a>{sp(", this site reports only what each public README or preprint states. ", ", este sitio reporta solo lo que declara cada README o preprint público. ")}<strong>{sp("This site has not built or checked these Lean 4 repositories.", "Este sitio no ha compilado ni verificado estos repositorios en Lean 4.")}</strong>{sp(" Use the links below and the Act III commands to inspect the primary files:", " Usa los enlaces siguientes y los comandos del Acto III para auditar los archivos primarios:")}</p>

        <div class="tp-table-wrap">
          <table class="tp-table" aria-label="{B.esc(lbl_table)}">
            <thead>
              <tr>
                {bi("th", "Repository / Project", "Repositorio / Proyecto", extra_attrs='scope="col"')}
                {bi("th", "What the Repository README / Preprint States", "Qué Declara el README / Preprint", extra_attrs='scope="col"')}
                {bi("th", "Verification Status Here", "Estado de Verificación Aquí", extra_attrs='scope="col"')}
                {bi("th", "Primary Links & Companion Folio", "Enlaces Primarios y Folio Compañero", extra_attrs='scope="col"')}
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">{sp("Fermat's Last Theorem (R = T Modularity Lifting)", "Último Teorema de Fermat (Levantamiento de Modularidad R = T)")}</th>
                <td>{sp("Classical proof by Wiles (1995) and Taylor–Wiles (1995) for ", "Demostración clásica de Wiles (1995) y Taylor–Wiles (1995) para ")}<code>x^n + y^n = z^n</code>{sp(" (", " (")}<code>n &gt; 2</code>{sp("). Anthropic's README states a 29,511-theorem Lean 4 formalization alongside the ongoing Imperial ", "). El README de Anthropic declara una formalización de 29,511 teoremas en Lean 4 junto al blueprint vivo de Imperial ")}<code>FLT</code>{sp(" blueprint.", ".")}</td>
                <td data-voice="repeat">{sp("Reported from README (read 2026-11-14); not built or checked here.", "Reportado del README (leído 2026-11-14); no compilado ni verificado aquí.")}</td>
                <td><a href="https://github.com/anthropics/fermats-last-theorem" target="_blank" rel="noopener noreferrer">anthropics/fermats-last-theorem</a> · <a href="https://www.anthropic.com/research/formalizing-fermats-last-theorem" target="_blank" rel="noopener noreferrer">{sp("Research post", "Nota técnica")}</a> · <a href="https://github.com/ImperialCollegeLondon/FLT" target="_blank" rel="noopener noreferrer">ImperialCollegeLondon/FLT</a> · <a href="../../math/m01/">Folio M.01</a></td>
              </tr>
              <tr>
                <th scope="row"><code>zeta23</code> · {sp("Critical-Line Zeros of Riemann Zeta", "Ceros de Zeta en la Recta Crítica")}</th>
                <td>{sp("Listed in ", "Listado en ")}<code>anthropics/formal-math</code>{sp(" as a Lean 4 project for Alpöge & Furman (", " como proyecto en Lean 4 para Alpöge y Furman (")}<code>arXiv:2608.13637</code>{sp("), stating that more than two-thirds of non-trivial Riemann zeta zeros are simple and on the critical line. Also includes ", "), que afirma que más de dos tercios de los ceros no triviales de zeta son simples y yacen en la recta crítica. Incluye ")}<code>zeta23/Challenge/XiPrime.lean</code>.</td>
                <td data-voice="repeat">{sp("Reported from README (read 2026-11-14); not built or checked here.", "Reportado del README (leído 2026-11-14); no compilado ni verificado aquí.")}</td>
                <td><a href="https://github.com/anthropics/formal-math/tree/main/zeta23" target="_blank" rel="noopener noreferrer">formal-math/zeta23</a> · <a href="https://arxiv.org/abs/2608.13637" target="_blank" rel="noopener noreferrer">arXiv:2608.13637</a> · <a href="../../math/m02/">Folio M.02</a></td>
              </tr>
              <tr>
                <th scope="row"><code>3sum-apsp</code> · {sp("Subquadratic 3SUM & Subcubic APSP", "3SUM Subcuadrático y APSP Subcúbico")}</th>
                <td>{sp("Listed in ", "Listado en ")}<code>anthropics/formal-math</code>{sp(" for Alman & Vassilevska Williams (", " para Alman y Vassilevska Williams (")}<code>arXiv:2610.06783</code>{sp("; ", "; ")}<code>PALOMAR-2026-10-08-000003</code>{sp("). States ", "). Declara tiempo ")}<code>O(n^1.9992)</code>{sp(" time for 3SUM and ", " para 3SUM y ")}<code>O(n^2.99942)</code>{sp(" for All-Pairs Shortest Paths.", " para Caminos Más Cortos entre Todos los Pares (APSP).")}</td>
                <td data-voice="repeat">{sp("Reported from README & preprint; not built or checked here.", "Reportado del README y preprint; no compilado ni verificado aquí.")}</td>
                <td><a href="https://github.com/anthropics/formal-math/tree/main/3sum-apsp" target="_blank" rel="noopener noreferrer">formal-math/3sum-apsp</a> · <a href="https://arxiv.org/abs/2610.06783" target="_blank" rel="noopener noreferrer">arXiv:2610.06783</a> · <a href="https://palomar-registry.org/entry.html?id=PALOMAR-2026-10-08-000003&amp;version=1" target="_blank" rel="noopener noreferrer">Palomar Registry</a> · <a href="../../math/m06/">Folio M.06</a></td>
              </tr>
              <tr>
                <th scope="row"><code>eth</code> · {sp("k-CNF Counting & ETH Claim", "Conteo k-CNF y Afirmación sobre ETH")}</th>
                <td>{sp("Described in ", "Descrito en ")}<code>anthropics/formal-math</code>{sp(" (read 2026-11-14) as a ", " (leído el 2026-11-14) como un algoritmo en tiempo ")}<code>2^o(n)</code>{sp(" k-CNF solution-counting algorithm claiming to refute the Exponential Time Hypothesis. Classical background: Impagliazzo, Paturi & Zane (2001).", " para contar soluciones k-CNF que afirma refutar la Hipótesis del Tiempo Exponencial. Antecedente clásico: Impagliazzo, Paturi y Zane (2001).")}</td>
                <td data-voice="repeat">{sp("Repository's own unchecked claim per README; not built or checked here.", "Afirmación no verificada del propio README; no compilado ni verificado aquí.")}</td>
                <td><a href="https://github.com/anthropics/formal-math/tree/main/eth" target="_blank" rel="noopener noreferrer">formal-math/eth</a> · <a href="../../math/m12/">Folio M.12</a> · <a href="../../math/m01/">Folio M.01</a></td>
              </tr>
            </tbody>
          </table>
        </div>

        {bi("h2", "Act III — Three Checks Every Human Reviewer Must Run", "Acto III — Tres Revisiones que Toda Persona Auditora Debe Ejecutar", extra_attrs='id="proof-act3"')}
        <p>{sp("A zero exit code from ", "Un código de salida cero de ")}<code>lake build</code>{sp(" shows only that a term inhabits the declared type in Lean's type theory. It does ", " muestra únicamente que un término habita el tipo declarado en la teoría de tipos de Lean. ")}<strong>{sp("not", "No")}</strong>{sp(" check whether that type matches the informal theorem. Independent review therefore requires three steps:", " comprueba si ese tipo coincide con el teorema matemático informal. Una revisión independiente exige tres pasos:")}</p>
        <ol>
          <li>
            <strong>{sp("Top-Level Statement & Definition Fidelity:", "Fidelidad del Enunciado y las Definiciones:")}</strong> {sp("Inspect every custom structure, coercion, quantifier, and domain hypothesis in the theorem header. Check that conventions such as natural-number subtraction truncation or division by zero in ", "Inspecciona cada estructura propia, coerción, cuantificador e hipótesis de dominio en el encabezado del teorema. Comprueba que convenciones como la resta truncada o la división entre cero en ")}<code>Nat</code> / <code>Real</code>{sp(" do not make a premise unsatisfiable. Registries such as ", " no vuelvan insatisfacible una premisa. Registros como ")}<a href="https://palomar-registry.org/" target="_blank" rel="noopener noreferrer">Palomar Registry</a>{sp(" freeze canonical statements to guard against specification drift.", " congelan enunciados canónicos para evitar desviaciones.")}
          </li>
          <li>
            <strong>{sp("Axiom Footprint Inspection (#print axioms):", "Huella de Axiomas (#print axioms):")}</strong> {sp("Run ", "Ejecuta ")}<code>#print axioms MainTheorem</code>{sp(" to list every axiom reachable from the proof term. Classical Mathlib4 proofs use only ", " para listar cada axioma alcanzable desde el término de prueba. Las pruebas clásicas en Mathlib4 usan solo ")}<code>propext</code>, <code>Classical.choice</code>, {sp("and ", "y ")}<code>Quot.sound</code>{sp("; any ", "; cualquier ")}<code>sorryAx</code>{sp(" or unvetted ", " o ")}<code>axiom</code>{sp(" marks an unfinished obligation.", " sin auditar indica una obligación inconclusa.")}
          </li>
          <li>
            <strong>{sp("Out-of-Process Kernel Replay (lean4checker):", "Reproducción Externa del Núcleo (lean4checker):")}</strong> {sp("Because Lean 4 allows metaprograms and macros during elaboration, run ", "Como Lean 4 permite metaprogramas y macros durante la elaboración, ejecuta ")}<code>lean4checker --fresh</code>{sp(" on compiled ", " sobre archivos ")}<code>.olean</code>{sp(" files so tactic code cannot bypass kernel type-checking.", " compilados para que las tácticas no eludan la revisión de tipos del núcleo.")}
          </li>
        </ol>

        {bi("h2", "Act IV — Primary Sources & Companion Informatico Monographs", "Acto IV — Fuentes Primarias y Monografías Compañeras en Informatico", extra_attrs='id="proof-act4"')}
        <ul>
          <li><strong>de Moura, L., &amp; Ullrich, S. (2021):</strong> <em>The Lean 4 Theorem Prover and Programming Language</em>, CADE-28, Lecture Notes in Computer Science, vol. 12699 — <a href="https://doi.org/10.1007/978-3-030-79876-5_37" target="_blank" rel="noopener noreferrer">doi:10.1007/978-3-030-79876-5_37</a>.</li>
          <li><strong>The mathlib Community (2020):</strong> <em>The Lean Mathematical Library</em>, CPP 2020 — <a href="https://doi.org/10.1145/3372885.3373824" target="_blank" rel="noopener noreferrer">doi:10.1145/3372885.3373824</a>.</li>
          <li><strong>Buzzard, K., Taylor, R., et al. (2024–2026):</strong> <em>Imperial College London Lean 4 Fermat's Last Theorem Blueprint &amp; Repository</em> — <a href="https://github.com/ImperialCollegeLondon/FLT" target="_blank" rel="noopener noreferrer">github.com/ImperialCollegeLondon/FLT</a>.</li>
          <li><strong>Alpöge, L., &amp; Furman, R. (2026):</strong> <em>More than two thirds of the zeta zeros are simple and on the critical line</em> — <a href="https://arxiv.org/abs/2608.13637" target="_blank" rel="noopener noreferrer">arXiv:2608.13637</a>. {sp("Listed as ", "Listado como ")}<code>zeta23</code> {sp("in ", "en ")}<a href="https://github.com/anthropics/formal-math" target="_blank" rel="noopener noreferrer">github.com/anthropics/formal-math</a> {sp("(README read 2026-11-14; not built or checked here).", "(README leído el 2026-11-14; no compilado ni verificado aquí).")}</li>
          <li><strong>Alman, J., &amp; Vassilevska Williams, V. (2026):</strong> <em>Truly Subquadratic 3SUM and Truly Subcubic APSP via Triangles in Sparse Lopsided Graphs</em> — <a href="https://arxiv.org/abs/2610.06783" target="_blank" rel="noopener noreferrer">arXiv:2610.06783</a> · <a href="https://palomar-registry.org/entry.html?id=PALOMAR-2026-10-08-000003&amp;version=1" target="_blank" rel="noopener noreferrer">PALOMAR-2026-10-08-000003</a> {sp("(not built or checked here).", "(no compilado ni verificado aquí).")}</li>
          <li><strong>Impagliazzo, R., Paturi, R., &amp; Zane, F. (2001):</strong> <em>Which Problems Have Strongly Exponential Complexity?</em> Journal of Computer and System Sciences, 63(4), 512–530 — <a href="https://doi.org/10.1006/jcss.2001.1774" target="_blank" rel="noopener noreferrer">doi:10.1006/jcss.2001.1774</a>.</li>
        </ul>
        <div class="tp-studio-pill-row">
          <a class="tp-bounty-pill" href="../../math/m12/" data-en="Companion Folio M.12: Post-Quantum Lattices &amp; Formal Repositories &rarr;" data-es="Folio Compañero M.12: Retículas Poscuánticas y Repositorios Formales &rarr;">Companion Folio M.12: Post-Quantum Lattices &amp; Formal Repositories &rarr;</a>
          <a class="tp-bounty-pill" href="../../math/" data-en="Browse All 15 Mathematics Folios (M.01–M.15) &rarr;" data-es="Explorar los 15 Folios de Matemáticas (M.01–M.15) &rarr;">Browse All 15 Mathematics Folios (M.01–M.15) &rarr;</a>
          <a class="tp-bounty-pill" href="../ai-loop/" data-en="Next Guide: The AI Loop (Local Models &amp; Verifiers) &rarr;" data-es="Siguiente Guía: El Ciclo de IA (Modelos Locales y Verificadores) &rarr;">Next Guide: The AI Loop (Local Models &amp; Verifiers) &rarr;</a>
        </div>
      </div>
    </section>"""


def render_ai_loop_body(lang: str = "en") -> str:
    """Main content for /toolchain/ai-loop/ with full EN + ES-MX parity and accurate script descriptions."""
    es = lang == "es"
    lbl_qs = "Adopta el ciclo local de verificación con IA en tres pasos" if es else "Adopt the local-first AI verification loop in three steps"
    lbl_jump = "Secciones de la guía El Ciclo de IA" if es else "Sections of The AI Loop guide"
    lbl_plain = "En palabras sencillas" if es else "In plain words"
    lbl_table = "Ciclo de ingeniería con IA en cuatro niveles de cómputo" if es else "Four-tier local-first AI engineering loop"

    return f"""    <div class="tp-studio-quickstart" role="region" aria-label="{B.esc(lbl_qs)}">
      <div class="tp-studio-quickstart-head">
        {bi("span", "⚡ 3-STEP VERIFICATION LOOP · MODELS PROPOSE, VERIFIERS DISPOSE", "⚡ CICLO DE VERIFICACIÓN EN 3 PASOS · LOS MODELOS PROPONEN, EL CÓDIGO DECIDE", "tp-studio-quickstart-badge")}
        {bi("span", "Practical architecture for small engineering teams, research software groups, and solo builders.", "Arquitectura práctica para pequeños equipos de ingeniería, grupos de software científico y desarrolladores independientes.", "tp-studio-quickstart-sub")}
      </div>
      <div class="tp-studio-steps-grid">
        <div class="tp-studio-step-card">
          {bi("span", "Step 1 · Write the Done Contract First", "Paso 1 · Escribe Primero el Contrato de Éxito", "tp-studio-step-num")}
          {bi("h2", "Scope One Bounded Slice", "Acota una Pieza Verificable", "tp-studio-step-title")}
          <p>{sp("Before asking any model to edit code or derive an equation, state the exact input files, target invariants, and deterministic test command that must exit ", "Antes de pedirle a cualquier modelo que edite código o deduzca una ecuación, define los archivos exactos, los invariantes objetivo y el comando determinista que debe terminar con código ")}<code>0</code>.</p>
        </div>
        <div class="tp-studio-step-card">
          {bi("span", "Step 2 · Delegate Locally on Ollama", "Paso 2 · Delega en Local con Ollama", "tp-studio-step-num")}
          {bi("h2", "Keep Routine Work on Local GPU", "Mantén el Trabajo Rutinario en GPU Local", "tp-studio-step-title")}
          <p>{sp("Route bounded code drafts, structured JSON extraction, and first-pass triage to local open-weight models on ", "Envía borradores acotados de código, extracción estructurada en JSON y triaje inicial a modelos locales de pesos abiertos en ")}<code>Ollama</code>{sp(" with zero cloud data egress.", " sin salida de datos a la nube.")}</p>
        </div>
        <div class="tp-studio-step-card">
          {bi("span", "Step 3 · Gate with Verifiers & Blind Diffs", "Paso 3 · Filtra con Verificadores y Diff Ciego", "tp-studio-step-num")}
          {bi("h2", "Stdlib Verifier + Cross-Lineage Check", "Verificador Stdlib + Revisión Ciega", "tp-studio-step-title")}
          <p>{sp("Require standalone skill verifiers to fail under ", "Exige que los verificadores independientes fallen bajo ")}<code>--planted-defect</code>{sp(" and review ", " y revisa ")}<code>git diff</code>{sp(" with a second model lineage that has zero tools.", " con un segundo linaje de modelo sin acceso a herramientas.")}</p>
        </div>
      </div>
    </div>

    <nav class="tp-essay-jump-bar" aria-label="{B.esc(lbl_jump)}">
      <a class="tp-essay-jump-pill" href="#loop-act1" data-en="I · Roles, Not Models" data-es="I · Roles, No Modelos">I · Roles, Not Models</a>
      <a class="tp-essay-jump-pill" href="#loop-act2" data-en="II · 4 Compute Tiers" data-es="II · 4 Niveles de Cómputo">II · 4 Compute Tiers</a>
      <a class="tp-essay-jump-pill" href="#loop-act3" data-en="III · Planted-Defect &amp; Security Gates" data-es="III · Defecto Plantado y Seguridad">III · Planted-Defect &amp; Security Gates</a>
      <a class="tp-essay-jump-pill" href="#loop-act4" data-en="IV · Open Verifiers &amp; Tools" data-es="IV · Verificadores y Herramientas">IV · Open Verifiers &amp; Tools</a>
    </nav>

    <section class="tp-folio-layout" aria-labelledby="loop-act1">
      <div class="tp-prose">
        {bi("h2", "Act I — Roles, Not Models: Why Single-Model Workflows Drift", "Acto I — Roles, No Modelos: Por Qué Derivan los Flujos de un Solo Modelo", extra_attrs='id="loop-act1"')}
        <p class="tp-dropcap">{sp("When the same language model writes a module, writes its unit test, and summarizes its own diff, correlated blind spots compound silently: a misunderstood sign convention, an off-by-one boundary, or a misattributed citation looks equally plausible to the author and to its self-review. Reliable AI-assisted engineering breaks that symmetry by assigning distinct roles to deterministic code, local open-weight workers, cross-lineage reviewers, and a human maintainer.", "Cuando el mismo modelo de lenguaje escribe un módulo, redacta su prueba unitaria y resume sus propios cambios, los puntos ciegos correlacionados se acumulan en silencio: una convención de signos mal entendida, un borde desplazado por uno o una cita mal atribuida lucen igual de plausibles para el autor y para su autorrevisión. La ingeniería confiable asistida por IA rompe esa simetría asignando roles distintos al código determinista, a trabajadores locales de pesos abiertos, a revisores de otro linaje y a la persona mantenedora.")}</p>
        <div class="tp-plain-bridge-box" role="note" aria-label="{B.esc(lbl_plain)}">
          {bi("span", "In Plain Words · The Core Engineering Rule", "En Palabras Sencillas · La Regla Central de Ingeniería", "tp-plain-bridge-kicker")}
          {bi("p", "Never ask a language model whether a number, mesh, or link is valid when a 40-line Python script can check it directly. Use language models where human judgment and pattern synthesis help—drafting code, proposing edge cases, and challenging diffs across model families—and let deterministic scripts hold non-negotiable pass/fail authority.", "Nunca le preguntes a un modelo de lenguaje si un número, una malla 3D o un enlace es válido cuando un script de 40 líneas en Python puede comprobarlo directamente. Usa modelos donde ayudan la síntesis y la exploración —redactar borradores, proponer casos límite y cuestionar diffs entre familias distintas— y deja la decisión binaria de aprobar o rechazar en manos de scripts deterministas.")}
        </div>

{_render_ai_loop_svg()}

        {bi("h2", "Act II — Capability-Based Routing Across Four Compute Tiers", "Acto II — Enrutamiento por Capacidad en Cuatro Niveles de Cómputo", extra_attrs='id="loop-act2"')}
        <p>{sp("Treating model names as replaceable seats behind explicit capability contracts keeps workflows portable as new open-weight and frontier releases appear. Each task slice is routed to the lightest tier capable of checking or producing it:", "Tratar los nombres de modelos como asientos intercambiables detrás de contratos explícitos de capacidad mantiene el flujo portátil conforme aparecen nuevos modelos abiertos y de frontera. Cada tarea se envía al nivel más ligero capaz de producirla o verificarla:")}</p>

        <div class="tp-table-wrap">
          <table class="tp-table" aria-label="{B.esc(lbl_table)}">
            <thead>
              <tr>
                {bi("th", "Compute Tier & Role", "Nivel de Cómputo y Rol", extra_attrs='scope="col"')}
                {bi("th", "Representative Runtime", "Entorno Representativo", extra_attrs='scope="col"')}
                {bi("th", "Assigned Work", "Trabajo Asignado", extra_attrs='scope="col"')}
                {bi("th", "Hard Boundary", "Frontera Estricta", extra_attrs='scope="col"')}
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">{sp("Tier 0 · Deterministic Verifier", "Nivel 0 · Verificador Determinista")}</th>
                <td><code>Python 3 stdlib</code> · <code>lean4checker</code></td>
                <td>{sp("Conservation laws, 2-manifold mesh checks, SHA-256 locks, HTML/CSP/link validation, and planted-defect rejection.", "Leyes de conservación, topología 2-variedad de mallas, candados SHA-256, validación HTML/CSP/enlaces y rechazo de defectos plantados.")}</td>
                <td>{sp("Zero LLM tokens; non-zero exit blocks publication.", "Cero tokens de LLM; salida distinta de cero bloquea la publicación.")}</td>
              </tr>
              <tr>
                <th scope="row">{sp("Tier 1 · Local Open-Weight Worker", "Nivel 1 · Trabajador Local de Pesos Abiertos")}</th>
                <td><code>Ollama</code> (<code>Qwen</code>, <code>Gemma</code>, <code>Nemotron</code>)</td>
                <td>{sp("Bounded single-file implementations, boilerplate refactoring, log/regex triage, and first-pass diff inspection on local VRAM.", "Implementaciones acotadas de un archivo, refactorización estructurada, triaje de registros e inspección inicial de diffs en VRAM local.")}</td>
                <td>{sp("No ambient credentials, no network mutations, explicit token/context cap.", "Sin credenciales en entorno, sin mutaciones de red y con límite explícito de contexto.")}</td>
              </tr>
              <tr>
                <th scope="row">{sp("Tier 2 · Blind Cross-Lineage Challenger", "Nivel 2 · Revisor Ciego de Otro Linaje")}</th>
                <td>{sp("Independent model family (local or cloud)", "Familia de modelo independiente (local o nube)")}</td>
                <td>{sp("Reads only ", "Lee únicamente el ")}<code>git diff</code>{sp(" and acceptance criteria to surface logic bugs, citation drift, or missing edge cases.", " y los criterios de aceptación para detectar errores lógicos, deriva de citas o casos límite omitidos.")}</td>
                <td>{sp("Zero tool calls; diff caged inside ", "Cero herramientas; diff aislado dentro de ")}<code>&lt;untrusted_data&gt;</code>{sp("; max 2 rounds.", "; máximo 2 rondas.")}</td>
              </tr>
              <tr>
                <th scope="row">{sp("Tier 3 · Scoping Orchestrator & Human", "Nivel 3 · Orquestador y Persona Mantenedora")}</th>
                <td>{sp("Frontier reasoning model + maintainer", "Modelo de razonamiento + persona mantenedora")}</td>
                <td>{sp("Multi-file architecture, task decomposition, verifying challenger findings against real code, and final pull-request merge.", "Arquitectura multiarchivo, descomposición de tareas, verificación de hallazgos contra el código real y fusión final del pull request.")}</td>
                <td>{sp("Owns the diff; never claims 'verified' without command output.", "Responde por el diff; jamás afirma 'verificado' sin salida ejecutable.")}</td>
              </tr>
            </tbody>
          </table>
        </div>

        {bi("h2", "Act III — Planted-Defect Falsifiability & Untrusted Data Caging", "Acto III — Falsabilidad con Defecto Plantado y Aislamiento de Datos No Confiables", extra_attrs='id="loop-act3"')}
        <p>{sp("Two lightweight guardrails prevent the two most common failure modes in automated coding pipelines—tautological tests and prompt injection through external text:", "Dos salvaguardas ligeras previenen las dos fallas más comunes en tuberías automatizadas de programación: pruebas tautológicas e inyección de instrucciones mediante texto externo:")}</p>
        <ol>
          <li>
            <strong>{sp("Skill Verifiers Must Fail Under a Planted Defect:", "Los Verificadores Deben Fallar Ante un Defecto Plantado:")}</strong> {sp("A test script that prints ", "Un script de prueba que imprime ")}<code>PASS</code>{sp(" without inspecting the computed state is worse than having no test at all. In this repository, ", " sin inspeccionar el estado calculado es peor que no tener prueba. En este repositorio, ")}<code>skills/verify_all_48_folios.py</code>{sp(" discovers every standalone ", " descubre cada script independiente ")}<code>verify_*.py</code>{sp(" under ", " dentro de ")}<code>skills/</code>{sp(", requires ", ", exige que ")}<code>--planted-defect</code>{sp(" to fail, and parses the Python AST to reject trivial scripts that merely exit on the flag without running a computation; alongside it, ", " falle y analiza el AST de Python para rechazar scripts triviales que solo salgan ante la bandera sin ejecutar el cálculo; en paralelo, ")}<code>toolchain/run_all_toolchain.py</code>{sp(" re-runs all seven deterministic CAD generators (", " vuelve a ejecutar los siete generadores deterministas de CAD (")}<code>make_x01.py..make_x07.py</code>{sp("), byte-level geometry verifiers, and claim gates.", "), sus verificadores geométricos a nivel de bytes y las compuertas de afirmaciones.")}
          </li>
          <li>
            <strong>{sp("Untrusted Inputs Run with Zero Tool Authority:", "Las Entradas No Confiables se Procesan con Cero Herramientas:")}</strong> {sp("Whenever a model inspects fetched web pages, third-party documentation, or repository diffs, that payload is wrapped inside explicit ", "Siempre que un modelo inspecciona páginas web externas, documentación de terceros o diffs de código, ese contenido se envuelve en delimitadores explícitos ")}<code>&lt;untrusted_data&gt;</code>{sp(" delimiters in a tool-free call. Embedded text can never invoke shell commands, read ", " dentro de una llamada sin herramientas. El texto incrustado jamás puede ejecutar comandos de terminal, leer ")}<code>.env</code>{sp(" files, or push branches.", " ni publicar ramas.")}
          </li>
          <li>
            <strong>{sp("Bounded Escalation Instead of Infinite Retries:", "Escalamiento Acotado en Lugar de Reintentos Infinitos:")}</strong> {sp("If a local worker fails deterministic checks twice on the same traceback, the loop stops burning tokens, records the exact failure signature, and escalates a minimal context packet rather than spinning in an ungrounded retry loop.", "Si un modelo local falla dos veces las pruebas deterministas con el mismo rastreo de error, el ciclo detiene el gasto de cómputo, registra la falla exacta y escala un paquete mínimo de contexto en lugar de girar sin rumbo.")}
          </li>
        </ol>

        {bi("h2", "Act IV — Inspect the Verifiers & Companion Toolboxes", "Acto IV — Inspecciona los Verificadores y Herramientas Compañeras", extra_attrs='id="loop-act4"')}
        <p>{sp("Every generator, byte-level mesh verifier, and HTML/CSP test suite described on this page is open for inspection and reuse in the public repository:", "Cada generador, verificador de mallas a nivel de bytes y suite de pruebas HTML/CSP descrito en esta página está abierto para inspección y reutilización en el repositorio público:")}</p>
        <ul>
          <li><strong>Informatico.ai Open Repository:</strong> <a href="https://github.com/senseiewok/informatico.ai" target="_blank" rel="noopener noreferrer">github.com/senseiewok/informatico.ai</a> — <code>skills/verify_all_48_folios.py</code>, <code>toolchain/run_all_toolchain.py</code>, <code>tests/test_informatico_seo.py</code>, {sp("and ", "y ")}<code>deploy/check_upload.py</code>.</li>
          <li><strong>Ollama Local Runtime Documentation:</strong> <a href="https://docs.ollama.com/" target="_blank" rel="noopener noreferrer">docs.ollama.com</a> — {sp("running quantized open-weight models locally over HTTP with explicit context lengths (", "ejecución local de modelos cuantizados de pesos abiertos mediante HTTP con longitud de contexto explícita (")}<code>num_ctx</code>).</li>
          <li><strong>OWASP Top 10 for LLM Applications:</strong> <a href="https://genai.owasp.org/" target="_blank" rel="noopener noreferrer">genai.owasp.org</a> — {sp("prompt-injection boundaries, least-privilege tool scoping, and deterministic output validation.", "fronteras contra inyección de prompts, privilegio mínimo en herramientas y validación determinista de salidas.")}</li>
        </ul>
        <div class="tp-studio-pill-row">
          <a class="tp-bounty-pill" href="../" data-en="Explore All 7 Tech &amp; Tools 3D CAD Folios (X.01–X.07) &rarr;" data-es="Explorar los 7 Folios 3D CAD de Herramientas (X.01–X.07) &rarr;">Explore All 7 Tech &amp; Tools 3D CAD Folios (X.01–X.07) &rarr;</a>
          <a class="tp-bounty-pill" href="../x01/" data-en="Toolbox X.01: Zero-Dependency WebGL2 &amp; Binary glTF 2.0 Verifier &rarr;" data-es="Herramienta X.01: Visor WebGL2 Sin Dependencias y Verificador glTF 2.0 &rarr;">Toolbox X.01: Zero-Dependency WebGL2 &amp; Binary glTF 2.0 Verifier &rarr;</a>
          <a class="tp-bounty-pill" href="../proof-observatory/" data-en="Companion Guide: Lean 4 Proof Observatory &rarr;" data-es="Guía Compañera: Observatorio de Pruebas en Lean 4 &rarr;">Companion Guide: Lean 4 Proof Observatory &rarr;</a>
        </div>
      </div>
    </section>"""


def render_toolchain_companion_band() -> str:
    """Render the 2-card Methodology & Verification Guides band on /toolchain/ (typographic cards so X.01-X.07 keep unique rack thumbs)."""
    cards = []
    for slug in GUIDE_SLUGS:
        c = GUIDE_CARDS[slug]
        cards.append(
            f"""        <a class="tp-rack-card" href="./{slug}/" data-guide-slug="{B.esc(slug)}">
          <span class="tp-rack-top"><span class="tp-rack-id">{B.esc(c['code'])}</span><span class="tp-rack-badge" data-en="{B.esc(c['reading_en'])}" data-es="{B.esc(c['reading_es'])}">{B.esc(c['reading_en'])}</span></span>
          <strong class="tp-rack-title" data-en="{B.esc(c['title_en'])}" data-es="{B.esc(c['title_es'])}">{B.esc(c['title_en'])}</strong>
          <span class="tp-rack-dek" data-en="{B.esc(c['dek_en'])}" data-es="{B.esc(c['dek_es'])}">{B.esc(c['dek_en'])}</span>
        </a>"""
        )
    joined = "\n".join(cards)
    return f"""    <section class="tp-issue-rack" aria-labelledby="toolchain-guides-heading">
      <div class="tp-bounty-head">
        {bi("p", "Verification Methodology & Formal Tooling · 2 Standalone Guides", "Metodología de Verificación y Herramientas Formales · 2 Guías Independientes", "tp-kicker")}
        {bi("h2", "Formal Proof Observatory & Local-First AI Verification Loop", "Observatorio de Pruebas Formales y Ciclo de Verificación Local con IA", "tp-h2", 'id="toolchain-guides-heading"')}
        {bi("p", "Alongside the seven 3D CAD generators above, these two companion engineering guides document how Lean 4 kernel checking and local-first Ollama + Python verification loops keep software and mathematical claims inspectable.", "Junto a los siete generadores CAD 3D anteriores, estas dos guías compañeras documentan cómo la revisión del núcleo de Lean 4 y los ciclos locales con Ollama y Python mantienen auditable cada afirmación matemática y de software.", "tp-standfirst")}
      </div>
      <div class="tp-rack-grid">
{joined}
      </div>
    </section>"""


def render_guide_page(slug: str, catalog: dict, lang: str = "en") -> str:
    """Render /toolchain/<slug>/index.html (and input to B.to_spanish_static for /es-mx/)."""
    assert slug in GUIDE_SLUGS, f"Unknown toolchain guide slug: {slug}"
    rel_root, rel_res = "../..", "../.."
    es = lang == "es"
    t_en, d_en, t_es, d_es = GUIDE_SEO[slug]
    card = GUIDE_CARDS[slug]
    seo_title = f"{t_es if es else t_en} | {B.BRAND}"
    seo_desc = d_es if es else d_en
    rel_path = f"toolchain/{slug}/"
    canon = B.page_url(rel_path, lang)
    image = f"https://informatico.ai/plates/{c_plate}.jpg" if (c_plate := card["plate"]) else "https://informatico.ai/plates/x01.jpg"
    crumbs = [
        (B.BRAND, B.page_url("", lang)),
        ("Herramientas" if es else "Tech & Tools", B.page_url("toolchain/", lang)),
        (t_es if es else t_en, canon),
    ]
    ld = B._ld(
        "TechArticle",
        t_es if es else t_en,
        seo_desc,
        canon,
        lang,
        image=image,
        date_published=GUIDE_DATE_PUBLISHED,
        date_modified=GUIDE_DATE_MODIFIED,
        crumbs=crumbs,
    )
    head = B.render_head(seo_title, seo_desc, rel_path, "article", image, rel_root, rel_res, ld, lang)
    body_inner = render_proof_observatory_body(lang) if slug == "proof-observatory" else render_ai_loop_body(lang)
    lbl_crumb = "Ruta de navegación" if es else "Breadcrumb"

    return f"""{head}
<body class="tp-body tp-page-folio">
{B.render_masthead(rel_res, "toolchain", lang)}
{B.render_contents_dialog(rel_res, catalog, slug)}
  <main id="main" class="tp-shell" tabindex="-1">
  <nav class="tp-breadcrumb-bar" aria-label="{B.esc(lbl_crumb)}">
    <ol class="tp-breadcrumb-list">
        <li class="tp-crumb-item"><a class="tp-crumb-link" href="{B._href(rel_res)}">Informatico.ai</a></li>
        <li class="tp-crumb-item"><a class="tp-crumb-link" href="{B._href(rel_res, 'toolchain/')}" data-en="Tech &amp; Tools" data-es="Herramientas">Tech &amp; Tools</a></li>
        <li class="tp-crumb-item" aria-current="page">{bi("span", t_en, t_es)}</li>
    </ol>
  </nav>
  <article data-folio-id="{B.esc(card['code'])}" data-folio-slug="{B.esc(slug)}">
    <section class="tp-hero">
      <p class="tp-kicker">{bi("span", "Tech & Tools · Verification Guide", "Herramientas · Guía de Verificación")} · {B.esc(card["code"])} · {bi("span", card["reading_en"], card["reading_es"])}</p>
      {bi("h1", card["title_en"], card["title_es"], "tp-h1")}
      {bi("p", card["dek_en"], card["dek_es"], "tp-standfirst")}
    </section>
{body_inner}
  </article>
{B.render_site_footer(rel_res)}
  </main>
  <script type="module" src="{rel_res}/modules/main.mjs"></script>
</body>
</html>
"""


def write_pages(catalog: dict | None = None) -> list[Path]:
    """Write EN + /es-mx/ HTML files for both toolchain methodology guides."""
    catalog = catalog or B.update_catalogs()
    res_dir = B.ROOT / "src"
    es_dir = res_dir / B.ES_PREFIX.strip("/")
    written: list[Path] = []
    for slug in GUIDE_SLUGS:
        en_dir = res_dir / "toolchain" / slug
        es_gdir = es_dir / "toolchain" / slug
        en_dir.mkdir(parents=True, exist_ok=True)
        es_gdir.mkdir(parents=True, exist_ok=True)
        en_file = en_dir / "index.html"
        es_file = es_gdir / "index.html"
        en_file.write_text(render_guide_page(slug, catalog, "en"), encoding="utf-8")
        es_file.write_text(B.to_spanish_static(render_guide_page(slug, catalog, "es")), encoding="utf-8")
        written.extend([en_file, es_file])
    return written


def main() -> int:
    catalog = B.update_catalogs()
    written = write_pages(catalog)
    (B.ROOT / "src" / "sitemap.xml").write_text(B.render_research_sitemap(catalog), encoding="utf-8")
    (B.ROOT / "src" / "llms.txt").write_text(B.render_llms_txt(catalog), encoding="utf-8")
    print(f"PASS: Built {len(written)} toolchain guide pages (EN + ES-MX) and refreshed sitemap.xml + llms.txt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
