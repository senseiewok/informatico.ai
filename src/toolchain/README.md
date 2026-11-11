# Tech & Tools · The Toolbox (`X.01`–`X.06`)

**30-Second Studio Quick-Start for 1–5 Person Architecture Studios, Solo Engineers, and Physics/Math Makers**

Every Folio in **Tech & Tools · The Toolbox** (`X.01`–`X.06`) ships:
1. **Committed Neutral 3D & 2D CAD Files** (`src/toolchain/x01..x06/files/`) — open directly in **Blender 4.2+**, **FreeCAD 1.0**, **OrcaSlicer / PrusaSlicer**, **QCAD / LibreCAD** with 100% Free & Open-Source Software (zero proprietary software required).
2. **Code-as-Source-of-Truth Generator** (`skills/toolchain/x01..x06/make_x01.py..make_x06.py`) — pure Python 3 standard library scripts that deterministically synthesize the `.glb`, `.step`, `.3mf`, `.dxf`, and `manifest.json` files byte-for-bit.
3. **Byte-Level Verifier & Planted-Defect Knockout** (`skills/toolchain/x01..x06/verify_x01_*.py..verify_x06_*.py`) — verifies $2$-manifold half-edge closure ($3F = 2E$), Euler–Poincaré characteristic ($\chi = V - E + F = 2 - 2g$), divergence-theorem volume, and rejects planted defects.
4. **Portable Agent Skill (`SKILL.md`)** (`skills/toolchain/x01..x06/SKILL.md`) — cross-provider AI skill with `security-runtime` guardrails.
5. **One-Command Runner** (`python toolchain/run_all_toolchain.py`) — runs all 6 generators, byte-level verifiers, and claim gates in `< 1s`.

> **Fixed Educational Artifact Boundary:** Educational and exploratory design calculation only. Nothing on this page, in the downloadable 3D/CAD files, or in the accompanying Python scripts is a stamped architectural or structural engineering design, building-code compliance certificate, or fabrication warranty. Before cutting, printing, or building any physical part, a licensed architect or professional engineer of record must independently verify all loads, material properties, connections, and local code requirements.
