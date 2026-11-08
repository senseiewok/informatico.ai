# Tech & Tools · The Toolbox (`X.01`–`X.06`)

**30-Second Studio Quick-Start for 1–5 Person Architecture Studios, Solo Engineers, and Physics/Math Makers**

Every Folio in **Tech & Tools · The Toolbox** (`X.01`–`X.06`) ships:
1. **Committed Neutral 3D & 2D CAD Files** (`src/research/toolchain/x01..x06/files/`) — open directly in **Blender 4.2+**, **FreeCAD 1.0**, **OrcaSlicer / PrusaSlicer**, **QCAD / LibreCAD**, or **Rhino / Grasshopper** with zero paid software required.
2. **Code-as-Source-of-Truth Generator** (`skills/toolchain/x01..x06/make_x01.py..make_x06.py`) — pure Python 3 standard library scripts that deterministically synthesize the `.glb`, `.step`, `.3mf`, `.dxf`, and `manifest.json` files byte-for-bit.
3. **Byte-Level Verifier & Planted-Defect Knockout** (`skills/toolchain/x01..x06/verify_x01_*.py..verify_x06_*.py`) — verifies $2$-manifold half-edge closure ($3F = 2E$), Euler–Poincaré characteristic ($\chi = V - E + F = 2 - 2g$), divergence-theorem volume, and rejects planted defects.
4. **Portable Agent Skill (`SKILL.md`)** (`skills/toolchain/x01..x06/SKILL.md`) — cross-provider AI skill with `security-runtime` guardrails.
5. **One-Command Runner** (`python toolchain/run_all_toolchain.py`) — runs all 6 generators, byte-level verifiers, and claim gates in `< 1s`.

> **Fixed Educational Artifact Boundary:** Educational and exploratory design calculation only. Nothing on this page, in the downloadable 3D/CAD files, or in the accompanying Python scripts is a stamped architectural or structural engineering design, building-code compliance certificate, or fabrication warranty. Before cutting, printing, or building any physical part, a licensed architect or professional engineer of record must independently verify all loads, material properties, connections, and local code requirements.

---

## Directory & Artifact Index

| Folio | Title | Downloadable Files (`src/research/toolchain/<slug>/files/`) | Free Desktop Tools | Generator & Verifier (`skills/toolchain/<slug>/`) |
| :--- | :--- | :--- | :--- | :--- |
| **`X.01`** | **Zero-Build WebGL2 GLB Inspector & Byte-Level 2-Manifold Geometry Verifier** | `x01_artifact.glb`, `x01_artifact.step`, `x01_artifact.3mf`, `manifest.json` (+ 4 fuzz fixtures) | Browser WebGL2, Blender 4.2+, FreeCAD 1.0 | `make_x01.py` · `verify_x01_toolchain_x01_glb_inspector_validator.py` |
| **`X.02`** | **Code-First Parametric Solids & Measured STEP AP242, 3MF, and GLB Round-Trip Fidelity** | `x02_artifact.step`, `x02_artifact.3mf`, `x02_artifact.glb`, `manifest.json` | FreeCAD 1.0, build123d, OrcaSlicer | `make_x02.py` · `verify_x02_toolchain_x02_parametric_step_3mf_roundtrip.py` |
| **`X.03`** | **The Small Architecture Studio's Vault, Timber & Reciprocal Frame Kit** | `x03_artifact.glb`, `x03_artifact.step`, `x03_artifact.3mf`, `x03_artifact.dxf`, `manifest.json` | Blender/Bonsai, FreeCAD BIM, QCAD, COMPAS | `make_x03.py` · `verify_x03_toolchain_x03_small_architect_vault_kit.py` |
| **`X.04`** | **Miura-Ori Deployable Solar Screens: From 3D Folding Kinematics (GLB) to Flat-Pattern DXF** | `x04_artifact.dxf` (`CUT`/`MOUNTAIN`/`VALLEY`), `x04_artifact.glb`, `x04_artifact.3mf`, `manifest.json` | QCAD, LibreCAD, Inkscape, LightBurn, Blender | `make_x04.py` · `verify_x04_toolchain_x04_miura_ori_dxf_fabricator.py` |
| **`X.05`** | **Topology-Optimized Structural Struts to Watertight 3MF & Build-Plate Overhang Audit** | `x05_artifact.3mf`, `x05_artifact.glb`, `x05_artifact.step`, `manifest.json` | OrcaSlicer, PrusaSlicer, FreeCAD 1.0 | `make_x05.py` · `verify_x05_toolchain_x05_simp_manifold_3mf.py` |
| **`X.06`** | **Sub-Wavelength Acoustic & Topological Metamaterial Unit Cells: Genus $g = 1$ & Betti Numbers** | `x06_artifact.glb`, `x06_artifact.3mf`, `x06_artifact.step`, `manifest.json` | Blender 4.2+, FreeCAD 1.0, Ripser/GUDHI | `make_x06.py` · `verify_x06_toolchain_x06_topological_metamaterial_cell.py` |

---

## How to Open Every File Format in Free Tools

- **`.glb` (Khronos glTF 2.0 Binary):** Open in **Blender 4.2+** (`File -> Import -> glTF 2.0`) or inspect directly in the browser on `/toolchain/x01/`–`/toolchain/x06/`.
- **`.step` (ISO 10303-21 AP242 B-Rep Solid):** Open in **FreeCAD 1.0** (`File -> Open`), **Rhino**, or **build123d / CadQuery** to inspect exact `CLOSED_SHELL` faces and millimeter units.
- **`.3mf` (3MF Core v1.2.3 Package):** Open in **OrcaSlicer**, **PrusaSlicer**, or **Bambu Studio** (`File -> Import -> Import 3MF/STL`) with explicit millimeter units and zero non-manifold edges.
- **`.dxf` (AutoCAD R2000 Layered 2D CAD):** Open in **QCAD**, **LibreCAD**, **Inkscape**, or **LightBurn**; `CUT` (perimeter), `MOUNTAIN` (dashed fold), and `VALLEY` (dash-dot fold) layers map directly to laser/CNC toolpaths.
