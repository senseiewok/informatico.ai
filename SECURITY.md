# Security Policy

## Reporting a Vulnerability

Please report security issues privately through [GitHub Security Advisories](https://github.com/senseiewok/informatico.ai/security/advisories/new) rather than opening a public issue.

## Scope & Architecture Guarantees

- **Zero Build / Zero Third-Party Runtime Dependencies**: `Informatico.ai` uses native ES6+ browser modules (`.mjs`), declarative SVG (`document.createElementNS`), and raw WebGL2 shaders with strict Content-Security-Policy (`CSP`) compatibility (zero `.innerHTML` injection sinks, zero inline `.style.` mutations).
- **Deterministic Citation & Numerical Verification**: All 48 Folios are verified offline against primary Crossref DOIs (`tools/check_folio_citations.py --offline`) ; the verifiers that exist under `skills/` must pass and must fail under a planted defect (`skills/verify_all_48_folios.py`). The pillar and bounty skills are plain text and ship no verifier.
